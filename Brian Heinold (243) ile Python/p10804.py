# coding:iso-8859-9 T�rk�e

dizge = 'Selam'
L1 = [1,14,5,9,12]
L2 = ['bir', 'iki', '��', 'd�rt', 'be�', 'alt�']
print ("dizge, L1 ve L2:\n", dizge, "\n", L1, "\n", L2)
print ("Yeni liste:", [0 for i in range (10)])
print ("Yeni liste:", [i for i in range (10)])
print ("Yeni liste:", [i**2 for i in range (1, 8)])
print ("Dizgesel liste:", [k*2 for k in dizge])
print ("Elemanlar�n ilk karakteri:", [e[0] for e in L2])
print ("3 uzunluklu L2'lerin ilk karakteri:", [e[2] for e in L2 if len (e) == 3])
print ("L1 * 10:", [i*10 for i in L1])
print ("L1 < 10:", [i for i in L1 if i < 10])
print ("��i�e 2 for d�ng�l� liste:", [[i,j] for i in range (2) for j in range (3)])
