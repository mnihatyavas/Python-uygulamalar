# coding:iso-8859-9 T�rk�e

from random import randint

say� = randint (5, 25)
for i in range (say�): print ('Selam')
print (say�, "\n")
saya�=0
for i in range (randint (5, 25)): print ('Selam'); saya� +=1
print (saya�, "\n")
say� = randint (1, 6)
for i in range (5): print ('Selam '*say�)
print (5, "\n")
for i in range (5): print ('Selam ' * randint (1, 6))
print (5, "\n")
saya� = 0
say� = randint (0,10000)
for i in range (say�):
    if randint (1, 100) % 12 == 0: saya�+=1
print (say�, 'kere [1->100] rasgele say�lardan 12 ile b�l�neni:', saya�, "adettir.")
print()