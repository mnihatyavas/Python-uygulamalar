# coding:iso-8859-9 T�rk�e
# Python 3 - Files I/O

print ("Python ger�ekten de b�y�k bir dil,", "de�il mi?")

veri = input ("Bir veri girin: ")
print ("Girdi�iniz veri: [" + veri + "]\n")

dosya = open ("dosya1.txt", "a+")
print ("Dosyan�n ad�:", dosya.name)
print ("�uanda kapal� m�?", dosya.closed)
print ("Dosya a��lma kipi:", dosya.mode)
dosya.write (veri + "\nPython ger�ekten de muhte�em bir dil, de�il mi?\nTabii ki!\n")
dosya.close()
print ("Peki �imdi kapal� m�?", dosya.closed)
print()

dosya1 = open ("dosya1.txt", "r+")
dizge = dosya1.read()
print ("Dosyadan okunanlar:", dizge)
print ("Dosya konum g�stergesi:", dosya1.tell())
print ("Dosyadan okunanlar:", dosya1.read())
print ("\nDosya konum g�stergesi:", dosya1.seek (0, 0))
print ("Dosyadan okunanlar:", dosya1.read())
dosya1.close()

import os
try:os.remove ("dosya2.txt")
except Exception: # Bo�ge�...
    print()
os.rename ( "dosya1.txt", "dosya2.txt" )
