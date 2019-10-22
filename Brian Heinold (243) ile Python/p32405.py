# coding:iso-8859-9 Türkçe

from collections import *

dizge = "Bu fonksiyon verili dizge içerik karakterlerinin tekrar sayısını karakter-tekrar çifti olarak ilk-rastlanan sırada içerir."
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
print ("\nCounter anahtar:değer çifti dökümü:")
for i in range (len (L) ): print (L[i][0], ":", L[i][1], sep="", end=" ")
#----------------------------------------------------------------------------------------------

print ("\n\nAzalan rastlanma sıklığıyla döküm:", sayar.most_common() )
print ("\nArtan rastlanma sıklığıyla döküm:", sayar.most_common()[::-1] )
print ("\nEn sık rastlanan 3 karakter azalan sırada:", sayar.most_common (3) )
print ("\nEn sık rastlanan 3 karakter artan sırada:", sayar.most_common (3)[::-1] )
print ("\nEn az rastlanan 3 karakter azalan sırada:", sayar.most_common()[-3:] )
print ("\nEn az rastlanan 3 karakter artan sırada:", sayar.most_common()[:-4:-1] )
