# coding:iso-8859-9 Türkçe

L = [satır.strip().split ("\t") for satır in open ("öğrenci3.txt")]
from pprint import pprint
print (len (L), " kişilik ÖĞRENCİ listesinin dosyadan dökümü:\n", "="*48, sep="")
pprint (L)

from random import randint
başharfler = input ("\nGörmek istediğin öğrencinin ad ve soyad baş harflerini bitişik gir: ").upper()
if len (başharfler) != 2 or not başharfler[0].isalpha() or not başharfler[1].isalpha(): başharfler = chr (randint (65, 90)) + chr (randint (65, 90))
print ("\nAd ve soyad ilk harfleri: [", başharfler[0], ",", başharfler[1], "] olanların listesi:\n", "-"*50, sep="")
for k in L:
    endeks = len (str (k[0])) - str (k[0])[::-1].index (".")
    if k[0][0] == başharfler[0] and k[0][endeks] == başharfler[1]: print (k)

try: telefon1, telefon2 = eval (input ("\nGörmek istediğin ilk, son 4 haneli telefon no'yu gir: "))
except Exception:
    telefon1 = randint (1000, 9999)
    telefon2 = randint (telefon1+1, 9999)
print ("\nİlk  ve son telefonları: [", telefon1, ",", telefon2, "] olanların listesi:\n", "-"*55, sep="")
for k in L:
    endeks = len (str (k[2])) - str (k[2])[::-1].index ("-")
    if int (k[2] [endeks:]) >= telefon1 and int (k[2] [endeks:]) <= telefon2: print (k)
