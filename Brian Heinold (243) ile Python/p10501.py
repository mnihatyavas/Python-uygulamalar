# coding:iso-8859-9 T�rk�e

from random import randint

saya�1=saya�2=0
for i in range (100):
    say�1 = randint (1,6)
    say�2 = randint (1,6)
    if say�1==say�2==6: saya�1 +=1
    if say�1==say�2: saya�2 +=1
print ("100 kez att���n�z �ift zar�n", saya�2, "adeti �ift ve bu �iftlerin de", saya�1, "adeti d��e� geldi!")
print()
saya�=ara=0
k���k=eval (input ("D�ng� ba�lang�� de�erini girin: "))
b�y�k=eval (input ("D�ng� son de�erini girin: "))
if k���k > b�y�k: k���k, b�y�k = b�y�k, k���k
for i in range (k���k, b�y�k+1):
    if 2**i % 10 == 4: saya� +=1
print ("2^", k���k, "-->2^", b�y�k, " aras�nda sonu 4'le biten say� adeti: ", saya�, sep="")
