# coding:iso-8859-9 T�rk�e

# from random import randint ==>Kullan�m: randint (0, 10)
# from random import randint as ri ==>Kullan�m: ri (0, 19)
# from random import * ==>Kullan�m: randint (0, 10)
import random #==>Kullan�m: random.randint (0, 10)

print ("B�y�k geli�ig�zel tamsay�:", random.randint (0, 10**100) )
print ("\nGeli�ig�zel k�s�ratl� say�:", random.randint (0, 1000) + random.random() )

print ("\n'dir' ile random mod�l�n�n i�erdi�i de�i�ken ve fonksiyonlar:", dir (random) )
print ("\n'help' ile random.randint(..) fonksiyonunun detayl� a��klamalar�:", help (random.randint) )
print ("\n'help' ile random mod�l�n�n i�erdi�i de�i�ken ve fonksiyonlar�n detayl� a��klamalar�:", help (random) )
