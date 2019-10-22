# coding:iso-8859-9 T�rk�e
# p_13412e.py: 50 adet farkl� ihtimal a��rl�kl� 0-1'ler serisi �reteci �rne�i.

import random

def tesad�fiBirlerS�f�rlar():
    ihtimal = 0.5
    while True:
        x = random.random()
        mesaj = yield 1 if x < ihtimal else 0
        if mesaj != None: ihtimal = mesaj

x = tesad�fiBirlerS�f�rlar()
next (x)  # �rete� ba�lat�l�yor...

print ("4 farkl� yo�unlukta 50 adet tesad�fi seri 1-0 �retimi:", "\n", "-"*76, sep="", end="")

for ih in [0.2, 0.4, 0.6, 0.8]:
    print ("\nBirler ihtimali y�zdesi: %" + str (ih*100) )
    saya� = 0
    x.send (ih)    
    for i in range (50):
        bit = next (x)
        print (bit, end="")
        if bit == 1: saya� +=1
    print ("\tBirler say�s�: ", saya�, "/50", sep="")

"""��kt�:
>python p_13412e.py
4 farkl� yo�unlukta 50 adet tesad�fi seri 1-0 �retimi:
----------------------------------------------------------------------------
Birler ihtimali y�zdesi: %20.0
00100000010000011100001001000010001000001100010000      Birler say�s�: 12/50

Birler ihtimali y�zdesi: %40.0
00110000101010000000110110000011010010001011000110      Birler say�s�: 18/50

Birler ihtimali y�zdesi: %60.0
10101111110101001000111111011100011101011010101111      Birler say�s�: 32/50

Birler ihtimali y�zdesi: %80.0
11111100011111101110111111111111101011011111111111      Birler say�s�: 42/50
"""