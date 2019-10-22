# coding:iso-8859-9 T�rk�e
# p_21403c.py: Dekorat�r saya�l� LM'in bellekle'mesini de dekorat�rleme �rne�i.

from collections import Counter

def saya� (fonk):
    def yard�mc� (*a, **kwa):
        yard�mc�.�a�r� += 1
        return fonk (*a, **kwa)
    yard�mc�.�a�r� = 0
    yard�mc�.__name__= fonk.__name__
    return yard�mc�

# bellek{} s�zl�k de�i�keni LM'den ar�nd�r�l�p bir dekorat�r fonksiyona konulabilir...
# LM i�i bellek yerine bellekle fonksiyonu �a�r�ld���ndan, �a�r� say�s� bir misli artar.
def bellekle (fonk):
    bellek = {}
    def bellekleyici (*a, **kwa):
        anahtar = str (a) + str (kwa)
        if anahtar not in bellek: bellek [anahtar] = fonk (*a, **kwa)
        return bellek [anahtar]
    return bellekleyici

@saya�
@bellekle
def LM (dizge1, dizge2):
    if dizge1 == "": return len (dizge2)
    if dizge2 == "": return len (dizge1)
    if dizge1 [-1] == dizge2 [-1]: fark = 0
    else: fark = 1
    sonu� = min ([LM (dizge1 [:-1], dizge2) + 1, LM (dizge1, dizge2 [:-1]) + 1, LM (dizge1 [:-1], dizge2 [:-1]) + fark])
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
>python p_21403c.py
�lk ve ikinci dizgelerin d�zeltme mesafesi ve �a�r� say�s�:
-----------------------------------------------------------
LM("Python","Peithen")==> 3 : 127
LM("Python","P") 5 : 128
LM("","Python")==> 6 : 129

LM("Akdeniz","Akdeniizz")==> 2 : 319
LM("Ku�adas�","Ku�addass�") 2 : 560
LM("�skender","�skender")==> 0 : 753
LM("�skenderun","�skendurun")==> 2 : 1054
"""