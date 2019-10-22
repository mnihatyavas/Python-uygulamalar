# coding:iso-8859-9 Türkçe
# p_10601.py: Python işlemcileriyle yapılan işlem çıktıları örneği.

print ("Toplama ve çıkarma (10+/-3):", 10+3, 10-3)
print ("Çarpma, bölme ve kalan (27*/+7):", 27*7, 27/7, 27%7)
print ("Küsüratsız (-+//) zemin bölme ve -+int(10/3) kesik bölmesi:", 10//3, int (10/3), -10//3.0, int (-10/3) )
print ("Çebirsel -+ işareti:", -3, +3)
print ("Bitvari negatifleme:", ~3-4, ~-4+3)
print ("-+Üs (**):", -2.5**5.78, 2.5**(-5.78) )
print ("Boolean or/veya, and/ve ve not/değil:", not (True or (True and False)) )
print ("Elemanı mı (True/False)?", 4 in [1957, 4, 17] )
print ("Karşılaştırma (2 ila 5) operatörleri (<, <=, >, >=, ==, !=):", 2<5, 2<=5, 2>5, 2>=5, 2==5, 2!=5)
print ("Bitvari |/veya, &/ve, ^/farklıysa (6=110 ila 3=011):", 6|3, 6&3, 6^3)
print ("Kaydırma << ve >> operatörleri (6=110'yı 2 kez kaydır):", 6<<2, 6>>2)


"""Çıktı:
>python p_10601.py
Toplama ve çıkarma (10+/-3): 13 7
Çarpma, bölme ve kalan (27*/+7): 189 3.857142857142857 6
Küsüratsız (-+//) zemin bölme ve -+int(10/3) kesik bölmesi: 3 3 -4.0 -3
Çebirsel -+ işareti: -3 3
Bitvari negatifleme: -8 6
-+Üs (**): -199.5690776400273 0.00501079632087968
Boolean or/veya, and/ve ve not/değil: False
Elemanı mı (True/False)? True
Karşılaştırma (2 ila 5) operatörleri (<, <=, >, >=, ==, !=): True True False Fal
se False True
Bitvari |/veya, &/ve, ^/farklıysa (6=110 ila 3=011): 7 2 5
Kaydırma << ve >> operatörleri (6=110'yı 2 kez kaydır): 24 1
"""