# coding:iso-8859-9 T�rk�e
# p_13402.py: �ehirli yield-next, dahili saya�l� fibonaki yield ve harici saya�l� fib yield �rete� �rne�i.

from p_13402x import �ehir_�reteci, fibonaki, fib2

�ehir = �ehir_�reteci()
print ("�ehir �reteci fonksiyonu yield elementleri:")

try:
    print ("-->Birsonraki �ehir: " + next (�ehir) )
    print ("-->Birsonraki �ehir: " + next (�ehir) )
    print ("-->Birsonraki �ehir: " + next (�ehir) )
    print ("-->Birsonraki �ehir: " + next (�ehir) )
    print ("-->Birsonraki �ehir: " + next (�ehir) )
    print ("-->Birsonraki �ehir: " + next (�ehir) )
    print ("-->Birsonraki �ehir: " + next (�ehir) )
    print ("-->Birsonraki �ehir: " + next (�ehir) )
    print ("-->Birsonraki �ehir: " + next (�ehir) )
    print ("-->Birsonraki �ehir: " + next (�ehir) )
    print ("-->Birsonraki �ehir: " + next (�ehir) )
    print ("-->Birsonraki �ehir: " + next (�ehir) )
    print ("-->Birsonraki �ehir: " + next (�ehir) )
except StopIteration: print ("�rete� elementleri sonuna ula��ld�...")
#----------------------------------------------------------------------------------------------

f = fibonaki (18)
print ("\nFibonaki �reteci fonksiyonu yield elementleri:")
for x in f: print (x, end=" ")
#----------------------------------------------------------------------------------------------

print ("\n\nSaya�l� Fibonaki �rete�i:")
saya� = 0
for x in fib2():
    print (x, " ", end="")
    saya� += 1
    if (saya� > 18): break 

"""��kt�:
>python p_13402.py
�ehir �reteci fonksiyonu yield elementleri:
-->Birsonraki �ehir: Londra
-->Birsonraki �ehir: Hamburg
-->Birsonraki �ehir: Konstanz
-->Birsonraki �ehir: Amsterdam
-->Birsonraki �ehir: Berlin
-->Birsonraki �ehir: Z�rih
-->Birsonraki �ehir: �afhoyzen
-->Birsonraki �ehir: �tutgart
-->Birsonraki �ehir: �stanbul
-->Birsonraki �ehir: �zmir
�rete� elementleri sonuna ula��ld�...

Fibonaki �reteci fonksiyonu yield elementleri:
0  1  1  2  3  5  8  13  21  34  55  89  144  233  377  610  987  1597  2584

Saya�l� Fibonaki �rete�i:
0  1  1  2  3  5  8  13  21  34  55  89  144  233  377  610  987  1597  2584
"""