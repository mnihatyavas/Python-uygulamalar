# coding:iso-8859-9 T�rk�e
# p_30306.py: G�ni�i zaman-s�cakl�k t�pleli de�erlerin dtype ile bi�imlendirilmesi �rne�i.

import numpy as np

#tip = np.dtype ( [ ('zaman', [('saat', int), ('dakika', int), ('saniye', int)] ), ('s�cakl�k', float) ] )
tip = [ ('zaman', [('saat', int), ('dakika', int), ('saniye', int)] ), ('s�cakl�k', float) ]
zamanIs� = np.array ([
    ((7, 42, 17), 20.8),
    ((9, 19, 3), 23.2),
    ((11, 8, 1), 29.3),
    ((12, 0, 0), 32.0),
    ((14, 1, 3), 37.98),
    ((18, 59, 59), 30),
    ((23, 19, 9), 24.32) ], dtype=tip)

print ("Zamanl� s�cakl�k listesi yan-yana:\n", zamanIs�, sep="")
print ("Zaman listesi yan-yana:\n", zamanIs� ['zaman'], sep="")
print ("S�cakl�k listesi yan-yana:", zamanIs� ['s�cakl�k'])
print ("Saat listesi yanyana:", zamanIs� ['zaman'] ['saat'])

print ("\nBi�imli zaman ve s�cakl�k de�erleri listesi alt-alta:\n", "-"*53, sep="")
print ("St:Dk:Sn   S�cakl�k\n", "-"*19, sep="")
for i in range (len (zamanIs�)): print ("{:02d}:{:02d}:{:02d}   {:5.2f}" .format (zamanIs� ["zaman"] ["saat"] [i], zamanIs� ["zaman"] ["dakika"] [i], zamanIs� ["zaman"] ["saniye"] [i], zamanIs� ["s�cakl�k"] [i]))



"""��kt�:
>python p_30306.py
Zamanl� s�cakl�k listesi yan-yana:
[(( 7, 42, 17), 20.8 ) (( 9, 19,  3), 23.2 ) ((11,  8,  1), 29.3 )
 ((12,  0,  0), 32.  ) ((14,  1,  3), 37.98) ((18, 59, 59), 30.  )
 ((23, 19,  9), 24.32)]
Zaman listesi yan-yana:
[( 7, 42, 17) ( 9, 19,  3) (11,  8,  1) (12,  0,  0) (14,  1,  3)
 (18, 59, 59) (23, 19,  9)]
S�cakl�k listesi yan-yana: [20.8  23.2  29.3  32.   37.98 30.   24.32]
Saat listesi yanyana: [ 7  9 11 12 14 18 23]

Bi�imli zaman ve s�cakl�k de�erleri listesi alt-alta:
-----------------------------------------------------
St:Dk:Sn   S�cakl�k
-------------------
07:42:17   20.80
09:19:03   23.20
11:08:01   29.30
12:00:00   32.00
14:01:03   37.98
18:59:59   30.00
23:19:09   24.32
"""