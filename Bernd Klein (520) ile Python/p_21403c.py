# coding:iso-8859-9 Türkçe
# p_21403c.py: Dekoratör sayaçlı LM'in bellekle'mesini de dekoratörleme örneği.

from collections import Counter

def sayaç (fonk):
    def yardımcı (*a, **kwa):
        yardımcı.çağrı += 1
        return fonk (*a, **kwa)
    yardımcı.çağrı = 0
    yardımcı.__name__= fonk.__name__
    return yardımcı

# bellek{} sözlük değişkeni LM'den arındırılıp bir dekoratör fonksiyona konulabilir...
# LM içi bellek yerine bellekle fonksiyonu çağrıldığından, çağrı sayısı bir misli artar.
def bellekle (fonk):
    bellek = {}
    def bellekleyici (*a, **kwa):
        anahtar = str (a) + str (kwa)
        if anahtar not in bellek: bellek [anahtar] = fonk (*a, **kwa)
        return bellek [anahtar]
    return bellekleyici

@sayaç
@bellekle
def LM (dizge1, dizge2):
    if dizge1 == "": return len (dizge2)
    if dizge2 == "": return len (dizge1)
    if dizge1 [-1] == dizge2 [-1]: fark = 0
    else: fark = 1
    sonuç = min ([LM (dizge1 [:-1], dizge2) + 1, LM (dizge1, dizge2 [:-1]) + 1, LM (dizge1 [:-1], dizge2 [:-1]) + fark])
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
>python p_21403c.py
İlk ve ikinci dizgelerin düzeltme mesafesi ve çağrı sayısı:
-----------------------------------------------------------
LM("Python","Peithen")==> 3 : 127
LM("Python","P") 5 : 128
LM("","Python")==> 6 : 129

LM("Akdeniz","Akdeniizz")==> 2 : 319
LM("Kuşadası","Kuşaddassı") 2 : 560
LM("İskender","İskender")==> 0 : 753
LM("İskenderun","İskendurun")==> 2 : 1054
"""