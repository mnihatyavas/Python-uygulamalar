# coding:iso-8859-9 Türkçe

from random import randint

sayı = randint (5, 25)
for i in range (sayı): print ('Selam')
print (sayı, "\n")
sayaç=0
for i in range (randint (5, 25)): print ('Selam'); sayaç +=1
print (sayaç, "\n")
sayı = randint (1, 6)
for i in range (5): print ('Selam '*sayı)
print (5, "\n")
for i in range (5): print ('Selam ' * randint (1, 6))
print (5, "\n")
sayaç = 0
sayı = randint (0,10000)
for i in range (sayı):
    if randint (1, 100) % 12 == 0: sayaç+=1
print (sayı, 'kere [1->100] rasgele sayılardan 12 ile bölüneni:', sayaç, "adettir.")
print()