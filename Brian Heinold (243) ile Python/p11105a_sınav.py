# coding:iso-8859-9 T�rk�e

S = {"han�m":1931, "memet":1934, "hatice":1951, "s�heyla":1953, "zeliha":1955,
    "nihat":1957, "song�l":1959, "nedim":1961, "sevim":1963, "nur":1972,
    "serap":1974, "y�cel":1976,"canan":1975, "zafer":1977, "belk�s":1981,
    "sema":1973, "selda":1975, "fatih":1977, "atilla":1982, "hilal":1984}
print (S)

devam = True
while devam:
    ad = input ("\nS�zl�kten bir ad girin [��k: q]: ").lower()
    if ad == "q": break
    if ad in S: print (ad.upper(), "'in ya��: ", 2018-S[ad], sep="")
    else: print ("<<", ad, ">> s�zl�kte yok!", sep="")

from random import randint
ya� = 0
while not (0 < ya� < 101):
    try: ya� = int (eval (input ("\nYa� gir: ")))
    except Exception: ya� = randint (1, 100)
print ("\nYa�lar� ", ya�, "'dan k���klerin listesi:\n", "-"*35, sep="")
for k in S.items(): # k burada art�k 2 elementli bir liste...
    if (2018 - k[1]) <= ya�: print ("{:10s} Do�um: {:4d}, Ya�: {:2d}" .format (k[0].upper(), k[1], 2018-k[1]))