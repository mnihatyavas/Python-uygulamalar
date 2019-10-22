# coding:iso-8859-9 Türkçe
# p_30201.py: Python range dizilerine karşılık numpy arange dizileri örneği.

import numpy as np

a1 = range (10)
a2 = np.arange (10)

print (type (a1), "\n", a1, list (a1))
print (type (a2), "\n", a2)
#------------------------------------------------------------------------------------

a1 = range (5, 10)
a2 = np.arange (5, 10)

print()
print (type (a1), "\n", a1, list (a1))
print (type (a2), "\n", a2)
#------------------------------------------------------------------------------------

a1 = range (1, 10, 2)
a2 = np.arange (1, 10, 2)

print()
print (type (a1), "\n", a1, list (a1))
print (type (a2), "\n", a2)
#------------------------------------------------------------------------------------

print()
x = np.arange (10.4)
print (x)

x = np.arange (0.5, 10.4, 0.8)
print (x)

x = np.arange (0.5, 10.4, 0.8, float)
print (x)

x = np.arange (0.5, 10.4, 0.8, int)
print (x)



"""Çıktı:
>python p_30201.py
<class 'range'>
 range(0, 10) [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
<class 'numpy.ndarray'>
 [0 1 2 3 4 5 6 7 8 9]

<class 'range'>
 range(5, 10) [5, 6, 7, 8, 9]
<class 'numpy.ndarray'>
 [5 6 7 8 9]

<class 'range'>
 range(1, 10, 2) [1, 3, 5, 7, 9]
<class 'numpy.ndarray'>
 [1 3 5 7 9]

[ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
[ 0.5  1.3  2.1  2.9  3.7  4.5  5.3  6.1  6.9  7.7  8.5  9.3 10.1]
[ 0.5  1.3  2.1  2.9  3.7  4.5  5.3  6.1  6.9  7.7  8.5  9.3 10.1]
[ 0  1  2  3  4  5  6  7  8  9 10 11 12]
"""