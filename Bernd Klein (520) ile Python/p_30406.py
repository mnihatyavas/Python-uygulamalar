# coding:iso-8859-9 T�rk�e
# p_30406.py: �ok boyutlu matris �arp�mlar�nda, ilkinin son ve ikincinin sondan bir�nceki boyut e�itli�i �rne�i.

import numpy as np
import sys

X = np.array ([
    [[3, 1, 2], [4, 2, 2]],
    [[-1, 0, 1], [1, -1, -2]],
    [[3, 2, 2], [4, 4, 3]],
    [[2, 2, 1], [3, 1, 3]] ]) # X(4,2,3) matrisi...

Y = np.array ([
    [[2, 3, 1, 2, 1], [2, 2, 2, 0, 0], [3, 4, 0, 1, -1]],
    [[1, 4, 3, 2, 2], [4, 1, 1, 4, -3], [4, 1, 0, 3, 0]] ]) # Y(2,3,5) matrisi...

# �arp�m uygunlu�u i�in ilkinin son de�eriyle, ikincinin sondan bir �nceki e�it olmal�d�r...
cevap = (X.shape[-1] == Y.shape[-2])
print ("�arp�m uygun mu?",  cevap)
if not cevap:
    print ("HATA: �arp�lan matris �ekilleri birbirleriyle uyumsuz!")
    sys.exit (-1)

Z = np.dot (X, Y)
print ("�ekilleri: X", X.shape, " * Y(", Y.shape, " = Z", Z.shape, sep="")
print("\nX, Y ve sonu� �arp�m matrisleri:")
print (X, "\n---\n", Y, "\n---\n", Z, sep="")
print ("-"*70)
#-----------------------------------------------------------------------------------------------------

"""Numpy'nin yapt��� �ok boyutlu matris �arp�m� i�in, ilk matrisin son boyutu
ve ikinci matrisin sondan bir�nceki boyutu ayr� tutulup, ilk matrisin kalan ba�lang��
boyutlar� i,j,.. d�� d�ng�lerini, ikinci matrisin de kalan boyutlar� ise k,m,.. i�
d�ng�lerini olu�turacak �ekilde d�ng�ler kurulur. Ayr� tutulan boyutlar ise en i�
d�ng�de ':' ile �arp�m matris indisleri s�ras�na konularak, �arp�mlar sum()/topla
fonksiyonuyla toplanarak sonu� matrisin ba�tan sona de�erleri elde edilerek
alt-alta s�ralan�r...
"""

print ("\nZ(4,2,2,5) = X(4,2,3) * Y(2,3,5) �arp�m sonu� matrisin ba�tan sona t�m s�ral� de�erlerinin alt-alta d�k�m�:\n", "-"*79, sep="")
s�ra = 0
for i in range (X.shape [0]):
    for j in range (X.shape [1]):
        for k in range (Y.shape [0]):
            for m in range (Y.shape [2]):
                s�ra +=1
                bi�im = "{:2d}.de�er = topla (X[{}, {}, :] * Y[{}, :, {}] :{:3d}"
                arg�manlar = (s�ra, i, j, k, m, sum (X [i, j, :] * Y [k, :, m]) )
                print (bi�im .format (*arg�manlar) )
print ("-"*79)
#-----------------------------------------------------------------------------------------------------

Z2 = np.zeros (Z.shape, dtype=np.int)
for i in range (X.shape [0]):
    for j in range (X.shape [1]):
        for k in range (Y.shape [0]):
            for m in range (Y.shape [2]):
                Z2 [i, j, k, m] = sum (X[i, j, :] * Y [k, :, m])

print ("\nZ2=X*Y d�ng�l� toplama metodlu matrisle Numpy Z=np.dot (X,Y) matrisleri e�itler mi?", np.array_equal (Z2, Z) )



