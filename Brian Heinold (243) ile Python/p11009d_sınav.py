# coding:iso-8859-9 T�rk�e

print ("T�m say�lar i�inde, basamaklar�n�n �arp�m ve toplamlar�na e�it 9 �zel say�:\n==>", end="")
for i in range (11, 10000):
    d = str (i)
    e = len (d)
    �arp = 1
    topla = sonu� = 0
    for j in range (e):
        �arp *= int (d[j])
        topla += int (d[j])
    sonu� = �arp + topla
    if i == sonu�: print (i, end=" ")

print ("\n\n�lk-son rakamlar� yerde�i�tirince oran� 3.5 olan ilk say�:")
for i in range (12, 1000000):
    d = str (i)
    e = len (d)
    d = d[1:] + d[:1]
    if 3.5 < float (d) / i < 3.50009: print (i, d, float (d) / i ); break

�arp�m = 1
for i in range (1, 1001):
    �arp�m *= i
d = str (�arp�m)
e = len (d)
for i in range (0, e):
    if d[e-i-1] != "0": break
print ("\n1000! fakt�riyel==>\n", d)
print ("Rakam�n uzunlu�u:", e)
print ("Sondaki 0-s�f�r say�s�:", i)
