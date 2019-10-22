# coding:iso-8859-9 T�rk�e
# p_30303a.py: numpy.dtype ile �lkeler tablosunun herbir kolonunu ayr� tipleyebilme �rne�i.

import numpy as np

dt = np.dtype ([('�lke', 'S20'), ('Yo�unluk', 'i4'), ('Alan', 'i4'), ('N�fus', 'i4')]) # i4=int32
# �lke adlar� "S20" tiple sadece binary(128) karakterlerle temsil edilebilir...
�lkelerTablosu = np.array ([ # Azalan n�fus yo�unlu�una g�re s�ral�d�r...
    ('Hollanda', 393, 41526, 16928800),
    ('Belcika', 337, 30510, 11007020), # Ascii(128) d��� T�rk�e karakterleri kabul etmiyor...
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

print ("Baz� Avrupa �lkelerinin n�fus-alan-yo�unluk bilgileri:\n", �lkelerTablosu, sep="")

print ("\n�lk �lke:", �lkelerTablosu [0])
print ("Orta �lke:", �lkelerTablosu [int (len (�lkelerTablosu) / 2)])
print ("Son �lke:", �lkelerTablosu [-1])

print ("\n�lke adlar�:\n", �lkelerTablosu ["�lke"], sep="")
print ("�lke n�fuslar�:\n", �lkelerTablosu ["N�fus"], sep="")
print ("�lke alanlar�:\n", �lkelerTablosu ["Alan"], sep="")
print ("�lke n�fus yo�unluklar�:\n", �lkelerTablosu ["Yo�unluk"], sep="")

print ("\nN�fus/Alan hesaplamas�yla �lkelerin n�fus yo�unluklar� listesi:")
for i in range (len (�lkelerTablosu)):
    print (�lkelerTablosu ["�lke"] [i], "=", (�lkelerTablosu ["N�fus"] [i] / �lkelerTablosu ["Alan"] [i]) )

print ("\nFormatl� N�fus/Alan hesaplamas�yla �lkelerin n�fus yo�unluklar� listesi:")
for i in range (len (�lkelerTablosu)):
    print ("{:17s}= {:6.2f} ki�i/km2" .format (str (�lkelerTablosu ["�lke"][i]) [2:-1], (�lkelerTablosu ["N�fus"] [i] / �lkelerTablosu ["Alan"] [i])) )



"""��kt�:
>python p_30303.py
Baz� Avrupa �lkelerinin n�fus-alan-yo�unluk bilgileri:
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

�lk �lke: (b'Hollanda', 393, 41526, 16928800)
Orta �lke: (b'Luksemburg', 173, 2586, 512000)
Son �lke: (b'Norvec', 13, 385252, 5033675)

�lke adlar�:
[b'Hollanda' b'Belcika' b'Birlesik Krallik' b'Almanya' b'Leh Cumhuriyeti'
 b'Italya' b'Isvicre' b'Luksemburg' b'Fransa' b'Avusturya' b'Yunanistan'
 b'Irlanda' b'Isvec' b'Finlandiya' b'Norvec']
�lke n�fuslar�:
[16928800 11007020 62262000 81799600    32842 59715625  7301994   512000
 63601002  8169929 11606813  4581269  9515744  5410233  5033675]
�lke alanlar�:
[ 41526  30510 243610 357021    160 301230  41290   2586 547030  83858
 131940  70280 449964 338424 385252]
�lke n�fus yo�unluklar�:
[393 337 256 233 205 192 177 173 111  97  81  65  20  16  13]

N�fus/Alan hesaplamas�yla �lkelerin n�fus yo�unluklar� listesi:
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

Formatl� N�fus/Alan hesaplamas�yla �lkelerin n�fus yo�unluklar� listesi:
Hollanda         = 407.67 ki�i/km2
Belcika          = 360.77 ki�i/km2
Birlesik Krallik = 255.58 ki�i/km2
Almanya          = 229.12 ki�i/km2
Leh Cumhuriyeti  = 205.26 ki�i/km2
Italya           = 198.24 ki�i/km2
Isvicre          = 176.85 ki�i/km2
Luksemburg       = 197.99 ki�i/km2
Fransa           = 116.27 ki�i/km2
Avusturya        =  97.43 ki�i/km2
Yunanistan       =  87.97 ki�i/km2
Irlanda          =  65.19 ki�i/km2
Isvec            =  21.15 ki�i/km2
Finlandiya       =  15.99 ki�i/km2
Norvec           =  13.07 ki�i/km2
"""