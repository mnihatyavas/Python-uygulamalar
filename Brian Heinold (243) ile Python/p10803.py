# coding:iso-8859-9 T�rk�e

from string import punctuation

dizge = "M.Nihat Yava�; Ye�ilyurt-Malatya; 17.04.1957"
print ("Dizge:", dizge)
for k in punctuation: dizge = dizge.replace (k, " ")
dizge = dizge.replace ("  ", " ")
liste = dizge.lower().split (" ")
print ("\nSplit'le liste:", liste)
print ("\nJoin'le tekrar liste'den arabo�luklu dizgeye:", " ".join (liste))
print ("\nJoin'le liste'den bo�luksuz dizgeye:", "".join (liste))
print ("\nJoin'le liste'den tireli dizgeye:", "-".join (liste))
print ("\nJoin'le liste'den �ift y�ld�zl� dizgeye:", "**".join (liste))
print ("\nJoin'le liste'den virg�l-bo�luklu dizgeye:", ", ".join (liste))

from random import shuffle

kelime = input ("\n10 adet anagram� t�retilecek kelimeyi girin: ").lower()
if len (kelime) == 0: kelime = "malatya"
liste = list (kelime)
for i in range (10):
    shuffle (liste)
    print (''.join (liste), end=" ")
