# coding:iso-8859-9 T�rk�e

from random import choice
adlar = ['Nihat', 'Mahmut', 'Sevim', 'Song�l', 'Memet', 'Necati', 'Han�m', 'Hatice']
print ("Akt�el oyuncu:", choice (adlar))

from random import sample
print ("Akt�el ��l�:", sample (adlar, 3))
print()
dizge='abc�defg�h�ijklmno�pqrs�tu�vwxyz1234567890!@#$%^&*().,:;'
for i in range (100): print (choice (dizge), end='')
print("\n")
from random import shuffle
shuffle (adlar)
for a in adlar: print (a, 'haz�rlan, senin s�ran geldi!')
print()
shuffle (adlar)
tak�m = []
if not len(adlar) % 2:
    for i in range (0, len (adlar), 2): tak�m.append ([adlar[i], adlar[i+1]])
    print ("�iftleri a��kl�yorum:", tak�m)