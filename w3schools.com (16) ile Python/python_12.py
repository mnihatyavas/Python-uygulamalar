# coding:iso-8859-9 T�rk�e

import random # Geli�ig�zel (0->1) say� �reten mod�l

print ("(100,500) aras� tesad�fi say�:", random.randint (100,500))
print ("(0,50000) aras� tesad�fi say�:", random.randint (1,50000))
print ("(-1000,+1000) aras� tesad�fi say�:", random.randint (-1000,1000))
print("\n\n")

say� = int (input ("Girece�iniz say�n�n 1->10 katlar� listenecektir: "))  
for i in range (1,11): # Erime ilk dahil, son hari�tir...
     print (say�, 'x', i, '=', say� * i) 