"""��kt�:
>python p_30406.py
�arp�m uygun mu? True
�ekilleri: X(4, 2, 3) * Y((2, 3, 5) = Z(4, 2, 2, 5)

X, Y ve sonu� �arp�m matrisleri:
[[[ 3  1  2]
  [ 4  2  2]]

 [[-1  0  1]
  [ 1 -1 -2]]

 [[ 3  2  2]
  [ 4  4  3]]

 [[ 2  2  1]
  [ 3  1  3]]]
---
[[[ 2  3  1  2  1]
  [ 2  2  2  0  0]
  [ 3  4  0  1 -1]]

 [[ 1  4  3  2  2]
  [ 4  1  1  4 -3]
  [ 4  1  0  3  0]]]
---
[[[[ 14  19   5   8   1]
   [ 15  15  10  16   3]]

  [[ 18  24   8  10   2]
   [ 20  20  14  22   2]]]


 [[[  1   1  -1  -1  -2]
   [  3  -3  -3   1  -2]]

  [[ -6  -7  -1   0   3]
   [-11   1   2  -8   5]]]


 [[[ 16  21   7   8   1]
   [ 19  16  11  20   0]]

  [[ 25  32  12  11   1]
   [ 32  23  16  33  -4]]]


 [[[ 11  14   6   5   1]
   [ 14  11   8  15  -2]]

  [[ 17  23   5   9   0]
   [ 19  16  10  19   3]]]]
----------------------------------------------------------------------

Z(4,2,2,5) = X(4,2,3) * Y(2,3,5) �arp�m sonu� matrisin ba�tan sona t�m s�ral� de�erlerinin alt-alta d�k�m�:
-------------------------------------------------------------------------------
 1.de�er = topla(X[0, 0, :] * Y[0, :, 0] : 14
 2.de�er = topla(X[0, 0, :] * Y[0, :, 1] : 19
 3.de�er = topla(X[0, 0, :] * Y[0, :, 2] :  5
 4.de�er = topla(X[0, 0, :] * Y[0, :, 3] :  8
 5.de�er = topla(X[0, 0, :] * Y[0, :, 4] :  1
 6.de�er = topla(X[0, 0, :] * Y[1, :, 0] : 15
 7.de�er = topla(X[0, 0, :] * Y[1, :, 1] : 15
 8.de�er = topla(X[0, 0, :] * Y[1, :, 2] : 10
 9.de�er = topla(X[0, 0, :] * Y[1, :, 3] : 16
10.de�er = topla(X[0, 0, :] * Y[1, :, 4] :  3
11.de�er = topla(X[0, 1, :] * Y[0, :, 0] : 18
12.de�er = topla(X[0, 1, :] * Y[0, :, 1] : 24
13.de�er = topla(X[0, 1, :] * Y[0, :, 2] :  8
14.de�er = topla(X[0, 1, :] * Y[0, :, 3] : 10
15.de�er = topla(X[0, 1, :] * Y[0, :, 4] :  2
16.de�er = topla(X[0, 1, :] * Y[1, :, 0] : 20
17.de�er = topla(X[0, 1, :] * Y[1, :, 1] : 20
18.de�er = topla(X[0, 1, :] * Y[1, :, 2] : 14
19.de�er = topla(X[0, 1, :] * Y[1, :, 3] : 22
20.de�er = topla(X[0, 1, :] * Y[1, :, 4] :  2
21.de�er = topla(X[1, 0, :] * Y[0, :, 0] :  1
22.de�er = topla(X[1, 0, :] * Y[0, :, 1] :  1
23.de�er = topla(X[1, 0, :] * Y[0, :, 2] : -1
24.de�er = topla(X[1, 0, :] * Y[0, :, 3] : -1
25.de�er = topla(X[1, 0, :] * Y[0, :, 4] : -2
26.de�er = topla(X[1, 0, :] * Y[1, :, 0] :  3
27.de�er = topla(X[1, 0, :] * Y[1, :, 1] : -3
28.de�er = topla(X[1, 0, :] * Y[1, :, 2] : -3
29.de�er = topla(X[1, 0, :] * Y[1, :, 3] :  1
30.de�er = topla(X[1, 0, :] * Y[1, :, 4] : -2
31.de�er = topla(X[1, 1, :] * Y[0, :, 0] : -6
32.de�er = topla(X[1, 1, :] * Y[0, :, 1] : -7
33.de�er = topla(X[1, 1, :] * Y[0, :, 2] : -1
34.de�er = topla(X[1, 1, :] * Y[0, :, 3] :  0
35.de�er = topla(X[1, 1, :] * Y[0, :, 4] :  3
36.de�er = topla(X[1, 1, :] * Y[1, :, 0] :-11
37.de�er = topla(X[1, 1, :] * Y[1, :, 1] :  1
38.de�er = topla(X[1, 1, :] * Y[1, :, 2] :  2
39.de�er = topla(X[1, 1, :] * Y[1, :, 3] : -8
40.de�er = topla(X[1, 1, :] * Y[1, :, 4] :  5
41.de�er = topla(X[2, 0, :] * Y[0, :, 0] : 16
42.de�er = topla(X[2, 0, :] * Y[0, :, 1] : 21
43.de�er = topla(X[2, 0, :] * Y[0, :, 2] :  7
44.de�er = topla(X[2, 0, :] * Y[0, :, 3] :  8
45.de�er = topla(X[2, 0, :] * Y[0, :, 4] :  1
46.de�er = topla(X[2, 0, :] * Y[1, :, 0] : 19
47.de�er = topla(X[2, 0, :] * Y[1, :, 1] : 16
48.de�er = topla(X[2, 0, :] * Y[1, :, 2] : 11
49.de�er = topla(X[2, 0, :] * Y[1, :, 3] : 20
50.de�er = topla(X[2, 0, :] * Y[1, :, 4] :  0
51.de�er = topla(X[2, 1, :] * Y[0, :, 0] : 25
52.de�er = topla(X[2, 1, :] * Y[0, :, 1] : 32
53.de�er = topla(X[2, 1, :] * Y[0, :, 2] : 12
54.de�er = topla(X[2, 1, :] * Y[0, :, 3] : 11
55.de�er = topla(X[2, 1, :] * Y[0, :, 4] :  1
56.de�er = topla(X[2, 1, :] * Y[1, :, 0] : 32
57.de�er = topla(X[2, 1, :] * Y[1, :, 1] : 23
58.de�er = topla(X[2, 1, :] * Y[1, :, 2] : 16
59.de�er = topla(X[2, 1, :] * Y[1, :, 3] : 33
60.de�er = topla(X[2, 1, :] * Y[1, :, 4] : -4
61.de�er = topla(X[3, 0, :] * Y[0, :, 0] : 11
62.de�er = topla(X[3, 0, :] * Y[0, :, 1] : 14
63.de�er = topla(X[3, 0, :] * Y[0, :, 2] :  6
64.de�er = topla(X[3, 0, :] * Y[0, :, 3] :  5
65.de�er = topla(X[3, 0, :] * Y[0, :, 4] :  1
66.de�er = topla(X[3, 0, :] * Y[1, :, 0] : 14
67.de�er = topla(X[3, 0, :] * Y[1, :, 1] : 11
68.de�er = topla(X[3, 0, :] * Y[1, :, 2] :  8
69.de�er = topla(X[3, 0, :] * Y[1, :, 3] : 15
70.de�er = topla(X[3, 0, :] * Y[1, :, 4] : -2
71.de�er = topla(X[3, 1, :] * Y[0, :, 0] : 17
72.de�er = topla(X[3, 1, :] * Y[0, :, 1] : 23
73.de�er = topla(X[3, 1, :] * Y[0, :, 2] :  5
74.de�er = topla(X[3, 1, :] * Y[0, :, 3] :  9
75.de�er = topla(X[3, 1, :] * Y[0, :, 4] :  0
76.de�er = topla(X[3, 1, :] * Y[1, :, 0] : 19
77.de�er = topla(X[3, 1, :] * Y[1, :, 1] : 16
78.de�er = topla(X[3, 1, :] * Y[1, :, 2] : 10
79.de�er = topla(X[3, 1, :] * Y[1, :, 3] : 19
80.de�er = topla(X[3, 1, :] * Y[1, :, 4] :  3
-------------------------------------------------------------------------------

Z2=X*Y d�ng�l� toplama metodlu matrisle Numpy Z=np.dot (X,Y) matrisleri e�itlermi? True
"""