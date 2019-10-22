# coding:iso-8859-9 T�rk�e
# p_12104.py: Hanoi kule a��l�m�, paskal kulesi, fibonakinin paskal ��kar�m� �rne�i.

from random import randint

def art�r3 (n):
    if n == 1: return 3
    else: return art�r3 (n-1) + 3

say� = randint (1,15)
print (say�, " (* 3=", say�*3, ") adet 3'�n katlar� say�l� Hanoi Kuleleri a��l�m�:", sep="")
for i in range (1,say�+1): print (art�r3 (i), end=" ")
#-----------------------------------------------------------------------------------------------------

def topla (n):
    if n== 0: return 0
    else: return n + topla (n-1)

print ("\n\n1'den itibaren ilk", say�, "s�ral� say�n�n toplam�:", topla (say�) )
#-----------------------------------------------------------------------------------------------------

def paskal (n):
    if n == 1: return [1]
    else:
        liste = [1]
        �ncekiListe = paskal (n-1)
        # Kapsaml� liste y�ntemiyle:
        liste = [�ncekiListe [i] + �ncekiListe [i+1] for i in range (len (�ncekiListe)-1)]
        liste.insert (0,1)
        liste.append (1)
        # For-d�ng�s� y�ntemiyle:
        #for i in range (len (�ncekiListe) - 1):liste.append (�ncekiListe[i] + �ncekiListe[i+1])
        #liste += [1]
    return liste

print ("\n", say�, " say�s� i�in Paskal ��geni:", sep="")
for i in range (1, say�+1): print ("{:d}:{:s}{}" .format (i, " "*(say�-i+2), paskal (i)) )
#-----------------------------------------------------------------------------------------------------

def fib_paskal (n, fibKonum):
    if n == 1:
        liste = [1]
        fibToplam = 1 if fibKonum == 0 else 0
    else:
        liste = [1]
        (�ncekiListe, fibToplam) = fib_paskal (n-1, fibKonum+1)
        for i in range (len(�ncekiListe)-1): liste.append (�ncekiListe[i] + �ncekiListe[i+1])
        liste += [1]
        if fibKonum < len(liste): fibToplam += liste[fibKonum]
    return (liste, fibToplam)

def fib (n): return fib_paskal (n, 0)[1]  # [0] paskal listesini, [1] ise fibonaki toplam�n� verir...

print ("\nFibonaki", say�, "say�s� a��l�m�n�n Paskal ��geniyle hesaplanmas�:\n0", end=" ")
for i in range (1, say�): print (fib(i), end=" ")


"""��kt�:
>python p_12104.py
13 (* 3=39) adet 3'�n katlar� say�l� Hanoi Kuleleri a��l�m�:
3 6 9 12 15 18 21 24 27 30 33 36 39

1'den itibaren ilk 13 s�ral� say�n�n toplam�: 91

13 say�s� i�in Paskal ��geni:
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

Fibonaki 13 say�s� a��l�m�n�n Paskal ��geniyle hesaplanmas�:
0 1 1 2 3 5 8 13 21 34 55 89 144
"""