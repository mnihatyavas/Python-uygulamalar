# coding:iso-8859-9 T�rk�e
# p_31003b.py: Numpy dizisel veya matrissel bire-bir b�l�m �rne�i.

import numpy as np

x = np.array ([
    (2, 3),
    (3, 5) ])

y = np.array (( # [ veya ( olabilir...
   (1, 2),
    (5, -1) ))

z = x / y

print ("x dizisi:\n", x, " ==>�ekli: ", x.shape, "\n\ny dizisi:\n", y, " ==>�ekli: ", y.shape,
    "\n\n(np.array(x) * np.array(y)) bire-bir b�l�m dizisi:\n", z, " ==>�ekli: ", z.shape, sep="")
print ("-"*50)
#-------------------------------------------------------------------------------------------

x = np.matrix (x)
y = np.matrix (y)
z = x / y

print ("Matris b�l�m� yoktur, her halukarda bire-bir b�l�m yapar==>")
print ("\n(np.matrix(x) / np.matrix (y)) matrissel b�l�m�:\n", z, " ==>�ekli: ", z.shape, sep="")



"""��kt�:
>python p_31003b.py
x dizisi:
[[2 3]
 [3 5]] ==>�ekli: (2, 2)

y dizisi:
[[ 1  2]
 [ 5 -1]] ==>�ekli: (2, 2)

(np.array(x) * np.array(y)) bire-bir b�l�m dizisi:
[[ 2.   1.5]
 [ 0.6 -5. ]] ==>�ekli: (2, 2)
--------------------------------------------------
Matris b�l�m� yoktur, her halukarda bire-bir b�l�m yapar==>

(np.matrix(x) / np.matrix (y)) matrissel b�l�m�:
[[ 2.   1.5]
 [ 0.6 -5. ]] ==>�ekli: (2, 2)
"""