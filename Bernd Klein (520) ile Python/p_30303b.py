# coding:iso-8859-9 T�rk�e
# p_30303b.py: numpy.unicode ile T�rk�e karakterli formatl� tabloyu ekrana ve dosyaya yazd�rma �rne�i.

import numpy as np

dt = np.dtype ([('�lke', np.unicode, 20), ('Yo�unluk', 'i4'), ('Alan', 'i4'), ('N�fus', 'i4')])
# �lke adlar� np.unicode ile art�k ba��nda b'siz ve t�m karakterleri alabilir...
�lkelerTablosu = np.array ([ # Azalan n�fus yo�unlu�una g�re s�ral�d�r...
    ('Hollanda', 393, 41526, 16928800),
    ('Bel�ika', 337, 30510, 11007020),
    ('Birle�ik Krall�k', 256, 243610, 62262000),
    ('Almanya', 233, 357021, 81799600),
    ('Leh Cumhuriyeti', 205, 160, 32842),
    ('�talya', 192, 301230, 59715625),
    ('�svi�re', 177, 41290, 7301994),
    ('L�ksemburg', 173, 2586, 512000),
    ('Fransa', 111, 547030, 63601002),
    ('Avusturya', 97, 83858, 8169929),
    ('Yunanistan', 81, 131940, 11606813),
    ('�rlanda', 65, 70280, 4581269),
    ('�sve�', 20, 449964, 9515744),
    ('Finlandiya', 16, 338424, 5410233),
    ('Norve�', 13, 385252, 5033675) ],
    dtype=dt)

print ("Baz� Avrupa �lkelerinin n�fus-alan-yo�unluk bilgileri:\n", �lkelerTablosu, sep="")

print ("\nFormatl� N�fus/Alan hesaplamas�yla �lkelerin hassas n�fus yo�unluklar� listesi:")
for i in range (len (�lkelerTablosu)):
    print ("{:17s}= {:8.4f} ki�i/km2" .format (�lkelerTablosu["�lke"][i], (�lkelerTablosu["N�fus"][i] / �lkelerTablosu["Alan"][i])) )

np.savetxt ("p_30303bx.csv",
    �lkelerTablosu,
    fmt="%s;%d;%d;%d",
    delimiter=";") # "�lkeler.cvs" ad�yla disk dosyas�na saklar...



"""��kt�:
>python p_30303b.py
Baz� Avrupa �lkelerinin n�fus-alan-yo�unluk bilgileri:
[('Hollanda', 393,  41526, 16928800) ('Bel�ika', 337,  30510, 11007020)
 ('Birle�ik Krall�k', 256, 243610, 62262000)
 ('Almanya', 233, 357021, 81799600)
 ('Leh Cumhuriyeti', 205,    160,    32842)
 ('�talya', 192, 301230, 59715625) ('�svi�re', 177,  41290,  7301994)
 ('L�ksemburg', 173,   2586,   512000) ('Fransa', 111, 547030, 63601002)
 ('Avusturya',  97,  83858,  8169929)
 ('Yunanistan',  81, 131940, 11606813) ('�rlanda',  65,  70280,  4581269)
 ('�sve�',  20, 449964,  9515744) ('Finlandiya',  16, 338424,  5410233)
 ('Norve�',  13, 385252,  5033675)]

Formatl� N�fus/Alan hesaplamas�yla �lkelerin hassas n�fus yo�unluklar� listesi:
Hollanda         = 407.6675 ki�i/km2
Bel�ika          = 360.7676 ki�i/km2
Birle�ik Krall�k = 255.5806 ki�i/km2
Almanya          = 229.1171 ki�i/km2
Leh Cumhuriyeti  = 205.2625 ki�i/km2
�talya           = 198.2393 ki�i/km2
�svi�re          = 176.8465 ki�i/km2
L�ksemburg       = 197.9892 ki�i/km2
Fransa           = 116.2660 ki�i/km2
Avusturya        =  97.4258 ki�i/km2
Yunanistan       =  87.9704 ki�i/km2
�rlanda          =  65.1860 ki�i/km2
�sve�            =  21.1478 ki�i/km2
Finlandiya       =  15.9866 ki�i/km2
Norve�           =  13.0659 ki�i/km2
"""