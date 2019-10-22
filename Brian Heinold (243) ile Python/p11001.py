# coding:iso-8859-9 T�rk�e

print ("1->10000 aras� palindromik (tersiyle ayn�) say�lar yanyana:", end=" ")
for i in range (1,10001):
    dizge = str (i)
    if dizge == dizge[::-1]: print (dizge, end=" ")

do�um_g�n� = 'Haziran 1, 1991'
y�l = int (do�um_g�n�[-4:])
print ("\n\nDo�um g�n�n�z:", do�um_g�n�, "ise bu g�nk� ya��n�z:", 2018 - y�l, "olur.")
do�um_g�n� = '17 Nisan 1957'
y�l = int (do�um_g�n�[-4:])
print ("Do�um g�n�n�z:", do�um_g�n�, "ise bu g�nk� ya��n�z:", 2018 - y�l, "olur.")
do�um_g�n� = '07/08/1955'
y�l = int (do�um_g�n�[-4:])
print ("Do�um g�n�n�z:", do�um_g�n�, "ise bu g�nk� ya��n�z:", 2018 - y�l, "olur.")
do�um_g�n� = '7.8.1955'
y�l = int (do�um_g�n�[-4:])
print ("Do�um g�n�n�z:", do�um_g�n�, "ise bu g�nk� ya��n�z:", 2018 - y�l, "olur.")

from random import randint
say� = randint (10, 100000)
dizge = str (say�)
toplam = 0
for i in range (len (dizge)): toplam += int (dizge[i])
print ("\nGeli�ig�zel", dizge, "say�s�n�n toplam�:", toplam)
print ("Ayn� toplam kapsaml� liste y�ntemiyle:", sum ([int (dizge) for dizge in str (say�)]))

ters = ""
for i in range (len (dizge)): ters = dizge[i] + ters
print ("Geli�ig�zel", dizge, "say�s�n�n tersi:", ters)

from random import random
say� = randint (1, 100000) + random()
tamsay� = int (say�)
k�s�rat = say� - tamsay�
print ("\nSay�m�z:", say�, ", tamsay� k�sm�:", tamsay�, "ve k�s�rat k�sm�:", k�s�rat)

say� = randint (2, 1000)
for i in range (2, int (say�**0.5)+1):
    if say� % i == 0: break
else: print ("\nKendisi ve 1'den ba�ka b�leni olmayan", say�, "asald�r.")
