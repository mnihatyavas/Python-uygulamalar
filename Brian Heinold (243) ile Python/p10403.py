# coding:iso-8859-9 Türkçe

Not = eval (input ('Yılsonu ortalama notunuzu girin: '))

if Not < 0: Not = 0
if Not > 100: Not = 100

if 100 >= Not >=95: print ('Diploma dereceniz: A+')
if 95 > Not >=85: print ('Diploma dereceniz: A')
if 85 > Not >=80: print ('Diploma dereceniz: B+')
if 80 > Not >=70: print ('Diploma dereceniz: B')
if 70 > Not >=65: print ('Diploma dereceniz: C+')
if 65 > Not >=50: print ('Diploma dereceniz: C')
if 50 > Not >=45: print ('Diploma dereceniz: D+')
if 45 > Not >=35: print ('Diploma dereceniz: D')
if 35 > Not >=25: print ('Diploma dereceniz: E')
if not (100>= Not >=25): print ('Diploma dereceniz: F')
