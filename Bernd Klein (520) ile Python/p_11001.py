# coding:iso-8859-9 T�rk�e
# p_11001.py: Anahtar:de�er �ifti i�erikli s�zl�k eleman�na eri�im ve yeni eleman ekleme �rne�i.

�ehirN�fusu = {}
print ("Bo� s�zl�k:", �ehirN�fusu, "\nEbat�:", len (�ehirN�fusu) )

�ehirN�fusu = {"New York City":8550405, "Los Angeles":3971883, "Toronto":2731571, "Chicago":2720546, "Houston":2296224, "Montreal":1704694, "Calgary":1239220, "Vancouver":631486, "Boston":667137}
print ("\nAmerika'da birka� �ehir ve n�fuslar� s�zl���:", �ehirN�fusu, "\nAnahtar-de�er �ifti say�s�:", len (�ehirN�fusu))

print ("\nNewYork, Toronto ve Boston'un n�fuslar�:", �ehirN�fusu["New York City"], �ehirN�fusu["Toronto"], �ehirN�fusu["Boston"])

print()
try: print ("Detroit'in n�fusu:", �ehirN�fusu["Detroit"])
except KeyError: print ("HATA: B�yle bir �ehir anahtar� �ehirN�fusu s�zl���nde YOK!")

print()
try: print ("Los Angeles'�n n�fusu:", �ehirN�fusu[1])
except KeyError: print ("HATA: S�zl�klerde endeks kullan�lmaz!")

�ehirN�fusu["Halifax"] = 390096 # Ayn� anahtar sadece bir kez girilebilir...
�ehirN�fusu["Halifax"] = 390096 # Hata vermez, fakat kabul de etmez...
print ("\nSona yeni ilave �ehirle s�zl�k d�k�m�:", �ehirN�fusu, "\nAnahtar-de�er �ifti say�s�:", len (�ehirN�fusu))


"""��kt�:
>python p_11001.py
Bo� s�zl�k: {}
Ebat�: 0

Amerika'da birka� �ehir ve n�fuslar� s�zl���: {'New York City': 8550405,
'Los Angeles': 3971883, 'Toronto': 2731571, 'Chicago': 2720546, 'Houston': 2296224,
'Montreal': 1704694, 'Calgary': 1239220, 'Vancouver': 631486, 'Boston': 667137}
Anahtar-de�er �ifti say�s�: 9

NewYork, Toronto ve Boston'un n�fuslar�: 8550405 2731571 667137

HATA: B�yle bir �ehir anahtar� �ehirN�fusu s�zl���nde YOK!

HATA: S�zl�klerde endeks kullan�lmaz!

Sona yeni ilave �ehirle s�zl�k d�k�m�: {'New York City': 8550405,
'Los Angeles': 3971883, 'Toronto': 2731571, 'Chicago': 2720546,
'Houston': 2296224, 'Montreal': 1704694, 'Calgary': 1239220,
'Vancouver': 631486, 'Boston': 667137, 'Halifax': 390096}
Anahtar-de�er �ifti say�s�: 10
"""