# coding:iso-8859-9 T�rk�e

S = {"Ocak":31, "�ubat":28, "Mart":31, "Nisan":30, "May�s":31, "Haziran":30, "Temmuz":31, "A�ustos":31, "Eyl�l":30, "Ekim":31, "Kas�m":30, "Aral�k":31}
print (S)
print ("\n<<pprint>>, s�zl��� a->z s�ralayarak altalta d�ker:\n", "-"*51, sep="")
from pprint import pprint
pprint (S)

while True:
    ay = input ("\nAy ad� (ilk 3 harf yeterli) girin [��k: q]: ")
    if ay == "q": break
    if ay in S: print (ay.upper(), "ay�", S[ay], "g�n �ekiyor.")
    elif len (ay) == 3:
        for k in S.items():
            if k[0][:3].lower() == ay.lower():
                print (k[0].upper(), "ay�", k[1], "g�n �ekiyor.")
    else: print (ay, "ad�n� s�zl�kte bulamad�m!")

print()
L =list (S)
L.sort()
pprint (L)

print()
L =list (S.items())
L.sort()
pprint (L)
print()
for k in L: print (k[0].upper(), "ay�", k[1], "g�n �eker")
print()
L = [(k[1], k[0]) for k in L]
L.sort()
for k in L: print (k[0], "�eken", k[1].upper(), "ay�")

print()
for k in S.items():
    if k[1] == 31: print (k[0], ":", k[1])

