# coding:iso-8859-9 Türkçe

from random import randint

sayı = randint (1,5)
tahmin = eval (input ('Bir sayı tahminle [1->5]: '))
if tahmin==sayı: print ('Bravo, tutturdunuz!')
else: print ('Maalesef, tutturamadınız!')