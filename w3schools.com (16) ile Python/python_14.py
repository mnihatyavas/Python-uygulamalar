# coding:iso-8859-9 T�rk�e

# 4 i�lem fonksiyonlar�n� tan�mlayal�m...
def topla (x, y): return x + y 
def ��kar (x, y): return x - y 
def �arp (x, y): return x * y 
def b�l (x, y): return x / y  
def kalan (x, y): return x % y  
def y�zde (x, y):
    if x >= y: return (x-y) / y * 100
    else: return -(y-x) / x * 100

print ("4 ��lem Men� Se�enekleri\n======================")  
print ("1. Toplama")  
print ("2. ��karma")  
print ("3. �arpma")  
print ("4. B�lme")  
print ("5. Y�zde")
print ("6. Kalan")

tercih = input ("Tercihiniz (1/2/3/4/5/6): ")  

say�1 = float (input ("�lk say�n�z� girin: "))  
say�2 = float (input ("�kinci say�n�z� girin: "))  

if tercih == '1': print (say�1, "+", say�2, "=", topla (say�1, say�2))
elif tercih == '2': print (say�1, "-", say�2, "=", ��kar (say�1, say�2))  
elif tercih == '3': print (say�1, "*", say�2, "=", �arp (say�1, say�2))  
elif tercih == '4': print (say�1, "/", say�2, "=", b�l (say�1, say�2))  
elif tercih == '5': print (say�1, "%", say�2, "= %", y�zde (say�1, say�2))  
elif tercih == '6': print (say�1, "%%", say�2, "=", kalan (say�1, say�2))  
else: print ("Ge�ersiz tercih yapt�n�z!") 
