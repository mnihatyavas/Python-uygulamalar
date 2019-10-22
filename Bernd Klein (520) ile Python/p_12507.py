# coding:iso-8859-9 Türkçe
# p_12507.py: İçiçe dekoratörlü ambalaja 3.dış selamlama fonksiyonu sarmalama örneği.

def ikindiSelamı (fonk):
    def ambalaj (x):
        print ("\nTünaydın, " + fonk.__name__ + " mesajınız: ")
        fonk (x)
    return ambalaj

def sabahSelamı (fonk):
    def ambalaj (x):
        print ("Günaydın, " + fonk.__name__ + " mesajınız: ")
        fonk (x)
    return ambalaj

@sabahSelamı
def doğum_günü (x): print (str (x) + " doğum gününüz kutlu olsun!..")

doğum_günü (7.8)

@ikindiSelamı
def doğum_günü (x): print (str (x) + " doğum gününüz kutlu olsun!..")

doğum_günü ("7 Ağustos")
print ("-"*75, "\n")
#--------------------------------------------------------------------------------------------------------

def selam (ibare):
    def dekoratör (fonk):
        def ambalaj (x):
            print ("\n" + ibare + ", " + fonk.__name__ + " mesajınız:")
            fonk (x)
        return ambalaj
    return dekoratör

def doğum_günü (x): print (str (x) + " doğum gününüz kutlu olsun!..")

# En anlaşılır ve @'siz kullanım...
selam ("Günaydın") (doğum_günü) (7.8)
selam ("Tünaydın") (doğum_günü) ("7 Ağustos")
selam ("Merhaba") (doğum_günü) ("14 Nisan")

# Veya pratik @'li kullanım...
@selam ("İyi akşamlar")
def doğum_günü2 (x): print (str (x) + " doğum gününüz kutlu olsun!..")

doğum_günü2 ("17 Nisan")

# Veya dolaylamalı @'siz kullanım...
kutlama = selam ("Selam") (doğum_günü)
kutlama ("4 Mayıs")


"""Çıktı:
>python p_12507.py
Günaydın, doğum_günü mesajınız:
7.8 doğum gününüz kutlu olsun!..

Tünaydın, doğum_günü mesajınız:
7 Ağustos doğum gününüz kutlu olsun!..
---------------------------------------------------------------------------


Günaydın, doğum_günü mesajınız:
7.8 doğum gününüz kutlu olsun!..

Tünaydın, doğum_günü mesajınız:
7 Ağustos doğum gününüz kutlu olsun!..

Merhaba, doğum_günü mesajınız:
14 Nisan doğum gününüz kutlu olsun!..

İyi akşamlar, doğum_günü2 mesajınız:
17 Nisan doğum gününüz kutlu olsun!..

Selam, doğum_günü mesajınız:
4 Mayıs doğum gününüz kutlu olsun!..
"""