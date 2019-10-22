# coding:iso-8859-9 Türkçe
# p_32102a.py: Ad, nüfus ve ülke içerikli şehirler veri çerçevesi index, reindex, rename örneği.

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
        "İspanya", "Almanya", "İItalya", "Türkiye", "Türkiye"] }

vç1 = pd.DataFrame (şehirler)
print ("Pandas'la yaratılan ŞEHİRLER DataFrame/VeriÇerçevesi:\n", vç1, sep="")
print ("\nŞehirler tablolama çerçevesinin kolon adları: ", vç1.columns.values, sep="")
#---------------------------------------------------------------------------------------------

sıralama = ["birinci","ikinci","üçüncü","dördüncü","beşinci",
    "altıncı","yedinci","sekizinci","dokuzuncu","onuncu",
    "onbirinci","onikinci","onüçüncü","ondördüncü","onbeşinci"]
vç2 = pd.DataFrame (şehirler, index=sıralama)
print ("\nÖzel endeksli şehirler çerçevesi:\n", vç2, sep="")
#---------------------------------------------------------------------------------------------

vç3 = vç2.reindex (index=sıralama, columns=["nüfus", "ad", "ülke"])
print ("\nKolonları değiştirilen özel endeksli şehirler çerçevesi:\n", vç3, sep="")
#---------------------------------------------------------------------------------------------

print ("\nKolonları tekrar değiştirilen özel endeksli şehirler çerçevesi:\n",
    vç3.reindex (columns=["nüfus", "ülke", "ad"]), sep="")
#---------------------------------------------------------------------------------------------

vç4 = vç1.rename (columns={"ad":"Nume", "ülke":"Tara", "nüfus":"Populatie"}, inplace=False)
# inplace=False ==> vç1 değişmedi...
print ("\nKolon adları Rumenceye değiştirilen şehirler çerçevesi:\n", vç4, sep="")
#---------------------------------------------------------------------------------------------

print ("\nÜlke endeksli şehirler çerçevesi:\n", vç1.set_index ("ülke"), sep="") # inplace=True ile vç1 değişir...
print ("\nŞehir endeksli şehirler çerçevesi:\n", vç1.set_index ("ad"), sep="")
print ("\nNüfus endeksli şehirler çerçevesi:\n", vç1.set_index ("nüfus"), sep="")
print ("\nTekrar şehir endeksli şehirler çerçevesi:\n", pd.DataFrame (şehirler, columns=["nüfus", "ülke"], index=şehirler["ad"]), sep="")



