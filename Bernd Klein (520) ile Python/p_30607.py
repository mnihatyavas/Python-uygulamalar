# coding:iso-8859-9 T�rk�e
# p_30607.py: (b-a)*numpy.random.random_sample((s,k))+a ile [a,b) aras� (s,k) �ekilli tesad�fi kayannoktal� matris �rne�i.

import numpy as np

x1 = np.random.random_sample ((3, 4))
print ("(3,4) ebatl� [0,1) geli�ig�zel kayannokta matrisi:\n", x1, sep="")

x2 = np.random.random_sample (7)
print ("\n7 elemanl� dizi: ", x2)

x3 = np.random.random_sample ((7,))
print ("7 elemanl� dizi: ", x3)
#--------------------------------------------------------------------------------------------------------

a = -3.4
b = 5.9
A = (b - a) * np.random.random_sample ((3, 4)) + a
print ("\n[-3.4, 5.9) aras� (3,4) matrisi:\n", A, "==>", A.shape, sep="")
print ("-"*79)
#--------------------------------------------------------------------------------------------------------

import random

print ("\n[0,50) tesad�fi 50 tamsay�dan 6'l�k bir num�ne listesi:", random.sample (range(1, 50), 6) )



"""��kt�:
>python p_30607.py
(3,4) ebatl� [0,1) geli�ig�zel kayannokta matrisi:
[[0.44750339 0.51194823 0.97722699 0.19178736]
 [0.25155559 0.67808018 0.43759609 0.75712815]
 [0.98830151 0.95046013 0.74498388 0.42779973]]

7 elemanl� dizi:  [0.01795007 0.17931219 0.65129305 0.68568509 0.66118532 0.17170964 0.85165824]
7 elemanl� dizi:  [0.70524045 0.38126852 0.40350953 0.9021165  0.03589639 0.42559566 0.72267338]

[-3.4, 5.9) aras� (3,4) matrisi:
[[ 2.82499256  0.72573171  0.20645358  1.43904266]
 [-0.51988671  3.75582887  5.4537278   5.55991125]
 [-1.05890231  0.19969802 -0.42570242 -3.02405592]]==>(3, 4)
-------------------------------------------------------------------------------

[0,50) tesad�fi 50 tamsay�dan 6'l�k bir num�ne listesi: [44, 25, 39, 26, 14, 19]
"""