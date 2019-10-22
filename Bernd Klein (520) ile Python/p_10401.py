# coding:iso-8859-9 Türkçe
# p_10401.pt: Girilen sayı altındaki iki tamsayı kareleri karekökünü diğerbir tamsayıya eşitleme örneği.

from math import sqrt

n = abs (int (eval (input ("Bir pozitif tamsayı girin [4-->]: "))))

print ("Bu sayı altında hangi 2 sayının kareleri toplamının karekökü 3.sayıya eşittir?\n", "-"*78, sep="")
for a in range (1, n+1):
    for b in range (a, n+1):
        cKare = a**2 + b**2
        c = int (sqrt (cKare))
        if cKare == c**2: print (a, b, c)


"""Çıktı:
>python p_10401.py
Bir pozitif tamsayı girin [4-->]: -0.15
Bu sayı altında hangi 2 sayının kareleri toplamının karekökü 3.sayıya eşittir?
------------------------------------------------------------------------------

>python p_10401.py  ** TEKRAR **
Bir pozitif tamsayı girin [4-->]: 21
Bu sayı altında hangi 2 sayının kareleri toplamının karekökü 3.sayıya eşittir?
------------------------------------------------------------------------------
3 4 5
5 12 13
6 8 10
8 15 17
9 12 15
12 16 20
15 20 25
20 21 29
"""