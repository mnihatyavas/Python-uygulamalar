# coding:iso-8859-9 Türkçe

S = {"Ocak":31, "Şubat":28, "Mart":31, "Nisan":30, "Mayıs":31, "Haziran":30, "Temmuz":31, "Ağustos":31, "Eylül":30, "Ekim":31, "Kasım":30, "Aralık":31}
print (S)
print ("\n<<pprint>>, sözlüğü a->z sıralayarak altalta döker:\n", "-"*51, sep="")
from pprint import pprint
pprint (S)

while True:
    ay = input ("\nAy adı (ilk 3 harf yeterli) girin [Çık: q]: ")
    if ay == "q": break
    if ay in S: print (ay.upper(), "ayı", S[ay], "gün çekiyor.")
    elif len (ay) == 3:
        for k in S.items():
            if k[0][:3].lower() == ay.lower():
                print (k[0].upper(), "ayı", k[1], "gün çekiyor.")
    else: print (ay, "adını sözlükte bulamadım!")

print()
L =list (S)
L.sort()
pprint (L)

print()
L =list (S.items())
L.sort()
pprint (L)
print()
for k in L: print (k[0].upper(), "ayı", k[1], "gün çeker")
print()
L = [(k[1], k[0]) for k in L]
L.sort()
for k in L: print (k[0], "çeken", k[1].upper(), "ayı")

print()
for k in S.items():
    if k[1] == 31: print (k[0], ":", k[1])

