# coding:iso-8859-9 Türkçe
# p_11403.py: if-else, if-elif-else, max ve for ile çoklu sayıların enbüyüğünün bulunması örneği.

from random import randint

a = randint (0, 100)
b = randint (0, 100)

büyük = a if a > b else b # Üçlü if ifadesi...
print ("a={}, b={} ise Büyük={}'dir." .format (a, b, büyük) )
#--------------------------------------------------------------------------------------------------

üs = randint (0, 100)
sonuç = (a if a > b else b)**üs%365
print ("a={}, b={} ise Büyük({})**{}%365 = {}'dir." .format (a, b, a if a>b else b, üs, sonuç) )
#--------------------------------------------------------------------------------------------------

c = randint (0, 100)

if a > b and a > c: enbüyük = a
elif b > a and b > c: enbüyük = b
else: enbüyük = c

print ("\n1.if-else yöntemiyle: a={}, b={} ve c={} ise Enbüyük={}'dir." .format (a, b, c, enbüyük) )
#--------------------------------------------------------------------------------------------------

if a > b:
    if a > c: enbüyük = a
    else: enbüyük = c
else:
    if b > c: enbüyük = b
    else: enbüyük = c

print ("2.if-else yöntemiyle: a={}, b={} ve c={} ise Enbüyük={}'dir." .format (a, b, c, enbüyük) )
#--------------------------------------------------------------------------------------------------

d = randint (0, 100)
e= randint (0, 100)

enbüyük = max ((a, b, c, d, e))

print ("\nTüpleli max fonksiyonuyla: a={}, b={}, c={}, d={} ve e={} ise Enbüyük={}'dir." .format (a, b, c, d, e, enbüyük) )
#--------------------------------------------------------------------------------------------------

enbüyük = max ([a, b, c, d, e])

print ("Listeli max fonksiyonuyla: a={}, b={}, c={}, d={} ve e={} ise Enbüyük={}'dir." .format (a, b, c, d, e, enbüyük) )
#--------------------------------------------------------------------------------------------------

try: tekrar = abs (int (eval (input ("Enbüyüğü bulunacak kaç değer girilecek? "))))
except: tekrar = randint (2, 100)

L = [randint (0, 100)]
enbüyük = 0

for i in range (1, tekrar - 1):
    L = L + [randint (0, 100)]
    if L[i] > L[enbüyük] :enbüyük = i

print(); print (tekrar, "adet tesadüfi sayı listesi:", L)
print ("Enbüğünün endeksi:", enbüyük, "ve değeri:", L[enbüyük] )


"""Çıktı:
>python p_11403.py
a=37, b=36 ise Büyük=37'dir.
a=37, b=36 ise Büyük(37)**96%365 = 81'dir.

1.if-else yöntemiyle: a=37, b=36 ve c=65 ise Enbüyük=65'dir.
2.if-else yöntemiyle: a=37, b=36 ve c=65 ise Enbüyük=65'dir.

Tüpleli max fonksiyonuyla: a=37, b=36, c=65, d=20 ve e=21 ise Enbüyük=65'dir.
Listeli max fonksiyonuyla: a=37, b=36, c=65, d=20 ve e=21 ise Enbüyük=65'dir.
Enbüyüğü bulunacak kaç değer girilecek?

38 adet tesadüfi sayı listesi: [37, 46, 94, 44, 71, 97, 12, 54, 93, 26, 66, 38,
33, 32, 68, 90, 18, 20, 43, 68, 99, 35, 6, 92, 92, 90, 20, 100, 48, 18, 56, 95,
40, 0, 0, 72, 58]
Enbüğünün endeksi: 27 ve değeri: 100
"""