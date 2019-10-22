# coding:iso-8859-9 T�rk�e
# p_10601.py: Python i�lemcileriyle yap�lan i�lem ��kt�lar� �rne�i.

print ("Toplama ve ��karma (10+/-3):", 10+3, 10-3)
print ("�arpma, b�lme ve kalan (27*/+7):", 27*7, 27/7, 27%7)
print ("K�s�rats�z (-+//) zemin b�lme ve -+int(10/3) kesik b�lmesi:", 10//3, int (10/3), -10//3.0, int (-10/3) )
print ("�ebirsel -+ i�areti:", -3, +3)
print ("Bitvari negatifleme:", ~3-4, ~-4+3)
print ("-+�s (**):", -2.5**5.78, 2.5**(-5.78) )
print ("Boolean or/veya, and/ve ve not/de�il:", not (True or (True and False)) )
print ("Eleman� m� (True/False)?", 4 in [1957, 4, 17] )
print ("Kar��la�t�rma (2 ila 5) operat�rleri (<, <=, >, >=, ==, !=):", 2<5, 2<=5, 2>5, 2>=5, 2==5, 2!=5)
print ("Bitvari |/veya, &/ve, ^/farkl�ysa (6=110 ila 3=011):", 6|3, 6&3, 6^3)
print ("Kayd�rma << ve >> operat�rleri (6=110'y� 2 kez kayd�r):", 6<<2, 6>>2)


"""��kt�:
>python p_10601.py
Toplama ve ��karma (10+/-3): 13 7
�arpma, b�lme ve kalan (27*/+7): 189 3.857142857142857 6
K�s�rats�z (-+//) zemin b�lme ve -+int(10/3) kesik b�lmesi: 3 3 -4.0 -3
�ebirsel -+ i�areti: -3 3
Bitvari negatifleme: -8 6
-+�s (**): -199.5690776400273 0.00501079632087968
Boolean or/veya, and/ve ve not/de�il: False
Eleman� m� (True/False)? True
Kar��la�t�rma (2 ila 5) operat�rleri (<, <=, >, >=, ==, !=): True True False Fal
se False True
Bitvari |/veya, &/ve, ^/farkl�ysa (6=110 ila 3=011): 7 2 5
Kayd�rma << ve >> operat�rleri (6=110'y� 2 kez kayd�r): 24 1
"""