# coding:iso-8859-9 Türkçe
# p_11601.py: for-in döngüsüyle programlama dilleri ve yiyecekler listelerini tarama örneği.

diller = ["Basic", "Fortran", "Cobol", "PL/I", "Pascal", "C", "Clipper", "Java", "Java Script", "Python", "Assembly"]
print ("Programlama dilleri: ", end="")
for dil in diller: print (dil, end=", ")
#=========================================================

print("\n")
yiyecekler = ["jambon", "yumurta", "fındık", "tost", "peynir", "simit"] #, "pasta"
for yiyecek in yiyecekler:
    if yiyecek == "pasta":
        print ("Lütfen kalsın, daha fazla pasta istemiyorum!")
        break
    print ("Müthiş lezzetli " + yiyecek +"'larınız var!")

else: print ("\nYiyecekler çok hoştu ama pastanız da yok muydu?")

print ("\nNihayet, ancak doyabildim!")
#=========================================================

print("\n")
yiyecekler = ["jambon", "yumurta", "pasta", "fındık", "tost", "peynir", "simit"]
for yiyecek in yiyecekler:
    if yiyecek == "pasta":
        print ("Lütfen kalsın, pastayla aram pek iyi değil!")
        continue
    print ("Müthiş lezzetli " + yiyecek +"'larınız var!")

print ("\nNihayet, ancak doyabildim!")


"""Çıktı:
>python p_11601.py
Programlama dilleri: Basic, Fortran, Cobol, PL/I, Pascal, C, Clipper, Java, Java Script, Python, Assembly,

Müthiş lezzetli jambon'larınız var!
Müthiş lezzetli yumurta'larınız var!
Müthiş lezzetli fındık'larınız var!
Müthiş lezzetli tost'larınız var!
Müthiş lezzetli peynir'larınız var!
Müthiş lezzetli simit'larınız var!

Yiyecekler çok hoştu ama pastanız da yok muydu?

Nihayet, ancak doyabildim!


Müthiş lezzetli jambon'larınız var!
Müthiş lezzetli yumurta'larınız var!
Lütfen kalsın, pastayla aram pek iyi değil!
Müthiş lezzetli fındık'larınız var!
Müthiş lezzetli tost'larınız var!
Müthiş lezzetli peynir'larınız var!
Müthiş lezzetli simit'larınız var!

Nihayet, ancak doyabildim!
"""