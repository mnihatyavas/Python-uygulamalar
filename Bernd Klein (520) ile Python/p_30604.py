# coding:iso-8859-9 Türkçe

from random import SystemRandom
# p_30604.py: SystemRandom() ile istenilen uzunlukta verili tesadüfi karakter seçimli şifre üretme örneği.

kripto = SystemRandom() # SystemRandom sınıfının bir tipleme nesnesini yaratır...

def şifreÜretici (şifreUzunluğu, kullanılabilirKarakterler=None):
    if kullanılabilirKarakterler==None:
        kullanılabilirKarakterler = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        kullanılabilirKarakterler += kullanılabilirKarakterler.lower() + "0123456789"
    uz = len (kullanılabilirKarakterler)-1
    şifrem = ""
    sayaç = 0
    while sayaç < şifreUzunluğu:
        #tesadüfi0_255Sayı = kripto.randint (0, 256)
        #krk = chr (tesadüfi0_255Sayı)
        #if krk in kullanılabilirKarakterler: şifrem += chr (tesadüfi0_255Sayı)
        şifrem += kullanılabilirKarakterler [kripto.randint (0, uz)]
        sayaç += 1
    return şifrem

print ("Python tarafından otomatik üretilen güvenli şifre: " + şifreÜretici (15, "ABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZbcçdefgğhıijklmnoöpqrsştuüvwxyz0123456789") )


"""Çıktı:
>python p_30604.py
Python tarafından otomatik üretilen güvenli şifre: oq1ÖWÇkptcPğY9p

>python p_30604.py  ** TEKRAR **
Python tarafından otomatik üretilen güvenli şifre: 4XşTpMEı1JBfCj2

>python p_30604.py  ** TEKRAR **
Python tarafından otomatik üretilen güvenli şifre: 9Hv9QmİHXWöETQh
"""