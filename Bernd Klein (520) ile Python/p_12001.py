# coding:iso-8859-9 T�rk�e
# p_12001.py: def-ine ile C->F ve C->K �s� �evrim fonksiyonlar� �rne�i.

from random import randint, random

def fahrenhayt (selsiy�s): return selsiy�s * 1.8 + 32
def kelvin (selsiy�s): return 273 + selsiy�s

print ("C derece'den F/Fahrenhayt ve K/Kelvin derece'ye �evrim:\n", "-"*55, sep="")
for �s� in (-273, 0, 100): # T�ple tekrarlanabilir...
    print ("{:.2f} C = {:.2f} F derecedir." .format (�s�, fahrenhayt (�s�)) )
    print ("{:.2f} C = {:.2f} K derecedir.\n" .format (�s�, kelvin (�s�)) )

for �s� in [randint (-273, 100) + random() for i in range (10)]: # Liste tekrarlanabilir...
    print ("{:.2f} C = {:.2f} F derecedir." .format (�s�, fahrenhayt (�s�)) )
    print ("{:.2f} C = {:.2f} K derecedir.\n" .format (�s�, kelvin (�s�)) )


"""��kt�:
>python p_12001.py
C derece'den F/Fahrenhayt ve K/Kelvin derece'ye �evrim:
-------------------------------------------------------
-273.00 C = -459.40 F derecedir.
-273.00 C = 0.00 K derecedir.

0.00 C = 32.00 F derecedir.
0.00 C = 273.00 K derecedir.

100.00 C = 212.00 F derecedir.
100.00 C = 373.00 K derecedir.

37.69 C = 99.85 F derecedir.
37.69 C = 310.69 K derecedir.

-173.55 C = -280.40 F derecedir.
-173.55 C = 99.45 K derecedir.

8.14 C = 46.65 F derecedir.
8.14 C = 281.14 K derecedir.

-2.64 C = 27.26 F derecedir.
-2.64 C = 270.36 K derecedir.

-151.82 C = -241.27 F derecedir.
-151.82 C = 121.18 K derecedir.

-104.59 C = -156.27 F derecedir.
-104.59 C = 168.41 K derecedir.

-101.07 C = -149.93 F derecedir.
-101.07 C = 171.93 K derecedir.

-18.08 C = -0.54 F derecedir.
-18.08 C = 254.92 K derecedir.

-113.01 C = -171.42 F derecedir.
-113.01 C = 159.99 K derecedir.

-35.12 C = -31.21 F derecedir.
-35.12 C = 237.88 K derecedir.
"""