# coding:iso-8859-9 Türkçe
# p_31104.py: Numpy tamsayı ardışık diziyi save ve load ile geçici dosyaya yazma ve okuma örneği.

import numpy as np
from tempfile import TemporaryFile as TF

try: n1 = abs (int (input ("Tamsayı dizi eleman sayısı [50]? ")))
except: n1 = 50

x = np.arange (n1)
print ("\nNumpy tamsayı dizisi:\n", x, sep="")

dosya = TF()
np.save (dosya, x)

#---------------------------------------------------------------------------------------------------
dosya.seek (0) # Geçici dosyayı kapatıp açmak için...
y = np.load (dosya)

print ("\nGeçici dosyadan okunan dizi dökümü:\n", y, sep="")

# Ayrıca loadtxt benzeri np.genfromtxt(filename, delimiter=",", dtype=None) ve
# daha kısası recfromcvs de kullanılabilir...



"""Çıktı:
>python p_31104.py
Tamsayı dizi eleman sayısı [50]?

Numpy tamsayı dizisi:
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49]

Geçici dosyadan okunan dizi dökümü:
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49]
"""