# coding:iso-8859-9 Türkçe

import random # from random... hata verir

print ("Seed, Gauss ve Uniform ile aynen tekrarlanan tesadüfivari sayı üretimi:\n", "-"*71, sep="")
random.seed (1)
print ("Tohum 1:", [random.randint (1, 100) for i in range (10)] )

random.seed (2)
print ("Tohum 2:", [random.randint (-50, 50) for i in range (10)])

random.seed (3)
print ("Tohum 3:", [round (random.randint (1, 10) + random.random(), 2) for i in range (10)])

random.seed (3)
print ("\nTekrar tohum 3:", [round (random.randint (1, 10) + random.random(), 2) for i in range (10)])

random.seed (1)
print ("Tekrar tohum 1:", [random.randint (1, 100) for i in range (10)] )

random.seed (2)
print ("Tekrar tohum 2:", [random.randint (-50, 50) for i in range (10)])

print ("\nGauss(64,3.5) tesadüfi dağılımı:", random.gauss (64, 3.5) )
print ([round (random.gauss (64, 3.5), 2) for i in range (10)] )

print ("\nEşit ihtimalli dağılım:", random.uniform (3, 8) )
print ([round (random.uniform (3, 8), 4) for i in range (10)] )