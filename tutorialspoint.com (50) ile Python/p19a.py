# coding:iso8859-9 Türkçe
# Python 3 - XML Processing
# XML: Extensible Markup Language (Genişletilebilir İşaret Dili)

import xml.sax

class FilmYönetimi (xml.sax.ContentHandler): # Alt-sınıf yaratma...
    def __init__ (self): # Sınıf kurucusu...
        self.AktüelVeri = ""
        self.katagori = ""
        self.bicim = ""
        self.yil = ""
        self.itibar = ""
        self.yildizlar = ""
        self.aciklama = ""

    # Her yeni element başladığında çağrılır...
    def startElement (self, yafta, özellikler):
        self.AktüelVeri = yafta
        if yafta == "film":
            print ("\n*****Film*****")
            baslik = özellikler["baslik"]
            print ("Başlığı:", baslik)

    # Her element sonlandığında çağrılır...
    def endElement (self, yafta):
        if self.AktüelVeri == "katagori":
            print ("Katagorisi:", self.katagori)
        elif self.AktüelVeri == "bicim":
            print ("Biçimi:", self.bicim)
        elif self.AktüelVeri == "yil":
            print ("Yılı:", self.yil)
        elif self.AktüelVeri == "itibar":
            print ("İtibarı:", self.itibar)
        elif self.AktüelVeri == "yildizlar":
            print ("Yıldızları:", self.yildizlar)
        elif self.AktüelVeri == "aciklama":
            print ("Açıklaması:", self.aciklama)
        self.AktüelVeri = ""

    # Her bir karakter okunduğunda çağrılır...
    def characters (self, krk):
        if self.AktüelVeri == "katagori": self.katagori = krk
        elif self.AktüelVeri == "bicim": self.bicim = krk
        elif self.AktüelVeri == "yil": self.yil = krk
        elif self.AktüelVeri == "itibar": self.itibar = krk
        elif self.AktüelVeri == "yildizlar": self.yildizlar = krk
        elif self.AktüelVeri == "aciklama": self.aciklama = krk

# Ana program başlıyor...  
if ( __name__ == "__main__"):
    # Bir XML okuyucu yaratalım...
    okuyucu = xml.sax.make_parser()
    # İsim boşluklarını kapatalım?..
    #okuyucu.setFeature (xml.sax.handler.feature_namespaces, 0)

    # Varsayılı ContextHandler'i esgeçip kendi alt-sınıf yöneticimizi kullanalım...
    Yönetim = FilmYönetimi()
    okuyucu.setContentHandler(Yönetim)

     # DİKKAT: XML dosyasında türkçe karakterleri kabul etmiyor...
    okuyucu.parse ("xml_19a.xml")

çıktı = """
**  >python p19a.py  **

*****Film*****
Başlığı: Arkadaki Dusman
Katagorisi: Savas, Heyecan
Biçimi: DVD
Yılı: 2003
İtibarı: PG
Yıldızları: 10
Açıklaması: Amerika-Japonya savasi hakkinda

*****Film*****
Başlığı: Donusenler
Katagorisi: Canlandirma, Bilim Kurgu
Biçimi: DVD
Yılı: 1989
İtibarı: R
Yıldızları: 8
Açıklaması: Bir bilim kurgu filmi

*****Film*****
Başlığı: Uc Silahli
Katagorisi: Canlandirma, Aksiyon
Biçimi: DVD
İtibarı: PG
Yıldızları: 10
Açıklaması: Korkmaya kendinizi hazirlayin!

*****Film*****
Başlığı: Istar
Katagorisi: Komedi
Biçimi: VHS
İtibarı: PG
Yıldızları: 2
Açıklaması: Izlemesi sikici

*****Film*****
Başlığı: Kudurus
Katagorisi: Bilim Kurgu
Biçimi: VHS
İtibarı: PG
Yıldızları: 8
Açıklaması: New York'ta canavarlar
"""