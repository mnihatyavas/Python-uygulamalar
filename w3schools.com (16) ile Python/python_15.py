# coding:iso-8859-9 T�rk�e

def fakt�riyel (n):
    if n == 1: return n  
    else: return n * fakt�riyel (n - 1)  

say� = int (input ("Herhangibir tamsay� girin: "))  
if say� < 0: print ("Hata, eksi say�lar�n fakt�riyeli olmaz!")  
elif say� == 0: print ("0 say�s�n�n fakt�riyeli 1'dir.")
else: print (say�, "say�s�n�n fakt�riyeli:", fakt�riyel (say�))
