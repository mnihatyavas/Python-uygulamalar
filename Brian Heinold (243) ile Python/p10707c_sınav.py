# coding:iso-8859-9 T�rk�e

from random import randint

try: a = eval (input ("Liste ka� elemanl� olacak: "))
except Exception: a = 10

if a < 2: a = 2
elif a > 100: a = 100

liste1=[]
liste2=[]
liste3=[]
liste4=[1,1]

for i in range (a):
    liste1.append (randint (0, 1000))
    liste2 = liste2 + [randint (-500, 500)]

print (a, "elemanl� Liste-1:", liste1)
print (a, "elemanl� Liste-2:", liste2)

for i in range (a): liste3= liste3 + [liste1[i] + liste2[i]]; liste4.append (liste4[i] + liste4[i+1])
print (a, "elemanl� toplam Liste-3:", liste3)
print (len (liste4), "fibonacci serisi elemanl� Liste-4:", liste4)
print ("\n10000 adet �if zar at���nda, herbir at�� toplamlar� da��l�m�:")
liste5=[]
for i in range(10000): liste5.append (randint (1,6) + randint (1,6))
#liste5.sort()
saya�=azami_kere=azami_toplam=0
for i in range (2,13):
    b = liste5.count (i)
    if b > azami_kere: azami_kere = b; azami_toplam = i
    saya� += b
    print (i, "toplam� ka� kez geldi?", b, "%", 100*b/10000)
print ("Toplamlar:", saya�, "%", 100*saya�/10000)
print ("�ift zar toplam�", azami_toplam, ",", azami_kere, "kere gelmi� ve %'si", azami_kere*100/10000)
print()
liste5.sort()
j=0
liste6=[liste5[0]]
for i in range (10000):
    if liste6[j] != liste5[i]: liste6 = liste6 + [liste5[i]]; j +=1
del liste5
print ("10000 elemanl�k Liste-5'in kalan farkl� de�erli", len (liste6), "adet elemanlar�:", liste6)
