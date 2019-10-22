# coding:iso-8859-9 T�rk�e

from collections import *

dizge = "Bu fonksiyon verili dizge i�erik karakterlerinin tekrar say�s�n� karakter-tekrar �ifti olarak ilk-rastlanan s�rada i�erir."
sayar = Counter (dizge)

print ("sayar=Counter(dizge):", sayar)

print ("\nlist(sayar.items()):", list (sayar.items()) )
print ("\nlist(sayar.keys()):", list (sayar.keys()) )
print ("\nlist(sayar.values()):", list (sayar.values()) )
print ("\nsayar['a']:", sayar['a'] )
print ("sayar[' ']:", sayar[' '] )
print ("sayar['-']:", sayar['-'] )
print ("sayar['.']:", sayar['.'] )
#----------------------------------------------------------------------------------------------

L = list (sayar.items() )
print ("\nDizge = [", dizge, "]", sep="")
print ("\nCounter anahtar:de�er �ifti d�k�m�:")
for i in range (len (L) ): print (L[i][0], ":", L[i][1], sep="", end=" ")
#----------------------------------------------------------------------------------------------

print ("\n\nAzalan rastlanma s�kl���yla d�k�m:", sayar.most_common() )
print ("\nArtan rastlanma s�kl���yla d�k�m:", sayar.most_common()[::-1] )
print ("\nEn s�k rastlanan 3 karakter azalan s�rada:", sayar.most_common (3) )
print ("\nEn s�k rastlanan 3 karakter artan s�rada:", sayar.most_common (3)[::-1] )
print ("\nEn az rastlanan 3 karakter azalan s�rada:", sayar.most_common()[-3:] )
print ("\nEn az rastlanan 3 karakter artan s�rada:", sayar.most_common()[:-4:-1] )
