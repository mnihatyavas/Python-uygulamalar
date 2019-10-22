# coding:iso-8859-9 Türkçe
# p_30602.py: 10bin adet normal, güvenli ve numpy tesadüfi sayı üretim 400/15/1 mS zamanlamaları örneği.

import random
from time import time as Z

z1 = Z()
kripto = random.SystemRandom()
[kripto.random() for _ in range (10000)]
print ("10 000 adet güvenli gelişigüzel sayı üretim zamanı: ", (Z() - z1) * 1000, " mS'dir.", sep="")

z1 = Z()
[random.random() for _ in range (10000)]
print ("10 000 adet normal gelişigüzel sayı üretim zamanı: ", (Z() - z1) * 1000, " mS'dir.", sep="")

import numpy as np
z1 = Z()
np.random.random (10000) # Saptanabilirdir...
print ("10 000 adet np gelişigüzel sayı üretim zamanı: ", (Z() - z1) * 1000, " mS'dir.", sep="")



"""Çıktı:
>python p_30602.py
10 000 adet güvenli gelişigüzel sayı üretim zamanı: 373.02160263061523 mS'dir.
10 000 adet normal gelişigüzel sayı üretim zamanı: 14.000892639160156 mS'dir.
10 000 adet np gelişigüzel sayı üretim zamanı: 0.9999275207519531 mS'dir.

>python p_30602.py  ** TEKRAR **
10 000 adet güvenli gelişigüzel sayı üretim zamanı: 429.02445793151855 mS'dir.
10 000 adet normal gelişigüzel sayı üretim zamanı: 17.000913619995117 mS'dir.
10 000 adet np gelişigüzel sayı üretim zamanı: 2.000093460083008 mS'dir.

>python p_30602.py  ** TEKRAR **
10 000 adet güvenli gelişigüzel sayı üretim zamanı: 386.02209091186523 mS'dir.
10 000 adet normal gelişigüzel sayı üretim zamanı: 17.00115203857422 mS'dir.
10 000 adet np gelişigüzel sayı üretim zamanı: 1.0001659393310547 mS'dir.
"""