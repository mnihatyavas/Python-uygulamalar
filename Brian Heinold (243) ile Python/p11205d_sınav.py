# coding:iso-8859-9 T�rk�e

L = [sat�r.strip().split ("\t") for sat�r in open ("��renci3.txt")]
from pprint import pprint
print (len (L), " ki�ilik ��RENC� listesinin dosyadan d�k�m�:\n", "="*48, sep="")
pprint (L)

from random import randint
ba�harfler = input ("\nG�rmek istedi�in ��rencinin ad ve soyad ba� harflerini biti�ik gir: ").upper()
if len (ba�harfler) != 2 or not ba�harfler[0].isalpha() or not ba�harfler[1].isalpha(): ba�harfler = chr (randint (65, 90)) + chr (randint (65, 90))
print ("\nAd ve soyad ilk harfleri: [", ba�harfler[0], ",", ba�harfler[1], "] olanlar�n listesi:\n", "-"*50, sep="")
for k in L:
    endeks = len (str (k[0])) - str (k[0])[::-1].index (".")
    if k[0][0] == ba�harfler[0] and k[0][endeks] == ba�harfler[1]: print (k)

try: telefon1, telefon2 = eval (input ("\nG�rmek istedi�in ilk, son 4 haneli telefon no'yu gir: "))
except Exception:
    telefon1 = randint (1000, 9999)
    telefon2 = randint (telefon1+1, 9999)
print ("\n�lk  ve son telefonlar�: [", telefon1, ",", telefon2, "] olanlar�n listesi:\n", "-"*55, sep="")
for k in L:
    endeks = len (str (k[2])) - str (k[2])[::-1].index ("-")
    if int (k[2] [endeks:]) >= telefon1 and int (k[2] [endeks:]) <= telefon2: print (k)
