# coding:iso-8859-9 Türkçe
# p_32102b.py: Süzgeçleme, sütun ekleme ve artan-azalan sıralama örneği.

import pandas as pd

şehirler = {
    "ad": ["Londra", "Berlin", "Madrid", "Roma", "Paris",
        "Viyana", "Buçarest", "Hamburg", "Budapeşte", "Varşova",
        "Barselona", "Münih", "Milano", "İstanbul", "Ankara"],
    "nüfus": [8615246, 3562166, 3165235, 2874038, 2273305,
        1805681, 1803425, 1760433, 1754000, 1740119,
        1602386, 1493900, 1350680, 14657321, 5731256],
    "ülke": ["İngiltere", "Almanya", "İspanya", "İtalya", "Fransa",
        "Avusturya", "Romanya", "Almanya", "Macaristan", "Polonya",
        "İspanya", "Almanya", "İtalya", "Türkiye", "Türkiye"] }

vç1 = pd.DataFrame (şehirler, columns=["ad", "nüfus"], index=şehirler ["ülke"] )
print ("Ülke endeksli şehirler veri çerçevesi:\n", vç1, sep="")

# Satır süzgeci...
print ("\nAlmanya'nın veri çerçevesi:\n", vç1.loc ["Almanya"], sep="")
print ("\nAlmanya ve Türkiye'nin veri çerçevesi:\n", vç1.loc [["Almanya", "Türkiye"]], sep="")
print ("\nNüfusu 2M'dan fazla şehirlerin veri çerçevesi:\n", vç1.loc [vç1.nüfus >= 2000000], sep="")
print ("-"*79)
#------------------------------------------------------------------------------------------------------

print ("\nÜlke endeksli toplam veriler:\n", vç1.sum(), sep="")
print ("\nVeri çerçevesi nüfus toplamı:", vç1 ["nüfus"].sum() )
x = vç1 ["nüfus"].cumsum()
print ("\nÜlke endeksli şehirlerin ardışık eklemeli kümülatif toplamı:\n", x, sep="")
print ("-"*79)
#------------------------------------------------------------------------------------------------------

vç1 ["nüfus"] = x
print ("\nNüfus=kümülatif şehir çerçevesi:\n", vç1, sep="")

vç2 = pd.DataFrame (şehirler, columns=["ad", "nüfus", "eklemeliNüfus"], index=şehirler ["ülke"])
# eklemeliNüfus=NaN
vç2 ["eklemeliNüfus"] = x
print ("\nEklemeli nüfus sütunlu ve ülke endeksli veri çerçevesi:\n", vç2, sep="")
print ("-"*79)
#------------------------------------------------------------------------------------------------------

alan = [1572, 891.85, 605.77, 1285, 105.4, 414.6, 228, 755, 525.2, 517,
    101.9, 310.4, 181.8, 2314, 3267.92]
vç3 = pd.DataFrame (şehirler, columns=["ülke", "alan", "nüfus"], index=şehirler ["ad"])
# alan=NaN
vç3 ["alan"] = alan
print ("\nŞehir km^2 alan sütunlu ve şehir endeksli veri çerçevesi:\n", vç3, sep="")

# Sütun süzgeci...
#print ("\nSadece nüfus sütunlu veri çerçevesi:\n", vç3 ["nüfus"], sep="")
print ("\nSadece nüfus sütunlu veri çerçevesi:\n", vç3.nüfus, sep="")
print ("\nNüfus ve alan sütunlu veri çerçevesi:\n", vç3 [["nüfus", "alan"]], sep="")
print ("-"*79)
#------------------------------------------------------------------------------------------------------

print ("\nNüfusa göre artan sıralı veri çerçevesi:\n", vç3.sort_values (by="nüfus"), sep="")
print ("\nAlana göre azalan sıralı veri çerçevesi:\n", vç3.sort_values (by="alan", ascending=False), sep="")
print ("-"*79)
#------------------------------------------------------------------------------------------------------

kişi = [0 for _ in range (len (alan))]
for i in range (len (alan)): kişi [i] = şehirler ["nüfus"] [i] / alan [i]

