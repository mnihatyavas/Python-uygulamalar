# coding:iso-8859-9 Türkçe

# from random import randint ==>Kullanım: randint (0, 10)
# from random import randint as ri ==>Kullanım: ri (0, 19)
# from random import * ==>Kullanım: randint (0, 10)
import random #==>Kullanım: random.randint (0, 10)

print ("Büyük gelişigüzel tamsayı:", random.randint (0, 10**100) )
print ("\nGelişigüzel küsüratlı sayı:", random.randint (0, 1000) + random.random() )

print ("\n'dir' ile random modülünün içerdiği değişken ve fonksiyonlar:", dir (random) )
print ("\n'help' ile random.randint(..) fonksiyonunun detaylı açıklamaları:", help (random.randint) )
print ("\n'help' ile random modülünün içerdiği değişken ve fonksiyonların detaylı açıklamaları:", help (random) )
