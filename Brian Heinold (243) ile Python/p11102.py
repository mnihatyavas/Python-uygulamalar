# coding:iso-8859-9 Türkçe

s = {'köpek' : 'Kuyruklu hayvandır ve havlar',
    'kedi' : 'Köpekler tarafından kovalanır ve miyavlar',
    'fare' : 'Kediler tarafından yakalanırsa yem olur',
    "piliç":"Kedi ve köpeklerin en sevdiği yiyecek"}

kelime = input ('Sözlük için bir kelime girin: ')
try: print (kelime, 'kelimesinin sözlükteki açıklaması:', s[kelime])
except Exception: print (kelime, "kelimesi sözlükte bulunamadı!")

print()
puan = {'A':1, 'B':3, 'C':3, "Ç":3, 'D':2, 'E':1, 'F':4, 'G':2, "Ğ":2,
    'H':4, 'I':1, "İ":1, 'J':8, 'K':5, 'L':1, 'M':3, 'N':1, 'O':1, "Ö":1, 'P':3, 'Q':10,
    'R':1, 'S':1, "Ş":1, 'T':1, 'U':1, "Ü":1, 'V':4, 'W':4, 'X':8, 'Y':4, 'Z':10}
print (kelime, "kelimesinin kazandığı toplam puan:", sum([puan[h.upper()] for h in kelime]) )

print()
deste = [{'sayı':s, 'takım':t} for t in ['sinek', 'maça', 'kupa', 'karo'] for s in range (1,14)]
from pprint import pprint
pprint (deste)
print()
for i in range (len (deste)):
    print (deste [i] ["takım"], deste [i] ["sayı"])
    if (i+1) % 13 == 0: print()
print (deste[0]["takım"], deste[0]["sayı"])
print (deste[25]["takım"], deste[25]["sayı"])
print (deste[26]["takım"], deste[26]["sayı"])
print (deste[51]["takım"], deste[51]["sayı"])
print()
from random import shuffle
shuffle (deste)
pprint (deste)
print()
for i in range (len (deste)):
    print (deste[i]["takım"], deste[i]["sayı"], end=" -->")
