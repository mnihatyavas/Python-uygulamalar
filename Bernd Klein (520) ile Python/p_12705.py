# coding:iso-8859-9 Türkçe
# p_12705.py: Metin txt dosyadan okuma, turşu pickle dosyaya yazma ve ordan tekrar okuma örneği.

import pickle

satırlar = open ("p_12705x.txt").readlines()
satırlar.sort()

şehirler = []
print ("Şehirler ve gün-saat:dakika zaman farkları:")
for satır in satırlar:
    şehir, gün, saat, dakika = satır.split (",")
    print ("{}==>{}-{:d}:{:d}" .format (şehir, gün, int (saat), int (dakika)) )
    şehirler.append (" ".join ((şehir, gün, str (saat), str (dakika)) ))

dosya = open ("şehirlerdeZaman.turşu", "bw")
pickle.dump (şehirler, dosya)
dosya.close()
print ("-"*75, "\n")
#---------------------------------------------------------------------------------------------------------

print ("şehirlerdeZaman.turşu dosyası içerikleri:")
dsy = open ("şehirlerdeZaman.turşu", "rb")
liste = pickle.load (dsy)
for satır in liste: print (satır, end="")



"""Çıktı:
>python p_12705.py
Şehirler ve gün-saat:dakika zaman farkları:
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

şehirlerdeZaman.turşu dosyası içerikleri:
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