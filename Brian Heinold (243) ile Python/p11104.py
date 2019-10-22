# coding:iso-8859-9 T�rk�e

# Metni dosyadan okuyup, k���k harfle�tirip, noktalamadan ar�nd�r�p kelimeler listesi yapal�m...
metin = open ('demo1.txt').read()
metin = metin.lower()

from string import punctuation
for noktalama in punctuation: metin = metin.replace (noktalama, '')
kelimelerListesi = metin.split() # Kelimeler listesi

# Kelime ve tekrar say�l� bir s�zl�k kural�m...
s�zl�k = {}
for kelime in kelimelerListesi:
    if kelime in s�zl�k: s�zl�k[kelime] = s�zl�k[kelime] + 1 # Mevcut kelime say�s� bir art�r�l�r...
    else: s�zl�k[kelime] = 1 # Yeni kelime s�zl��e eklenir...
print (s�zl�k)

print()
# S�zl���, anahtar kelimeye g�re a->z s�ralayal�m...
tupleListe1 = list (s�zl�k.items())
tupleListe1.sort()
for i in tupleListe1: print (i)

print()
# S�zl��� tekrar say�s�na g�re artan s�ralayal�m...
tupleListe2 = list (s�zl�k.items())
tupleListe2 = [(i[1], i[0]) for i in tupleListe2]
tupleListe2.sort()
for i in tupleListe2: print (i)
