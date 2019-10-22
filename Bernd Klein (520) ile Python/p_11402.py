# coding:iso-8859-9 Türkçe
# p_11402.py: if-elif ile köpek ve insan yaşlarının karşılaştırılması örneği.

from random import randint

try: yaş = abs (int (eval (input ("Köpeğinizin yaşı kaç? "))))
except: yaş = randint (0, 15)

print()
if yaş < 1: print ("Bir yıldan küçük köpek yaşı, yaklaşık 5 insan yaşına eşdeğerdir")
elif yaş == 1: print ("1 köpek yaşı yaklaşık 14 insan yaşına eşdeğerdir")
elif yaş == 2:print ("2 köpek yaşı yaklaşık 22 insan yaşına eşdeğerdir")
elif yaş > 2: print (yaş, "köpek yaşı yaklaşık", 22+(yaş-2)*5, "insan yaşına eşdeğerdir")


"""Çıktı:
>python p_11402.py
Köpeğinizin yaşı kaç?

6 köpek yaşı yaklaşık 42 insan yaşına eşdeğerdir

>python p_11402.py  ** TEKRAR **
Köpeğinizin yaşı kaç? 15

15 köpek yaşı yaklaşık 87 insan yaşına eşdeğerdir
"""