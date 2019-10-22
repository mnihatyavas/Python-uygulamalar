# coding:iso-8859-9 Türkçe
# p_31003b.py: Numpy dizisel veya matrissel bire-bir bölüm örneği.

import numpy as np

x = np.array ([
    (2, 3),
    (3, 5) ])

y = np.array (( # [ veya ( olabilir...
   (1, 2),
    (5, -1) ))

z = x / y

print ("x dizisi:\n", x, " ==>Şekli: ", x.shape, "\n\ny dizisi:\n", y, " ==>Şekli: ", y.shape,
    "\n\n(np.array(x) * np.array(y)) bire-bir bölüm dizisi:\n", z, " ==>Şekli: ", z.shape, sep="")
print ("-"*50)
#-------------------------------------------------------------------------------------------

x = np.matrix (x)
y = np.matrix (y)
z = x / y

print ("Matris bölümü yoktur, her halukarda bire-bir bölüm yapar==>")
print ("\n(np.matrix(x) / np.matrix (y)) matrissel bölümü:\n", z, " ==>Şekli: ", z.shape, sep="")



"""Çıktı:
>python p_31003b.py
x dizisi:
[[2 3]
 [3 5]] ==>Şekli: (2, 2)

y dizisi:
[[ 1  2]
 [ 5 -1]] ==>Şekli: (2, 2)

(np.array(x) * np.array(y)) bire-bir bölüm dizisi:
[[ 2.   1.5]
 [ 0.6 -5. ]] ==>Şekli: (2, 2)
--------------------------------------------------
Matris bölümü yoktur, her halukarda bire-bir bölüm yapar==>

(np.matrix(x) / np.matrix (y)) matrissel bölümü:
[[ 2.   1.5]
 [ 0.6 -5. ]] ==>Şekli: (2, 2)
"""