# coding:iso-8859-9 T�rk�e
# p_31104.py: Numpy tamsay� ard���k diziyi save ve load ile ge�ici dosyaya yazma ve okuma �rne�i.

import numpy as np
from tempfile import TemporaryFile as TF

try: n1 = abs (int (input ("Tamsay� dizi eleman say�s� [50]? ")))
except: n1 = 50

x = np.arange (n1)
print ("\nNumpy tamsay� dizisi:\n", x, sep="")

dosya = TF()
np.save (dosya, x)

#---------------------------------------------------------------------------------------------------
dosya.seek (0) # Ge�ici dosyay� kapat�p a�mak i�in...
y = np.load (dosya)

print ("\nGe�ici dosyadan okunan dizi d�k�m�:\n", y, sep="")

# Ayr�ca loadtxt benzeri np.genfromtxt(filename, delimiter=",", dtype=None) ve
# daha k�sas� recfromcvs de kullan�labilir...



"""��kt�:
>python p_31104.py
Tamsay� dizi eleman say�s� [50]?

Numpy tamsay� dizisi:
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49]

Ge�ici dosyadan okunan dizi d�k�m�:
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49]
"""