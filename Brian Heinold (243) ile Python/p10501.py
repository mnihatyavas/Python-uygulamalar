# coding:iso-8859-9 Türkçe

from random import randint

sayaç1=sayaç2=0
for i in range (100):
    sayı1 = randint (1,6)
    sayı2 = randint (1,6)
    if sayı1==sayı2==6: sayaç1 +=1
    if sayı1==sayı2: sayaç2 +=1
print ("100 kez attığınız çift zarın", sayaç2, "adeti çift ve bu çiftlerin de", sayaç1, "adeti düşeş geldi!")
print()
sayaç=ara=0
küçük=eval (input ("Döngü başlangıç değerini girin: "))
büyük=eval (input ("Döngü son değerini girin: "))
if küçük > büyük: küçük, büyük = büyük, küçük
for i in range (küçük, büyük+1):
    if 2**i % 10 == 4: sayaç +=1
print ("2^", küçük, "-->2^", büyük, " arasında sonu 4'le biten sayı adeti: ", sayaç, sep="")
