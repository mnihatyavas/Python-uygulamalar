# coding:iso-8859-9 Türkçe
# p_30805.py: Çoklu ülkelerden depremzedelere ağırlıklı, yegane ve biçimli yardım listesi örneği.

import p_30801 as p381

ülkeliAdlar = {
    "Fransa" : [
        ("Marie", 10), ("Thomas", 10), ("Camille", 10), ("Nicolas", 9),
        ("Léa", 10), ("Julien", 9), ("Manon", 9), ("Quentin", 9),
        ("Chloé", 8), ("Maxime", 9), ("Laura", 7), ("Alexandre", 6),
        ("Clementine", 2), ("Grégory", 2), ("Sandra", 1), ("Philippe", 1) ],
    "İsviçre": [
        ("Sarah", 10), ("Hans", 10), ("Laura", 9), ("Peter", 8),
        ("Mélissa", 9), ("Walter", 7), ("Océane", 7), ("Daniel", 7),
        ("Noémie", 6), ("Reto", 7), ("Laura", 7), ("Bruno", 6),
        ("Eva", 2), ("Urli", 4), ("Sandra", 1), ("Marcel", 1) ],
    "Almanya": [
        ("Ursula", 10), ("Peter", 10), ("Monika", 9), ("Michael", 8),
        ("Brigitte", 9), ("Thomas", 7), ("Stefanie", 7), ("Andreas", 7),
        ("Maria", 6), ("Wolfgang", 7), ("Gabriele", 7), ("Manfred", 6),
        ("Nicole", 2), ("Matthias", 4), ("Christine", 1), ("Dirk", 1) ],
    "İtalya" : [
        ("Francesco", 20), ("Alessandro", 19), ("Mattia", 19), ("Lorenzo", 18),
        ("Leonardo", 16), ("Andrea", 15), ("Gabriele", 14), ("Matteo", 14),
        ("Tommaso", 12), ("Riccardo", 11), ("Sofia", 20), ("Aurora", 18),
        ("Giulia", 16), ("Giorgia", 15), ("Alice", 14), ("Martina", 13) ],
    "Türkiye":[
        ("Mehmet", 35), ("Nihat", 3), ("Hatice", 32), ("Ali", 19),
        ("Hasan", 25), ("Ayşe", 27), ("Kezban", 9), ("Yavuz", 3),
        ("Özcan", 8), ("Mahmut", 22), ("Belkıs", 1) ] }

ülkeliSoyadlar = {
    "Fransa" : [
        ("Matin", 10), ("Bernard", 10), ("Camille", 10), ("Nicolas", 9),
        ("Dubois", 10), ("Petit", 9), ("Durand", 8), ("Leroy", 8),
        ("Fournier", 7), ("Lambert", 6), ("Mercier", 5), ("Rousseau", 4),
        ("Mathieu", 2), ("Fontaine", 2), ("Muller", 1), ("Robin", 1) ],
    "İsviçre": [
        ("Müller", 10), ("Meier", 10), ("Schmid", 9), ("Keller", 8),
        ("Weber", 9), ("Huber", 7), ("Schneider", 7), ("Meyer", 7),
        ("Steiner", 6), ("Fischer", 7), ("Gerber", 7), ("Brunner", 6),
        ("Baumann", 2), ("Frei", 4), ("Zimmermann", 1), ("Moser", 1) ],
    "Almanya": [
        ("Müller", 10), ("Schmidt", 10), ("Schneider", 9), ("Fischer", 8),
        ("Weber", 9), ("Meyer", 7), ("Wagner", 7), ("Becker", 7),
        ("Schulz", 6), ("Hoffmann", 7), ("Schäfer", 7), ("Koch", 6),
        ("Bauer", 2), ("Richter", 4), ("Klein", 2), ("Schröder", 1) ],
    "İtalya" : [
        ("Rossi", 20), ("Russo", 19), ("Ferrari", 19), ("Esposito", 18),
        ("Bianchi", 16), ("Romano", 15), ("Colombo", 14), ("Ricci", 14),
        ("Marino", 12), ("Grecco", 11), ("Bruno", 10), ("Gallo", 12),
        ("Conti", 16), ("De Luca", 15), ("Costa", 14), ("Giordano", 13),
        ("Mancini", 14), ("Rizzo", 13), ("Lombardi", 11), ("Moretto", 9) ],
    "Türkiye" : [
        ("Öztürk", 25), ("Hastürk", 19), ("Göktürk", 19), ("Yavaş", 3),
        ("Özen", 14), ("Fırat", 13), ("Kölük", 1), ("Eskici", 1) ] }

ülkelerinAğırlığı = [
    ("Almanya", 0.3),
    ("Fransa", 0.4),
    ("İsviçre", 0.1),
    ("İtalya", 0.1),
    ("Türkiye", 0.1)]

