# coding:iso-8859-9 T�rk�e
# p_12704.py: Shelve ile s�zl�k dosyalar� yazma, okuma ve g�r�nt�leme �rne�i.

import shelve

s�zl�k = shelve.open ("Raf�m")

s�zl�k ["�lke"] = "Almanya"
s�zl�k ["ba�kent"] = "Berlin"
s�zl�k ["n�fus"] = 12000000
s�zl�k ["y�z�l��m"] = 85000
s�zl�k ["il�eler"] = 108

for anahtar in s�zl�k: print (anahtar, ": ", s�zl�k [anahtar], sep="")
s�zl�k.close()
print ("-"*75, "\n")
#------------------------------------------------------------------------------------------------------

s�zl�k2 = shelve.open ("Raf�m")
print (s�zl�k2)
print (dict (s�zl�k2) )
s�zl�k2.close()
print ("-"*75, "\n")
#------------------------------------------------------------------------------------------------------

s�zl�k = shelve.open ("tlfRehberim")
s�zl�k ["nihat"] = {"ad": "Mahmut Nihat", "soyad": "Yava�", "telefon": 905515559464}
s�zl�k ["nihal"] = {"ad": "Zeliha Nihal Yava�", "soyad": "Candan", "telefon": 905557449709}
s�zl�k ["hatice"] = {"ad": "Hatice Yava�", "soyad": "Ka�ar", "telefon": 905515530195}
s�zl�k ["y�cel"] = {"ad": "Y�cel", "soyad": "K���kbay", "telefon": 905322141528}
s�zl�k ["s�heyla"] = {"ad": "S�heyla Yava�", "soyad": "�zbay", "telefon": 905074576156}
s�zl�k ["sevim"] = {"ad": "Sevim", "soyad": "Yava�", "telefon": 905365864761}
s�zl�k ["canan"] = {"ad": "Canan", "soyad": "Candan", "telefon": 905432501944}
s�zl�k ["zafer"] = {"ad": "Zafer Nihat", "soyad": "Candan", "telefon": 905325573750}
s�zl�k ["y�cel"] = {"ad": "Y�cel", "soyad": "K���kbay", "telefon": 905322141528}
s�zl�k.close()

s�zl�k1 = shelve.open ("tlfRehberim")
for anahtar in s�zl�k1: print ("Soyad�, ad�: ", s�zl�k1[anahtar]["soyad"], ", ", s�zl�k1[anahtar]["ad"],  "; GSM: ", s�zl�k1[anahtar]["telefon"], sep="")
print ("-"*75, "\n")
#------------------------------------------------------------------------------------------------------

dosya = shelve.open ("dosyam")
from random import randint
for i in range (100): dosya [str (i)] = randint (0, 10000)
dosya.close()

dsy = shelve.open ("dosyam")

print ("100 adet geli�ig�zel say�lar s�zl���:", dict (dsy) )
print ("\nSadece s�zl�k de�erlerinin yanyana d�k�m�:", end=" ")
for a in dsy: print (dsy [a], end=", ")
dsy.close()



"""��kt�:
>python p_12704.py
�lke: Almanya
ba�kent: Berlin
n�fus: 12000000
y�z�l��m: 85000
il�eler: 108
---------------------------------------------------------------------------

<shelve.DbfilenameShelf object at 0x014690B0>
{'�lke': 'Almanya', 'ba�kent': 'Berlin', 'n�fus': 12000000, 'y�z�l��m': 85000, 'il�eler': 108}
---------------------------------------------------------------------------

Soyad�, ad�: Yava�, Mahmut Nihat; GSM: 905515559464
Soyad�, ad�: Candan, Zeliha Nihal Yava�; GSM: 905557449709
Soyad�, ad�: Ka�ar, Hatice Yava�; GSM: 905515530195
Soyad�, ad�: K���kbay, Y�cel; GSM: 905322141528
Soyad�, ad�: �zbay, S�heyla Yava�; GSM: 905074576156
Soyad�, ad�: Yava�, Sevim; GSM: 905365864761
Soyad�, ad�: Candan, Canan; GSM: 905432501944
Soyad�, ad�: Candan, Zafer Nihat; GSM: 905325573750
---------------------------------------------------------------------------

100 adet geli�ig�zel say�lar s�zl���: {'0': 6773, '1': 9501, '2': 7216, '3': 6965,
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

Sadece s�zl�k de�erlerinin yanyana d�k�m�: 6773, 9501, 7216, 6965, 4623, 1325,
8994, 2791, 1924, 304, 622, 4239, 2111, 7796, 6960, 4130, 496, 9582, 1110, 900,
3844, 3734, 9384, 5458, 2779, 7765, 630, 269, 4407, 9533, 1360, 4214, 6391, 8063,
 4200, 8901, 6928, 8071, 3302, 1791, 5855, 4264, 6797, 6914, 5025, 7554, 2034,
1638, 5306, 3779, 9305, 9971, 1299, 8938, 4775, 457, 3156, 8721, 4922, 3502, 6685,
9943, 3934, 4603, 407, 3606, 1761, 2391, 8985, 3272, 541, 7520, 2341, 8119, 19
9, 3886, 7381, 9611, 2002, 693, 8684, 9338, 7942, 5945, 5078, 749, 9259, 9734,
9495, 4145, 2918, 6979, 9037, 6143, 7103, 4596, 6307, 7507, 1417, 400,
"""