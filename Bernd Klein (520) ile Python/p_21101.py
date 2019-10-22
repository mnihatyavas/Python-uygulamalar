# coding:iso-8859-9 T�rk�e
# p_21101.py: ��i�e 2 fonksiyonun s�ralar�n�n de�i�tirilmesinin farkl� sonu�lar� �rne�i.

def i�i�eFonksiyon (g, f):
    def h (x): return g (f (x))
    return h

def selsiy�stenFahrenhayta (t): return 1.8 * t + 32
def hataAyar� (t): return 0.9 * t - 0.5

�evir1 = i�i�eFonksiyon (hataAyar�, selsiy�stenFahrenhayta)
print ("10 dereceyi �nce fahrenhayt'a �evir, sonra hata d�zeltmesi yap:")
print (�evir1 (10), "=", hataAyar� (selsiy�stenFahrenhayta (10)) )

�evir2 = i�i�eFonksiyon (selsiy�stenFahrenhayta, hataAyar�)
print ("\n10 derecenin �nce hata d�zeltmesini yap, sonra fahrenhayt'a �evir:")
print (�evir2 (10), "=", selsiy�stenFahrenhayta (hataAyar� (10)) )



"""��kt�:
>python p_21101.py
10 dereceyi �nce fahrenhayt'a �evir, sonra hata d�zeltmesi yap:
44.5 = 44.5

10 derecenin �nce hata d�zeltmesini yap, sonra fahrenhayt'a �evir:
47.3 = 47.3
"""