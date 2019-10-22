# coding:iso8859-9 T�rk�e
# Python 3 - XML Processing
# XML: Extensible Markup Language (Geni�letilebilir ��aret Dili)
# DOM: DocumentObjectModel (D�k�man Nesnesi Modeli)

import xml.dom.minidom

# minidom okuyucusunu (parse) kullanarak XML d�k�man�n� a�al�m...
# D�KKAT: DOM da SAX gibi XML d�k�man�ndaki T�rk�e karakterlere hata veriyor...
DOMA�ac� = xml.dom.minidom.parse ("p19aXML.xml")
koleksiyoncu = DOMA�ac�.documentElement # �lk k�k elementi al�r...
if koleksiyoncu.hasAttribute ("raf"):
    print ("K�k element: [%s]" % koleksiyoncu.getAttribute ("raf"))

# Koleksiyoncu'nun t�m filimlerini alal�m...
filimler = koleksiyoncu.getElementsByTagName ("film")

# Herbir film elementi detaylar�n� g�r�nt�leyelim...
for film in filimler:
    print ("\n*****Film*****")
    if film.hasAttribute ("baslik"):
      print ("Ba�l�k: %s" % film.getAttribute ("baslik"))

    tip = film.getElementsByTagName ('katagori')[0]
    print ("Katagori: %s" % tip.childNodes[0].data)
    format = film.getElementsByTagName ('bicim')[0]
    print ("Bi�im: %s" % format.childNodes[0].data)
    derece = film.getElementsByTagName ('itibar')[0]
    print ("�tibar: %s" % derece.childNodes[0].data)
    izahat = film.getElementsByTagName ('aciklama')[0]
    print ("A��klama: %s" % izahat.childNodes[0].data)

��kt� = """
**  >python p19b.py  **
K�k element: [Yeni Gelenler]

*****Film*****
Ba�l�k: Arkadaki Dusman
Katagori: Savas, Heyecan
Bi�im: DVD
�tibar: PG
A��klama: Amerika-Japonya savasi hakkinda

*****Film*****
Ba�l�k: Donusenler
Katagori: Canlandirma, Bilim Kurgu
Bi�im: DVD
�tibar: R
A��klama: Bir bilim kurgu filmi

*****Film*****
Ba�l�k: Uc Silahli
Katagori: Canlandirma, Aksiyon
Bi�im: DVD
�tibar: PG
A��klama: Korkmaya kendinizi hazirlayin!

*****Film*****
Ba�l�k: Istar
Katagori: Komedi
Bi�im: VHS
�tibar: PG
A��klama: Izlemesi sikici

*****Film*****
Ba�l�k: Kudurus
Katagori: Bilim Kurgu
Bi�im: VHS
�tibar: PG
A��klama: New York'ta canavarlar
"""