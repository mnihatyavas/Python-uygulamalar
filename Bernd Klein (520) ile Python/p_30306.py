# coding:iso-8859-9 Türkçe
# p_30306.py: Güniçi zaman-sıcaklık tüpleli değerlerin dtype ile biçimlendirilmesi örneği.

import numpy as np

#tip = np.dtype ( [ ('zaman', [('saat', int), ('dakika', int), ('saniye', int)] ), ('sıcaklık', float) ] )
tip = [ ('zaman', [('saat', int), ('dakika', int), ('saniye', int)] ), ('sıcaklık', float) ]
zamanIsı = np.array ([
    ((7, 42, 17), 20.8),
    ((9, 19, 3), 23.2),
    ((11, 8, 1), 29.3),
    ((12, 0, 0), 32.0),
    ((14, 1, 3), 37.98),
    ((18, 59, 59), 30),
    ((23, 19, 9), 24.32) ], dtype=tip)

print ("Zamanlı sıcaklık listesi yan-yana:\n", zamanIsı, sep="")
print ("Zaman listesi yan-yana:\n", zamanIsı ['zaman'], sep="")
print ("Sıcaklık listesi yan-yana:", zamanIsı ['sıcaklık'])
print ("Saat listesi yanyana:", zamanIsı ['zaman'] ['saat'])

print ("\nBiçimli zaman ve sıcaklık değerleri listesi alt-alta:\n", "-"*53, sep="")
print ("St:Dk:Sn   Sıcaklık\n", "-"*19, sep="")
for i in range (len (zamanIsı)): print ("{:02d}:{:02d}:{:02d}   {:5.2f}" .format (zamanIsı ["zaman"] ["saat"] [i], zamanIsı ["zaman"] ["dakika"] [i], zamanIsı ["zaman"] ["saniye"] [i], zamanIsı ["sıcaklık"] [i]))



"""Çıktı:
>python p_30306.py
Zamanlı sıcaklık listesi yan-yana:
[(( 7, 42, 17), 20.8 ) (( 9, 19,  3), 23.2 ) ((11,  8,  1), 29.3 )
 ((12,  0,  0), 32.  ) ((14,  1,  3), 37.98) ((18, 59, 59), 30.  )
 ((23, 19,  9), 24.32)]
Zaman listesi yan-yana:
[( 7, 42, 17) ( 9, 19,  3) (11,  8,  1) (12,  0,  0) (14,  1,  3)
 (18, 59, 59) (23, 19,  9)]
Sıcaklık listesi yan-yana: [20.8  23.2  29.3  32.   37.98 30.   24.32]
Saat listesi yanyana: [ 7  9 11 12 14 18 23]

Biçimli zaman ve sıcaklık değerleri listesi alt-alta:
-----------------------------------------------------
St:Dk:Sn   Sıcaklık
-------------------
07:42:17   20.80
09:19:03   23.20
11:08:01   29.30
12:00:00   32.00
14:01:03   37.98
18:59:59   30.00
23:19:09   24.32
"""