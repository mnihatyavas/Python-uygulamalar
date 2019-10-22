# coding:iso-8859-9 Türkçe
# p_13402.py: Şehirli yield-next, dahili sayaçlı fibonaki yield ve harici sayaçlı fib yield üreteç örneği.

from p_13402x import şehir_üreteci, fibonaki, fib2

şehir = şehir_üreteci()
print ("Şehir üreteci fonksiyonu yield elementleri:")

try:
    print ("-->Birsonraki şehir: " + next (şehir) )
    print ("-->Birsonraki şehir: " + next (şehir) )
    print ("-->Birsonraki şehir: " + next (şehir) )
    print ("-->Birsonraki şehir: " + next (şehir) )
    print ("-->Birsonraki şehir: " + next (şehir) )
    print ("-->Birsonraki şehir: " + next (şehir) )
    print ("-->Birsonraki şehir: " + next (şehir) )
    print ("-->Birsonraki şehir: " + next (şehir) )
    print ("-->Birsonraki şehir: " + next (şehir) )
    print ("-->Birsonraki şehir: " + next (şehir) )
    print ("-->Birsonraki şehir: " + next (şehir) )
    print ("-->Birsonraki şehir: " + next (şehir) )
    print ("-->Birsonraki şehir: " + next (şehir) )
except StopIteration: print ("Üreteç elementleri sonuna ulaşıldı...")
#----------------------------------------------------------------------------------------------

f = fibonaki (18)
print ("\nFibonaki üreteci fonksiyonu yield elementleri:")
for x in f: print (x, end=" ")
#----------------------------------------------------------------------------------------------

print ("\n\nSayaçlı Fibonaki üreteçi:")
sayaç = 0
for x in fib2():
    print (x, " ", end="")
    sayaç += 1
    if (sayaç > 18): break 

"""Çıktı:
>python p_13402.py
Şehir üreteci fonksiyonu yield elementleri:
-->Birsonraki şehir: Londra
-->Birsonraki şehir: Hamburg
-->Birsonraki şehir: Konstanz
-->Birsonraki şehir: Amsterdam
-->Birsonraki şehir: Berlin
-->Birsonraki şehir: Zürih
-->Birsonraki şehir: Şafhoyzen
-->Birsonraki şehir: Ştutgart
-->Birsonraki şehir: İstanbul
-->Birsonraki şehir: İzmir
Üreteç elementleri sonuna ulaşıldı...

Fibonaki üreteci fonksiyonu yield elementleri:
0  1  1  2  3  5  8  13  21  34  55  89  144  233  377  610  987  1597  2584

Sayaçlı Fibonaki üreteçi:
0  1  1  2  3  5  8  13  21  34  55  89  144  233  377  610  987  1597  2584
"""