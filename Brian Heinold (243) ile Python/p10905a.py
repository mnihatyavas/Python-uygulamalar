#coding:iso-8859-9 Türkçe

from random import randint
tesadüfi_sayı = randint(0,100)
tahmin_kereniz = 0
tahmininiz = tahmininiz1 = 0
tahmininiz2 = 100
while tahmininiz != tesadüfi_sayı and tahmin_kereniz <= 9:
    if tahmininiz > tahmininiz1: tahmininiz = eval (input ("Tahmininiz (" + str(tahmininiz - (tahmininiz2 - tahmininiz1)//2) + "): "))
    else: tahmininiz = eval (input ("Tahmininiz (" + str(tahmininiz + (tahmininiz2 - tahmininiz1)//2) + "): "))
    tahmin_kereniz +=1
    if tahmininiz < tesadüfi_sayı: print (tahmin_kereniz, ": DAHA YÜKSEK [", tahmininiz, "->", tahmininiz2, "] GİR", sep=""); tahmininiz1 = tahmininiz
    elif tahmininiz > tesadüfi_sayı: print (tahmin_kereniz, ": DAHA DÜŞÜK [", tahmininiz1, "->", tahmininiz, "] GİR", sep=""); tahmininiz2 = tahmininiz
    else: print (tahmin_kereniz, '.tahminde BULDUNUZ!', sep="")

if tahmin_kereniz > 9: print ('\nKAYBETTİNİZ. Doğru tahmin', tesadüfi_sayı, "olmalıydı!")
