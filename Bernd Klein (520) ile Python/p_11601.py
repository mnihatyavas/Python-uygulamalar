# coding:iso-8859-9 T�rk�e
# p_11601.py: for-in d�ng�s�yle programlama dilleri ve yiyecekler listelerini tarama �rne�i.

diller = ["Basic", "Fortran", "Cobol", "PL/I", "Pascal", "C", "Clipper", "Java", "Java Script", "Python", "Assembly"]
print ("Programlama dilleri: ", end="")
for dil in diller: print (dil, end=", ")
#=========================================================

print("\n")
yiyecekler = ["jambon", "yumurta", "f�nd�k", "tost", "peynir", "simit"] #, "pasta"
for yiyecek in yiyecekler:
    if yiyecek == "pasta":
        print ("L�tfen kals�n, daha fazla pasta istemiyorum!")
        break
    print ("M�thi� lezzetli " + yiyecek +"'lar�n�z var!")

else: print ("\nYiyecekler �ok ho�tu ama pastan�z da yok muydu?")

print ("\nNihayet, ancak doyabildim!")
#=========================================================

print("\n")
yiyecekler = ["jambon", "yumurta", "pasta", "f�nd�k", "tost", "peynir", "simit"]
for yiyecek in yiyecekler:
    if yiyecek == "pasta":
        print ("L�tfen kals�n, pastayla aram pek iyi de�il!")
        continue
    print ("M�thi� lezzetli " + yiyecek +"'lar�n�z var!")

print ("\nNihayet, ancak doyabildim!")


"""��kt�:
>python p_11601.py
Programlama dilleri: Basic, Fortran, Cobol, PL/I, Pascal, C, Clipper, Java, Java Script, Python, Assembly,

M�thi� lezzetli jambon'lar�n�z var!
M�thi� lezzetli yumurta'lar�n�z var!
M�thi� lezzetli f�nd�k'lar�n�z var!
M�thi� lezzetli tost'lar�n�z var!
M�thi� lezzetli peynir'lar�n�z var!
M�thi� lezzetli simit'lar�n�z var!

Yiyecekler �ok ho�tu ama pastan�z da yok muydu?

Nihayet, ancak doyabildim!


M�thi� lezzetli jambon'lar�n�z var!
M�thi� lezzetli yumurta'lar�n�z var!
L�tfen kals�n, pastayla aram pek iyi de�il!
M�thi� lezzetli f�nd�k'lar�n�z var!
M�thi� lezzetli tost'lar�n�z var!
M�thi� lezzetli peynir'lar�n�z var!
M�thi� lezzetli simit'lar�n�z var!

Nihayet, ancak doyabildim!
"""