# coding:iso-8859-9 Türkçe
# p_12104.py: Hanoi kule açılımı, paskal kulesi, fibonakinin paskal çıkarımı örneği.

from random import randint

def artır3 (n):
    if n == 1: return 3
    else: return artır3 (n-1) + 3

sayı = randint (1,15)
print (sayı, " (* 3=", sayı*3, ") adet 3'ün katları sayılı Hanoi Kuleleri açılımı:", sep="")
for i in range (1,sayı+1): print (artır3 (i), end=" ")
#-----------------------------------------------------------------------------------------------------

def topla (n):
    if n== 0: return 0
    else: return n + topla (n-1)

print ("\n\n1'den itibaren ilk", sayı, "sıralı sayının toplamı:", topla (sayı) )
#-----------------------------------------------------------------------------------------------------

def paskal (n):
    if n == 1: return [1]
    else:
        liste = [1]
        öncekiListe = paskal (n-1)
        # Kapsamlı liste yöntemiyle:
        liste = [öncekiListe [i] + öncekiListe [i+1] for i in range (len (öncekiListe)-1)]
        liste.insert (0,1)
        liste.append (1)
        # For-döngüsü yöntemiyle:
        #for i in range (len (öncekiListe) - 1):liste.append (öncekiListe[i] + öncekiListe[i+1])
        #liste += [1]
    return liste

print ("\n", sayı, " sayısı için Paskal üçgeni:", sep="")
for i in range (1, sayı+1): print ("{:d}:{:s}{}" .format (i, " "*(sayı-i+2), paskal (i)) )
#-----------------------------------------------------------------------------------------------------

def fib_paskal (n, fibKonum):
    if n == 1:
        liste = [1]
        fibToplam = 1 if fibKonum == 0 else 0
    else:
        liste = [1]
        (öncekiListe, fibToplam) = fib_paskal (n-1, fibKonum+1)
        for i in range (len(öncekiListe)-1): liste.append (öncekiListe[i] + öncekiListe[i+1])
        liste += [1]
        if fibKonum < len(liste): fibToplam += liste[fibKonum]
    return (liste, fibToplam)

def fib (n): return fib_paskal (n, 0)[1]  # [0] paskal listesini, [1] ise fibonaki toplamını verir...

print ("\nFibonaki", sayı, "sayısı açılımının Paskal üçgeniyle hesaplanması:\n0", end=" ")
for i in range (1, sayı): print (fib(i), end=" ")


"""Çıktı:
>python p_12104.py
13 (* 3=39) adet 3'ün katları sayılı Hanoi Kuleleri açılımı:
3 6 9 12 15 18 21 24 27 30 33 36 39

1'den itibaren ilk 13 sıralı sayının toplamı: 91

13 sayısı için Paskal üçgeni:
1:              [1]
2:             [1, 1]
3:            [1, 2, 1]
4:           [1, 3, 3, 1]
5:          [1, 4, 6, 4, 1]
6:         [1, 5, 10, 10, 5, 1]
7:        [1, 6, 15, 20, 15, 6, 1]
8:       [1, 7, 21, 35, 35, 21, 7, 1]
9:      [1, 8, 28, 56, 70, 56, 28, 8, 1]
10:     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
11:    [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]
12:   [1, 11, 55, 165, 330, 462, 462, 330, 165, 55, 11, 1]
13:  [1, 12, 66, 220, 495, 792, 924, 792, 495, 220, 66, 12, 1]

Fibonaki 13 sayısı açılımının Paskal üçgeniyle hesaplanması:
0 1 1 2 3 5 8 13 21 34 55 89 144
"""