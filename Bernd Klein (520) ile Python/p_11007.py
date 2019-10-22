# coding:iso-8859-9 Türkçe
# p_11007.py: Kompleks sözlüklerde kopyalamanın birbirlerini etkilemesi örneği.

kurslar = {"kurs1":{"konu":"Yeni başlayanlar için Python programcılık kursu", 
                         "şehir":"Malatya", 
                         "eğitmen":"Songül Yavaş Göktürk"},
              "kurs2":{"konu":"Orta seviye Python eğitimi",
                         "şehir":"Bursa",
                         "eğitmen":"Sevim Yavaş"},
              "kurs3":{"konu":"Python metin işleme kursu",
                         "şehir":"İstanbul",
                         "eğitmen":"M.Nihat Yavaş"}
              }

print (kurslar)

kurslar2 = kurslar.copy()

kurslar["kurs2"]["konu"] = "Yeni başlayanlar için Perl eğitim kursu"

print()
print (kurslar2) # Tek anahtar-değer değişimi kurslar2'yi de değiştirdi!..

kurslar["kurs2"] = {"konu":"Yeni başlayanlar için Perl Semineri",
                         "şehir":"İzmir",
                         "eğitmen":"Talip Amanat"}
print()
print (kurslar)

print()
print (kurslar2["kurs2"]) # Tüm nesne değişimi kurslar2'yi etkilemedi!..

# Çözüm deepcopy() kullanmak, ama o da liste'ler için geçerli,
# sözlük'lerde kabul etmiyor; şimdilik salla gitsin...
#---------------------------------------------------------------------------------------------------

kurslar.clear()
print ("\nİlk sözlüğün silinmesi 2.yi değiştirmedi: ", kurslar, "\n", kurslar2, sep="")

kurslar2.clear()
print ("\nHer iki sözlük de silindi:", kurslar, kurslar2)


"""Çıktı:
>python p_11007.py
{'kurs1': {'konu': 'Yeni başlayanlar için Python programcılık kursu', 'şehir': '
Malatya', 'eğitmen': 'Songül Yavaş Göktürk'}, 'kurs2': {'konu': 'Orta seviye Python eğitimi',
'şehir': 'Bursa', 'eğitmen': 'Sevim Yavaş'}, 'kurs3': {'konu': 'Python metin işleme kursu',
'şehir': 'İstanbul', 'eğitmen': 'M.Nihat Yavaş'}}

{'kurs1': {'konu': 'Yeni başlayanlar için Python programcılık kursu', 'şehir': '
Malatya', 'eğitmen': 'Songül Yavaş Göktürk'}, 'kurs2': {'konu': 'Yeni başlayanlar için Perl eğitim kursu',
'şehir': 'Bursa', 'eğitmen': 'Sevim Yavaş'}, 'kurs3': {'konu': 'Python metin işleme kursu',
'şehir': 'İstanbul', 'eğitmen': 'M.Nihat Yavaş'}}

{'kurs1': {'konu': 'Yeni başlayanlar için Python programcılık kursu', 'şehir': '
Malatya', 'eğitmen': 'Songül Yavaş Göktürk'}, 'kurs2': {'konu': 'Yeni başlayanlar için Perl Semineri',
'şehir': 'İzmir', 'eğitmen': 'Talip Amanat'}, 'kurs3': {'konu': 'Python metin işleme kursu',
'şehir': 'İstanbul', 'eğitmen': 'M.Nihat Yavaş'}}

{'konu': 'Yeni başlayanlar için Perl eğitim kursu', 'şehir': 'Bursa', 'eğitmen': 'Sevim Yavaş'}

İlk sözlüğün silinmesi 2.yi değiştirmedi: {}
{'kurs1': {'konu': 'Yeni başlayanlar için Python programcılık kursu', 'şehir': '
Malatya', 'eğitmen': 'Songül Yavaş Göktürk'}, 'kurs2': {'konu': 'Yeni başlayanlar için Perl eğitim kursu',
'şehir': 'Bursa', 'eğitmen': 'Sevim Yavaş'}, 'kurs3': {'konu': 'Python metin işleme kursu',
'şehir': 'İstanbul', 'eğitmen': 'M.Nihat Yavaş'}}

Her iki sözlük de silindi: {} {}
"""