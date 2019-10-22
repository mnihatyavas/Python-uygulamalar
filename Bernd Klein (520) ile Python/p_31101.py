# coding:iso-8859-9 T�rk�e
# p_31101.py: Numpy dizisini disk dosyas�na savetxt ve loadtxt ile saklama ve okuma �rne�i.

import numpy as np

x = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]], np.int32)

print ("Numpy x dizisi:\n", x, " ==>", x.shape, sep="")

if input ("\nDosyaya yaz�lacak m� [e/h]? ") == "e":
    np.savetxt ("p_31101ax.txt", x) # Varsay�l� "%.18e" formatl�...
    np.savetxt ("p_31101bx.txt", x, fmt="%2.3f", delimiter=",")
    np.savetxt ("p_31101cx.txt", x, fmt="%04d", delimiter=" :-) ")

if input ("Dosya okunsun mu [Veri/Ent]: "):
    x1 = np.loadtxt ("p_31101ax.txt") # Varsay�l� "%f" formatla...
    x2 = np.loadtxt ("p_31101bx.txt", delimiter=",", usecols=(0, 2)) # Varsay�l� "%f" formatla...
    x3 = np.loadtxt ("p_31101cx.txt", delimiter=" :-) ", usecols=(1)) # Varsay�l� "%f" formatla...
    print ("\nNumpy x1 dizisi:\n", x1, " ==>", x1.shape,
        "\n\nNumpy x2 dizisi:\n", x2, " ==>", x2.shape,
        "\n\nNumpy x3 dizisi:\n", x3, " ==>", x3.shape, sep="")



"""��kt�:
>python p_31101.py
Numpy x dizisi:
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]] ==>(4, 3)

Dosyaya yaz�lacak m� [e/h]? e
Dosya okunsun mu [Veri/Ent]: 1

Numpy x1 dizisi:
[[ 1.  2.  3.]
 [ 4.  5.  6.]
 [ 7.  8.  9.]
 [10. 11. 12.]] ==>(4, 3)

Numpy x2 dizisi:
[[ 1.  3.]
 [ 4.  6.]
 [ 7.  9.]
 [10. 12.]] ==>(4, 2)

Numpy x3 dizisi:
[ 2.  5.  8. 11.] ==>(4,)

>python p_31101.py  ** TEKRAR **
Numpy x dizisi:
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]] ==>(4, 3)

Dosyaya yaz�lacak m� [e/h]?
Dosya okunsun mu [Veri/Ent]:
"""