# coding:iso-8859-9 T�rk�e

Not = eval (input ('Y�lsonu ortalama notunuzu girin: '))

if Not < 0: Not = 0
if Not > 100: Not = 100
hasta = True

if Not <= 100 and Not >=95: print ('Diploma dereceniz: A+')
if Not < 95 and Not >=85: print ('Diploma dereceniz: A')
if Not < 85 and Not >=80: print ('Diploma dereceniz: B+')
if Not < 80 and Not >=70: print ('Diploma dereceniz: B')
if Not < 70 and Not >=65: print ('Diploma dereceniz: C+')
if Not < 65 and Not >=50: print ('Diploma dereceniz: C')
if Not < 50 and Not >=45: print ('Diploma dereceniz: D+ (�artl� Ge�er)')
if Not < 45 and Not >=35: print ('Diploma dereceniz: D (�kmale Kal�r)')
if Not < 35 and Not >=25: print ('Diploma dereceniz: E (Ders Tekrar�)')
if hasta and Not == 0: print ('Diploma dereceniz: D- (Makeup Telafisi)')
elif not (Not > 24): print ('Diploma dereceniz: F (S�n�f Tekrar�)')
