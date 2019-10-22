# coding:iso-8859-9 Türkçe

# Metni dosyadan okuyup, küçük harfleştirip, noktalamadan arındırıp kelimeler listesi yapalım...
metin = open ('demo1.txt').read()
metin = metin.lower()

from string import punctuation
for noktalama in punctuation: metin = metin.replace (noktalama, '')
kelimelerListesi = metin.split() # Kelimeler listesi

# Kelime ve tekrar sayılı bir sözlük kuralım...
sözlük = {}
for kelime in kelimelerListesi:
    if kelime in sözlük: sözlük[kelime] = sözlük[kelime] + 1 # Mevcut kelime sayısı bir artırılır...
    else: sözlük[kelime] = 1 # Yeni kelime sözlüğe eklenir...
print (sözlük)

print()
# Sözlüğü, anahtar kelimeye göre a->z sıralayalım...
tupleListe1 = list (sözlük.items())
tupleListe1.sort()
for i in tupleListe1: print (i)

print()
# Sözlüğü tekrar sayısına göre artan sıralayalım...
tupleListe2 = list (sözlük.items())
tupleListe2 = [(i[1], i[0]) for i in tupleListe2]
tupleListe2.sort()
for i in tupleListe2: print (i)
