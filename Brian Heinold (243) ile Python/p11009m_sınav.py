# coding:iso-8859-9 T�rk�e

from random import randint

try: n = abs (int (eval (input ("Ka� kere zar atacaks�n: "))))
except Exception: n = randint (100, 1000)

saya� = 0
for i in range (n):
    zar1 = randint (1, 6); zar2 = randint (1, 6)
    if zar1 == zar2 == 6: saya� +=1
print ("{:,d} kere at�lan zar ��FT�NDE {:,d} kez D��E� gelmi�tir ve Y�ZDES�: % {:.2f}'dir." .format (n, saya�, saya� * 100 / n))

print()
saya�1 = saya�2 = 0
for i in range (n):
    zar1 = randint (1, 6); zar2 = randint (1, 6); zar3 = randint (1, 6); zar4 = randint (1, 6); zar5 = randint (1, 6)
    if zar1 == zar2 == zar3 == zar4 == zar5: saya�1 +=1
    L = [zar1] + [zar2] + [zar3] + [zar4] + [zar5]
    L.sort()
    if (L[0] == 1 and L[1] == 2 and L[2] == 3 and L[3] == 4 and L[4] == 5) or (L[0] == 2 and L[1] == 3 and L[2] == 4 and L[3] == 5 and L[4] == 6): saya�2 +=1
print ("{:,d} kere at�lan zar BE�L�S�NDE {:,d} kez HEPE� gelmi�tir ve Y�ZDES�: % {:.2f}'dir." .format (n, saya�1, saya�1 * 100 / n))
print ("{:,d} kere at�lan zar BE�L�S�NDE {:,d} kez SIRA gelmi�tir ve Y�ZDES�: % {:.2f}'dir." .format (n, saya�2, saya�2 * 100 / n))

print()
yaz� = tura = 0
L = Ly = Lt = []
for i in range (n):
    at�� = randint (0,1)
    if at�� == 0: yaz� +=1
    else: tura +=1
    L = L + [at��]
print ("{:,d} YAZI/TURA'da {:,d} kez (% {:.2f}) YAZI ve {:,d} kez de (% {:.2f}) TURA gelmi�tir." .format (n, yaz�, yaz�*100/n, tura, tura*100/n))
y = t = 1
for i in range (n-1):
    if L[i] == L[i+1] == 0: y +=1
    if L[i] == L[i+1] == 1: t +=1
    if L[i] == 0 and L[i+1] == 1:
        Ly = Ly + [y]
        t = 1
    if L[i] == 1 and L[i+1] == 0:
        Lt = Lt + [t]
        y = 1

print()
print (n, " at��ta ard���k YAZI gelme sonu�lar�:\n", "-"*41, sep="")
Ly.sort()
tekrar = 1
toplam = 0
for i in range (len (Ly)-1):
    if Ly[i] == Ly[i+1]: tekrar +=1
    else:
        print ("{:2d} ard���k: {:d} kere (% {:.2f})" .format (Ly[i], tekrar, Ly[i]*tekrar*100/n) )
        toplam +=tekrar * Ly[i]
        tekrar = 1
print ("{:2d} ard���k: {:d} kere (% {:.2f})" .format (Ly[i+1], tekrar, Ly[i+1]*tekrar*100/n) )
toplam +=tekrar * Ly[i+1]
print ("-->Toplam:", toplam, "kere")

print()
print (n, " at��ta ard���k TURA gelme sonu�lar�:\n", "-"*41, sep="")
Lt.sort()
tekrar = 1
toplam = 0
for i in range (len (Lt)-1):
    if Lt[i] == Lt[i+1]: tekrar +=1
    else:
        print ("{:2d} ard���k: {:d} kere (% {:.2f})" .format (Lt[i], tekrar, Lt[i]*tekrar*100/n) )
        toplam +=tekrar * Lt[i]
        tekrar = 1
print ("{:2d} ard���k: {:d} kere (% {:.2f})" .format (Lt[i+1], tekrar, Lt[i+1]*tekrar*100/n) )
toplam +=tekrar * Lt[i+1]
print ("-->Toplam:", toplam, "kere")
print()