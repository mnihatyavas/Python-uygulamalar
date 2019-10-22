# coding:iso-8859-9 T�rk�e
# p_11007.py: Kompleks s�zl�klerde kopyalaman�n birbirlerini etkilemesi �rne�i.

kurslar = {"kurs1":{"konu":"Yeni ba�layanlar i�in Python programc�l�k kursu", 
                         "�ehir":"Malatya", 
                         "e�itmen":"Song�l Yava� G�kt�rk"},
              "kurs2":{"konu":"Orta seviye Python e�itimi",
                         "�ehir":"Bursa",
                         "e�itmen":"Sevim Yava�"},
              "kurs3":{"konu":"Python metin i�leme kursu",
                         "�ehir":"�stanbul",
                         "e�itmen":"M.Nihat Yava�"}
              }

print (kurslar)

kurslar2 = kurslar.copy()

kurslar["kurs2"]["konu"] = "Yeni ba�layanlar i�in Perl e�itim kursu"

print()
print (kurslar2) # Tek anahtar-de�er de�i�imi kurslar2'yi de de�i�tirdi!..

kurslar["kurs2"] = {"konu":"Yeni ba�layanlar i�in Perl Semineri",
                         "�ehir":"�zmir",
                         "e�itmen":"Talip Amanat"}
print()
print (kurslar)

print()
print (kurslar2["kurs2"]) # T�m nesne de�i�imi kurslar2'yi etkilemedi!..

# ��z�m deepcopy() kullanmak, ama o da liste'ler i�in ge�erli,
# s�zl�k'lerde kabul etmiyor; �imdilik salla gitsin...
#---------------------------------------------------------------------------------------------------

kurslar.clear()
print ("\n�lk s�zl���n silinmesi 2.yi de�i�tirmedi: ", kurslar, "\n", kurslar2, sep="")

kurslar2.clear()
print ("\nHer iki s�zl�k de silindi:", kurslar, kurslar2)


"""��kt�:
>python p_11007.py
{'kurs1': {'konu': 'Yeni ba�layanlar i�in Python programc�l�k kursu', '�ehir': '
Malatya', 'e�itmen': 'Song�l Yava� G�kt�rk'}, 'kurs2': {'konu': 'Orta seviye Python e�itimi',
'�ehir': 'Bursa', 'e�itmen': 'Sevim Yava�'}, 'kurs3': {'konu': 'Python metin i�leme kursu',
'�ehir': '�stanbul', 'e�itmen': 'M.Nihat Yava�'}}

{'kurs1': {'konu': 'Yeni ba�layanlar i�in Python programc�l�k kursu', '�ehir': '
Malatya', 'e�itmen': 'Song�l Yava� G�kt�rk'}, 'kurs2': {'konu': 'Yeni ba�layanlar i�in Perl e�itim kursu',
'�ehir': 'Bursa', 'e�itmen': 'Sevim Yava�'}, 'kurs3': {'konu': 'Python metin i�leme kursu',
'�ehir': '�stanbul', 'e�itmen': 'M.Nihat Yava�'}}

{'kurs1': {'konu': 'Yeni ba�layanlar i�in Python programc�l�k kursu', '�ehir': '
Malatya', 'e�itmen': 'Song�l Yava� G�kt�rk'}, 'kurs2': {'konu': 'Yeni ba�layanlar i�in Perl Semineri',
'�ehir': '�zmir', 'e�itmen': 'Talip Amanat'}, 'kurs3': {'konu': 'Python metin i�leme kursu',
'�ehir': '�stanbul', 'e�itmen': 'M.Nihat Yava�'}}

{'konu': 'Yeni ba�layanlar i�in Perl e�itim kursu', '�ehir': 'Bursa', 'e�itmen': 'Sevim Yava�'}

�lk s�zl���n silinmesi 2.yi de�i�tirmedi: {}
{'kurs1': {'konu': 'Yeni ba�layanlar i�in Python programc�l�k kursu', '�ehir': '
Malatya', 'e�itmen': 'Song�l Yava� G�kt�rk'}, 'kurs2': {'konu': 'Yeni ba�layanlar i�in Perl e�itim kursu',
'�ehir': 'Bursa', 'e�itmen': 'Sevim Yava�'}, 'kurs3': {'konu': 'Python metin i�leme kursu',
'�ehir': '�stanbul', 'e�itmen': 'M.Nihat Yava�'}}

Her iki s�zl�k de silindi: {} {}
"""