"""Çıktı:
>python p_32102.py
Pandas'la yaratılan ŞEHİRLER DataFrame/VeriÇerçevesi:
           ad     nüfus        ülke
0      Londra   8615246   İngiltere
1      Berlin   3562166     Almanya
2      Madrid   3165235     İspanya
3        Roma   2874038      İtalya
4       Paris   2273305      Fransa
5      Viyana   1805681   Avusturya
6    Buçarest   1803425     Romanya
7     Hamburg   1760433     Almanya
8   Budapeşte   1754000  Macaristan
9     Varşova   1740119     Polonya
10  Barselona   1602386     İspanya
11      Münih   1493900     Almanya
12     Milano   1350680     İItalya
13   İstanbul  14657321     Türkiye
14     Ankara   5731256     Türkiye

Şehirler tablolama çerçevesinin kolon adları: ['ad' 'nüfus' 'ülke']

Özel endeksli şehirler çerçevesi:
                   ad     nüfus        ülke
birinci        Londra   8615246   İngiltere
ikinci         Berlin   3562166     Almanya
üçüncü         Madrid   3165235     İspanya
dördüncü         Roma   2874038      İtalya
beşinci         Paris   2273305      Fransa
altıncı        Viyana   1805681   Avusturya
yedinci      Buçarest   1803425     Romanya
sekizinci     Hamburg   1760433     Almanya
dokuzuncu   Budapeşte   1754000  Macaristan
onuncu        Varşova   1740119     Polonya
onbirinci   Barselona   1602386     İspanya
onikinci        Münih   1493900     Almanya
onüçüncü       Milano   1350680     İItalya
ondördüncü   İstanbul  14657321     Türkiye
onbeşinci      Ankara   5731256     Türkiye

Kolonları değiştirilen özel endeksli şehirler çerçevesi:
               nüfus         ad        ülke
birinci      8615246     Londra   İngiltere
ikinci       3562166     Berlin     Almanya
üçüncü       3165235     Madrid     İspanya
dördüncü     2874038       Roma      İtalya
beşinci      2273305      Paris      Fransa
altıncı      1805681     Viyana   Avusturya
yedinci      1803425   Buçarest     Romanya
sekizinci    1760433    Hamburg     Almanya
dokuzuncu    1754000  Budapeşte  Macaristan
onuncu       1740119    Varşova     Polonya
onbirinci    1602386  Barselona     İspanya
onikinci     1493900      Münih     Almanya
onüçüncü     1350680     Milano     İItalya
ondördüncü  14657321   İstanbul     Türkiye
onbeşinci    5731256     Ankara     Türkiye

Kolonları tekrar değiştirilen özel endeksli şehirler çerçevesi:
               nüfus        ülke         ad
birinci      8615246   İngiltere     Londra
ikinci       3562166     Almanya     Berlin
üçüncü       3165235     İspanya     Madrid
dördüncü     2874038      İtalya       Roma
beşinci      2273305      Fransa      Paris
altıncı      1805681   Avusturya     Viyana
yedinci      1803425     Romanya   Buçarest
sekizinci    1760433     Almanya    Hamburg
dokuzuncu    1754000  Macaristan  Budapeşte
onuncu       1740119     Polonya    Varşova
onbirinci    1602386     İspanya  Barselona
onikinci     1493900     Almanya      Münih
onüçüncü     1350680     İItalya     Milano
ondördüncü  14657321     Türkiye   İstanbul
onbeşinci    5731256     Türkiye     Ankara

Kolon adları Rumenceye değiştirilen şehirler çerçevesi:
         Nume  Populatie        Tara
0      Londra    8615246   İngiltere
1      Berlin    3562166     Almanya
2      Madrid    3165235     İspanya
3        Roma    2874038      İtalya
4       Paris    2273305      Fransa
5      Viyana    1805681   Avusturya
6    Buçarest    1803425     Romanya
7     Hamburg    1760433     Almanya
8   Budapeşte    1754000  Macaristan
9     Varşova    1740119     Polonya
10  Barselona    1602386     İspanya
11      Münih    1493900     Almanya
12     Milano    1350680     İItalya
13   İstanbul   14657321     Türkiye
14     Ankara    5731256     Türkiye

Ülke endeksli şehirler çerçevesi:
                   ad     nüfus
ülke
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
İItalya        Milano   1350680
Türkiye      İstanbul  14657321
Türkiye        Ankara   5731256

Şehir endeksli şehirler çerçevesi:
              nüfus        ülke
ad
Londra      8615246   İngiltere
Berlin      3562166     Almanya
Madrid      3165235     İspanya
Roma        2874038      İtalya
Paris       2273305      Fransa
Viyana      1805681   Avusturya
Buçarest    1803425     Romanya
Hamburg     1760433     Almanya
Budapeşte   1754000  Macaristan
Varşova     1740119     Polonya
Barselona   1602386     İspanya
Münih       1493900     Almanya
Milano      1350680     İItalya
İstanbul   14657321     Türkiye
Ankara      5731256     Türkiye

Nüfus endeksli şehirler çerçevesi:
                 ad        ülke
nüfus
8615246      Londra   İngiltere
3562166      Berlin     Almanya
3165235      Madrid     İspanya
2874038        Roma      İtalya
2273305       Paris      Fransa
1805681      Viyana   Avusturya
1803425    Buçarest     Romanya
1760433     Hamburg     Almanya
1754000   Budapeşte  Macaristan
1740119     Varşova     Polonya
1602386   Barselona     İspanya
1493900       Münih     Almanya
1350680      Milano     İItalya
14657321   İstanbul     Türkiye
5731256      Ankara     Türkiye

Tekrar şehir endeksli şehirler çerçevesi:
              nüfus        ülke
Londra      8615246   İngiltere
Berlin      3562166     Almanya
Madrid      3165235     İspanya
Roma        2874038      İtalya
Paris       2273305      Fransa
Viyana      1805681   Avusturya
Buçarest    1803425     Romanya
Hamburg     1760433     Almanya
Budapeşte   1754000  Macaristan
Varşova     1740119     Polonya
Barselona   1602386     İspanya
Münih       1493900     Almanya
Milano      1350680     İItalya
İstanbul   14657321     Türkiye
Ankara      5731256     Türkiye
"""