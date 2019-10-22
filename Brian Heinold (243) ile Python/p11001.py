# coding:iso-8859-9 Türkçe

print ("1->10000 arası palindromik (tersiyle aynı) sayılar yanyana:", end=" ")
for i in range (1,10001):
    dizge = str (i)
    if dizge == dizge[::-1]: print (dizge, end=" ")

doğum_günü = 'Haziran 1, 1991'
yıl = int (doğum_günü[-4:])
print ("\n\nDoğum gününüz:", doğum_günü, "ise bu günkü yaşınız:", 2018 - yıl, "olur.")
doğum_günü = '17 Nisan 1957'
yıl = int (doğum_günü[-4:])
print ("Doğum gününüz:", doğum_günü, "ise bu günkü yaşınız:", 2018 - yıl, "olur.")
doğum_günü = '07/08/1955'
yıl = int (doğum_günü[-4:])
print ("Doğum gününüz:", doğum_günü, "ise bu günkü yaşınız:", 2018 - yıl, "olur.")
doğum_günü = '7.8.1955'
yıl = int (doğum_günü[-4:])
print ("Doğum gününüz:", doğum_günü, "ise bu günkü yaşınız:", 2018 - yıl, "olur.")

from random import randint
sayı = randint (10, 100000)
dizge = str (sayı)
toplam = 0
for i in range (len (dizge)): toplam += int (dizge[i])
print ("\nGelişigüzel", dizge, "sayısının toplamı:", toplam)
print ("Aynı toplam kapsamlı liste yöntemiyle:", sum ([int (dizge) for dizge in str (sayı)]))

ters = ""
for i in range (len (dizge)): ters = dizge[i] + ters
print ("Gelişigüzel", dizge, "sayısının tersi:", ters)

from random import random
sayı = randint (1, 100000) + random()
tamsayı = int (sayı)
küsürat = sayı - tamsayı
print ("\nSayımız:", sayı, ", tamsayı kısmı:", tamsayı, "ve küsürat kısmı:", küsürat)

sayı = randint (2, 1000)
for i in range (2, int (sayı**0.5)+1):
    if sayı % i == 0: break
else: print ("\nKendisi ve 1'den başka böleni olmayan", sayı, "asaldır.")
