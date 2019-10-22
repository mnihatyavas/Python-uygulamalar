# coding:iso-8859-9 T�rk�e
# p_30602.py: 10bin adet normal, g�venli ve numpy tesad�fi say� �retim 400/15/1 mS zamanlamalar� �rne�i.

import random
from time import time as Z

z1 = Z()
kripto = random.SystemRandom()
[kripto.random() for _ in range (10000)]
print ("10 000 adet g�venli geli�ig�zel say� �retim zaman�: ", (Z() - z1) * 1000, " mS'dir.", sep="")

z1 = Z()
[random.random() for _ in range (10000)]
print ("10 000 adet normal geli�ig�zel say� �retim zaman�: ", (Z() - z1) * 1000, " mS'dir.", sep="")

import numpy as np
z1 = Z()
np.random.random (10000) # Saptanabilirdir...
print ("10 000 adet np geli�ig�zel say� �retim zaman�: ", (Z() - z1) * 1000, " mS'dir.", sep="")



"""��kt�:
>python p_30602.py
10 000 adet g�venli geli�ig�zel say� �retim zaman�: 373.02160263061523 mS'dir.
10 000 adet normal geli�ig�zel say� �retim zaman�: 14.000892639160156 mS'dir.
10 000 adet np geli�ig�zel say� �retim zaman�: 0.9999275207519531 mS'dir.

>python p_30602.py  ** TEKRAR **
10 000 adet g�venli geli�ig�zel say� �retim zaman�: 429.02445793151855 mS'dir.
10 000 adet normal geli�ig�zel say� �retim zaman�: 17.000913619995117 mS'dir.
10 000 adet np geli�ig�zel say� �retim zaman�: 2.000093460083008 mS'dir.

>python p_30602.py  ** TEKRAR **
10 000 adet g�venli geli�ig�zel say� �retim zaman�: 386.02209091186523 mS'dir.
10 000 adet normal geli�ig�zel say� �retim zaman�: 17.00115203857422 mS'dir.
10 000 adet np geli�ig�zel say� �retim zaman�: 1.0001659393310547 mS'dir.
"""