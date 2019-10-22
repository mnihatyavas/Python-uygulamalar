# coding:iso-8859-9 Türkçe
# p_30205.py: numpy.array ile çeşitli 2-3 boyutlu şekiller örneği.

import numpy as np

x = np.array ([
    [67, 63, 87],
    [77, 69, 59],
    [85, 87, 99],
    [79, 72, 71],
    [63, 89, 93],
    [68, 92, 78] ])
print ("Dizi:\n", x, "\nŞekli:", x.shape, sep="")

x.shape = (3, 6) # 3*6 = 6*3 = 2*3*3 = 1*18 = 1*2*9 = 18 olmalıdır...
print ("\nDizi:\n", x, "\nŞekli:", x.shape, sep="")

x.shape = (2, 3, 3)
print ("\nDizi:\n", x, "\nŞekli:", x.shape, sep="")

x.shape = (1, 2, 9)
print ("\nDizi:\n", x, "\nŞekli:", x.shape, sep="")

x.shape = (1, 18)
print ("\nDizi:\n", x, "\nŞekli:", x.shape, sep="")

x.shape = (18, 1)
print ("\nDizi:\n", x, "\nŞekli:", x.shape, sep="")

x.shape = (18, 1, 1)
print ("\nDizi:\n", x, "\nŞekli:", x.shape, sep="")



"""Çıktı:
>python p_30205.py
Dizi:
[[67 63 87]
 [77 69 59]
 [85 87 99]
 [79 72 71]
 [63 89 93]
 [68 92 78]]
Şekli:(6, 3)

Dizi:
[[67 63 87 77 69 59]
 [85 87 99 79 72 71]
 [63 89 93 68 92 78]]
Şekli:(3, 6)

Dizi:
[[[67 63 87]
  [77 69 59]
  [85 87 99]]

 [[79 72 71]
  [63 89 93]
  [68 92 78]]]
Şekli:(2, 3, 3)

Dizi:
[[[67 63 87 77 69 59 85 87 99]
  [79 72 71 63 89 93 68 92 78]]]
Şekli:(1, 2, 9)

Dizi:
[[67 63 87 77 69 59 85 87 99 79 72 71 63 89 93 68 92 78]]
Şekli:(1, 18)

Dizi:
[[67]
 [63]
 [87]
 [77]
 [69]
 [59]
 [85]
 [87]
 [99]
 [79]
 [72]
 [71]
 [63]
 [89]
 [93]
 [68]
 [92]
 [78]]
Şekli:(18, 1)

Dizi:
[[[67]]

 [[63]]

 [[87]]

 [[77]]

 [[69]]

 [[59]]

 [[85]]

 [[87]]

 [[99]]

 [[79]]

 [[72]]

 [[71]]

 [[63]]

 [[89]]

 [[93]]

 [[68]]

 [[92]]

 [[78]]]
Şekli:(18, 1, 1)
"""