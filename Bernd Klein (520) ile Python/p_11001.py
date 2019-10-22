# coding:iso-8859-9 Türkçe
# p_11001.py: Anahtar:değer çifti içerikli sözlük elemanına erişim ve yeni eleman ekleme örneği.

şehirNüfusu = {}
print ("Boş sözlük:", şehirNüfusu, "\nEbatı:", len (şehirNüfusu) )

şehirNüfusu = {"New York City":8550405, "Los Angeles":3971883, "Toronto":2731571, "Chicago":2720546, "Houston":2296224, "Montreal":1704694, "Calgary":1239220, "Vancouver":631486, "Boston":667137}
print ("\nAmerika'da birkaç şehir ve nüfusları sözlüğü:", şehirNüfusu, "\nAnahtar-değer çifti sayısı:", len (şehirNüfusu))

print ("\nNewYork, Toronto ve Boston'un nüfusları:", şehirNüfusu["New York City"], şehirNüfusu["Toronto"], şehirNüfusu["Boston"])

print()
try: print ("Detroit'in nüfusu:", şehirNüfusu["Detroit"])
except KeyError: print ("HATA: Böyle bir şehir anahtarı şehirNüfusu sözlüğünde YOK!")

print()
try: print ("Los Angeles'ın nüfusu:", şehirNüfusu[1])
except KeyError: print ("HATA: Sözlüklerde endeks kullanılmaz!")

şehirNüfusu["Halifax"] = 390096 # Aynı anahtar sadece bir kez girilebilir...
şehirNüfusu["Halifax"] = 390096 # Hata vermez, fakat kabul de etmez...
print ("\nSona yeni ilave şehirle sözlük dökümü:", şehirNüfusu, "\nAnahtar-değer çifti sayısı:", len (şehirNüfusu))


"""Çıktı:
>python p_11001.py
Boş sözlük: {}
Ebatı: 0

Amerika'da birkaç şehir ve nüfusları sözlüğü: {'New York City': 8550405,
'Los Angeles': 3971883, 'Toronto': 2731571, 'Chicago': 2720546, 'Houston': 2296224,
'Montreal': 1704694, 'Calgary': 1239220, 'Vancouver': 631486, 'Boston': 667137}
Anahtar-değer çifti sayısı: 9

NewYork, Toronto ve Boston'un nüfusları: 8550405 2731571 667137

HATA: Böyle bir şehir anahtarı şehirNüfusu sözlüğünde YOK!

HATA: Sözlüklerde endeks kullanılmaz!

Sona yeni ilave şehirle sözlük dökümü: {'New York City': 8550405,
'Los Angeles': 3971883, 'Toronto': 2731571, 'Chicago': 2720546,
'Houston': 2296224, 'Montreal': 1704694, 'Calgary': 1239220,
'Vancouver': 631486, 'Boston': 667137, 'Halifax': 390096}
Anahtar-değer çifti sayısı: 10
"""