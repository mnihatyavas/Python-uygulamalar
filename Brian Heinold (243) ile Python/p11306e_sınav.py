# coding:iso-8859-9 Türkçe

def lafzileştir (L1):
    L2 = [("bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz", ""),
        ("on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan", ""),
        ("yüz", "ikiyüz", "üçyüz", "dörtyüz", "beşyüz", "altıyüz", "yediyüz", "sekizyüz", "dokuzyüz", "")]
    L3 = ["", "bin","milyon", "milyar", "trilyon", "trilyar", "katrilyon", "katrilyar"]
    if "".join (L1) == "0": return "sıfır"
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
try: sayı = abs (int (eval (input ("Bir pozitif tamsayı gir: "))))
except Exception: sayı = randint (0, 10**23)

L = []
k = str (sayı)
u = len (k)
for i in range (0, u-2, 3): L = [k[u-i-3:u-i]] + L
if u%3 != 0: L = [k[0:u%3]] + L

dizge = lafzileştir (L)
print ("\nRakamsal: ({:,d}) = Sözel: ({:})" .format (sayı, dizge.strip()))
