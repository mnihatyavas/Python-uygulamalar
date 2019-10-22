# coding:iso-8859-9 Türkçe

S = {"hanım":1931, "memet":1934, "hatice":1951, "süheyla":1953, "zeliha":1955,
    "nihat":1957, "songül":1959, "nedim":1961, "sevim":1963, "nur":1972,
    "serap":1974, "yücel":1976,"canan":1975, "zafer":1977, "belkıs":1981,
    "sema":1973, "selda":1975, "fatih":1977, "atilla":1982, "hilal":1984}
print (S)

devam = True
while devam:
    ad = input ("\nSözlükten bir ad girin [Çık: q]: ").lower()
    if ad == "q": break
    if ad in S: print (ad.upper(), "'in yaşı: ", 2018-S[ad], sep="")
    else: print ("<<", ad, ">> sözlükte yok!", sep="")

from random import randint
yaş = 0
while not (0 < yaş < 101):
    try: yaş = int (eval (input ("\nYaş gir: ")))
    except Exception: yaş = randint (1, 100)
print ("\nYaşları ", yaş, "'dan küçüklerin listesi:\n", "-"*35, sep="")
for k in S.items(): # k burada artık 2 elementli bir liste...
    if (2018 - k[1]) <= yaş: print ("{:10s} Doğum: {:4d}, Yaş: {:2d}" .format (k[0].upper(), k[1], 2018-k[1]))