# coding:iso-8859-9 Türkçe
# p_10502.py: 2-8-10-16 tabanlı sayılar, sınırsız tamsayı, kompleks sayılar, / ve // ile bölme örneği.

import math

print ("Hexa: 0x10={}, 0X14={}" .format (0x10, 0X14) )
print ("Octal: 0o10={}, 0O24={}" .format (0o10, 0O24) )
print ("Binary: 0b10={}, 0B10100={}" .format (0b10, 0B10100) )

print ("\nhex (16) =", hex (16) )
print ("oct (8) =", oct (8) )
print ("bin (2) =", bin (2) )

print ("\nhex(65) =", hex (65) )
print ("int(0x41) =", int (0x41) )
print ("chr(65) =", chr (65) )
print ("chr(0x41) =", chr (0x41) )
print ("ord('A') =", ord ("A") )

print ("\nPython tamsayısı sınırsızdır; 34**100 = ", 34**100)
print ("\nPython kayannoktalı sayısı küsüratlı: {}; veya 'e'lidir: {}" .format (math.pi, math.pi**100) )

x = 3 + 5j
y = 7.8 - 45.12j
z1 = x - y
z2 = x * y
z3 = x / y
print ("\nPython kompleks sayısı gerçel ve sanal-j kısımlıdır (x, y, x-y, x*y, x/y):", x, y, z1, z2, z3)

print ("\n'/' bölme ile kayan noktalı sonuç elde edilir:", 9/3, 10/3, 11/3, -7.0/3)
print ("\n'//' bölme ile küsüratsız temel sonuç elde edilir:", 9//3, 10//3, 11//3, -7.0//3)


"""Çıktı:
>python p_10502.py
Hexa: 0x10=16, 0X14=20
Octal: 0o10=8, 0O24=20
Binary: 0b10=2, 0B10100=20

hex (16) = 0x10
oct (8) = 0o10
bin (2) = 0b10

hex(65) = 0x41
int(0x41) = 65
chr(65) = A
chr(0x41) = A
ord('A') = 65

Python tamsayısı sınırsızdır; 34**100 =  1405696955498267491541705127961637555026742863683784726712507274522355585042137573835346212619282244621664528557733175717906457091122459228663147843813376

Python kayannoktalı sayısı küsüratlı: 3.141592653589793; veya 'e'lidir: 5.187848314319592e+49

Python kompleks sayısı gerçel ve sanal-j kısımlıdır (x, y, x-y, x*y, x/y): (3+5j)
(7.8-45.12j) (-4.8+50.12j) (249-96.35999999999999j) (-0.09643935595680435+0.0831610588755114j)

'/' bölme ile kayan noktalı sonuç elde edilir: 3.0 3.3333333333333335 3.6666666666666665
-2.3333333333333335

'//' bölme ile küsüratsız temel sonuç elde edilir: 3 3 3 -3.0
"""