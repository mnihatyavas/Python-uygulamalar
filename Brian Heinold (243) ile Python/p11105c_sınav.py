# coding:iso-8859-9 T�rk�e

S = {"han�m":"1931hnm", "memet":"1934mmt", "hatice":"1951htc", "s�heyla":"1953shyl", "zeliha":"1955zlh", "nihat":"1957nht", "song�l":"1959sngl", "nedim":"1961ndm", "sevim":"1963svm", "nur":"1972nr"}
print (S)
print()
from pprint import pprint
pprint (S)

print()
ad = input ("Kullan�c� ad�n� girin: ").lower()
if ad not in S: print ("<<", ad, ">> adl� bir kullan�c� sistemimizde mevcut de�il!", sep="")
else:
    �ifre = input ("�ifrenizi girin: ").lower()
    if S[ad] != �ifre: print ("Maalesef girdi�iniz �ifre sistemimizdekiyle uyu�muyor!")
    else: print ("Sistemimize girmi� bulunuyorsunuz. Ho�geldiniz say�n <<", ad.upper(), ">>", sep="")
