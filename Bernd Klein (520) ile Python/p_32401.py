#coding:iso-8859-9 T�rk�e
# p_32401.py: Grupland�rma ve verili de�erlerin gruplar�n� bulma �rne�i.

def gruplar�Yarat (altS�n�r, art��, adet):
    gruplar = []
    for alt in range (altS�n�r, (altS�n�r + (adet - 1) * art�� + 1), art��):
        gruplar.append ( (alt + 1, alt + art��) )
    return gruplar

adet = 6
art�� = 10
gruplar1 = gruplar�Yarat (10, 10, 6)
print ("Toplam ", adet, " adet ", art��, "'ar geni�likteki grup t�pleleri listesi:\n", gruplar1, sep="")
print ("-"*79)
#--------------------------------------------------------------------------------------------------------

from collections import Counter
from random import random

def grubuBul (de�er, gruplar):
    for i in range (0, len (gruplar)):
        if gruplar [i] [0] <= de�er < gruplar [i] [1] + 1: return i
    return -1

gruplar2 = gruplar�Yarat (altS�n�r=50, art��=4, adet=15)
print ("\n�nsan a��rl�klar� s�n�fland�rmas� (", len (gruplar2), " adet):\n", gruplar2, sep="")

insanKilolar� = [random() * 60 + 51 for _ in range (30)]
s�n�fland�r�lanA��rl�klar = []
i = 1
print ("\nS�ra A��rl�k(kg) Endeks S�n�f�\n", "-"*30, sep="")
for kilo in insanKilolar�:
    grupEndeksi = grubuBul (kilo, gruplar2)
    print (i, "==> ", (int (kilo * 10) / 10.0), "   ", grupEndeksi, "   ", gruplar2 [grupEndeksi], sep="")
    i+=1
    s�n�fland�r�lanA��rl�klar.append (grupEndeksi)

s�kl�k = Counter (s�n�fland�r�lanA��rl�klar)
print ("\nAzalan s�ral� a��rl�k endeksleri s�kl��� (endeks: s�kl�k)==>\n", s�kl�k, sep="")



"""��kt�:
>python p_32401.py
Toplam 6 adet 10'ar geni�likteki grup t�pleleri listesi:
[(11, 20), (21, 30), (31, 40), (41, 50), (51, 60), (61, 70)]
-------------------------------------------------------------------------------

�nsan a��rl�klar� s�n�fland�rmas� (15 adet):
[(51, 54), (55, 58), (59, 62), (63, 66), (67, 70), (71, 74), (75, 78), (79, 82),
 (83, 86), (87, 90), (91, 94), (95, 98), (99, 102), (103, 106), (107, 110)]

S�ra A��rl�k(kg) Endeks S�n�f�
------------------------------
1==> 96.4   11   (95, 98)
2==> 76.8   6   (75, 78)
3==> 88.8   9   (87, 90)
4==> 65.8   3   (63, 66)
5==> 78.7   6   (75, 78)
6==> 82.8   7   (79, 82)
7==> 92.2   10   (91, 94)
8==> 75.6   6   (75, 78)
9==> 92.0   10   (91, 94)
10==> 104.7   13   (103, 106)
11==> 64.2   3   (63, 66)
12==> 100.1   12   (99, 102)
13==> 87.2   9   (87, 90)
14==> 102.1   12   (99, 102)
15==> 69.0   4   (67, 70)
16==> 99.7   12   (99, 102)
17==> 71.8   5   (71, 74)
18==> 90.7   9   (87, 90)
19==> 83.0   8   (83, 86)
20==> 53.8   0   (51, 54)
21==> 71.7   5   (71, 74)
22==> 58.5   1   (55, 58)
23==> 62.8   2   (59, 62)
24==> 71.1   5   (71, 74)
25==> 60.9   2   (59, 62)
26==> 56.6   1   (55, 58)
27==> 61.7   2   (59, 62)
28==> 105.5   13   (103, 106)
29==> 87.0   9   (87, 90)
30==> 102.4   12   (99, 102)

Azalan s�ral� a��rl�k endeksleri s�kl��� (endeks: s�kl�k)==>
Counter({9: 4, 12: 4, 6: 3, 5: 3, 2: 3, 3: 2, 10: 2, 13: 2, 1: 2, 11: 1, 7: 1, 4: 1,
 8: 1, 0: 1})
"""