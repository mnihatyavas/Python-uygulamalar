# coding:iso-8859-9 T�rk�e

print ("Fatura: {} TL, Bah�i�: {} TL, ve Toplam�: {} TL'd�r." .format (23.60, 23.60 * 0.25, 23.60 + 23.6*.25) )
print ("Fatura: {:.2f} TL, Bah�i�: {:.2f} TL, ve Toplam�: {:.2f} TL'd�r." .format (23.60, 23.60 * 0.25, 23.60 + 23.6*.25) )

L = [0, 19, 765, 7690, 17851, 432578, 4765345]
print ("\nVarsay�l� sa�a yana��k tamsay�lar:")
for k in L: print ("{:7d}" .format (k) ) # Veya {:>7d}

print ("\nOrtalanm�� tamsay�lar:")
for k in L: print ("{:^7d}" .format (k) )

print ("\nSola yana��k tamsay�lar:")
for k in L: print ("{:<7d}" .format (k) )

print ("\nSa�a yana��k binleri ayr�k tamsay�lar:")
for k in L: print ("{:>9,d}" .format (k) )


from random import random
for i in range (len (L)): L[i] = L[i] + random()
L = L + [3.141592653589793]
print ("Ondal�kl� say�lar listesi:", L)

print ("\nVarsay�l� sola yana��k, varsay�l� 6 ondal�k haneli kayan noktal� say�lar:")
for k in L: print ("{:f}" . format (k) )

print ("\nSa�a yana��k 2 ondal�k haneli say�lar:")
for k in L: print ("{:10.2f}" . format (k) )

print ("\nSa�a yana��k binleri ayr�k ve 2 ondal�k haneli say�lar:")
for k in L: print ("{:12,.2f}" . format (k) )

L = ["Hey", "Oradaki", "Sana", "Sesleniyorum", "Merhabalar"]
print ("\nVarsay�l� sola yana��k dizgeler:")
for k in L: print ("{:s}" .format (k) )

print ("\nSa�a yana��k dizgeler:")
for k in L: print ("{:>12s}" .format (k) )

print ("\nOrtalanm�� dizgeler:")
for k in L: print ("{:^12s}" .format (k) )