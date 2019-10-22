# coding:iso-8859-9 T�rk�e
# p_30708.py: Ayn� numaral� tesad�fi tohumla hep ayn� geli�ig�zel say�lar�n �retilmesi �rne�i.

import random

help (random.seed)

print ("1 no'lu tesad�fi tohumla geli�ig�zel say�lar yaratal�m:")
random.seed (1)
for _ in range (10): print (random.randint (-50, 51), end=", ")

print ("\nEkti�imiz 1 no'lu tesad�fi tohum numaras�yla ayn� say�lar� tekrardan yaratal�m:")
random.seed (1)
for _ in range (10): print (random.randint (-50, 51), end=", ")



"""��kt�:
>python p_30708.py
Help on method seed in module random:

seed(a=None, version=2) method of random.Random instance
    Initialize internal state from hashable object.

    None or no argument seeds from current time or from an operating
    system specific randomness source if available.

    If *a* is an int, all bits are used.

    For version 2 (the default), all of the bits are used if *a* is a str,
    bytes, or bytearray.  For version 1 (provided for reproducing random
    sequences from older versions of Python), the algorithm for str and
    bytes generates a narrower range of seeds.

1 no'lu tesad�fi tohumla geli�ig�zel say�lar yaratal�m:
-33, 22, 47, -42, -18, -35, 13, 47, 7, 10,
Ekti�imiz 1 no'lu tesad�fi tohum numaras�yla ayn� say�lar� tekrardan yaratal�m:
-33, 22, 47, -42, -18, -35, 13, 47, 7, 10,

>python p_30708.py  ** TEKRAR **
1 no'lu tesad�fi tohumla geli�ig�zel say�lar yaratal�m:
-33, 22, 47, -42, -18, -35, 13, 47, 7, 10,
Ekti�imiz 1 no'lu tesad�fi tohum numaras�yla ayn� say�lar� tekrardan yaratal�m:
-33, 22, 47, -42, -18, -35, 13, 47, 7, 10,
"""