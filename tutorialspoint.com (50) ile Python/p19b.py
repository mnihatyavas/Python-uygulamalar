# coding:iso8859-9 Türkçe
# Python 3 - XML Processing
# XML: Extensible Markup Language (Genişletilebilir İşaret Dili)
# DOM: DocumentObjectModel (Döküman Nesnesi Modeli)

import xml.dom.minidom

# minidom okuyucusunu (parse) kullanarak XML dökümanını açalım...
# DİKKAT: DOM da SAX gibi XML dökümanındaki Türkçe karakterlere hata veriyor...
DOMAğacı = xml.dom.minidom.parse ("p19aXML.xml")
koleksiyoncu = DOMAğacı.documentElement # İlk kök elementi alır...
if koleksiyoncu.hasAttribute ("raf"):
    print ("Kök element: [%s]" % koleksiyoncu.getAttribute ("raf"))

# Koleksiyoncu'nun tüm filimlerini alalım...
filimler = koleksiyoncu.getElementsByTagName ("film")

# Herbir film elementi detaylarını görüntüleyelim...
for film in filimler:
    print ("\n*****Film*****")
    if film.hasAttribute ("baslik"):
      print ("Başlık: %s" % film.getAttribute ("baslik"))

    tip = film.getElementsByTagName ('katagori')[0]
    print ("Katagori: %s" % tip.childNodes[0].data)
    format = film.getElementsByTagName ('bicim')[0]
    print ("Biçim: %s" % format.childNodes[0].data)
    derece = film.getElementsByTagName ('itibar')[0]
    print ("İtibar: %s" % derece.childNodes[0].data)
    izahat = film.getElementsByTagName ('aciklama')[0]
    print ("Açıklama: %s" % izahat.childNodes[0].data)

çıktı = """
**  >python p19b.py  **
Kök element: [Yeni Gelenler]

*****Film*****
Başlık: Arkadaki Dusman
Katagori: Savas, Heyecan
Biçim: DVD
İtibar: PG
Açıklama: Amerika-Japonya savasi hakkinda

*****Film*****
Başlık: Donusenler
Katagori: Canlandirma, Bilim Kurgu
Biçim: DVD
İtibar: R
Açıklama: Bir bilim kurgu filmi

*****Film*****
Başlık: Uc Silahli
Katagori: Canlandirma, Aksiyon
Biçim: DVD
İtibar: PG
Açıklama: Korkmaya kendinizi hazirlayin!

*****Film*****
Başlık: Istar
Katagori: Komedi
Biçim: VHS
İtibar: PG
Açıklama: Izlemesi sikici

*****Film*****
Başlık: Kudurus
Katagori: Bilim Kurgu
Biçim: VHS
İtibar: PG
Açıklama: New York'ta canavarlar
"""