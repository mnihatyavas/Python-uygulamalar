#coding:iso-8859-9 "T�rk�e"

dosya = open ("demo1.txt", "a")
dosya.write ("�imdi dosyam�za bir sat�r daha eklendi!\n")
dosya.close()

dosya = open ("demo1.txt", "r")

# print (dosya.read())
# dosya = close ("demo1.txt")

for x in dosya:
   print(x)
dosya.close()

import os
if os.path.exists ("demo2.txt"):
    os.remove ("demo2.txt")
else:
    print ("Silinecek [demo2.txt] dosyas� mevcut de�il!")