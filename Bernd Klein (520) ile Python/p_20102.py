# coding:iso-8859-9 T�rk�e
# p_20102.py: Komut iletisinden girilen arg�manlar�n y�netilmesi �rne�i.

import sys

print ("Komut sat�r� iletileri listesi:", sys.argv)

for i in range (len (sys.argv) ):
    if i == 0: print ("\n�al��t�r�lan program�n ad�: %s" % sys.argv [0] )
    else: print ("%d.arg�man: %s" % (i, sys.argv [i]) )



"""��kt�:
>python p_20102.py "M.Nihat Yava�"
1957 Ye�ilyurt-Malatya TR
Komut sat�r� iletileri listesi: ['p_20102.py', 'M.Nihat Yava�', '1957', 'Ye�ilyurt-Malatya', 'TR']

�al��t�r�lan program�n ad�: p_20102.py
1.arg�man: M.Nihat Yava�
2.arg�man: 1957
3.arg�man: Ye�ilyurt-Malatya
4.arg�man: TR
"""