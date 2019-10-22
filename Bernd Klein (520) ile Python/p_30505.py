# coding:iso-8859-9 Türkçe
# p_30505.py: Sıfır boyut (6,) diziyi newaxis, transpose ve concatenate ile 2 boyut ve (6,4)-(4,6) şekillere çevirme örneği.

import numpy as np

x = np.array ([2, 5, 18, 14, 4, -9])
x1 = x[np.newaxis, :]
x2 = np.concatenate ((x1, x1, x1, x1)).transpose()
x3 = x2.transpose()

x4 = np.array ([[2,5,18,14,4,-9],]*4)
x5 = np.array ([[2,5,18,14,4,-9],]*4).transpose()

print ("x(6,) dizisi: ", x, "==>", x.shape,
    "\n\nx1(1,6) matrisi:\n", x1, "==>", x1.shape,
    "\n\nx2(6,4) np.concatenate((x1,x1,x1,x1)).transpose() matrisi:\n", x2, "==>", x2.shape,
    "\n\nx3(4,6) x2.transpose() matrisi:\n", x3, "==>", x3.shape,
    "\n\nx4(6,4) np.array ([2,5,18,14,4,-9],]*4) matrisi:\n", x4, "==>", x4.shape,
    "\n\nx5(4,6) np.array ([2,5,18,14,4,-9],]*4).transpose() matrisi:\n", x5, "==>", x5.shape,
    sep="")



"""Çıktı:
>python p_30505.py
x(6,) dizisi: [ 2  5 18 14  4 -9]==>(6,)

x1(1,6) matrisi:
[[ 2  5 18 14  4 -9]]==>(1, 6)

x2(6,4) np.concatenate((x1,x1,x1,x1)).transpose() matrisi:
[[ 2  2  2  2]
 [ 5  5  5  5]
 [18 18 18 18]
 [14 14 14 14]
 [ 4  4  4  4]
 [-9 -9 -9 -9]]==>(6, 4)

x3(4,6) x2.transpose() matrisi:
[[ 2  5 18 14  4 -9]
 [ 2  5 18 14  4 -9]
 [ 2  5 18 14  4 -9]
 [ 2  5 18 14  4 -9]]==>(4, 6)

x4(6,4) np.array ([2,5,18,14,4,-9],]*4) matrisi:
[[ 2  5 18 14  4 -9]
 [ 2  5 18 14  4 -9]
 [ 2  5 18 14  4 -9]
 [ 2  5 18 14  4 -9]]==>(4, 6)

x5(4,6) np.array ([2,5,18,14,4,-9],]*4).transpose() matrisi:
[[ 2  2  2  2]
 [ 5  5  5  5]
 [18 18 18 18]
 [14 14 14 14]
 [ 4  4  4  4]
 [-9 -9 -9 -9]]==>(6, 4)
"""