# coding:iso-8859-9 T�rk�e

def cf (c):
    #assert (c >= -273), "Mutlak s�f�rdan daha so�uk!"
    if c < -273: return
    return c*9/5+32

def kf (k):
    #assert (k >= 0), "Mutlak s�f�rdan daha so�uk!"
    if k < 0: return
    return ((k-273)*1.8)+32

def fc (f):
    #assert (f >= -459.41), "Mutlak s�f�rdan daha so�uk!"
    if f < -459.41: return
    return ((5 / 9) * (f - 32));

print ("Celcius->Fahrenheit: 0, -274:", cf (0), cf (-275))
print ("Kelvin->Fahrenheit: 0, -1:", kf (0), kf (-1))
print ("Fahrenheit->Celcius: 0, -460:", fc (0), fc (-460))

print()
from math import pi, sin
def sin_derece (x): return sin (pi*x/180)

print ("Sin�s 0, 30, 45, 60, 75, 90, 180, 270==>\n", sin_derece (0), sin_derece (30), sin_derece (45), sin_derece (60), sin_derece (75), sin_derece (90), sin_derece (180), sin_derece (270))

print()
def ��z (a,b,e, c,d,f):
    x = (d*e-b*f)/(a*d-b*c)
    y = (a*f-c*e)/(a*d-b*c)
    return [x,y]

x, y = ��z (2,3,2, 1,2,5)
print ('2x+3y=2 ve x+2y=5 ��z�m�: x =', x, 've y =', y)
