# coding:iso-8859-9 Türkçe
# p_30712a.py: Zar atışlarında çift, ikiden büyük ve birleşik etkili gelme oranları örneği.

from random import randint

try: kere = abs (int (input ("Zar kaç kere atılsın [10 000]? ")))
except: kere = 10000

tümAtışlar = [randint (1, 6) for _ in range (kere)]
çiftGelenler = [x for x in tümAtışlar if x % 2 == 0]
ikidenBüyükGelenler = [x for x in tümAtışlar if x > 2]
ikidenbüyükVeçiftGelenler = [x for x in tümAtışlar if x % 2 == 0 and x > 2]

print ("\nÇift gelen zarların yüzdesi: %{:.2f}" .format (len (çiftGelenler) / len (tümAtışlar) * 100))
print ("İkiden büyük gelen zarların yüzdesi: %{:.2f}" .format (len (ikidenBüyükGelenler) / len (tümAtışlar) * 100))
print ("İkiden büyük ve çift gelen zarların yüzdesi: %{:.2f}" .format (len (ikidenbüyükVeçiftGelenler) / len (tümAtışlar) * 100))



"""Çıktı:
>python p_30712.py
Zar kaç kere atılsın [10 000]?

Çift gelen zarların yüzdesi: %49.88
İkiden büyük gelen zarların yüzdesi: %66.27
İkiden büyük ve çift gelen zarların yüzdesi: %32.84

>python p_30712.py  ** TEKRAR **
Zar kaç kere atılsın [10 000]? 100

Çift gelen zarların yüzdesi: %48.00
İkiden büyük gelen zarların yüzdesi: %69.00
İkiden büyük ve çift gelen zarların yüzdesi: %34.00
"""