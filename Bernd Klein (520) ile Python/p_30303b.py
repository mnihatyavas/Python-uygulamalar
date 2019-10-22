# coding:iso-8859-9 Türkçe
# p_30303b.py: numpy.unicode ile Türkçe karakterli formatlı tabloyu ekrana ve dosyaya yazdırma örneği.

import numpy as np

dt = np.dtype ([('Ülke', np.unicode, 20), ('Yoğunluk', 'i4'), ('Alan', 'i4'), ('Nüfus', 'i4')])
# Ülke adları np.unicode ile artık başında b'siz ve tüm karakterleri alabilir...
ülkelerTablosu = np.array ([ # Azalan nüfus yoğunluğuna göre sıralıdır...
    ('Hollanda', 393, 41526, 16928800),
    ('Belçika', 337, 30510, 11007020),
    ('Birleşik Krallık', 256, 243610, 62262000),
    ('Almanya', 233, 357021, 81799600),
    ('Leh Cumhuriyeti', 205, 160, 32842),
    ('İtalya', 192, 301230, 59715625),
    ('İsviçre', 177, 41290, 7301994),
    ('Lüksemburg', 173, 2586, 512000),
    ('Fransa', 111, 547030, 63601002),
    ('Avusturya', 97, 83858, 8169929),
    ('Yunanistan', 81, 131940, 11606813),
    ('İrlanda', 65, 70280, 4581269),
    ('İsveç', 20, 449964, 9515744),
    ('Finlandiya', 16, 338424, 5410233),
    ('Norveç', 13, 385252, 5033675) ],
    dtype=dt)

print ("Bazı Avrupa ülkelerinin nüfus-alan-yoğunluk bilgileri:\n", ülkelerTablosu, sep="")

print ("\nFormatlı Nüfus/Alan hesaplamasıyla ülkelerin hassas nüfus yoğunlukları listesi:")
for i in range (len (ülkelerTablosu)):
    print ("{:17s}= {:8.4f} kişi/km2" .format (ülkelerTablosu["Ülke"][i], (ülkelerTablosu["Nüfus"][i] / ülkelerTablosu["Alan"][i])) )

np.savetxt ("p_30303bx.csv",
    ülkelerTablosu,
    fmt="%s;%d;%d;%d",
    delimiter=";") # "ülkeler.cvs" adıyla disk dosyasına saklar...



"""Çıktı:
>python p_30303b.py
Bazı Avrupa ülkelerinin nüfus-alan-yoğunluk bilgileri:
[('Hollanda', 393,  41526, 16928800) ('Belçika', 337,  30510, 11007020)
 ('Birleşik Krallık', 256, 243610, 62262000)
 ('Almanya', 233, 357021, 81799600)
 ('Leh Cumhuriyeti', 205,    160,    32842)
 ('İtalya', 192, 301230, 59715625) ('İsviçre', 177,  41290,  7301994)
 ('Lüksemburg', 173,   2586,   512000) ('Fransa', 111, 547030, 63601002)
 ('Avusturya',  97,  83858,  8169929)
 ('Yunanistan',  81, 131940, 11606813) ('İrlanda',  65,  70280,  4581269)
 ('İsveç',  20, 449964,  9515744) ('Finlandiya',  16, 338424,  5410233)
 ('Norveç',  13, 385252,  5033675)]

Formatlı Nüfus/Alan hesaplamasıyla ülkelerin hassas nüfus yoğunlukları listesi:
Hollanda         = 407.6675 kişi/km2
Belçika          = 360.7676 kişi/km2
Birleşik Krallık = 255.5806 kişi/km2
Almanya          = 229.1171 kişi/km2
Leh Cumhuriyeti  = 205.2625 kişi/km2
İtalya           = 198.2393 kişi/km2
İsviçre          = 176.8465 kişi/km2
Lüksemburg       = 197.9892 kişi/km2
Fransa           = 116.2660 kişi/km2
Avusturya        =  97.4258 kişi/km2
Yunanistan       =  87.9704 kişi/km2
İrlanda          =  65.1860 kişi/km2
İsveç            =  21.1478 kişi/km2
Finlandiya       =  15.9866 kişi/km2
Norveç           =  13.0659 kişi/km2
"""