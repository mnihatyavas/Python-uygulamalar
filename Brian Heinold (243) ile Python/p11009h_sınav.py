# coding:iso-8859-9 T�rk�e

pay=payda=i=kontrol=0
while not (abs (pay) < abs (payda)) or pay == 0 or payda == 0:
    dizge = input ("[Pay<Payda] Pay/Payda girin: ")
    try:
        pay = int (dizge[:dizge.index ("/")])
        payda = int (dizge[dizge.index ("/")+1:])
    except Exception: pay=payda=0
for i in range (abs(pay), 1, -1):
    if (pay % i == 0) and (payda % i == 0):
        kontrol=1
        break
if kontrol== 1: print ("Ortak b�len:", i, "\nSadele�tirilen sonu�:", pay//i, "/", payda//i)
else: print ("Sadele�tirme yok:", pay, "/", payda)