# coding:iso-8859-9 Türkçe
# p_31103b.py: Numpy tamsayı dizi dtype ardışık verilerini tofile ve fromfile ile dosyaya yazma ve okuma örneği.

import numpy as np
import os

try: n1 = abs (int (input ("Tamsayı dizi eleman sayısı [50]? ")))
except: n1 = 50

try: n2 = abs (int (input ("Kaçıncı elemandan sonrasını dosyadan okusun [son %20]? ")))
except: n2 = n1 - int (n1 / 5)

veriler = np.arange (n1, dtype=np.int32)
print ("\nDosyaya yazılacak veriler:\n", veriler, sep="")
veriler.tofile ("p_31103bx.txt") # Varsayılı "bw" olarak yazar...
#---------------------------------------------------------------------------------------------

dosya = open ("p_31103bx.txt", "rb")
ilk = 4 * n2
dosya.seek (ilk, os.SEEK_SET)
x = np.fromfile (dosya, dtype=np.int32)
print ("\n", n2, ".inci kayıttan sonrasının dökümü:\n", x, sep="")