# coding:iso-8859-9 T�rk�e
# p_31003a.py: Numpy dizisel bire-bir veya matrissel �arp�m �rne�i.

import numpy as np

x = np.array ([
    (2, 3),
    (3, 5) ])

y = np.array (( # [ veya ( olabilir...
   (1, 2),
    (5, -1) ))

z = x * y

print ("x dizisi:\n", x, " ==>�ekli: ", x.shape, "\n\ny dizisi:\n", y, " ==>�ekli: ", y.shape,
    "\n\n(np.array(x) * np.array(y)) bire-bir �arp�m dizisi:\n", z, " ==>�ekli: ", z.shape, sep="")
print ("-"*79)
#-------------------------------------------------------------------------------------------

x = np.matrix (x)
y = np.matrix (y)
z = x * y

print ("Matris �arp�m� i�in enaz biri np.matris(x) olarak tan�mlanmal�, veya \
    np.dot(x,y) ile �arp�lmal�, yada np.mat(x) * np.mat(y) �eklinde �arp�lmal�d�r==>")
print ("\n(np.matrix(x) * np.matrix (y)) matrissel �arp�m�:\n", z, " ==>�ekli: ", z.shape, sep="")
print ("-"*79)
#-------------------------------------------------------------------------------------------

x = np.array (x)
y = np.matrix (y)
z = x * y

print ("(np.array(x) * np.matrix(y)) matrissel �arp�m�:\n", z, " ==>�ekli: ", z.shape, sep="")
print ("-"*79)
#-------------------------------------------------------------------------------------------

x = np.array (x)
y = np.array (y)
z = np.mat (x) * np.mat (y)

print ("(np.mat(np.array(x)) * np.mat(np.array(y))) matrissel �arp�m�:\n", z, " ==>�ekli: ", z.shape, sep="")
print ("-"*79)
#-------------------------------------------------------------------------------------------

x = np.array (x)
y = np.array (y)
z = np.dot (x, y)

print ("(np.dot(np.array(x), np.array(*y)) matrissel �arp�m�:\n", z, " ==>�ekli: ", z.shape, sep="")



"""��kt�:
>python p_31003.py
x dizisi:
[[2 3]
 [3 5]] ==>�ekli: (2, 2)

y dizisi:
[[ 1  2]
 [ 5 -1]] ==>�ekli: (2, 2)

(np.array(x) * np.array(y)) bire-bir �arp�m dizisi:
[[ 2  6]
 [15 -5]] ==>�ekli: (2, 2)
-------------------------------------------------------------------------------
Matris �arp�m� i�in enaz biri np.matris(x) olarak tan�mlanmal�, veya
np.dot(x,y) ile �arp�lmal�, yada np.mat(x) * np.mat(y) �eklinde �arp�lmal�d�r==>

(np.matrix(x) * np.matrix (y)) matrissel �arp�m�:
[[17  1]
 [28  1]] ==>�ekli: (2, 2)
-------------------------------------------------------------------------------
(np.array(x) * np.matrix(y)) matrissel �arp�m�:
[[17  1]
 [28  1]] ==>�ekli: (2, 2)
-------------------------------------------------------------------------------
(np.mat(np.array(x)) * np.mat(np.array(y))) matrissel �arp�m�:
[[17  1]
 [28  1]] ==>�ekli: (2, 2)
-------------------------------------------------------------------------------
(np.dot(np.array(x), np.array(y)) matrissel �arp�m�:
[[17  1]
 [28  1]] ==>�ekli: (2, 2)
"""