# coding:iso-8859-9 T�rk�e
# p_11403.py: if-else, if-elif-else, max ve for ile �oklu say�lar�n enb�y���n�n bulunmas� �rne�i.

from random import randint

a = randint (0, 100)
b = randint (0, 100)

b�y�k = a if a > b else b # ��l� if ifadesi...
print ("a={}, b={} ise B�y�k={}'dir." .format (a, b, b�y�k) )
#--------------------------------------------------------------------------------------------------

�s = randint (0, 100)
sonu� = (a if a > b else b)**�s%365
print ("a={}, b={} ise B�y�k({})**{}%365 = {}'dir." .format (a, b, a if a>b else b, �s, sonu�) )
#--------------------------------------------------------------------------------------------------

c = randint (0, 100)

if a > b and a > c: enb�y�k = a
elif b > a and b > c: enb�y�k = b
else: enb�y�k = c

print ("\n1.if-else y�ntemiyle: a={}, b={} ve c={} ise Enb�y�k={}'dir." .format (a, b, c, enb�y�k) )
#--------------------------------------------------------------------------------------------------

if a > b:
    if a > c: enb�y�k = a
    else: enb�y�k = c
else:
    if b > c: enb�y�k = b
    else: enb�y�k = c

print ("2.if-else y�ntemiyle: a={}, b={} ve c={} ise Enb�y�k={}'dir." .format (a, b, c, enb�y�k) )
#--------------------------------------------------------------------------------------------------

d = randint (0, 100)
e= randint (0, 100)

enb�y�k = max ((a, b, c, d, e))

print ("\nT�pleli max fonksiyonuyla: a={}, b={}, c={}, d={} ve e={} ise Enb�y�k={}'dir." .format (a, b, c, d, e, enb�y�k) )
#--------------------------------------------------------------------------------------------------

enb�y�k = max ([a, b, c, d, e])

print ("Listeli max fonksiyonuyla: a={}, b={}, c={}, d={} ve e={} ise Enb�y�k={}'dir." .format (a, b, c, d, e, enb�y�k) )
#--------------------------------------------------------------------------------------------------

try: tekrar = abs (int (eval (input ("Enb�y��� bulunacak ka� de�er girilecek? "))))
except: tekrar = randint (2, 100)

L = [randint (0, 100)]
enb�y�k = 0

for i in range (1, tekrar - 1):
    L = L + [randint (0, 100)]
    if L[i] > L[enb�y�k] :enb�y�k = i

print(); print (tekrar, "adet tesad�fi say� listesi:", L)
print ("Enb���n�n endeksi:", enb�y�k, "ve de�eri:", L[enb�y�k] )


"""��kt�:
>python p_11403.py
a=37, b=36 ise B�y�k=37'dir.
a=37, b=36 ise B�y�k(37)**96%365 = 81'dir.

1.if-else y�ntemiyle: a=37, b=36 ve c=65 ise Enb�y�k=65'dir.
2.if-else y�ntemiyle: a=37, b=36 ve c=65 ise Enb�y�k=65'dir.

T�pleli max fonksiyonuyla: a=37, b=36, c=65, d=20 ve e=21 ise Enb�y�k=65'dir.
Listeli max fonksiyonuyla: a=37, b=36, c=65, d=20 ve e=21 ise Enb�y�k=65'dir.
Enb�y��� bulunacak ka� de�er girilecek?

38 adet tesad�fi say� listesi: [37, 46, 94, 44, 71, 97, 12, 54, 93, 26, 66, 38,
33, 32, 68, 90, 18, 20, 43, 68, 99, 35, 6, 92, 92, 90, 20, 100, 48, 18, 56, 95,
40, 0, 0, 72, 58]
Enb���n�n endeksi: 27 ve de�eri: 100
"""