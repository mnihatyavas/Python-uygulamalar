# coding:iso-8859-9 T�rk�e

L = [sat�r.strip().split ("\t") for sat�r in open ("��renci2.txt")]
from pprint import pprint
print (len (L), " ki�ilik ��RENC� listesinin dosyadan d�k�m�:\n", "="*48, sep="")
pprint (L)

sorgu = input ("\nG�rmek istedi�in ��rencinin herhangi ARDI�IK isim i�eri�ini gir: ").lower()
print ("\n�sim i�eri�inde ARDI�IK [", sorgu, "] bulunan kay�tlar�n listesi:\n", "-"*60, sep="")
for k in L:
    if sorgu in str (k[0]).lower(): print (k)

sorgu = input ("\nG�rmek istedi�in ��rencinin herhangi ard���k-SIZ isim i�eri�ini gir: ").lower()
print ("\n�sim i�eri�inde ard���k-SIZ [", sorgu, "] bulunan kay�tlar�n listesi:\n", "-"*63, sep="")
for k in L:
    isim = str (k[0]).lower()
    kontrol = 0
    j = -1
    for i in range (len (sorgu)):
        while j < len (isim)-1:
            j +=1
            if sorgu[i] == isim[j]:
                kontrol +=1
                break
    if kontrol == len (sorgu): print (k)
