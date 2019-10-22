# coding:iso-8859-9 T�rk�e
# p_30403.py: Numpy.array iki matrisin toplamas�, say�l ve y�nel �arp�mlar� �rne�i.

import numpy as np

A = np.array ([ [11, 12, 13], [21, 22, 23], [31, 32, 33] ])
B = np.ones ((3,3), int) # varsay�l�: float

print ("A (3,3) matrisi:\n", A, sep="")
print ("\nB (3,3) birler matrisi:\n", B, sep="")
print ("\n'A+(B+1)' toplam matrisi:\n", (A + (B + 1)), sep="")
print ("\n'A*(B+1)' skalar/say�l �arp�m matrisi:\n",  (A * (B + 1)), sep="")
print ("\n'np.dot(A,B)' vekt�rel/y�nel �arp�m matrisi:\n",  np.dot (A, B), sep="")
print ("\n'np.dot(A,(B+1))' vekt�rel/y�nel �arp�m matrisi:\n",  np.dot (A, (B + 1)), sep="")



"""��kt�:
>python p_30403.py
A (3,3) matrisi:
[[11 12 13]
 [21 22 23]
 [31 32 33]]

B (3,3) birler matrisi:
[[1 1 1]
 [1 1 1]
 [1 1 1]]

'A+(B+1)' toplam matrisi:
[[13 14 15]
 [23 24 25]
 [33 34 35]]

'A*(B+1)' skalar/say�l �arp�m matrisi:
[[22 24 26]
 [42 44 46]
 [62 64 66]]

'np.dot(A,B)' vekt�rel/y�nel �arp�m matrisi:
[[36 36 36]
 [66 66 66]
 [96 96 96]]

'np.dot(A,(B+1))' vekt�rel/y�nel �arp�m matrisi:
[[ 72  72  72]
 [132 132 132]
 [192 192 192]]
"""