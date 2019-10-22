# coding:iso-8859-9 Türkçe
# p_12204.py: *parametre, *argüman, parametreler ve argümanlar çeşitlemesi örneği.

def göster (*x): print (x)

print (göster)
print (göster())
print ( göster ("M.Nihat Yavaş", 2019-1957, "Yeşilyurt - Malatya", "TR") )
#-------------------------------------------------------------------------------------------------------

def şehirler (zaruri, *tercihi): print (zaruri, tercihi)

print()
print (şehirler)

try: print (şehirler() )
except Exception as ist: print (ist)

print (şehirler ("Ankara") )
print (şehirler ("Ankara", "İstanbul", "İzmir", "Mersin", "Adana", "Bursa") )
#-------------------------------------------------------------------------------------------------------

def ortalama1 (x, y): # İlk parametre float, ikincisi liste...
    toplam = x
    for i in y: toplam += i
    return toplam / (1.0 + len (y))

from random import randint

uz = randint (0, 100)
zaruri = randint (35, 100)
liste = [randint (35, 100) for i in range (uz)]

print ("\n[0->100] arası toplam gelişigüzel {} notun ortalaması = {:.2f}'dir." .format (len(liste)+1, ortalama1 (zaruri, liste)) )
#-------------------------------------------------------------------------------------------------------

def ortalama2 (x, *y): # Tüm parametreler float...
    toplam = x
    for i in y: toplam += i
    return toplam / (1.0 + len (y))

print ("\n3 adet notun ortalaması:", ortalama2 (74.5, 67.35, 90.56) )
print ("6 adet gelişigüzel +/- sayının tamsayı ortalaması:", int (ortalama2 (4, 7, 9, 45, -3.7, 99)) )

uz = randint (1, 100)
liste = [randint (45, 100) for i in range (uz)]
# ortalama2 (*liste) çağrısı, zaruri float ve listeyi tümüyle değişken elemansal float argümanlara dönüştürmektedir...
print ("[0->100] arası toplam gelişigüzel {} notun ortalaması = {:.2f}'dir." .format (len(liste)+1, ortalama2 (*liste)) )
#-------------------------------------------------------------------------------------------------------

def fonk (x, y, z): print ("\nx=", x, ", y=", y, ", z=", z, sep="")

liste = [87,71, 62.5]
print ("Liste elemanları değişken argümana dönüştürülür:", fonk (*liste) )
print ("Liste elemanları tek-tek sabit argüman yapılır:",  fonk (liste[0], liste[1], liste[2]) )


"""Çıktı:
>python p_12204.py
<function göster at 0x00BAC5D0>
()
None
('M.Nihat Yavaş', 62, 'Yeşilyurt - Malatya', 'TR')
None

<function şehirler at 0x00BAC4F8>
şehirler() missing 1 required positional argument: 'zaruri'
Ankara ()
None
Ankara ('İstanbul', 'İzmir', 'Mersin', 'Adana', 'Bursa')
None

[0->100] arası toplam gelişigüzel 4 notun ortalaması = 70.75'dir.

3 adet notun ortalaması: 77.47
6 adet gelişigüzel +/- sayının tamsayı ortalaması: 26
[0->100] arası toplam gelişigüzel 92 notun ortalaması = 73.29'dir.

x=87, y=71, z=62.5
Liste elemanları değişken argümana dönüştürülür: None

x=87, y=71, z=62.5
Liste elemanları tek-tek sabit argüman yapılır: None
"""