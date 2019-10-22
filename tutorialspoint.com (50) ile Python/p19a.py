# coding:iso8859-9 T�rk�e
# Python 3 - XML Processing
# XML: Extensible Markup Language (Geni�letilebilir ��aret Dili)

import xml.sax

class FilmY�netimi (xml.sax.ContentHandler): # Alt-s�n�f yaratma...
    def __init__ (self): # S�n�f kurucusu...
        self.Akt�elVeri = ""
        self.katagori = ""
        self.bicim = ""
        self.yil = ""
        self.itibar = ""
        self.yildizlar = ""
        self.aciklama = ""

    # Her yeni element ba�lad���nda �a�r�l�r...
    def startElement (self, yafta, �zellikler):
        self.Akt�elVeri = yafta
        if yafta == "film":
            print ("\n*****Film*****")
            baslik = �zellikler["baslik"]
            print ("Ba�l���:", baslik)

    # Her element sonland���nda �a�r�l�r...
    def endElement (self, yafta):
        if self.Akt�elVeri == "katagori":
            print ("Katagorisi:", self.katagori)
        elif self.Akt�elVeri == "bicim":
            print ("Bi�imi:", self.bicim)
        elif self.Akt�elVeri == "yil":
            print ("Y�l�:", self.yil)
        elif self.Akt�elVeri == "itibar":
            print ("�tibar�:", self.itibar)
        elif self.Akt�elVeri == "yildizlar":
            print ("Y�ld�zlar�:", self.yildizlar)
        elif self.Akt�elVeri == "aciklama":
            print ("A��klamas�:", self.aciklama)
        self.Akt�elVeri = ""

    # Her bir karakter okundu�unda �a�r�l�r...
    def characters (self, krk):
        if self.Akt�elVeri == "katagori": self.katagori = krk
        elif self.Akt�elVeri == "bicim": self.bicim = krk
        elif self.Akt�elVeri == "yil": self.yil = krk
        elif self.Akt�elVeri == "itibar": self.itibar = krk
        elif self.Akt�elVeri == "yildizlar": self.yildizlar = krk
        elif self.Akt�elVeri == "aciklama": self.aciklama = krk

# Ana program ba�l�yor...  
if ( __name__ == "__main__"):
    # Bir XML okuyucu yaratal�m...
    okuyucu = xml.sax.make_parser()
    # �sim bo�luklar�n� kapatal�m?..
    #okuyucu.setFeature (xml.sax.handler.feature_namespaces, 0)

    # Varsay�l� ContextHandler'i esge�ip kendi alt-s�n�f y�neticimizi kullanal�m...
    Y�netim = FilmY�netimi()
    okuyucu.setContentHandler(Y�netim)

     # D�KKAT: XML dosyas�nda t�rk�e karakterleri kabul etmiyor...
    okuyucu.parse ("xml_19a.xml")

��kt� = """
**  >python p19a.py  **

*****Film*****
Ba�l���: Arkadaki Dusman
Katagorisi: Savas, Heyecan
Bi�imi: DVD
Y�l�: 2003
�tibar�: PG
Y�ld�zlar�: 10
A��klamas�: Amerika-Japonya savasi hakkinda

*****Film*****
Ba�l���: Donusenler
Katagorisi: Canlandirma, Bilim Kurgu
Bi�imi: DVD
Y�l�: 1989
�tibar�: R
Y�ld�zlar�: 8
A��klamas�: Bir bilim kurgu filmi

*****Film*****
Ba�l���: Uc Silahli
Katagorisi: Canlandirma, Aksiyon
Bi�imi: DVD
�tibar�: PG
Y�ld�zlar�: 10
A��klamas�: Korkmaya kendinizi hazirlayin!

*****Film*****
Ba�l���: Istar
Katagorisi: Komedi
Bi�imi: VHS
�tibar�: PG
Y�ld�zlar�: 2
A��klamas�: Izlemesi sikici

*****Film*****
Ba�l���: Kudurus
Katagorisi: Bilim Kurgu
Bi�imi: VHS
�tibar�: PG
Y�ld�zlar�: 8
A��klamas�: New York'ta canavarlar
"""