# coding:iso-8859-9 Türkçe

from random import choice
adlar = ['Nihat', 'Mahmut', 'Sevim', 'Songül', 'Memet', 'Necati', 'Hanım', 'Hatice']
print ("Aktüel oyuncu:", choice (adlar))

from random import sample
print ("Aktüel üçlü:", sample (adlar, 3))
print()
dizge='abcçdefgğhıijklmnoöpqrsştuüvwxyz1234567890!@#$%^&*().,:;'
for i in range (100): print (choice (dizge), end='')
print("\n")
from random import shuffle
shuffle (adlar)
for a in adlar: print (a, 'hazırlan, senin sıran geldi!')
print()
shuffle (adlar)
takım = []
if not len(adlar) % 2:
    for i in range (0, len (adlar), 2): takım.append ([adlar[i], adlar[i+1]])
    print ("Çiftleri açıklıyorum:", takım)