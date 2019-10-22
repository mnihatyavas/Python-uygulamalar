# coding:iso-8859-9 Türkçe
# p_21403a.py: Dekoratörlü LM'le hatalı kelime ağırlığı ve tespit çağrı sayısı örneği.

from collections import Counter

def sayaç (fonk):
    def yardımcı (*argümanlar, **kwargümanlar):
        yardımcı.çağrı += 1
        anahtar = str (argümanlar) + str (kwargümanlar)
        yardımcı.say [anahtar] += 1
        return fonk (*argümanlar, **kwargümanlar)
    yardımcı.say = Counter()
    yardımcı.çağrı = 0
    yardımcı.__name__= fonk.__name__
    return yardımcı

@sayaç # Belleksiz dekoratörle kendini çağıran işlem yavaştır...
def LM (d1, d2):
    if d1 == "": return len (d2)
    if d2 == "": return len (d1)
    if d1 [-1] == d2 [-1]: maliyet = 0
    else: maliyet = 1
    sonuç = min ([LM (d1 [:-1], d2) + 1, LM (d1, d2 [:-1]) + 1,  LM (d1 [:-1], d2 [:-1]) + maliyet])
    return sonuç

print (LM ("Python", "Peithen"))
print ("LM tam " + str (LM.çağrı) + " kere çağrıldı!")
#print (LM.say.most_common() )

print ("\nİlk ve ikinci dizgelerin düzeltme mesafesi ve çağrı sayısı:")
print ('LM("Python","Peithen"):', LM ("Python", "Peithen"), LM.çağrı)
print ('LM("Python","P")', LM ("Python", "P"), LM.çağrı)
print ('LM("","Python"):', LM ("", "Python"), LM.çağrı)

print ('LM("Akdeniz","Akdeniizz"):', LM ("Akdeniz", "Akdeniizz"), LM.çağrı)
print ('LM("Kuşadası","Kuşaddassı")', LM ("Kuşadası", "Kuşaddassı"), LM.çağrı)
print ('LM("İskender","İskender"):', LM ("İskender", "İskender"), LM.çağrı)



"""Çıktı:
>python p_21403.py
3
LM tam 29737 kere çağrıldı!

İlk ve ikinci dizgelerin düzeltme mesafesi ve çağrı sayısı:
LM("Python","Peithen"): 3 59474
LM("Python","P") 5 59493
LM("","Python"): 6 59494
LM("Akdeniz","Akdeniizz"): 2 395708
LM("Kuşadası","Kuşaddassı") 2 2280405
LM("İskender","İskender"): 0 2678998
"""