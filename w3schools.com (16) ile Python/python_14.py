# coding:iso-8859-9 Türkçe

# 4 işlem fonksiyonlarını tanımlayalım...
def topla (x, y): return x + y 
def çıkar (x, y): return x - y 
def çarp (x, y): return x * y 
def böl (x, y): return x / y  
def kalan (x, y): return x % y  
def yüzde (x, y):
    if x >= y: return (x-y) / y * 100
    else: return -(y-x) / x * 100

print ("4 İşlem Menü Seçenekleri\n======================")  
print ("1. Toplama")  
print ("2. Çıkarma")  
print ("3. Çarpma")  
print ("4. Bölme")  
print ("5. Yüzde")
print ("6. Kalan")

tercih = input ("Tercihiniz (1/2/3/4/5/6): ")  

sayı1 = float (input ("İlk sayınızı girin: "))  
sayı2 = float (input ("İkinci sayınızı girin: "))  

if tercih == '1': print (sayı1, "+", sayı2, "=", topla (sayı1, sayı2))
elif tercih == '2': print (sayı1, "-", sayı2, "=", çıkar (sayı1, sayı2))  
elif tercih == '3': print (sayı1, "*", sayı2, "=", çarp (sayı1, sayı2))  
elif tercih == '4': print (sayı1, "/", sayı2, "=", böl (sayı1, sayı2))  
elif tercih == '5': print (sayı1, "%", sayı2, "= %", yüzde (sayı1, sayı2))  
elif tercih == '6': print (sayı1, "%%", sayı2, "=", kalan (sayı1, sayı2))  
else: print ("Geçersiz tercih yaptınız!") 
