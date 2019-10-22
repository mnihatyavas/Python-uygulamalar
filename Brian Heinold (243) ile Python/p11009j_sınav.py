# coding:iso-8859-9 T�rk�e

fiyat = 12
print ("1000 TL'ye kadar 7 ve 11 kuru�'luk madeni paralarla �denebilen fiyatlar:")
print ("-"*72)
while True:
    if fiyat % 7 == 0 and fiyat % 11 == 0: print ("{:d} TL ve {:d} kuru�" .format (fiyat//100, fiyat - (fiyat//100)*100 ))
    fiyat +=1
    if fiyat > 1000: break

# 43 + 57 = 207 ==> 52 + 56 = 108 veya 42 + 66 = 108 olabilir (her rakam -1/+1)...
# x^2 - 2y^2 = 1, 1 <= (x,y) <= 100
print ("\n[x^2 - 2y^2 = 1] \"1 <= (x,y) <= 100\" �art�n� sa�layan (x,y) de�erleri:")
print ("-"*70)
for i in range (1, 101):
    for j in range (1, 101):
        if i**2 - 2*j**2 == 1: print ("(x,y): ({:2d},{:2d}) ve {:4d} - {:4d} = 1" .format (i, j, i**2, 2*j**2))

print()
print ("\n4 adet zar�n 10,000 kere at���n�n herbir 4 zar�n 6 farkl� �iftler toplam� olan (2->12) da��l�m�n�n genel toplamdaki %'lerinin tablosu:")
print ("-"*79)
print (" 2: 1+1")
print (" 3: 1+2, 2+1")
print (" 4: 1+3, 2+2, 3+1")
print (" 5: 1+4, 2+3, 3+2, 4+1")
print (" 6: 1+5, 2+4, 3+3, 4+2, 5+1")
print (" 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1")
print (" 8: 2+6, 3+5, 4+4, 5+3, 6+2")
print (" 9: 3+6, 4+5, 5+4, 6+3")
print ("10: 4+6, 5+5, 6+4")
print ("11: 5+6, 6+5")
print ("12: 6+6")
print ("="*65)
from random import randint
L1 = [[randint (1,6) for j in range (4)] for i in range (10000)]
from pprint import pprint

L2 = [[L1[i][0]+L1[i][1], L1[i][0]+L1[i][2], L1[i][0]+L1[i][3], L1[i][1]+L1[i][2], L1[i][1]+L1[i][3], L1[i][2]+L1[i][3]] for i in range (10000)]
L3 = [0 for i in range (11)]

for i in range (10000):
    for j in range (6):
        for k in range (2, 13):
            if L2[i][j] == k: L3[k-2] +=1

toplam = sum (L3)
y�zde = 0
for i in range (11):
    y = L3[i]*100/toplam
    print ("�ifti {:2d} olanlar�n toplam�: {:5d} ve genel toplamdaki %'si: {:5.2f}" .format (i+2, L3[i], y) )
    y�zde +=y
print ("-"*65)
print ("Genel toplamlar:{}{:5d}{}% {:.2f}" .format (" "*12, toplam, " "*24, y�zde))
