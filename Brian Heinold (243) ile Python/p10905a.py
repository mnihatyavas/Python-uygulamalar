#coding:iso-8859-9 T�rk�e

from random import randint
tesad�fi_say� = randint(0,100)
tahmin_kereniz = 0
tahmininiz = tahmininiz1 = 0
tahmininiz2 = 100
while tahmininiz != tesad�fi_say� and tahmin_kereniz <= 9:
    if tahmininiz > tahmininiz1: tahmininiz = eval (input ("Tahmininiz (" + str(tahmininiz - (tahmininiz2 - tahmininiz1)//2) + "): "))
    else: tahmininiz = eval (input ("Tahmininiz (" + str(tahmininiz + (tahmininiz2 - tahmininiz1)//2) + "): "))
    tahmin_kereniz +=1
    if tahmininiz < tesad�fi_say�: print (tahmin_kereniz, ": DAHA Y�KSEK [", tahmininiz, "->", tahmininiz2, "] G�R", sep=""); tahmininiz1 = tahmininiz
    elif tahmininiz > tesad�fi_say�: print (tahmin_kereniz, ": DAHA D���K [", tahmininiz1, "->", tahmininiz, "] G�R", sep=""); tahmininiz2 = tahmininiz
    else: print (tahmin_kereniz, '.tahminde BULDUNUZ!', sep="")

if tahmin_kereniz > 9: print ('\nKAYBETT�N�Z. Do�ru tahmin', tesad�fi_say�, "olmal�yd�!")
