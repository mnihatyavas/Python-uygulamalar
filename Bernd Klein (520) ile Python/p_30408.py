# coding:iso-8859-9 Türkçe
# p_30408.py: numpy.array_equal(a,b), numpy.logical_or(a,b) ve numpy.logical_and(a,b) örneği.

import numpy as np

A = np.array ([
    [11, 12, 13],
    [21, 22, 23],
    [31, 32, 33] ])

B = np.array ([
    [11, 102, 13],
    [201, 22, 203],
    [31, 32, 303] ])

print ("A ve B matrisleri:\n", A, "\n\n", B, sep="")
print ("\n'A==B?':\n", (A == B), sep="")

print ("\n'np.array_equal(A,B)':", np.array_equal (A, B) )
print ("'np.array_equal(A,A)':", np.array_equal (A, A) )
print ("-"*45)
#--------------------------------------------------------------------------------------------------

a = np.array ([
    [True, True],
    [False, False] ])

b = np.array ([
    [True, False],
    [True, False] ])

print ("\nA ve B boolean (ikili True/False) matrisleri:\n", a, "\n\n", b, sep="")
print ("\n'np.logical_or(a,b)' VEYA kıyas sonucu matrisi:\n", np.logical_or (a, b), sep="")
print ("\n'np.logical_and(a,b)' VE kıyas sonucu matrisi:\n", np.logical_and (a, b), sep="")



"""Çıktı:
>python p_30408.py
A ve B matrisleri:
[[11 12 13]
 [21 22 23]
 [31 32 33]]

[[ 11 102  13]
 [201  22 203]
 [ 31  32 303]]

'A==B?':
[[ True False  True]
 [False  True False]
 [ True  True False]]

'np.array_equal(A,B)': False
'np.array_equal(A,A)': True
---------------------------------------------

A ve B boolean (ikili True/False) matrisleri:
[[ True  True]
 [False False]]

[[ True False]
 [ True False]]

'np.logical_or(a,b)' VEYA kıyas sonucu matrisi:
[[ True  True]
 [ True False]]

'np.logical_and(a,b)' VE kıyas sonucu matrisi:
[[ True False]
 [False False]]
"""