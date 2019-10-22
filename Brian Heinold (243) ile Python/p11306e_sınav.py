# coding:iso-8859-9 T�rk�e

def lafzile�tir (L1):
    L2 = [("bir", "iki", "��", "d�rt", "be�", "alt�", "yedi", "sekiz", "dokuz", ""),
        ("on", "yirmi", "otuz", "k�rk", "elli", "altm��", "yetmi�", "seksen", "doksan", ""),
        ("y�z", "ikiy�z", "��y�z", "d�rty�z", "be�y�z", "alt�y�z", "yediy�z", "sekizy�z", "dokuzy�z", "")]
    L3 = ["", "bin","milyon", "milyar", "trilyon", "trilyar", "katrilyon", "katrilyar"]
    if "".join (L1) == "0": return "s�f�r"
    u1 = len (L1)
    tt = ""
    for i in range (u1):
        u2 = len (str (L1[i]))
        if u2 == 1: t = L2[0][int (L1[i][0])-1]
        elif u2 == 2: t = L2[1][int (L1[i][0])-1] + " " + L2[0][int (L1[i][1])-1]
        else:
            if int (L1[i]) == 0: t = ""
            else: t = L2[2][int (L1[i][0])-1]+ " " + L2[1][int (L1[i][1])-1] + " " + L2[0][int (L1[i][2])-1]
        if u1 == 2 and t == "bir": t = ""
        if int (L1[i]) != 0: tt = tt + " " + t + " " + L3[u1-i-1] + " "
    return tt

from random import randint
try: say� = abs (int (eval (input ("Bir pozitif tamsay� gir: "))))
except Exception: say� = randint (0, 10**23)

L = []
k = str (say�)
u = len (k)
for i in range (0, u-2, 3): L = [k[u-i-3:u-i]] + L
if u%3 != 0: L = [k[0:u%3]] + L

dizge = lafzile�tir (L)
print ("\nRakamsal: ({:,d}) = S�zel: ({:})" .format (say�, dizge.strip()))
