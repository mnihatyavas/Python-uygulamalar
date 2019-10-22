# coding:iso-8859-9 T�rk�e
# p_32102b.py: S�zge�leme, s�tun ekleme ve artan-azalan s�ralama �rne�i.

import pandas as pd

�ehirler = {
    "ad": ["Londra", "Berlin", "Madrid", "Roma", "Paris",
        "Viyana", "Bu�arest", "Hamburg", "Budape�te", "Var�ova",
        "Barselona", "M�nih", "Milano", "�stanbul", "Ankara"],
    "n�fus": [8615246, 3562166, 3165235, 2874038, 2273305,
        1805681, 1803425, 1760433, 1754000, 1740119,
        1602386, 1493900, 1350680, 14657321, 5731256],
    "�lke": ["�ngiltere", "Almanya", "�spanya", "�talya", "Fransa",
        "Avusturya", "Romanya", "Almanya", "Macaristan", "Polonya",
        "�spanya", "Almanya", "�talya", "T�rkiye", "T�rkiye"] }

v�1 = pd.DataFrame (�ehirler, columns=["ad", "n�fus"], index=�ehirler ["�lke"] )
print ("�lke endeksli �ehirler veri �er�evesi:\n", v�1, sep="")

# Sat�r s�zgeci...
print ("\nAlmanya'n�n veri �er�evesi:\n", v�1.loc ["Almanya"], sep="")
print ("\nAlmanya ve T�rkiye'nin veri �er�evesi:\n", v�1.loc [["Almanya", "T�rkiye"]], sep="")
print ("\nN�fusu 2M'dan fazla �ehirlerin veri �er�evesi:\n", v�1.loc [v�1.n�fus >= 2000000], sep="")
print ("-"*79)
#------------------------------------------------------------------------------------------------------

print ("\n�lke endeksli toplam veriler:\n", v�1.sum(), sep="")
print ("\nVeri �er�evesi n�fus toplam�:", v�1 ["n�fus"].sum() )
x = v�1 ["n�fus"].cumsum()
print ("\n�lke endeksli �ehirlerin ard���k eklemeli k�m�latif toplam�:\n", x, sep="")
print ("-"*79)
#------------------------------------------------------------------------------------------------------

v�1 ["n�fus"] = x
print ("\nN�fus=k�m�latif �ehir �er�evesi:\n", v�1, sep="")

v�2 = pd.DataFrame (�ehirler, columns=["ad", "n�fus", "eklemeliN�fus"], index=�ehirler ["�lke"])
# eklemeliN�fus=NaN
v�2 ["eklemeliN�fus"] = x
print ("\nEklemeli n�fus s�tunlu ve �lke endeksli veri �er�evesi:\n", v�2, sep="")
print ("-"*79)
#------------------------------------------------------------------------------------------------------

alan = [1572, 891.85, 605.77, 1285, 105.4, 414.6, 228, 755, 525.2, 517,
    101.9, 310.4, 181.8, 2314, 3267.92]
v�3 = pd.DataFrame (�ehirler, columns=["�lke", "alan", "n�fus"], index=�ehirler ["ad"])
# alan=NaN
v�3 ["alan"] = alan
print ("\n�ehir km^2 alan s�tunlu ve �ehir endeksli veri �er�evesi:\n", v�3, sep="")

# S�tun s�zgeci...
#print ("\nSadece n�fus s�tunlu veri �er�evesi:\n", v�3 ["n�fus"], sep="")
print ("\nSadece n�fus s�tunlu veri �er�evesi:\n", v�3.n�fus, sep="")
print ("\nN�fus ve alan s�tunlu veri �er�evesi:\n", v�3 [["n�fus", "alan"]], sep="")
print ("-"*79)
#------------------------------------------------------------------------------------------------------

print ("\nN�fusa g�re artan s�ral� veri �er�evesi:\n", v�3.sort_values (by="n�fus"), sep="")
print ("\nAlana g�re azalan s�ral� veri �er�evesi:\n", v�3.sort_values (by="alan", ascending=False), sep="")
print ("-"*79)
#------------------------------------------------------------------------------------------------------

ki�i = [0 for _ in range (len (alan))]
for i in range (len (alan)): ki�i [i] = �ehirler ["n�fus"] [i] / alan [i]

