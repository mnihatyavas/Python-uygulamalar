# coding:iso-8859-9 Türkçe

def faktöriyel (n):
    if n == 1: return n  
    else: return n * faktöriyel (n - 1)  

sayı = int (input ("Herhangibir tamsayı girin: "))  
if sayı < 0: print ("Hata, eksi sayıların faktöriyeli olmaz!")  
elif sayı == 0: print ("0 sayısının faktöriyeli 1'dir.")
else: print (sayı, "sayısının faktöriyeli:", faktöriyel (sayı))