yardımcılarınAğırlığı = [
    ("Tıbbi Yardım", 0.3),
    ("Barınma Yardımı", 0.1),
    ("Beslenme Yardımı", 0.2),
    ("Sosyal Yardım", 0.1),
    ("Enkaz Kazıcı", 0.3)]

bireşim = {}
for ülke in ülkeliAdlar:
    adlar, ağırlıkları = zip (*ülkeliAdlar[ülke])
    ağırlıklarToplamı = sum (ağırlıkları)
    adlarınAğırlıkları = [x / ağırlıklarToplamı for x in ağırlıkları]
    ülkeliAdlar[ülke] = [adlar, adlarınAğırlıkları]
    soyadlar, ağırlıkları = zip (*ülkeliSoyadlar[ülke])
    ağırlıklarToplamı = sum (ağırlıkları)
    soyadlarınAğırlıkları = [x / ağırlıklarToplamı for x in ağırlıkları]
    ülkeliSoyadlar[ülke] = [soyadlar, adlarınAğırlıkları]
    bireşim[ülke] = p381.bireşimci (
        (adlar, soyadlar),
        (adlarınAğırlıkları, soyadlarınAğırlıkları),
        biçimlemeFonksiyonu=lambda x: " ".join (x),
        tekrarlanabilirSeçimMi=False)

try: sayı = abs (int (input ("Kaç afetzade yardımcısı seçilecek [10]? "))); print()
except: sayı = 10

yardımcılar = []
kimlikNo = 1
for _ in range (sayı):
    ülke = p381.ağırlıklıKarşılıklıSeçim (zip (*ülkelerinAğırlığı))
    yardımKonusu = p381.ağırlıklıKarşılıklıSeçim (zip (*yardımcılarınAğırlığı))
    ülke, yardımKonusu = ülke[0], yardımKonusu[0]
    yardımcı = bireşim[ülke]()
    kn = "{kn:05d}".format (kn=kimlikNo)
    yardımcılar.append ( (kn, ülke, next (yardımcı), yardımKonusu) )
    kimlikNo += 1

print (yardımcılar); print()
for i in range (sayı):
    for j in range (4): print (yardımcılar[i][j], end=", ")
    print()

if input ("\nGönüllüler listesi disk dosyasına yazılsın mı? [e/h] ") == "e":
    with open ("p_30805x.txt", "w") as dosya:
        dosya.write ("Referans No, Ülkesi, Ad ve Soyadı, Görevi\n")
        for gönüllü in yardımcılar: dosya.write (", ".join (gönüllü) + "\n")



"""Çıktı:
>python p_30805.py
Kaç afetzade yardımcısı seçilecek [10]? 2

[('00001', 'Almanya', 'Brigitte Richter', 'Enkaz Kazıcı'), ('00002', 'Almanya', 'Ursula Wagner', 'Enkaz Kazıcı')]

00001, Almanya, Brigitte Richter, Enkaz Kazıcı,
00002, Almanya, Ursula Wagner, Enkaz Kazıcı,

Gönüllüler listesi disk dosyasına yazılsın mı? [e/h]

>python p_30805.py  ** TEKRAR **
Kaç afetzade yardımcısı seçilecek [10]?
[('00001', 'Fransa', 'Marie Petit', 'Barınma Yardımı'), ('00002', 'Türkiye', 'Hatice Öztürk', 'Enkaz Kazıcı'),
('00003', 'Türkiye', 'Kezban Özen', 'Tıbbi Yardım'), ('00004', 'Almanya', 'Manfred Bauer', 'Tıbbi Yardım'),
('00005', 'İsviçre', 'Daniel Meyer', 'Tıbbi Yardım'), ('00006', 'Fransa', 'Thomas Mercier', 'Beslenme Yardımı'),
('00007', 'Almanya', 'Manfred Becker', 'Beslenme Yardımı'), ('00008', 'Türkiye', 'Özcan Fırat', 'Tıbbi Yardım'),
('00009', 'Türkiye', 'Mahmut Göktürk', 'Tıbbi Yardım'), ('00010', 'Fransa', 'Nicolas Nicolas', 'Enkaz Kazıcı')]

00001, Fransa, Marie Petit, Barınma Yardımı,
00002, Türkiye, Hatice Öztürk, Enkaz Kazıcı,
00003, Türkiye, Kezban Özen, Tıbbi Yardım,
00004, Almanya, Manfred Bauer, Tıbbi Yardım,
00005, İsviçre, Daniel Meyer, Tıbbi Yardım,
00006, Fransa, Thomas Mercier, Beslenme Yardımı,
00007, Almanya, Manfred Becker, Beslenme Yardımı,
00008, Türkiye, Özcan Fırat, Tıbbi Yardım,
00009, Türkiye, Mahmut Göktürk, Tıbbi Yardım,
00010, Fransa, Nicolas Nicolas, Enkaz Kazıcı,
"""