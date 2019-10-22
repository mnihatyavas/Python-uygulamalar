# coding:iso-8859-9 Türkçe
# p_21403b.py: Dekoratör sayaçlı LM süratinin belleklemeyle verimlileştirilmesi örneği.

from collections import Counter

def sayaç (fonk):
    def yardımcı (*argümanlar, **kwargümanlar):
        yardımcı.çağrı += 1
        return fonk (*argümanlar, **kwargümanlar)
    yardımcı.çağrı = 0
    yardımcı.__name__= fonk.__name__
    return yardımcı

bellek = {} # bellek'le 5 bin, 300 bin gibi çağrı sayıları çok çok düşürülür...

@sayaç
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
    sonuç = min ([bellek [i1] + 1, bellek [i2] + 1, bellek [i3] + mesafe])
    return sonuç

print ("İlk ve ikinci dizgelerin düzeltme mesafesi ve çağrı sayısı:\n", "-"*59, sep="")
print ('LM("Python","Peithen")==>', LM ("Python", "Peithen"), ":", LM.çağrı)
print ('LM("Python","P")', LM ("Python", "P"), ":", LM.çağrı)
print ('LM("","Python")==>', LM ("", "Python"), ":", LM.çağrı)

print ('\nLM("Akdeniz","Akdeniizz")==>', LM ("Akdeniz", "Akdeniizz"), ":", LM.çağrı)
print ('LM("Kuşadası","Kuşaddassı")', LM ("Kuşadası", "Kuşaddassı"), ":", LM.çağrı)
print ('LM("İskender","İskender")==>', LM ("İskender", "İskender"), ":", LM.çağrı)
print ('LM("İskenderun","İskendurun")==>', LM ("İskenderun", "Iskendurun"), ":", LM.çağrı)



"""Çıktı:
>python p_21403b.py
İlk ve ikinci dizgelerin düzeltme mesafesi ve çağrı sayısı:
-----------------------------------------------------------
LM("Python","Peithen")==> 3 : 56
LM("Python","P") 5 : 57
LM("","Python")==> 6 : 58

LM("Akdeniz","Akdeniizz")==> 2 : 137
LM("Kuşadası","Kuşaddassı") 2 : 235
LM("İskender","İskender")==> 0 : 315
LM("İskenderun","İskendurun")==> 2 : 427
"""