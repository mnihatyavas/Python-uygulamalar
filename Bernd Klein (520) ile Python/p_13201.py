# coding:iso-8859-9 T�rk�e
# p_13201.py: Normal def ve anonim lambda fonksiyonlarla ayn� i�lem sonu�lar� �rne�i.

from random import randint

def topla (x,y): return x+y
def ��kar (x,y): return x-y
def �arp (x,y): return x*y
def b�l (x,y): return x/y
def kalan (x,y): return x%y
def y�zde (x,y):
    if (x>y): return (x-y)/y*100
    else: return -(y-x)/x*100

try:a = float (input ("a say�s�n� girin: "))
except: a = randint (-100, 100)
try: b = float (input ("b say�s�n� girin: "))
except: b = randint (-100, 100)

print ("\nNormal 'def fonksiyon(a,b):return a#b' ile 6 i�lem:", "\n", "-"*51, sep="")
print ("a={} ve b={} say�s�n�n toplam�={}" .format (a, b, topla (a, b)) )
print ("a={} ve b={} say�s�n�n ��kar�m�={}" .format (a, b, ��kar (a, b)) )
print ("a={} ve b={} say�s�n�n �arp�m�={}" .format (a, b, �arp (a, b)) )
print ("a={} ve b={} say�s�n�n b�l�m�={}" .format (a, b, b�l (a, b)) )
print ("a={} ve b={} say�s�n�n kalan�={}" .format (a, b, kalan (a, b)) )
print ("a={} ve b={} say�s�n�n y�zdesi=%{}" .format (a, b, y�zde (a, b)) )
#---------------------------------------------------------------------------------------------------------

topla2 = lambda x,y: x+y
��kar2 = lambda x,y: x-y
�arp2 = lambda x,y: x*y
b�l2 = lambda x,y: x/y
kalan2 = lambda x,y: x%y
if (a>b): y�zde2 = lambda x,y: (x-y)/y*100
else: y�zde2 = lambda x,y: -(y-x)/x*100

print ("\nLambdal� anonim fonksiyon 'i�lem = lambda a,b:a#b' ile 6 i�lem:", "\n", "-"*63, sep="")
print ("a={} ve b={} say�s�n�n toplam�={}" .format (a, b, topla2 (a, b)) )
print ("a={} ve b={} say�s�n�n ��kar�m�={}" .format (a, b, ��kar2 (a, b)) )
print ("a={} ve b={} say�s�n�n �arp�m�={}" .format (a, b, �arp2 (a, b)) )
print ("a={} ve b={} say�s�n�n b�l�m�={}" .format (a, b, b�l2 (a, b)) )
print ("a={} ve b={} say�s�n�n kalan�={}" .format (a, b, kalan2 (a, b)) )
print ("a={} ve b={} say�s�n�n y�zdesi=%{}" .format (a, b, y�zde2 (a, b)) )

"""��kt�:
>python p_13201.py
a say�s�n� girin:
b say�s�n� girin:

Normal 'def fonksiyon(a,b):return a#b' ile 6 i�lem:
---------------------------------------------------
a=18 ve b=62 say�s�n�n toplam�=80
a=18 ve b=62 say�s�n�n ��kar�m�=-44
a=18 ve b=62 say�s�n�n �arp�m�=1116
a=18 ve b=62 say�s�n�n b�l�m�=0.2903225806451613
a=18 ve b=62 say�s�n�n kalan�=18
a=18 ve b=62 say�s�n�n y�zdesi=%-244.44444444444446

Lambdal� anonim fonksiyon 'i�lem = lambda a,b:a#b' ile 6 i�lem:
---------------------------------------------------------------
a=18 ve b=62 say�s�n�n toplam�=80
a=18 ve b=62 say�s�n�n ��kar�m�=-44
a=18 ve b=62 say�s�n�n �arp�m�=1116
a=18 ve b=62 say�s�n�n b�l�m�=0.2903225806451613
a=18 ve b=62 say�s�n�n kalan�=18
a=18 ve b=62 say�s�n�n y�zdesi=%-244.44444444444446
"""