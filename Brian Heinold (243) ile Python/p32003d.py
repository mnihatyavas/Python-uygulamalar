# coding:iso-8859-9 T�rk�e

import os

i = 0
# python ve altdizinlerindeki T�M dosyalar�n d�k�m� 20'�er ekran sat�r�yla listelenecek...
for (yol, dizinler, dosyalar) in os.walk ("C:/Users/pc/Desktop/MyFiles/4. Dersler/python/"):
    for dosya in dosyalar:
            #if dosya [-3:] == ".py": ==>Sadece .py dosyalar� listelenir...
            print (dosya)
            i +=1
            if i%20 == 0: input ("\nEnt")
print ("\n\n��lem tamamland�!..")