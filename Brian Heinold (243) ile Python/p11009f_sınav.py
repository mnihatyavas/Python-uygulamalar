# coding:iso-8859-9 T�rk�e

from random import randint
L = []
for i in range (1000):
    g�n = randint (1, 365)
    if g�n <= 31: L = L + [0 + g�n / 100] # Ocak-31
    elif g�n <= 59: L = L + [1 + (g�n-31) / 100] # �ubat-28
    elif g�n <= 90: L = L + [2 + (g�n-59) / 100] # Mart-31
    elif g�n <= 120: L = L + [3 + (g�n-90) / 100] # Nisan-30
    elif g�n <= 151: L = L + [4 + (g�n-120) / 100] # May�s-31
    elif g�n <= 181: L = L + [5 + (g�n-151) / 100] # Haziran-30
    elif g�n <= 212: L = L + [6 + (g�n-181) / 100] # Temmuz-31
    elif g�n <= 243: L = L + [7 + (g�n-212) / 100] # A�ustos-31
    elif g�n <= 273: L = L + [8 + (g�n-243) / 100] # Eyl�l-30
    elif g�n <= 304: L = L + [9 + (g�n-273) / 100] # Ekim-31
    elif g�n <= 334: L = L + [10 + (g�n-304) / 100] # Kas�m-30
    else: L = L + [11 + (g�n-334) / 100] # Aral�k-31
L.sort()
print ("Ayl�k do�umg�n� frekans tablosu==>")
ay = int (L[0])
g�n = (L[0] - int (L[0])) * 100
aySaya� = g�nSaya� = 0
for i in range (len (L)):
    if ay != int (L[i]):
        print ("=" * 18)
        print ("   Ay toplam�:", aySaya�)
        aySaya� = 0
        ay = int (L[i])
    if g�n != (L[i] - int (L[i])) * 100:
        print ("-" * 18)
        print ("   G�n toplam�:", g�nSaya�)
        g�n = (L[i] - int (L[i])) * 100
        g�nSaya� = 0
    print ("Ay: {:2.0f}, G�n: {:2.0f}" .format (int (L[i])+1, (L[i] - int (L[i])) * 100))
    g�nSaya� += 1
    aySaya� += 1
print ("-" * 18)
print ("   G�n toplam�:", g�nSaya�)
print ("=" * 18)
print ("   Ay toplam�:", aySaya�)

ay=g�n=-1
while not (0 < ay < 13): ay = abs (eval (input ("\nAy girin [1->12]: ")))
while not (0 < g�n < 32): g�n = abs (eval (input ("G�n girin [1->32]: ")))
saya� = len ([L[i] for i in range (len (L)) if L[i] == ((ay-1)+(g�n/100))])
print (ay, ".ay ve ", g�n, ".g�ne ait do�umg�n� toplam�: ", saya�, sep="")