# coding:iso-8859-9 T�rk�e

def fonk1():
    for i in range (10): print (i, end=" ")
    print()

def fonk2():
    i=100
    fonk1()
    print (i)

fonk1()
print()
fonk2()

print()
def s�f�rla():
    global kalan_zaman
    kalan_zaman = 0

def zaman�Yaz():
    print (kalan_zaman, "saniye")

kalan_zaman = 30
zaman�Yaz()
s�f�rla()
zaman�Yaz()

print()
def f1 (x):
    x = x + 1
    print (x)

def f2 (L):
    L = L + [4]
    print (L)

a = 3
M = [1,2,3]
f1 (a)
print (a) # a de�i�medi...
f2 (M)
print (M) # M de de�i�medi!..
