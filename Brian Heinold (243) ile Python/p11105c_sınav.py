# coding:iso-8859-9 Türkçe

S = {"hanım":"1931hnm", "memet":"1934mmt", "hatice":"1951htc", "süheyla":"1953shyl", "zeliha":"1955zlh", "nihat":"1957nht", "songül":"1959sngl", "nedim":"1961ndm", "sevim":"1963svm", "nur":"1972nr"}
print (S)
print()
from pprint import pprint
pprint (S)

print()
ad = input ("Kullanıcı adını girin: ").lower()
if ad not in S: print ("<<", ad, ">> adlı bir kullanıcı sistemimizde mevcut değil!", sep="")
else:
    şifre = input ("Şifrenizi girin: ").lower()
    if S[ad] != şifre: print ("Maalesef girdiğiniz şifre sistemimizdekiyle uyuşmuyor!")
    else: print ("Sistemimize girmiş bulunuyorsunuz. Hoşgeldiniz sayın <<", ad.upper(), ">>", sep="")
