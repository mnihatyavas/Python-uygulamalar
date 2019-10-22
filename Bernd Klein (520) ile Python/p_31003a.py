# coding:iso-8859-9 Türkçe
# p_31003a.py: Numpy dizisel bire-bir veya matrissel çarpım örneği.

import numpy as np

x = np.array ([
    (2, 3),
    (3, 5) ])

y = np.array (( # [ veya ( olabilir...
   (1, 2),
    (5, -1) ))

z = x * y

print ("x dizisi:\n", x, " ==>Şekli: ", x.shape, "\n\ny dizisi:\n", y, " ==>Şekli: ", y.shape,
    "\n\n(np.array(x) * np.array(y)) bire-bir çarpım dizisi:\n", z, " ==>Şekli: ", z.shape, sep="")
print ("-"*79)
#-------------------------------------------------------------------------------------------

x = np.matrix (x)
y = np.matrix (y)
z = x * y

print ("Matris çarpımı için enaz biri np.matris(x) olarak tanımlanmalı, veya \
    np.dot(x,y) ile çarpılmalı, yada np.mat(x) * np.mat(y) şeklinde çarpılmalıdır==>")
print ("\n(np.matrix(x) * np.matrix (y)) matrissel çarpımı:\n", z, " ==>Şekli: ", z.shape, sep="")
print ("-"*79)
#-------------------------------------------------------------------------------------------

x = np.array (x)
y = np.matrix (y)
z = x * y

print ("(np.array(x) * np.matrix(y)) matrissel çarpımı:\n", z, " ==>Şekli: ", z.shape, sep="")
print ("-"*79)
#-------------------------------------------------------------------------------------------

x = np.array (x)
y = np.array (y)
z = np.mat (x) * np.mat (y)

print ("(np.mat(np.array(x)) * np.mat(np.array(y))) matrissel çarpımı:\n", z, " ==>Şekli: ", z.shape, sep="")
print ("-"*79)
#-------------------------------------------------------------------------------------------

x = np.array (x)
y = np.array (y)
z = np.dot (x, y)

print ("(np.dot(np.array(x), np.array(*y)) matrissel çarpımı:\n", z, " ==>Şekli: ", z.shape, sep="")



"""Çıktı:
>python p_31003.py
x dizisi:
[[2 3]
 [3 5]] ==>Şekli: (2, 2)

y dizisi:
[[ 1  2]
 [ 5 -1]] ==>Şekli: (2, 2)

(np.array(x) * np.array(y)) bire-bir çarpım dizisi:
[[ 2  6]
 [15 -5]] ==>Şekli: (2, 2)
-------------------------------------------------------------------------------
Matris çarpımı için enaz biri np.matris(x) olarak tanımlanmalı, veya
np.dot(x,y) ile çarpılmalı, yada np.mat(x) * np.mat(y) şeklinde çarpılmalıdır==>

(np.matrix(x) * np.matrix (y)) matrissel çarpımı:
[[17  1]
 [28  1]] ==>Şekli: (2, 2)
-------------------------------------------------------------------------------
(np.array(x) * np.matrix(y)) matrissel çarpımı:
[[17  1]
 [28  1]] ==>Şekli: (2, 2)
-------------------------------------------------------------------------------
(np.mat(np.array(x)) * np.mat(np.array(y))) matrissel çarpımı:
[[17  1]
 [28  1]] ==>Şekli: (2, 2)
-------------------------------------------------------------------------------
(np.dot(np.array(x), np.array(y)) matrissel çarpımı:
[[17  1]
 [28  1]] ==>Şekli: (2, 2)
"""