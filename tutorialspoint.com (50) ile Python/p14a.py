# coding:iso-8859-9 Türkçe
# Python 3 - Files I/O

print ("Python gerçekten de büyük bir dil,", "değil mi?")

veri = input ("Bir veri girin: ")
print ("Girdiğiniz veri: [" + veri + "]\n")

dosya = open ("dosya1.txt", "a+")
print ("Dosyanın adı:", dosya.name)
print ("Şuanda kapalı mı?", dosya.closed)
print ("Dosya açılma kipi:", dosya.mode)
dosya.write (veri + "\nPython gerçekten de muhteşem bir dil, değil mi?\nTabii ki!\n")
dosya.close()
print ("Peki şimdi kapalı mı?", dosya.closed)
print()

dosya1 = open ("dosya1.txt", "r+")
dizge = dosya1.read()
print ("Dosyadan okunanlar:", dizge)
print ("Dosya konum göstergesi:", dosya1.tell())
print ("Dosyadan okunanlar:", dosya1.read())
print ("\nDosya konum göstergesi:", dosya1.seek (0, 0))
print ("Dosyadan okunanlar:", dosya1.read())
dosya1.close()

import os
try:os.remove ("dosya2.txt")
except Exception: # Boşgeç...
    print()
os.rename ( "dosya1.txt", "dosya2.txt" )
