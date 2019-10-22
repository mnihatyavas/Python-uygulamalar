# coding:iso-8859-9 T�rk�e
# p_30409a.py: Skalar/say�sal �arpma ve toplamada k���k matrisin b�y��e otomatik yay�lmas� �rne�i.

import numpy as np

A = np.array ([
    [11, 12, 13],
    [21, 22, 23],
    [31, 32, 33] ])

B = np.array ([1, 2, 3])

b = np.array ([
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3] ])

# A ve B dizileri farkl�ysa, Numpy i�lemleri b�y��e uyumluluk yay�l�m�yla ger�ekle�tirir...

print ("A ve B dizileri:\n", A, "\n\n", B, sep="")
print ("\n'A*B' bire-bir �arp�m:\n", (A * B), sep="")
print ("\n'A+B' bire-bir toplam:\n", (A + B), sep="")

print ("\nB�y�k A'ya otomatikmen uyumlu yay�lan B dizisi:\n", b, sep="")



"""��kt�:
>python p_30409a.py
A ve B dizileri:
[[11 12 13]
 [21 22 23]
 [31 32 33]]

[1 2 3]

'A*B' bire-bir �arp�m:
[[11 24 39]
 [21 44 69]
 [31 64 99]]

'A+B' bire-bir toplam:
[[12 14 16]
 [22 24 26]
 [32 34 36]]

B�y�k A'ya otomatikmen uyumlu yay�lan B dizisi:
[[1 2 3]
 [1 2 3]
 [1 2 3]]
"""