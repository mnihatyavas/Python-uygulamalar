# coding:iso-8859-9 Türkçe
# p_30303a.py: numpy.dtype ile ülkeler tablosunun herbir kolonunu ayrı tipleyebilme örneği.

import numpy as np

dt = np.dtype ([('Ülke', 'S20'), ('Yoğunluk', 'i4'), ('Alan', 'i4'), ('Nüfus', 'i4')]) # i4=int32
# Ülke adları "S20" tiple sadece binary(128) karakterlerle temsil edilebilir...
ülkelerTablosu = np.array ([ # Azalan nüfus yoğunluğuna göre sıralıdır...
    ('Hollanda', 393, 41526, 16928800),
    ('Belcika', 337, 30510, 11007020), # Ascii(128) dışı Türkçe karakterleri kabul etmiyor...
    ('Birlesik Krallik', 256, 243610, 62262000),
    ('Almanya', 233, 357021, 81799600),
    ('Leh Cumhuriyeti', 205, 160, 32842),
    ('Italya', 192, 301230, 59715625),
    ('Isvicre', 177, 41290, 7301994),
    ('Luksemburg', 173, 2586, 512000),
    ('Fransa', 111, 547030, 63601002),
    ('Avusturya', 97, 83858, 8169929),
    ('Yunanistan', 81, 131940, 11606813),
    ('Irlanda', 65, 70280, 4581269),
    ('Isvec', 20, 449964, 9515744),
    ('Finlandiya', 16, 338424, 5410233),
    ('Norvec', 13, 385252, 5033675) ],
    dtype=dt)

print ("Bazı Avrupa ülkelerinin nüfus-alan-yoğunluk bilgileri:\n", ülkelerTablosu, sep="")

print ("\nİlk ülke:", ülkelerTablosu [0])
print ("Orta ülke:", ülkelerTablosu [int (len (ülkelerTablosu) / 2)])
print ("Son ülke:", ülkelerTablosu [-1])

print ("\nÜlke adları:\n", ülkelerTablosu ["Ülke"], sep="")
print ("Ülke nüfusları:\n", ülkelerTablosu ["Nüfus"], sep="")
print ("Ülke alanları:\n", ülkelerTablosu ["Alan"], sep="")
print ("Ülke nüfus yoğunlukları:\n", ülkelerTablosu ["Yoğunluk"], sep="")

print ("\nNüfus/Alan hesaplamasıyla ülkelerin nüfus yoğunlukları listesi:")
for i in range (len (ülkelerTablosu)):
    print (ülkelerTablosu ["Ülke"] [i], "=", (ülkelerTablosu ["Nüfus"] [i] / ülkelerTablosu ["Alan"] [i]) )

print ("\nFormatlı Nüfus/Alan hesaplamasıyla ülkelerin nüfus yoğunlukları listesi:")
for i in range (len (ülkelerTablosu)):
    print ("{:17s}= {:6.2f} kişi/km2" .format (str (ülkelerTablosu ["Ülke"][i]) [2:-1], (ülkelerTablosu ["Nüfus"] [i] / ülkelerTablosu ["Alan"] [i])) )



"""Çıktı:
>python p_30303.py
Bazı Avrupa ülkelerinin nüfus-alan-yoğunluk bilgileri:
[(b'Hollanda', 393,  41526, 16928800) (b'Belcika', 337,  30510, 11007020)
 (b'Birlesik Krallik', 256, 243610, 62262000)
 (b'Almanya', 233, 357021, 81799600)
 (b'Leh Cumhuriyeti', 205,    160,    32842)
 (b'Italya', 192, 301230, 59715625) (b'Isvicre', 177,  41290,  7301994)
 (b'Luksemburg', 173,   2586,   512000) (b'Fransa', 111, 547030, 63601002)
 (b'Avusturya',  97,  83858,  8169929)
 (b'Yunanistan',  81, 131940, 11606813)
 (b'Irlanda',  65,  70280,  4581269) (b'Isvec',  20, 449964,  9515744)
 (b'Finlandiya',  16, 338424,  5410233) (b'Norvec',  13, 385252,  5033675)]

İlk ülke: (b'Hollanda', 393, 41526, 16928800)
Orta ülke: (b'Luksemburg', 173, 2586, 512000)
Son ülke: (b'Norvec', 13, 385252, 5033675)

Ülke adları:
[b'Hollanda' b'Belcika' b'Birlesik Krallik' b'Almanya' b'Leh Cumhuriyeti'
 b'Italya' b'Isvicre' b'Luksemburg' b'Fransa' b'Avusturya' b'Yunanistan'
 b'Irlanda' b'Isvec' b'Finlandiya' b'Norvec']
Ülke nüfusları:
[16928800 11007020 62262000 81799600    32842 59715625  7301994   512000
 63601002  8169929 11606813  4581269  9515744  5410233  5033675]
Ülke alanları:
[ 41526  30510 243610 357021    160 301230  41290   2586 547030  83858
 131940  70280 449964 338424 385252]
Ülke nüfus yoğunlukları:
[393 337 256 233 205 192 177 173 111  97  81  65  20  16  13]

Nüfus/Alan hesaplamasıyla ülkelerin nüfus yoğunlukları listesi:
b'Hollanda' = 407.66748543081445
b'Belcika' = 360.7676171746968
b'Birlesik Krallik' = 255.58064118878536
b'Almanya' = 229.11705473907696
b'Leh Cumhuriyeti' = 205.2625
b'Italya' = 198.23930219433655
b'Isvicre' = 176.8465488011625
b'Luksemburg' = 197.98917246713071
b'Fransa' = 116.26602197320074
b'Avusturya' = 97.4257554437263
b'Yunanistan' = 87.9703880551766
b'Irlanda' = 65.1859561752988
b'Isvec' = 21.147789600945853
b'Finlandiya' = 15.986552372172186
b'Norvec' = 13.065928275518361

Formatlı Nüfus/Alan hesaplamasıyla ülkelerin nüfus yoğunlukları listesi:
Hollanda         = 407.67 kişi/km2
Belcika          = 360.77 kişi/km2
Birlesik Krallik = 255.58 kişi/km2
Almanya          = 229.12 kişi/km2
Leh Cumhuriyeti  = 205.26 kişi/km2
Italya           = 198.24 kişi/km2
Isvicre          = 176.85 kişi/km2
Luksemburg       = 197.99 kişi/km2
Fransa           = 116.27 kişi/km2
Avusturya        =  97.43 kişi/km2
Yunanistan       =  87.97 kişi/km2
Irlanda          =  65.19 kişi/km2
Isvec            =  21.15 kişi/km2
Finlandiya       =  15.99 kişi/km2
Norvec           =  13.07 kişi/km2
"""