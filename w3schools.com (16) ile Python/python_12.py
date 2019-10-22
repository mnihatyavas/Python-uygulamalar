# coding:iso-8859-9 Türkçe

import random # Gelişigüzel (0->1) sayı üreten modül

print ("(100,500) arası tesadüfi sayı:", random.randint (100,500))
print ("(0,50000) arası tesadüfi sayı:", random.randint (1,50000))
print ("(-1000,+1000) arası tesadüfi sayı:", random.randint (-1000,1000))
print("\n\n")

sayı = int (input ("Gireceğiniz sayının 1->10 katları listenecektir: "))  
for i in range (1,11): # Erime ilk dahil, son hariçtir...
     print (sayı, 'x', i, '=', sayı * i) 
