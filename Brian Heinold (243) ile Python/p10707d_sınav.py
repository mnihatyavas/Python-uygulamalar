# coding:iso-8859-9 T�rk�e

from random import randint

try: a=abs(eval(input("Feet cinsinden de�er girin: ")))
except Exception: a=randint(1,10000)

b= eval(input("�evir [1:in�, 2:yard, 3:mil, 4:mm, 5:sm, 6:m, 7:km]: "))
if b < 1 or b > 7: b = randint (1,7)

�evrim=[12, 1/3, 1/5292, 304.8, 30.48, 1/3.281, 1/3281]
izah= ["in�", "yard", "mil", "mm", "sm", "m", "km"]

print (a, " feet=", round (a*�evrim[b-1], 5), " ", izah[b-1], "'dir.", sep="")

""" Not: �evrim de�erleri...
1 mil = 1.6129 km
1 feet = 12 in�
1 in� = 2.54 sm
1 yard = 3 feet
"""