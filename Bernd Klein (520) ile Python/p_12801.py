# coding:iso-8859-9 T�rk�e
# p_12801.py: Python ve kendi mod�l�m�z� import'lama �e�itleri �rne�i.

import math, random
# from math import pi, sin, cos
# from math import *

print ("PI say�s�:", math.pi)
print ("Sin(0/90/180):", math.sin (0), math.sin (math.pi/2), math.sin (math.pi) )
print ("Cos(0/90/180):", math.cos (0), math.cos (math.pi/2), math.cos (math.pi) )

import math as m
print (m.cos (m.pi/4))
print (m.pi)
print (m.e)
print ("-"*75, "\n")
#--------------------------------------------------------------------------------------------------------

from p_12801x import fib1, fib2
f = fib2

while True:
    try: adet = abs (int (input ("\nFibonaki seri adedini girin [0:��k]: ")))
    except: adet = random.randint (1, 20)

    if adet == 0: break
    print ("fib1 y�temiyle: ")
    for i in range (adet): print (fib1 (i), end=" ")
    print ("\n\nfib2 y�ntemiyle: ")
    for i in range (adet): print (f (i), end=" ")
print ("\n", "-"*75, "\n", sep="")
#--------------------------------------------------------------------------------------------------------

import p_12801x # A��klama tekrar g�r�lmeyecektir...
import p_12801x # A��klama tekrar g�r�lmeyecektir...
import p_12801x # A��klama tekrar g�r�lmeyecektir...

from importlib import reload
reload (p_12801x) # A��klama tekrar g�r�lecektir...
reload (p_12801x) # A��klama tekrar g�r�lecektir...
reload (p_12801x) # A��klama tekrar g�r�lecektir...



"""��kt�:
>python p_12801.py
PI say�s�: 3.141592653589793
Sin(0/90/180): 0.0 1.0 1.2246467991473532e-16
Cos(0/90/180): 1.0 6.123233995736766e-17 -1.0
0.7071067811865476
3.141592653589793
2.718281828459045
---------------------------------------------------------------------------

==>p_12801x fibonaki mod�l� �uanda import/ithal edilmi�tir.

Fibonaki seri adedini girin [0:��k]: 12
fib1 y�temiyle:
0 1 1 2 3 5 8 13 21 34 55 89

fib2 y�ntemiyle:
0 1 1 2 3 5 8 13 21 34 55 89
Fibonaki seri adedini girin [0:��k]: 0

---------------------------------------------------------------------------

==>p_12801x fibonaki mod�l� �uanda import/ithal edilmi�tir.
==>p_12801x fibonaki mod�l� �uanda import/ithal edilmi�tir.
==>p_12801x fibonaki mod�l� �uanda import/ithal edilmi�tir.
"""