# coding:iso-8859-9 T�rk�e
# p_12204.py: *parametre, *arg�man, parametreler ve arg�manlar �e�itlemesi �rne�i.

def g�ster (*x): print (x)

print (g�ster)
print (g�ster())
print ( g�ster ("M.Nihat Yava�", 2019-1957, "Ye�ilyurt - Malatya", "TR") )
#-------------------------------------------------------------------------------------------------------

def �ehirler (zaruri, *tercihi): print (zaruri, tercihi)

print()
print (�ehirler)

try: print (�ehirler() )
except Exception as ist: print (ist)

print (�ehirler ("Ankara") )
print (�ehirler ("Ankara", "�stanbul", "�zmir", "Mersin", "Adana", "Bursa") )
#-------------------------------------------------------------------------------------------------------

def ortalama1 (x, y): # �lk parametre float, ikincisi liste...
    toplam = x
    for i in y: toplam += i
    return toplam / (1.0 + len (y))

from random import randint

uz = randint (0, 100)
zaruri = randint (35, 100)
liste = [randint (35, 100) for i in range (uz)]

print ("\n[0->100] aras� toplam geli�ig�zel {} notun ortalamas� = {:.2f}'dir." .format (len(liste)+1, ortalama1 (zaruri, liste)) )
#-------------------------------------------------------------------------------------------------------

def ortalama2 (x, *y): # T�m parametreler float...
    toplam = x
    for i in y: toplam += i
    return toplam / (1.0 + len (y))

print ("\n3 adet notun ortalamas�:", ortalama2 (74.5, 67.35, 90.56) )
print ("6 adet geli�ig�zel +/- say�n�n tamsay� ortalamas�:", int (ortalama2 (4, 7, 9, 45, -3.7, 99)) )

uz = randint (1, 100)
liste = [randint (45, 100) for i in range (uz)]
# ortalama2 (*liste) �a�r�s�, zaruri float ve listeyi t�m�yle de�i�ken elemansal float arg�manlara d�n��t�rmektedir...
print ("[0->100] aras� toplam geli�ig�zel {} notun ortalamas� = {:.2f}'dir." .format (len(liste)+1, ortalama2 (*liste)) )
#-------------------------------------------------------------------------------------------------------

def fonk (x, y, z): print ("\nx=", x, ", y=", y, ", z=", z, sep="")

liste = [87,71, 62.5]
print ("Liste elemanlar� de�i�ken arg�mana d�n��t�r�l�r:", fonk (*liste) )
print ("Liste elemanlar� tek-tek sabit arg�man yap�l�r:",  fonk (liste[0], liste[1], liste[2]) )


"""��kt�:
>python p_12204.py
<function g�ster at 0x00BAC5D0>
()
None
('M.Nihat Yava�', 62, 'Ye�ilyurt - Malatya', 'TR')
None

<function �ehirler at 0x00BAC4F8>
�ehirler() missing 1 required positional argument: 'zaruri'
Ankara ()
None
Ankara ('�stanbul', '�zmir', 'Mersin', 'Adana', 'Bursa')
None

[0->100] aras� toplam geli�ig�zel 4 notun ortalamas� = 70.75'dir.

3 adet notun ortalamas�: 77.47
6 adet geli�ig�zel +/- say�n�n tamsay� ortalamas�: 26
[0->100] aras� toplam geli�ig�zel 92 notun ortalamas� = 73.29'dir.

x=87, y=71, z=62.5
Liste elemanlar� de�i�ken arg�mana d�n��t�r�l�r: None

x=87, y=71, z=62.5
Liste elemanlar� tek-tek sabit arg�man yap�l�r: None
"""