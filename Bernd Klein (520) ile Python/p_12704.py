# coding:iso-8859-9 Türkçe
# p_12704.py: Shelve ile sözlük dosyaları yazma, okuma ve görüntüleme örneği.

import shelve

sözlük = shelve.open ("Rafım")

sözlük ["ülke"] = "Almanya"
sözlük ["başkent"] = "Berlin"
sözlük ["nüfus"] = 12000000
sözlük ["yüzölçüm"] = 85000
sözlük ["ilçeler"] = 108

for anahtar in sözlük: print (anahtar, ": ", sözlük [anahtar], sep="")
sözlük.close()
print ("-"*75, "\n")
#------------------------------------------------------------------------------------------------------

sözlük2 = shelve.open ("Rafım")
print (sözlük2)
print (dict (sözlük2) )
sözlük2.close()
print ("-"*75, "\n")
#------------------------------------------------------------------------------------------------------

sözlük = shelve.open ("tlfRehberim")
sözlük ["nihat"] = {"ad": "Mahmut Nihat", "soyad": "Yavaş", "telefon": 905515559464}
sözlük ["nihal"] = {"ad": "Zeliha Nihal Yavaş", "soyad": "Candan", "telefon": 905557449709}
sözlük ["hatice"] = {"ad": "Hatice Yavaş", "soyad": "Kaçar", "telefon": 905515530195}
sözlük ["yücel"] = {"ad": "Yücel", "soyad": "Küçükbay", "telefon": 905322141528}
sözlük ["süheyla"] = {"ad": "Süheyla Yavaş", "soyad": "Özbay", "telefon": 905074576156}
sözlük ["sevim"] = {"ad": "Sevim", "soyad": "Yavaş", "telefon": 905365864761}
sözlük ["canan"] = {"ad": "Canan", "soyad": "Candan", "telefon": 905432501944}
sözlük ["zafer"] = {"ad": "Zafer Nihat", "soyad": "Candan", "telefon": 905325573750}
sözlük ["yücel"] = {"ad": "Yücel", "soyad": "Küçükbay", "telefon": 905322141528}
sözlük.close()

sözlük1 = shelve.open ("tlfRehberim")
for anahtar in sözlük1: print ("Soyadı, adı: ", sözlük1[anahtar]["soyad"], ", ", sözlük1[anahtar]["ad"],  "; GSM: ", sözlük1[anahtar]["telefon"], sep="")
print ("-"*75, "\n")
#------------------------------------------------------------------------------------------------------

dosya = shelve.open ("dosyam")
from random import randint
for i in range (100): dosya [str (i)] = randint (0, 10000)
dosya.close()

dsy = shelve.open ("dosyam")

print ("100 adet gelişigüzel sayılar sözlüğü:", dict (dsy) )
print ("\nSadece sözlük değerlerinin yanyana dökümü:", end=" ")
for a in dsy: print (dsy [a], end=", ")
dsy.close()



"""Çıktı:
>python p_12704.py
ülke: Almanya
başkent: Berlin
nüfus: 12000000
yüzölçüm: 85000
ilçeler: 108
---------------------------------------------------------------------------

<shelve.DbfilenameShelf object at 0x014690B0>
{'ülke': 'Almanya', 'başkent': 'Berlin', 'nüfus': 12000000, 'yüzölçüm': 85000, 'ilçeler': 108}
---------------------------------------------------------------------------

Soyadı, adı: Yavaş, Mahmut Nihat; GSM: 905515559464
Soyadı, adı: Candan, Zeliha Nihal Yavaş; GSM: 905557449709
Soyadı, adı: Kaçar, Hatice Yavaş; GSM: 905515530195
Soyadı, adı: Küçükbay, Yücel; GSM: 905322141528
Soyadı, adı: Özbay, Süheyla Yavaş; GSM: 905074576156
Soyadı, adı: Yavaş, Sevim; GSM: 905365864761
Soyadı, adı: Candan, Canan; GSM: 905432501944
Soyadı, adı: Candan, Zafer Nihat; GSM: 905325573750
---------------------------------------------------------------------------

100 adet gelişigüzel sayılar sözlüğü: {'0': 6773, '1': 9501, '2': 7216, '3': 6965,
'4': 4623, '5': 1325, '6': 8994, '7': 2791, '8': 1924, '9': 304, '10': 622, '11': 4239,
'12': 2111, '13': 7796, '14': 6960, '15': 4130, '16': 496, '17': 9582, '18': 1110,
'19': 900, '20': 3844, '21': 3734, '22': 9384, '23': 5458, '24': 2779, '25': 7765,
'26': 630, '27': 269, '28': 4407, '29': 9533, '30': 1360, '31': 4214, '32': 6391,
'33': 8063, '34': 4200, '35': 8901, '36': 6928, '37': 8071, '38': 3302, '39': 1791,
'40': 5855, '41': 4264, '42': 6797, '43': 6914, '44': 5025, '45': 7554, '46': 2034,
'47': 1638, '48': 5306, '49': 3779, '50': 9305, '51': 9971, '52': 1299, '53': 8938,
'54': 4775, '55': 457, '56': 3156, '57': 8721, '58': 4922, '59': 3502, '60': 6685,
'61': 9943, '62': 3934, '63': 4603, '64': 407, '65': 3606, '66': 1761, '67': 2391,
'68': 8985, '69': 3272, '70': 541, '71': 7520, '72': 2341, '73': 8119, '74': 199,
'75': 3886, '76': 7381, '77': 9611, '78': 2002, '79': 693, '80': 8684, '81': 9338,
'82': 7942, '83': 5945, '84': 5078, '85': 749, '86': 9259, '87': 9734, '88': 9495,
'89': 4145, '90': 2918, '91': 6979, '92': 9037, '93': 6143, '94': 7103, '95': 4596,
'96': 6307, '97': 7507, '98': 1417, '99': 400}

Sadece sözlük değerlerinin yanyana dökümü: 6773, 9501, 7216, 6965, 4623, 1325,
8994, 2791, 1924, 304, 622, 4239, 2111, 7796, 6960, 4130, 496, 9582, 1110, 900,
3844, 3734, 9384, 5458, 2779, 7765, 630, 269, 4407, 9533, 1360, 4214, 6391, 8063,
 4200, 8901, 6928, 8071, 3302, 1791, 5855, 4264, 6797, 6914, 5025, 7554, 2034,
1638, 5306, 3779, 9305, 9971, 1299, 8938, 4775, 457, 3156, 8721, 4922, 3502, 6685,
9943, 3934, 4603, 407, 3606, 1761, 2391, 8985, 3272, 541, 7520, 2341, 8119, 19
9, 3886, 7381, 9611, 2002, 693, 8684, 9338, 7942, 5945, 5078, 749, 9259, 9734,
9495, 4145, 2918, 6979, 9037, 6143, 7103, 4596, 6307, 7507, 1417, 400,
"""