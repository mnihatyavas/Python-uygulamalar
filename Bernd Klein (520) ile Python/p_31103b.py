# coding:iso-8859-9 T�rk�e
# p_31103b.py: Numpy tamsay� dizi dtype ard���k verilerini tofile ve fromfile ile dosyaya yazma ve okuma �rne�i.

import numpy as np
import os

try: n1 = abs (int (input ("Tamsay� dizi eleman say�s� [50]? ")))
except: n1 = 50

try: n2 = abs (int (input ("Ka��nc� elemandan sonras�n� dosyadan okusun [son %20]? ")))
except: n2 = n1 - int (n1 / 5)

veriler = np.arange (n1, dtype=np.int32)
print ("\nDosyaya yaz�lacak veriler:\n", veriler, sep="")
veriler.tofile ("p_31103bx.txt") # Varsay�l� "bw" olarak yazar...
#---------------------------------------------------------------------------------------------

dosya = open ("p_31103bx.txt", "rb")
ilk = 4 * n2
dosya.seek (ilk, os.SEEK_SET)
x = np.fromfile (dosya, dtype=np.int32)
print ("\n", n2, ".inci kay�ttan sonras�n�n d�k�m�:\n", x, sep="")