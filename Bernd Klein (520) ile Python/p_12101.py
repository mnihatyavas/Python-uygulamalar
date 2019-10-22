# coding:iso-8859-9 Türkçe
# p_12101.py: Faktöryel fonksiyonunun nihai ve arasonuçlu özyinelemeli ile for döngülü örneği.

from random import randint

def faktöryel1 (n):
    if n == 0: return 1
    else: return n * faktöryel1 (n-1)

sayı = randint (0, 10)
print (sayı, "sayısının özyinelemeli faktöryeli:", faktöryel1 (sayı) )
#-----------------------------------------------------------------------------------------------------

def faktöryel (n):
    print ("Faktöryel fonksiyonu [n=" + str (n) + "] için çağırıldı")
    if n == 0:
        print()
        return 1
    else:
        sonuç = n * faktöryel (n-1)
        print ("Ara sonuç: ", n, "*faktöryel(", n-1, ")=", sonuç, sep="")
        return sonuç

print()
print ("\n", sayı, " sayısının özyinelemeli ve arasonuç açıklamalı faktöryeli: ", faktöryel (sayı), sep="")
#-----------------------------------------------------------------------------------------------------

def döngülüFaktöryel (n):
    sonuç = 1
    for i in range (2, n+1): sonuç *= i
    return sonuç

print ("\n", sayı, " sayısının for döngülü tekrarlamalı faktöryeli: ", döngülüFaktöryel (sayı), sep="")


"""Çıktı:
>python p_12101.py
10 sayısının özyinelemeli faktöryeli: 3628800

Faktöryel fonksiyonu [n=10] için çağırıldı
Faktöryel fonksiyonu [n=9] için çağırıldı
Faktöryel fonksiyonu [n=8] için çağırıldı
Faktöryel fonksiyonu [n=7] için çağırıldı
Faktöryel fonksiyonu [n=6] için çağırıldı
Faktöryel fonksiyonu [n=5] için çağırıldı
Faktöryel fonksiyonu [n=4] için çağırıldı
Faktöryel fonksiyonu [n=3] için çağırıldı
Faktöryel fonksiyonu [n=2] için çağırıldı
Faktöryel fonksiyonu [n=1] için çağırıldı
Faktöryel fonksiyonu [n=0] için çağırıldı

Ara sonuç: 1*faktöryel(0)=1
Ara sonuç: 2*faktöryel(1)=2
Ara sonuç: 3*faktöryel(2)=6
Ara sonuç: 4*faktöryel(3)=24
Ara sonuç: 5*faktöryel(4)=120
Ara sonuç: 6*faktöryel(5)=720
Ara sonuç: 7*faktöryel(6)=5040
Ara sonuç: 8*faktöryel(7)=40320
Ara sonuç: 9*faktöryel(8)=362880
Ara sonuç: 10*faktöryel(9)=3628800

10 sayısının özyinelemeli ve arasonuç açıklamalı faktöryeli: 3628800

10 sayısının for döngülü tekrarlamalı faktöryeli: 3628800
"""