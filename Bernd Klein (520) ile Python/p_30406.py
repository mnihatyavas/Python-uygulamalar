# coding:iso-8859-9 Türkçe
# p_30406.py: Çok boyutlu matris çarpımlarında, ilkinin son ve ikincinin sondan birönceki boyut eşitliği örneği.

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

# Çarpım uygunluğu için ilkinin son değeriyle, ikincinin sondan bir önceki eşit olmalıdır...
cevap = (X.shape[-1] == Y.shape[-2])
print ("Çarpım uygun mu?",  cevap)
if not cevap:
    print ("HATA: Çarpılan matris şekilleri birbirleriyle uyumsuz!")
    sys.exit (-1)

Z = np.dot (X, Y)
print ("Şekilleri: X", X.shape, " * Y(", Y.shape, " = Z", Z.shape, sep="")
print("\nX, Y ve sonuç çarpım matrisleri:")
print (X, "\n---\n", Y, "\n---\n", Z, sep="")
print ("-"*70)
#-----------------------------------------------------------------------------------------------------

"""Numpy'nin yaptığı çok boyutlu matris çarpımı için, ilk matrisin son boyutu
ve ikinci matrisin sondan birönceki boyutu ayrı tutulup, ilk matrisin kalan başlangıç
boyutları i,j,.. dış döngülerini, ikinci matrisin de kalan boyutları ise k,m,.. iç
döngülerini oluşturacak şekilde döngüler kurulur. Ayrı tutulan boyutlar ise en iç
döngüde ':' ile çarpım matris indisleri sırasına konularak, çarpımlar sum()/topla
fonksiyonuyla toplanarak sonuç matrisin baştan sona değerleri elde edilerek
alt-alta sıralanır...
"""

print ("\nZ(4,2,2,5) = X(4,2,3) * Y(2,3,5) çarpım sonuç matrisin baştan sona tüm sıralı değerlerinin alt-alta dökümü:\n", "-"*79, sep="")
sıra = 0
for i in range (X.shape [0]):
    for j in range (X.shape [1]):
        for k in range (Y.shape [0]):
            for m in range (Y.shape [2]):
                sıra +=1
                biçim = "{:2d}.değer = topla (X[{}, {}, :] * Y[{}, :, {}] :{:3d}"
                argümanlar = (sıra, i, j, k, m, sum (X [i, j, :] * Y [k, :, m]) )
                print (biçim .format (*argümanlar) )
print ("-"*79)
#-----------------------------------------------------------------------------------------------------

Z2 = np.zeros (Z.shape, dtype=np.int)
for i in range (X.shape [0]):
    for j in range (X.shape [1]):
        for k in range (Y.shape [0]):
            for m in range (Y.shape [2]):
                Z2 [i, j, k, m] = sum (X[i, j, :] * Y [k, :, m])

print ("\nZ2=X*Y döngülü toplama metodlu matrisle Numpy Z=np.dot (X,Y) matrisleri eşitler mi?", np.array_equal (Z2, Z) )