vç3.insert (loc=3, column='kişi/km^2', value=kişi)
print ("\nKm^2'deki kişi sayısına göre artan sıralı sütun eklemeli veri çerçevesi:\n",
    vç3.sort_values (by="kişi/km^2"), sep="")



"""Çıktı:
>python p_32102b.py
Ülke endeksli şehirler veri çerçevesi:
                   ad     nüfus
İngiltere      Londra   8615246
Almanya        Berlin   3562166
İspanya        Madrid   3165235
İtalya           Roma   2874038
Fransa          Paris   2273305
Avusturya      Viyana   1805681
Romanya      Buçarest   1803425
Almanya       Hamburg   1760433
Macaristan  Budapeşte   1754000
Polonya       Varşova   1740119
İspanya     Barselona   1602386
Almanya         Münih   1493900
İtalya         Milano   1350680
Türkiye      İstanbul  14657321
Türkiye        Ankara   5731256

Almanya'nın veri çerçevesi:
              ad    nüfus
Almanya   Berlin  3562166
Almanya  Hamburg  1760433
Almanya    Münih  1493900

Almanya ve Türkiye'nin veri çerçevesi:
               ad     nüfus
Almanya    Berlin   3562166
Almanya   Hamburg   1760433
Almanya     Münih   1493900
Türkiye  İstanbul  14657321
Türkiye    Ankara   5731256

Nüfusu 2M'dan fazla şehirlerin veri çerçevesi:
                 ad     nüfus
İngiltere    Londra   8615246
Almanya      Berlin   3562166
İspanya      Madrid   3165235
İtalya         Roma   2874038
Fransa        Paris   2273305
Türkiye    İstanbul  14657321
Türkiye      Ankara   5731256
-------------------------------------------------------------------------------

Ülke endeksli toplam veriler:
ad       LondraBerlinMadridRomaParisViyanaBuçarestHambu...
nüfus                                             54189191
dtype: object

Veri çerçevesi nüfus toplamı: 54189191

Ülke endeksli şehirlerin ardışık eklemeli kümülatif toplamı:
İngiltere      8615246
Almanya       12177412
İspanya       15342647
İtalya        18216685
Fransa        20489990
Avusturya     22295671
Romanya       24099096
Almanya       25859529
Macaristan    27613529
Polonya       29353648
İspanya       30956034
Almanya       32449934
İtalya        33800614
Türkiye       48457935
Türkiye       54189191
Name: nüfus, dtype: int64
-------------------------------------------------------------------------------

Nüfus=kümülatif şehir çerçevesi:
                   ad     nüfus
İngiltere      Londra   8615246
Almanya        Berlin  12177412
İspanya        Madrid  15342647
İtalya           Roma  18216685
Fransa          Paris  20489990
Avusturya      Viyana  22295671
Romanya      Buçarest  24099096
Almanya       Hamburg  25859529
Macaristan  Budapeşte  27613529
Polonya       Varşova  29353648
İspanya     Barselona  30956034
Almanya         Münih  32449934
İtalya         Milano  33800614
Türkiye      İstanbul  48457935
Türkiye        Ankara  54189191

Eklemeli nüfus sütunlu ve ülke endeksli veri çerçevesi:
                   ad     nüfus  eklemeliNüfus
İngiltere      Londra   8615246        8615246
Almanya        Berlin   3562166       12177412
İspanya        Madrid   3165235       15342647
İtalya           Roma   2874038       18216685
Fransa          Paris   2273305       20489990
Avusturya      Viyana   1805681       22295671
Romanya      Buçarest   1803425       24099096
Almanya       Hamburg   1760433       25859529
Macaristan  Budapeşte   1754000       27613529
Polonya       Varşova   1740119       29353648
İspanya     Barselona   1602386       30956034
Almanya         Münih   1493900       32449934
İtalya         Milano   1350680       33800614
Türkiye      İstanbul  14657321       48457935
Türkiye        Ankara   5731256       54189191
-------------------------------------------------------------------------------

Şehir km^2 alan sütunlu ve şehir endeksli veri çerçevesi:
                 ülke     alan     nüfus
Londra      İngiltere  1572.00   8615246
Berlin        Almanya   891.85   3562166
Madrid        İspanya   605.77   3165235
Roma           İtalya  1285.00   2874038
Paris          Fransa   105.40   2273305
Viyana      Avusturya   414.60   1805681
Buçarest      Romanya   228.00   1803425
Hamburg       Almanya   755.00   1760433
Budapeşte  Macaristan   525.20   1754000
Varşova       Polonya   517.00   1740119
Barselona     İspanya   101.90   1602386
Münih         Almanya   310.40   1493900
Milano         İtalya   181.80   1350680
İstanbul      Türkiye  2314.00  14657321
Ankara        Türkiye  3267.92   5731256

Sadece nüfus sütunlu veri çerçevesi:
Londra        8615246
Berlin        3562166
Madrid        3165235
Roma          2874038
Paris         2273305
Viyana        1805681
Buçarest      1803425
Hamburg       1760433
Budapeşte     1754000
Varşova       1740119
Barselona     1602386
Münih         1493900
Milano        1350680
İstanbul     14657321
Ankara        5731256
Name: nüfus, dtype: int64

Nüfus ve alan sütunlu veri çerçevesi:
              nüfus     alan
Londra      8615246  1572.00
Berlin      3562166   891.85
Madrid      3165235   605.77
Roma        2874038  1285.00
Paris       2273305   105.40
Viyana      1805681   414.60
Buçarest    1803425   228.00
Hamburg     1760433   755.00
Budapeşte   1754000   525.20
Varşova     1740119   517.00
Barselona   1602386   101.90
Münih       1493900   310.40
Milano      1350680   181.80
İstanbul   14657321  2314.00
Ankara      5731256  3267.92
-------------------------------------------------------------------------------

Nüfusa göre artan sıralı veri çerçevesi:
                 ülke     alan     nüfus
Milano         İtalya   181.80   1350680
Münih         Almanya   310.40   1493900
Barselona     İspanya   101.90   1602386
Varşova       Polonya   517.00   1740119
Budapeşte  Macaristan   525.20   1754000
Hamburg       Almanya   755.00   1760433
Buçarest      Romanya   228.00   1803425
Viyana      Avusturya   414.60   1805681
Paris          Fransa   105.40   2273305
Roma           İtalya  1285.00   2874038
Madrid        İspanya   605.77   3165235
Berlin        Almanya   891.85   3562166
Ankara        Türkiye  3267.92   5731256
Londra      İngiltere  1572.00   8615246
İstanbul      Türkiye  2314.00  14657321

Alana göre azalan sıralı veri çerçevesi:
                 ülke     alan     nüfus
Ankara        Türkiye  3267.92   5731256
İstanbul      Türkiye  2314.00  14657321
Londra      İngiltere  1572.00   8615246
Roma           İtalya  1285.00   2874038
Berlin        Almanya   891.85   3562166
Hamburg       Almanya   755.00   1760433
Madrid        İspanya   605.77   3165235
Budapeşte  Macaristan   525.20   1754000
Varşova       Polonya   517.00   1740119
Viyana      Avusturya   414.60   1805681
Münih         Almanya   310.40   1493900
Buçarest      Romanya   228.00   1803425
Milano         İtalya   181.80   1350680
Paris          Fransa   105.40   2273305
Barselona     İspanya   101.90   1602386
-------------------------------------------------------------------------------

Km^2'deki kişi sayısına göre artan sıralı sütun eklemeli veri çerçevesi:
                 ülke     alan     nüfus     kişi/km^2
Ankara        Türkiye  3267.92   5731256   1753.793239
Roma           İtalya  1285.00   2874038   2236.605447
Hamburg       Almanya   755.00   1760433   2331.699338
Budapeşte  Macaristan   525.20   1754000   3339.680122
Varşova       Polonya   517.00   1740119   3365.800774
Berlin        Almanya   891.85   3562166   3994.131300
Viyana      Avusturya   414.60   1805681   4355.236372
Münih         Almanya   310.40   1493900   4812.822165
Madrid        İspanya   605.77   3165235   5225.143206
Londra      İngiltere  1572.00   8615246   5480.436387
İstanbul      Türkiye  2314.00  14657321   6334.192308
Milano         İtalya   181.80   1350680   7429.482948
Buçarest      Romanya   228.00   1803425   7909.758772
Barselona     İspanya   101.90   1602386  15725.083415
Paris          Fransa   105.40   2273305  21568.358634
"""