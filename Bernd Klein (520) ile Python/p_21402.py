# coding:iso-8859-9 T�rk�e
# p_21402.py: LevenshteinDistance d�zeltme mesafesi metoduyla kelimenin hata a��rl��� �rne�i.

def LM (d1, d2): # LevenshteinDistance/LevenshteinMesafesi/LM: EditDistance
    if d1 == "": return len (d2)
    if d2 == "": return len (d1)
    if d1 [-1] == d2 [-1]: maliyet = 0
    else: maliyet = 1
    sonu� = min ([LM (d1 [:-1], d2) + 1, LM (d1, d2 [:-1]) + 1, LM (d1 [:-1], d2 [:-1]) + maliyet])
    return sonu�

print ("�lk ve ikinci dizgelerin d�zeltme mesafesi:")
print ('LM("Python","Peithen"):', LM ("Python", "Peithen") )
print ('LM("Python","P")', LM ("Python", "P") )
print ('LM("","Python"):', LM ("", "Python") )
print()
print ('LM("Akdeniz","Akdeniizz"):', LM ("Akdeniz", "Akdeniizz"))
print ('LM("Ku�adas�","Ku�addass�")', LM ("Ku�adas�", "Ku�addass�"))
print ('LM("�skender","�skender"):', LM ("�skender", "�skender"))



"""��kt�:
>python p_21402.py
�lk ve ikinci dizgelerin d�zeltme mesafesi:
LM("Python","Peithen"): 3
LM("Python","P") 5
LM("","Python"): 6

LM("Akdeniz","Akdeniizz"): 2
LM("Ku�adas�","Ku�addass�") 2
LM("�skender","�skender"): 0
"""