# coding:iso-8859-9 Türkçe

from random import randint

print ("Sade Ent harici bir tuşu Ent'larsanız çıkarsınız...")
while not input():
    sayı = randint (3, 10000)
    i = 2
    while i < sayı and sayı % i != 0: i+=1
    if i==sayı: print (sayı, "bir ASAL sayıdır!")
    else: print (sayı, "bir asal sayı DEĞİLDİR!")

print ("\nSadece Ent harici bir HARFİ Ent'larsanız çıkarsınız...")
while not input().isalpha():
    sayı = randint (3, 10000)
    for i in range (2,sayı):
        if sayı % i == 0:
            print (sayı, "bir asal sayı DEĞİLDİR!")
            break
    else: print (sayı, "bir ASAL sayıdır!")
