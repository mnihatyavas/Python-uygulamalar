# coding:iso-8859-9 Türkçe
# p_13412e.py: 50 adet farklı ihtimal ağırlıklı 0-1'ler serisi üreteci örneği.

import random

def tesadüfiBirlerSıfırlar():
    ihtimal = 0.5
    while True:
        x = random.random()
        mesaj = yield 1 if x < ihtimal else 0
        if mesaj != None: ihtimal = mesaj

x = tesadüfiBirlerSıfırlar()
next (x)  # Üreteç başlatılıyor...

print ("4 farklı yoğunlukta 50 adet tesadüfi seri 1-0 üretimi:", "\n", "-"*76, sep="", end="")

for ih in [0.2, 0.4, 0.6, 0.8]:
    print ("\nBirler ihtimali yüzdesi: %" + str (ih*100) )
    sayaç = 0
    x.send (ih)    
    for i in range (50):
        bit = next (x)
        print (bit, end="")
        if bit == 1: sayaç +=1
    print ("\tBirler sayısı: ", sayaç, "/50", sep="")

"""Çıktı:
>python p_13412e.py
4 farklı yoğunlukta 50 adet tesadüfi seri 1-0 üretimi:
----------------------------------------------------------------------------
Birler ihtimali yüzdesi: %20.0
00100000010000011100001001000010001000001100010000      Birler sayısı: 12/50

Birler ihtimali yüzdesi: %40.0
00110000101010000000110110000011010010001011000110      Birler sayısı: 18/50

Birler ihtimali yüzdesi: %60.0
10101111110101001000111111011100011101011010101111      Birler sayısı: 32/50

Birler ihtimali yüzdesi: %80.0
11111100011111101110111111111111101011011111111111      Birler sayısı: 42/50
"""