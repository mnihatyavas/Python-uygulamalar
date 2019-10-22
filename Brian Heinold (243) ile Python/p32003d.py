# coding:iso-8859-9 Türkçe

import os

i = 0
# python ve altdizinlerindeki TÜM dosyaların dökümü 20'şer ekran satırıyla listelenecek...
for (yol, dizinler, dosyalar) in os.walk ("C:/Users/pc/Desktop/MyFiles/4. Dersler/python/"):
    for dosya in dosyalar:
            #if dosya [-3:] == ".py": ==>Sadece .py dosyaları listelenir...
            print (dosya)
            i +=1
            if i%20 == 0: input ("\nEnt")
print ("\n\nİşlem tamamlandı!..")