"""Çıktı:
>python p_30406.py
Çarpım uygun mu? True
Şekilleri: X(4, 2, 3) * Y((2, 3, 5) = Z(4, 2, 2, 5)

X, Y ve sonuç çarpım matrisleri:
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

Z(4,2,2,5) = X(4,2,3) * Y(2,3,5) çarpım sonuç matrisin baştan sona tüm sıralı değerlerinin alt-alta dökümü:
-------------------------------------------------------------------------------
 1.değer = topla(X[0, 0, :] * Y[0, :, 0] : 14
 2.değer = topla(X[0, 0, :] * Y[0, :, 1] : 19
 3.değer = topla(X[0, 0, :] * Y[0, :, 2] :  5
 4.değer = topla(X[0, 0, :] * Y[0, :, 3] :  8
 5.değer = topla(X[0, 0, :] * Y[0, :, 4] :  1
 6.değer = topla(X[0, 0, :] * Y[1, :, 0] : 15
 7.değer = topla(X[0, 0, :] * Y[1, :, 1] : 15
 8.değer = topla(X[0, 0, :] * Y[1, :, 2] : 10
 9.değer = topla(X[0, 0, :] * Y[1, :, 3] : 16
10.değer = topla(X[0, 0, :] * Y[1, :, 4] :  3
11.değer = topla(X[0, 1, :] * Y[0, :, 0] : 18
12.değer = topla(X[0, 1, :] * Y[0, :, 1] : 24
13.değer = topla(X[0, 1, :] * Y[0, :, 2] :  8
14.değer = topla(X[0, 1, :] * Y[0, :, 3] : 10
15.değer = topla(X[0, 1, :] * Y[0, :, 4] :  2
16.değer = topla(X[0, 1, :] * Y[1, :, 0] : 20
17.değer = topla(X[0, 1, :] * Y[1, :, 1] : 20
18.değer = topla(X[0, 1, :] * Y[1, :, 2] : 14
19.değer = topla(X[0, 1, :] * Y[1, :, 3] : 22
20.değer = topla(X[0, 1, :] * Y[1, :, 4] :  2
21.değer = topla(X[1, 0, :] * Y[0, :, 0] :  1
22.değer = topla(X[1, 0, :] * Y[0, :, 1] :  1
23.değer = topla(X[1, 0, :] * Y[0, :, 2] : -1
24.değer = topla(X[1, 0, :] * Y[0, :, 3] : -1
25.değer = topla(X[1, 0, :] * Y[0, :, 4] : -2
26.değer = topla(X[1, 0, :] * Y[1, :, 0] :  3
27.değer = topla(X[1, 0, :] * Y[1, :, 1] : -3
28.değer = topla(X[1, 0, :] * Y[1, :, 2] : -3
29.değer = topla(X[1, 0, :] * Y[1, :, 3] :  1
30.değer = topla(X[1, 0, :] * Y[1, :, 4] : -2
31.değer = topla(X[1, 1, :] * Y[0, :, 0] : -6
32.değer = topla(X[1, 1, :] * Y[0, :, 1] : -7
33.değer = topla(X[1, 1, :] * Y[0, :, 2] : -1
34.değer = topla(X[1, 1, :] * Y[0, :, 3] :  0
35.değer = topla(X[1, 1, :] * Y[0, :, 4] :  3
36.değer = topla(X[1, 1, :] * Y[1, :, 0] :-11
37.değer = topla(X[1, 1, :] * Y[1, :, 1] :  1
38.değer = topla(X[1, 1, :] * Y[1, :, 2] :  2
39.değer = topla(X[1, 1, :] * Y[1, :, 3] : -8
40.değer = topla(X[1, 1, :] * Y[1, :, 4] :  5
41.değer = topla(X[2, 0, :] * Y[0, :, 0] : 16
42.değer = topla(X[2, 0, :] * Y[0, :, 1] : 21
43.değer = topla(X[2, 0, :] * Y[0, :, 2] :  7
44.değer = topla(X[2, 0, :] * Y[0, :, 3] :  8
45.değer = topla(X[2, 0, :] * Y[0, :, 4] :  1
46.değer = topla(X[2, 0, :] * Y[1, :, 0] : 19
47.değer = topla(X[2, 0, :] * Y[1, :, 1] : 16
48.değer = topla(X[2, 0, :] * Y[1, :, 2] : 11
49.değer = topla(X[2, 0, :] * Y[1, :, 3] : 20
50.değer = topla(X[2, 0, :] * Y[1, :, 4] :  0
51.değer = topla(X[2, 1, :] * Y[0, :, 0] : 25
52.değer = topla(X[2, 1, :] * Y[0, :, 1] : 32
53.değer = topla(X[2, 1, :] * Y[0, :, 2] : 12
54.değer = topla(X[2, 1, :] * Y[0, :, 3] : 11
55.değer = topla(X[2, 1, :] * Y[0, :, 4] :  1
56.değer = topla(X[2, 1, :] * Y[1, :, 0] : 32
57.değer = topla(X[2, 1, :] * Y[1, :, 1] : 23
58.değer = topla(X[2, 1, :] * Y[1, :, 2] : 16
59.değer = topla(X[2, 1, :] * Y[1, :, 3] : 33
60.değer = topla(X[2, 1, :] * Y[1, :, 4] : -4
61.değer = topla(X[3, 0, :] * Y[0, :, 0] : 11
62.değer = topla(X[3, 0, :] * Y[0, :, 1] : 14
63.değer = topla(X[3, 0, :] * Y[0, :, 2] :  6
64.değer = topla(X[3, 0, :] * Y[0, :, 3] :  5
65.değer = topla(X[3, 0, :] * Y[0, :, 4] :  1
66.değer = topla(X[3, 0, :] * Y[1, :, 0] : 14
67.değer = topla(X[3, 0, :] * Y[1, :, 1] : 11
68.değer = topla(X[3, 0, :] * Y[1, :, 2] :  8
69.değer = topla(X[3, 0, :] * Y[1, :, 3] : 15
70.değer = topla(X[3, 0, :] * Y[1, :, 4] : -2
71.değer = topla(X[3, 1, :] * Y[0, :, 0] : 17
72.değer = topla(X[3, 1, :] * Y[0, :, 1] : 23
73.değer = topla(X[3, 1, :] * Y[0, :, 2] :  5
74.değer = topla(X[3, 1, :] * Y[0, :, 3] :  9
75.değer = topla(X[3, 1, :] * Y[0, :, 4] :  0
76.değer = topla(X[3, 1, :] * Y[1, :, 0] : 19
77.değer = topla(X[3, 1, :] * Y[1, :, 1] : 16
78.değer = topla(X[3, 1, :] * Y[1, :, 2] : 10
79.değer = topla(X[3, 1, :] * Y[1, :, 3] : 19
80.değer = topla(X[3, 1, :] * Y[1, :, 4] :  3
-------------------------------------------------------------------------------

Z2=X*Y döngülü toplama metodlu matrisle Numpy Z=np.dot (X,Y) matrisleri eşitlermi? True
"""