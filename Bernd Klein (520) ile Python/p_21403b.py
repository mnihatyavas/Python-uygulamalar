# coding:iso-8859-9 T�rk�e
# p_21403b.py: Dekorat�r saya�l� LM s�ratinin belleklemeyle verimlile�tirilmesi �rne�i.

from collections import Counter

def saya� (fonk):
    def yard�mc� (*arg�manlar, **kwarg�manlar):
        yard�mc�.�a�r� += 1
        return fonk (*arg�manlar, **kwarg�manlar)
    yard�mc�.�a�r� = 0
    yard�mc�.__name__= fonk.__name__
    return yard�mc�

bellek = {} # bellek'le 5 bin, 300 bin gibi �a�r� say�lar� �ok �ok d���r�l�r...

@saya�
def LM (d1, d2):
    if d1 == "": return len (d2)
    if d2 == "": return len (d1)
    mesafe = 0 if d1 [-1] == d2 [-1] else 1
    i1 = (d1 [:-1], d2)
    if not i1 in bellek: bellek [i1] = LM (*i1)
    i2 = (d1, d2 [:-1])
    if not i2 in bellek: bellek [i2] = LM (*i2)
    i3 = (d1 [:-1], d2 [:-1])
    if not i3 in bellek: bellek [i3] = LM (*i3)
    sonu� = min ([bellek [i1] + 1, bellek [i2] + 1, bellek [i3] + mesafe])
    return sonu�

print ("�lk ve ikinci dizgelerin d�zeltme mesafesi ve �a�r� say�s�:\n", "-"*59, sep="")
print ('LM("Python","Peithen")==>', LM ("Python", "Peithen"), ":", LM.�a�r�)
print ('LM("Python","P")', LM ("Python", "P"), ":", LM.�a�r�)
print ('LM("","Python")==>', LM ("", "Python"), ":", LM.�a�r�)

print ('\nLM("Akdeniz","Akdeniizz")==>', LM ("Akdeniz", "Akdeniizz"), ":", LM.�a�r�)
print ('LM("Ku�adas�","Ku�addass�")', LM ("Ku�adas�", "Ku�addass�"), ":", LM.�a�r�)
print ('LM("�skender","�skender")==>', LM ("�skender", "�skender"), ":", LM.�a�r�)
print ('LM("�skenderun","�skendurun")==>', LM ("�skenderun", "Iskendurun"), ":", LM.�a�r�)



"""��kt�:
>python p_21403b.py
�lk ve ikinci dizgelerin d�zeltme mesafesi ve �a�r� say�s�:
-----------------------------------------------------------
LM("Python","Peithen")==> 3 : 56
LM("Python","P") 5 : 57
LM("","Python")==> 6 : 58

LM("Akdeniz","Akdeniizz")==> 2 : 137
LM("Ku�adas�","Ku�addass�") 2 : 235
LM("�skender","�skender")==> 0 : 315
LM("�skenderun","�skendurun")==> 2 : 427
"""