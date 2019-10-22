# coding:iso-8859-9 T�rk�e
# p_21403a.py: Dekorat�rl� LM'le hatal� kelime a��rl��� ve tespit �a�r� say�s� �rne�i.

from collections import Counter

def saya� (fonk):
    def yard�mc� (*arg�manlar, **kwarg�manlar):
        yard�mc�.�a�r� += 1
        anahtar = str (arg�manlar) + str (kwarg�manlar)
        yard�mc�.say [anahtar] += 1
        return fonk (*arg�manlar, **kwarg�manlar)
    yard�mc�.say = Counter()
    yard�mc�.�a�r� = 0
    yard�mc�.__name__= fonk.__name__
    return yard�mc�

@saya� # Belleksiz dekorat�rle kendini �a��ran i�lem yava�t�r...
def LM (d1, d2):
    if d1 == "": return len (d2)
    if d2 == "": return len (d1)
    if d1 [-1] == d2 [-1]: maliyet = 0
    else: maliyet = 1
    sonu� = min ([LM (d1 [:-1], d2) + 1, LM (d1, d2 [:-1]) + 1,  LM (d1 [:-1], d2 [:-1]) + maliyet])
    return sonu�

print (LM ("Python", "Peithen"))
print ("LM tam " + str (LM.�a�r�) + " kere �a�r�ld�!")
#print (LM.say.most_common() )

print ("\n�lk ve ikinci dizgelerin d�zeltme mesafesi ve �a�r� say�s�:")
print ('LM("Python","Peithen"):', LM ("Python", "Peithen"), LM.�a�r�)
print ('LM("Python","P")', LM ("Python", "P"), LM.�a�r�)
print ('LM("","Python"):', LM ("", "Python"), LM.�a�r�)

print ('LM("Akdeniz","Akdeniizz"):', LM ("Akdeniz", "Akdeniizz"), LM.�a�r�)
print ('LM("Ku�adas�","Ku�addass�")', LM ("Ku�adas�", "Ku�addass�"), LM.�a�r�)
print ('LM("�skender","�skender"):', LM ("�skender", "�skender"), LM.�a�r�)



"""��kt�:
>python p_21403.py
3
LM tam 29737 kere �a�r�ld�!

�lk ve ikinci dizgelerin d�zeltme mesafesi ve �a�r� say�s�:
LM("Python","Peithen"): 3 59474
LM("Python","P") 5 59493
LM("","Python"): 6 59494
LM("Akdeniz","Akdeniizz"): 2 395708
LM("Ku�adas�","Ku�addass�") 2 2280405
LM("�skender","�skender"): 0 2678998
"""