# coding:iso-8859-9 T�rk�e
# p_30506.py: Bir matrisin �e�itli numpy.row_stack/column_stack/dstack y���n matrislere �evrilmesi �rne�i.

import numpy as np

A = np.array ([3, 4, 5])
B = np.array ([1, 9, 0])

C = np.row_stack ((A,  B))
D = np.column_stack ((A,  B))

print ("A dizisi: ", A, "==>", A.shape,
    "\nB dizisi: ", B, "==>", B.shape,
    "\n\nnp.row_stack((A,B)):\n", C, "==>", C.shape,
    "\n\nnp.column_stack((A,B)):\n", D, "==>", D.shape, sep="")
print ("-"*30)
#-------------------------------------------------------------------------------------------

print ("\nA(3,1) ve B(3,1) kolonvari y���n:\n", np.column_stack ((A[:, np.newaxis], B[:, np.newaxis])), sep="")
print ("-"*30)
#-------------------------------------------------------------------------------------------

E = np.array ([
    [3, 4, 5],
    [1, 9, 0],
    [4, 6, 8] ])

E1 = np.row_stack ((E, E, E))
E2 = np.column_stack ((E, E, E))

print ("\nE matrisi:\n", E, "==>", E.shape,
    "\n\nE 3'l� sat�rvari y���n:\n", E1, "==>", E1.shape,
    "\n\nE 3'l� s�tunvari y���n:\n", E2, "==>", E2.shape, sep="")

E3 = np.row_stack ((E[0], E[0], E[0]))
E4 = np.column_stack ((E[0], E[0], E[0]))

print ("\nE ilk sat�r�n�n sat�rvari y���n�:\n", E3, "==>", E3.shape,
    "\n\nE ilk sat�r�n�n s�tunvari y���n�:\n", E4, "==>", E4.shape, sep ="")

E5 = np.dstack ((E, E, E))

print ("\nE t�m 3 sat�r�n�n s�tunvari y���n�:\n", E5, "==>", E5.shape, sep="")



"""��kt�:
>python p_30506.py
A dizisi: [3 4 5]==>(3,)
B dizisi: [1 9 0]==>(3,)

np.row_stack((A,B)):
[[3 4 5]
 [1 9 0]]==>(2, 3)

np.column_stack((A,B)):
[[3 1]
 [4 9]
 [5 0]]==>(3, 2)
------------------------------

A(3,1) ve B(3,1) kolonvari y���n:
[[3 1]
 [4 9]
 [5 0]]
------------------------------

E matrisi:
[[3 4 5]
 [1 9 0]
 [4 6 8]]==>(3, 3)

E 3'l� sat�rvari y���n:
[[3 4 5]
 [1 9 0]
 [4 6 8]
 [3 4 5]
 [1 9 0]
 [4 6 8]
 [3 4 5]
 [1 9 0]
 [4 6 8]]==>(9, 3)

E 3'l� s�tunvari y���n:
[[3 4 5 3 4 5 3 4 5]
 [1 9 0 1 9 0 1 9 0]
 [4 6 8 4 6 8 4 6 8]]==>(3, 9)

E ilk sat�r�n�n sat�rvari y���n�:
[[3 4 5]
 [3 4 5]
 [3 4 5]]==>(3, 3)

E ilk sat�r�n�n s�tunvari y���n�:
[[3 3 3]
 [4 4 4]
 [5 5 5]]==>(3, 3)

E t�m 3 sat�r�n�n s�tunvari y���n�:
[[[3 3 3]
  [4 4 4]
  [5 5 5]]

 [[1 1 1]
  [9 9 9]
  [0 0 0]]

 [[4 4 4]
  [6 6 6]
  [8 8 8]]]==>(3, 3, 3)
"""