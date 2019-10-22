# coding:iso-8859-9 Türkçe
# p_13201.py: Normal def ve anonim lambda fonksiyonlarla aynı işlem sonuçları örneği.

from random import randint

def topla (x,y): return x+y
def çıkar (x,y): return x-y
def çarp (x,y): return x*y
def böl (x,y): return x/y
def kalan (x,y): return x%y
def yüzde (x,y):
    if (x>y): return (x-y)/y*100
    else: return -(y-x)/x*100

try:a = float (input ("a sayısını girin: "))
except: a = randint (-100, 100)
try: b = float (input ("b sayısını girin: "))
except: b = randint (-100, 100)

print ("\nNormal 'def fonksiyon(a,b):return a#b' ile 6 işlem:", "\n", "-"*51, sep="")
print ("a={} ve b={} sayısının toplamı={}" .format (a, b, topla (a, b)) )
print ("a={} ve b={} sayısının çıkarımı={}" .format (a, b, çıkar (a, b)) )
print ("a={} ve b={} sayısının çarpımı={}" .format (a, b, çarp (a, b)) )
print ("a={} ve b={} sayısının bölümü={}" .format (a, b, böl (a, b)) )
print ("a={} ve b={} sayısının kalanı={}" .format (a, b, kalan (a, b)) )
print ("a={} ve b={} sayısının yüzdesi=%{}" .format (a, b, yüzde (a, b)) )
#---------------------------------------------------------------------------------------------------------

topla2 = lambda x,y: x+y
çıkar2 = lambda x,y: x-y
çarp2 = lambda x,y: x*y
böl2 = lambda x,y: x/y
kalan2 = lambda x,y: x%y
if (a>b): yüzde2 = lambda x,y: (x-y)/y*100
else: yüzde2 = lambda x,y: -(y-x)/x*100

print ("\nLambdalı anonim fonksiyon 'işlem = lambda a,b:a#b' ile 6 işlem:", "\n", "-"*63, sep="")
print ("a={} ve b={} sayısının toplamı={}" .format (a, b, topla2 (a, b)) )
print ("a={} ve b={} sayısının çıkarımı={}" .format (a, b, çıkar2 (a, b)) )
print ("a={} ve b={} sayısının çarpımı={}" .format (a, b, çarp2 (a, b)) )
print ("a={} ve b={} sayısının bölümü={}" .format (a, b, böl2 (a, b)) )
print ("a={} ve b={} sayısının kalanı={}" .format (a, b, kalan2 (a, b)) )
print ("a={} ve b={} sayısının yüzdesi=%{}" .format (a, b, yüzde2 (a, b)) )

"""Çıktı:
>python p_13201.py
a sayısını girin:
b sayısını girin:

Normal 'def fonksiyon(a,b):return a#b' ile 6 işlem:
---------------------------------------------------
a=18 ve b=62 sayısının toplamı=80
a=18 ve b=62 sayısının çıkarımı=-44
a=18 ve b=62 sayısının çarpımı=1116
a=18 ve b=62 sayısının bölümü=0.2903225806451613
a=18 ve b=62 sayısının kalanı=18
a=18 ve b=62 sayısının yüzdesi=%-244.44444444444446

Lambdalı anonim fonksiyon 'işlem = lambda a,b:a#b' ile 6 işlem:
---------------------------------------------------------------
a=18 ve b=62 sayısının toplamı=80
a=18 ve b=62 sayısının çıkarımı=-44
a=18 ve b=62 sayısının çarpımı=1116
a=18 ve b=62 sayısının bölümü=0.2903225806451613
a=18 ve b=62 sayısının kalanı=18
a=18 ve b=62 sayısının yüzdesi=%-244.44444444444446
"""