v�3.insert (loc=3, column='ki�i/km^2', value=ki�i)
print ("\nKm^2'deki ki�i say�s�na g�re artan s�ral� s�tun eklemeli veri �er�evesi:\n",
    v�3.sort_values (by="ki�i/km^2"), sep="")



"""��kt�:
>python p_32102b.py
�lke endeksli �ehirler veri �er�evesi:
                   ad     n�fus
�ngiltere      Londra   8615246
Almanya        Berlin   3562166
�spanya        Madrid   3165235
�talya           Roma   2874038
Fransa          Paris   2273305
Avusturya      Viyana   1805681
Romanya      Bu�arest   1803425
Almanya       Hamburg   1760433
Macaristan  Budape�te   1754000
Polonya       Var�ova   1740119
�spanya     Barselona   1602386
Almanya         M�nih   1493900
�talya         Milano   1350680
T�rkiye      �stanbul  14657321
T�rkiye        Ankara   5731256

Almanya'n�n veri �er�evesi:
              ad    n�fus
Almanya   Berlin  3562166
Almanya  Hamburg  1760433
Almanya    M�nih  1493900

Almanya ve T�rkiye'nin veri �er�evesi:
               ad     n�fus
Almanya    Berlin   3562166
Almanya   Hamburg   1760433
Almanya     M�nih   1493900
T�rkiye  �stanbul  14657321
T�rkiye    Ankara   5731256

N�fusu 2M'dan fazla �ehirlerin veri �er�evesi:
                 ad     n�fus
�ngiltere    Londra   8615246
Almanya      Berlin   3562166
�spanya      Madrid   3165235
�talya         Roma   2874038
Fransa        Paris   2273305
T�rkiye    �stanbul  14657321
T�rkiye      Ankara   5731256
-------------------------------------------------------------------------------

�lke endeksli toplam veriler:
ad       LondraBerlinMadridRomaParisViyanaBu�arestHambu...
n�fus                                             54189191
dtype: object

Veri �er�evesi n�fus toplam�: 54189191

�lke endeksli �ehirlerin ard���k eklemeli k�m�latif toplam�:
�ngiltere      8615246
Almanya       12177412
�spanya       15342647
�talya        18216685
Fransa        20489990
Avusturya     22295671
Romanya       24099096
Almanya       25859529
Macaristan    27613529
Polonya       29353648
�spanya       30956034
Almanya       32449934
�talya        33800614
T�rkiye       48457935
T�rkiye       54189191
Name: n�fus, dtype: int64
-------------------------------------------------------------------------------

N�fus=k�m�latif �ehir �er�evesi:
                   ad     n�fus
�ngiltere      Londra   8615246
Almanya        Berlin  12177412
�spanya        Madrid  15342647
�talya           Roma  18216685
Fransa          Paris  20489990
Avusturya      Viyana  22295671
Romanya      Bu�arest  24099096
Almanya       Hamburg  25859529
Macaristan  Budape�te  27613529
Polonya       Var�ova  29353648
�spanya     Barselona  30956034
Almanya         M�nih  32449934
�talya         Milano  33800614
T�rkiye      �stanbul  48457935
T�rkiye        Ankara  54189191

Eklemeli n�fus s�tunlu ve �lke endeksli veri �er�evesi:
                   ad     n�fus  eklemeliN�fus
�ngiltere      Londra   8615246        8615246
Almanya        Berlin   3562166       12177412
�spanya        Madrid   3165235       15342647
�talya           Roma   2874038       18216685
Fransa          Paris   2273305       20489990
Avusturya      Viyana   1805681       22295671
Romanya      Bu�arest   1803425       24099096
Almanya       Hamburg   1760433       25859529
Macaristan  Budape�te   1754000       27613529
Polonya       Var�ova   1740119       29353648
�spanya     Barselona   1602386       30956034
Almanya         M�nih   1493900       32449934
�talya         Milano   1350680       33800614
T�rkiye      �stanbul  14657321       48457935
T�rkiye        Ankara   5731256       54189191
-------------------------------------------------------------------------------

�ehir km^2 alan s�tunlu ve �ehir endeksli veri �er�evesi:
                 �lke     alan     n�fus
Londra      �ngiltere  1572.00   8615246
Berlin        Almanya   891.85   3562166
Madrid        �spanya   605.77   3165235
Roma           �talya  1285.00   2874038
Paris          Fransa   105.40   2273305
Viyana      Avusturya   414.60   1805681
Bu�arest      Romanya   228.00   1803425
Hamburg       Almanya   755.00   1760433
Budape�te  Macaristan   525.20   1754000
Var�ova       Polonya   517.00   1740119
Barselona     �spanya   101.90   1602386
M�nih         Almanya   310.40   1493900
Milano         �talya   181.80   1350680
�stanbul      T�rkiye  2314.00  14657321
Ankara        T�rkiye  3267.92   5731256

Sadece n�fus s�tunlu veri �er�evesi:
Londra        8615246
Berlin        3562166
Madrid        3165235
Roma          2874038
Paris         2273305
Viyana        1805681
Bu�arest      1803425
Hamburg       1760433
Budape�te     1754000
Var�ova       1740119
Barselona     1602386
M�nih         1493900
Milano        1350680
�stanbul     14657321
Ankara        5731256
Name: n�fus, dtype: int64

N�fus ve alan s�tunlu veri �er�evesi:
              n�fus     alan
Londra      8615246  1572.00
Berlin      3562166   891.85
Madrid      3165235   605.77
Roma        2874038  1285.00
Paris       2273305   105.40
Viyana      1805681   414.60
Bu�arest    1803425   228.00
Hamburg     1760433   755.00
Budape�te   1754000   525.20
Var�ova     1740119   517.00
Barselona   1602386   101.90
M�nih       1493900   310.40
Milano      1350680   181.80
�stanbul   14657321  2314.00
Ankara      5731256  3267.92
-------------------------------------------------------------------------------

N�fusa g�re artan s�ral� veri �er�evesi:
                 �lke     alan     n�fus
Milano         �talya   181.80   1350680
M�nih         Almanya   310.40   1493900
Barselona     �spanya   101.90   1602386
Var�ova       Polonya   517.00   1740119
Budape�te  Macaristan   525.20   1754000
Hamburg       Almanya   755.00   1760433
Bu�arest      Romanya   228.00   1803425
Viyana      Avusturya   414.60   1805681
Paris          Fransa   105.40   2273305
Roma           �talya  1285.00   2874038
Madrid        �spanya   605.77   3165235
Berlin        Almanya   891.85   3562166
Ankara        T�rkiye  3267.92   5731256
Londra      �ngiltere  1572.00   8615246
�stanbul      T�rkiye  2314.00  14657321

Alana g�re azalan s�ral� veri �er�evesi:
                 �lke     alan     n�fus
Ankara        T�rkiye  3267.92   5731256
�stanbul      T�rkiye  2314.00  14657321
Londra      �ngiltere  1572.00   8615246
Roma           �talya  1285.00   2874038
Berlin        Almanya   891.85   3562166
Hamburg       Almanya   755.00   1760433
Madrid        �spanya   605.77   3165235
Budape�te  Macaristan   525.20   1754000
Var�ova       Polonya   517.00   1740119
Viyana      Avusturya   414.60   1805681
M�nih         Almanya   310.40   1493900
Bu�arest      Romanya   228.00   1803425
Milano         �talya   181.80   1350680
Paris          Fransa   105.40   2273305
Barselona     �spanya   101.90   1602386
-------------------------------------------------------------------------------

Km^2'deki ki�i say�s�na g�re artan s�ral� s�tun eklemeli veri �er�evesi:
                 �lke     alan     n�fus     ki�i/km^2
Ankara        T�rkiye  3267.92   5731256   1753.793239
Roma           �talya  1285.00   2874038   2236.605447
Hamburg       Almanya   755.00   1760433   2331.699338
Budape�te  Macaristan   525.20   1754000   3339.680122
Var�ova       Polonya   517.00   1740119   3365.800774
Berlin        Almanya   891.85   3562166   3994.131300
Viyana      Avusturya   414.60   1805681   4355.236372
M�nih         Almanya   310.40   1493900   4812.822165
Madrid        �spanya   605.77   3165235   5225.143206
Londra      �ngiltere  1572.00   8615246   5480.436387
�stanbul      T�rkiye  2314.00  14657321   6334.192308
Milano         �talya   181.80   1350680   7429.482948
Bu�arest      Romanya   228.00   1803425   7909.758772
Barselona     �spanya   101.90   1602386  15725.083415
Paris          Fransa   105.40   2273305  21568.358634
"""