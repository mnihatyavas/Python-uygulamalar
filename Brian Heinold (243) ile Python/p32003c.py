# coding:iso-8859-9 T�rk�e

import os

print ("Dizge'den Liste'ye==>", os.path.split ("C:/Users/pc/Desktop/MyFiles/4. Dersler/python/"))
print ("Yal�n dosya ad�==>", os.path.basename ("C:/Users/pc/Desktop/MyFiles/4. Dersler/python/p32003c.py"))
print ("Yal�n dizin ad�==>", os.path.dirname ("C:/Users/pc/Desktop/MyFiles/4. Dersler/python/p32003c.py"))
print ("Liste'den Dizge'ye==>", os.path.join ("dizin", "mny1.txt"))
#-------------------------------------------------------------------------------------

print()
if os.path.exists ("mny1.txt"):
    os.remove ("mny1.txt")
    print ("<mny1.txt> dosyas� silindi!..")
else: print ("<mny1.txt> dosyas� YOK...")
#-------------------------------------------------------------------------------------

print()
dizin = "C:/Users/pc/Desktop/MyFiles/4. Dersler/python/"
dosyalar = os.listdir (dizin)
for d in dosyalar: print ("{} dosyas�n�n ebat�: {} byte" .format (d, os.path.getsize (d)) )
