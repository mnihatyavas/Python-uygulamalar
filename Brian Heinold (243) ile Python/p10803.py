# coding:iso-8859-9 Türkçe

from string import punctuation

dizge = "M.Nihat Yavaş; Yeşilyurt-Malatya; 17.04.1957"
print ("Dizge:", dizge)
for k in punctuation: dizge = dizge.replace (k, " ")
dizge = dizge.replace ("  ", " ")
liste = dizge.lower().split (" ")
print ("\nSplit'le liste:", liste)
print ("\nJoin'le tekrar liste'den araboşluklu dizgeye:", " ".join (liste))
print ("\nJoin'le liste'den boşluksuz dizgeye:", "".join (liste))
print ("\nJoin'le liste'den tireli dizgeye:", "-".join (liste))
print ("\nJoin'le liste'den çift yıldızlı dizgeye:", "**".join (liste))
print ("\nJoin'le liste'den virgül-boşluklu dizgeye:", ", ".join (liste))

from random import shuffle

kelime = input ("\n10 adet anagramı türetilecek kelimeyi girin: ").lower()
if len (kelime) == 0: kelime = "malatya"
liste = list (kelime)
for i in range (10):
    shuffle (liste)
    print (''.join (liste), end=" ")
