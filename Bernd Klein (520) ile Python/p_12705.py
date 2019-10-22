# coding:iso-8859-9 T�rk�e
# p_12705.py: Metin txt dosyadan okuma, tur�u pickle dosyaya yazma ve ordan tekrar okuma �rne�i.

import pickle

sat�rlar = open ("p_12705x.txt").readlines()
sat�rlar.sort()

�ehirler = []
print ("�ehirler ve g�n-saat:dakika zaman farklar�:")
for sat�r in sat�rlar:
    �ehir, g�n, saat, dakika = sat�r.split (",")
    print ("{}==>{}-{:d}:{:d}" .format (�ehir, g�n, int (saat), int (dakika)) )
    �ehirler.append (" ".join ((�ehir, g�n, str (saat), str (dakika)) ))

dosya = open ("�ehirlerdeZaman.tur�u", "bw")
pickle.dump (�ehirler, dosya)
dosya.close()
print ("-"*75, "\n")
#---------------------------------------------------------------------------------------------------------

print ("�ehirlerdeZaman.tur�u dosyas� i�erikleri:")
dsy = open ("�ehirlerdeZaman.tur�u", "rb")
liste = pickle.load (dsy)
for sat�r in liste: print (sat�r, end="")



"""��kt�:
>python p_12705.py
�ehirler ve g�n-saat:dakika zaman farklar�:
'Amsterdam'==> 'Pazar'-8:52
'Anchorage'==> 'Cumartesi'-23:52
'Ankara'==> 'Pazar'-10:52
'Athens'==> 'Pazar'-9:52
'Atlanta'==> 'Pazar'-2:52
'Auckland'==> 'Pazar'-20:52
'Barcelona'==> 'Pazar'-8:52
'Beirut'==> 'Pazar'-9:52
'Toronto'==> 'Pazar'-2:52
'Vancouver'==> 'Pazar'-0:52
'Vienna'==> 'Pazar'-8:52
'Warsaw'==> 'Pazar'-8:52
'Washington DC'==> 'Pazar'-2:52
'Winnipeg'==> 'Pazar'-1:52
'Zurich'==> 'Pazar'-8:52
---------------------------------------------------------------------------

�ehirlerdeZaman.tur�u dosyas� i�erikleri:
'Amsterdam'  'Pazar'  8  52
'Anchorage'  'Cumartesi'  23  52
'Ankara'  'Pazar'  10  52
'Athens'  'Pazar'  9  52
'Atlanta'  'Pazar'  2  52
'Auckland'  'Pazar'  20  52
'Barcelona'  'Pazar'  8  52
'Beirut'  'Pazar'  9  52
'Toronto'  'Pazar'  2  52
'Vancouver'  'Pazar'  0  52
'Vienna'  'Pazar'  8  52
'Warsaw'  'Pazar'  8  52
'Washington DC'  'Pazar'  2  52
'Winnipeg'  'Pazar'  1  52
'Zurich'  'Pazar'  8  52
"""