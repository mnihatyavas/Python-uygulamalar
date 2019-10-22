# coding:iso-8859-9 Türkçe
# p_21101.py: İçiçe 2 fonksiyonun sıralarının değiştirilmesinin farklı sonuçları örneği.

def içiçeFonksiyon (g, f):
    def h (x): return g (f (x))
    return h

def selsiyüstenFahrenhayta (t): return 1.8 * t + 32
def hataAyarı (t): return 0.9 * t - 0.5

çevir1 = içiçeFonksiyon (hataAyarı, selsiyüstenFahrenhayta)
print ("10 dereceyi önce fahrenhayt'a çevir, sonra hata düzeltmesi yap:")
print (çevir1 (10), "=", hataAyarı (selsiyüstenFahrenhayta (10)) )

çevir2 = içiçeFonksiyon (selsiyüstenFahrenhayta, hataAyarı)
print ("\n10 derecenin önce hata düzeltmesini yap, sonra fahrenhayt'a çevir:")
print (çevir2 (10), "=", selsiyüstenFahrenhayta (hataAyarı (10)) )



"""Çıktı:
>python p_21101.py
10 dereceyi önce fahrenhayt'a çevir, sonra hata düzeltmesi yap:
44.5 = 44.5

10 derecenin önce hata düzeltmesini yap, sonra fahrenhayt'a çevir:
47.3 = 47.3
"""