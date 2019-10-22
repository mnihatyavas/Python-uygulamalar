# coding:iso-8859-9 Türkçe
# p_21402.py: LevenshteinDistance düzeltme mesafesi metoduyla kelimenin hata ağırlığı örneği.

def LM (d1, d2): # LevenshteinDistance/LevenshteinMesafesi/LM: EditDistance
    if d1 == "": return len (d2)
    if d2 == "": return len (d1)
    if d1 [-1] == d2 [-1]: maliyet = 0
    else: maliyet = 1
    sonuç = min ([LM (d1 [:-1], d2) + 1, LM (d1, d2 [:-1]) + 1, LM (d1 [:-1], d2 [:-1]) + maliyet])
    return sonuç

print ("İlk ve ikinci dizgelerin düzeltme mesafesi:")
print ('LM("Python","Peithen"):', LM ("Python", "Peithen") )
print ('LM("Python","P")', LM ("Python", "P") )
print ('LM("","Python"):', LM ("", "Python") )
print()
print ('LM("Akdeniz","Akdeniizz"):', LM ("Akdeniz", "Akdeniizz"))
print ('LM("Kuşadası","Kuşaddassı")', LM ("Kuşadası", "Kuşaddassı"))
print ('LM("İskender","İskender"):', LM ("İskender", "İskender"))



"""Çıktı:
>python p_21402.py
İlk ve ikinci dizgelerin düzeltme mesafesi:
LM("Python","Peithen"): 3
LM("Python","P") 5
LM("","Python"): 6

LM("Akdeniz","Akdeniizz"): 2
LM("Kuşadası","Kuşaddassı") 2
LM("İskender","İskender"): 0
"""