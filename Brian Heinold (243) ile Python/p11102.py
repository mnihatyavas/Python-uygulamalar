# coding:iso-8859-9 T�rk�e

s = {'k�pek' : 'Kuyruklu hayvand�r ve havlar',
    'kedi' : 'K�pekler taraf�ndan kovalan�r ve miyavlar',
    'fare' : 'Kediler taraf�ndan yakalan�rsa yem olur',
    "pili�":"Kedi ve k�peklerin en sevdi�i yiyecek"}

kelime = input ('S�zl�k i�in bir kelime girin: ')
try: print (kelime, 'kelimesinin s�zl�kteki a��klamas�:', s[kelime])
except Exception: print (kelime, "kelimesi s�zl�kte bulunamad�!")

print()
puan = {'A':1, 'B':3, 'C':3, "�":3, 'D':2, 'E':1, 'F':4, 'G':2, "�":2,
    'H':4, 'I':1, "�":1, 'J':8, 'K':5, 'L':1, 'M':3, 'N':1, 'O':1, "�":1, 'P':3, 'Q':10,
    'R':1, 'S':1, "�":1, 'T':1, 'U':1, "�":1, 'V':4, 'W':4, 'X':8, 'Y':4, 'Z':10}
print (kelime, "kelimesinin kazand��� toplam puan:", sum([puan[h.upper()] for h in kelime]) )

print()
deste = [{'say�':s, 'tak�m':t} for t in ['sinek', 'ma�a', 'kupa', 'karo'] for s in range (1,14)]
from pprint import pprint
pprint (deste)
print()
for i in range (len (deste)):
    print (deste [i] ["tak�m"], deste [i] ["say�"])
    if (i+1) % 13 == 0: print()
print (deste[0]["tak�m"], deste[0]["say�"])
print (deste[25]["tak�m"], deste[25]["say�"])
print (deste[26]["tak�m"], deste[26]["say�"])
print (deste[51]["tak�m"], deste[51]["say�"])
print()
from random import shuffle
shuffle (deste)
pprint (deste)
print()
for i in range (len (deste)):
    print (deste[i]["tak�m"], deste[i]["say�"], end=" -->")
