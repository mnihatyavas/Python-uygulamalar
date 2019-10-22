# coding:iso-8859-9 T�rk�e
# p_32102a.py: Ad, n�fus ve �lke i�erikli �ehirler veri �er�evesi index, reindex, rename �rne�i.

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
        "�spanya", "Almanya", "�Italya", "T�rkiye", "T�rkiye"] }

v�1 = pd.DataFrame (�ehirler)
print ("Pandas'la yarat�lan �EH�RLER DataFrame/Veri�er�evesi:\n", v�1, sep="")
print ("\n�ehirler tablolama �er�evesinin kolon adlar�: ", v�1.columns.values, sep="")
#---------------------------------------------------------------------------------------------

s�ralama = ["birinci","ikinci","���nc�","d�rd�nc�","be�inci",
    "alt�nc�","yedinci","sekizinci","dokuzuncu","onuncu",
    "onbirinci","onikinci","on���nc�","ond�rd�nc�","onbe�inci"]
v�2 = pd.DataFrame (�ehirler, index=s�ralama)
print ("\n�zel endeksli �ehirler �er�evesi:\n", v�2, sep="")
#---------------------------------------------------------------------------------------------

v�3 = v�2.reindex (index=s�ralama, columns=["n�fus", "ad", "�lke"])
print ("\nKolonlar� de�i�tirilen �zel endeksli �ehirler �er�evesi:\n", v�3, sep="")
#---------------------------------------------------------------------------------------------

print ("\nKolonlar� tekrar de�i�tirilen �zel endeksli �ehirler �er�evesi:\n",
    v�3.reindex (columns=["n�fus", "�lke", "ad"]), sep="")
#---------------------------------------------------------------------------------------------

v�4 = v�1.rename (columns={"ad":"Nume", "�lke":"Tara", "n�fus":"Populatie"}, inplace=False)
# inplace=False ==> v�1 de�i�medi...
print ("\nKolon adlar� Rumenceye de�i�tirilen �ehirler �er�evesi:\n", v�4, sep="")
#---------------------------------------------------------------------------------------------

print ("\n�lke endeksli �ehirler �er�evesi:\n", v�1.set_index ("�lke"), sep="") # inplace=True ile v�1 de�i�ir...
print ("\n�ehir endeksli �ehirler �er�evesi:\n", v�1.set_index ("ad"), sep="")
print ("\nN�fus endeksli �ehirler �er�evesi:\n", v�1.set_index ("n�fus"), sep="")
print ("\nTekrar �ehir endeksli �ehirler �er�evesi:\n", pd.DataFrame (�ehirler, columns=["n�fus", "�lke"], index=�ehirler["ad"]), sep="")



"""��kt�:
>python p_32102.py
Pandas'la yarat�lan �EH�RLER DataFrame/Veri�er�evesi:
           ad     n�fus        �lke
0      Londra   8615246   �ngiltere
1      Berlin   3562166     Almanya
2      Madrid   3165235     �spanya
3        Roma   2874038      �talya
4       Paris   2273305      Fransa
5      Viyana   1805681   Avusturya
6    Bu�arest   1803425     Romanya
7     Hamburg   1760433     Almanya
8   Budape�te   1754000  Macaristan
9     Var�ova   1740119     Polonya
10  Barselona   1602386     �spanya
11      M�nih   1493900     Almanya
12     Milano   1350680     �Italya
13   �stanbul  14657321     T�rkiye
14     Ankara   5731256     T�rkiye

�ehirler tablolama �er�evesinin kolon adlar�: ['ad' 'n�fus' '�lke']

�zel endeksli �ehirler �er�evesi:
                   ad     n�fus        �lke
birinci        Londra   8615246   �ngiltere
ikinci         Berlin   3562166     Almanya
���nc�         Madrid   3165235     �spanya
d�rd�nc�         Roma   2874038      �talya
be�inci         Paris   2273305      Fransa
alt�nc�        Viyana   1805681   Avusturya
yedinci      Bu�arest   1803425     Romanya
sekizinci     Hamburg   1760433     Almanya
dokuzuncu   Budape�te   1754000  Macaristan
onuncu        Var�ova   1740119     Polonya
onbirinci   Barselona   1602386     �spanya
onikinci        M�nih   1493900     Almanya
on���nc�       Milano   1350680     �Italya
ond�rd�nc�   �stanbul  14657321     T�rkiye
onbe�inci      Ankara   5731256     T�rkiye

Kolonlar� de�i�tirilen �zel endeksli �ehirler �er�evesi:
               n�fus         ad        �lke
birinci      8615246     Londra   �ngiltere
ikinci       3562166     Berlin     Almanya
���nc�       3165235     Madrid     �spanya
d�rd�nc�     2874038       Roma      �talya
be�inci      2273305      Paris      Fransa
alt�nc�      1805681     Viyana   Avusturya
yedinci      1803425   Bu�arest     Romanya
sekizinci    1760433    Hamburg     Almanya
dokuzuncu    1754000  Budape�te  Macaristan
onuncu       1740119    Var�ova     Polonya
onbirinci    1602386  Barselona     �spanya
onikinci     1493900      M�nih     Almanya
on���nc�     1350680     Milano     �Italya
ond�rd�nc�  14657321   �stanbul     T�rkiye
onbe�inci    5731256     Ankara     T�rkiye

Kolonlar� tekrar de�i�tirilen �zel endeksli �ehirler �er�evesi:
               n�fus        �lke         ad
birinci      8615246   �ngiltere     Londra
ikinci       3562166     Almanya     Berlin
���nc�       3165235     �spanya     Madrid
d�rd�nc�     2874038      �talya       Roma
be�inci      2273305      Fransa      Paris
alt�nc�      1805681   Avusturya     Viyana
yedinci      1803425     Romanya   Bu�arest
sekizinci    1760433     Almanya    Hamburg
dokuzuncu    1754000  Macaristan  Budape�te
onuncu       1740119     Polonya    Var�ova
onbirinci    1602386     �spanya  Barselona
onikinci     1493900     Almanya      M�nih
on���nc�     1350680     �Italya     Milano
ond�rd�nc�  14657321     T�rkiye   �stanbul
onbe�inci    5731256     T�rkiye     Ankara

Kolon adlar� Rumenceye de�i�tirilen �ehirler �er�evesi:
         Nume  Populatie        Tara
0      Londra    8615246   �ngiltere
1      Berlin    3562166     Almanya
2      Madrid    3165235     �spanya
3        Roma    2874038      �talya
4       Paris    2273305      Fransa
5      Viyana    1805681   Avusturya
6    Bu�arest    1803425     Romanya
7     Hamburg    1760433     Almanya
8   Budape�te    1754000  Macaristan
9     Var�ova    1740119     Polonya
10  Barselona    1602386     �spanya
11      M�nih    1493900     Almanya
12     Milano    1350680     �Italya
13   �stanbul   14657321     T�rkiye
14     Ankara    5731256     T�rkiye

�lke endeksli �ehirler �er�evesi:
                   ad     n�fus
�lke
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
�Italya        Milano   1350680
T�rkiye      �stanbul  14657321
T�rkiye        Ankara   5731256

�ehir endeksli �ehirler �er�evesi:
              n�fus        �lke
ad
Londra      8615246   �ngiltere
Berlin      3562166     Almanya
Madrid      3165235     �spanya
Roma        2874038      �talya
Paris       2273305      Fransa
Viyana      1805681   Avusturya
Bu�arest    1803425     Romanya
Hamburg     1760433     Almanya
Budape�te   1754000  Macaristan
Var�ova     1740119     Polonya
Barselona   1602386     �spanya
M�nih       1493900     Almanya
Milano      1350680     �Italya
�stanbul   14657321     T�rkiye
Ankara      5731256     T�rkiye

N�fus endeksli �ehirler �er�evesi:
                 ad        �lke
n�fus
8615246      Londra   �ngiltere
3562166      Berlin     Almanya
3165235      Madrid     �spanya
2874038        Roma      �talya
2273305       Paris      Fransa
1805681      Viyana   Avusturya
1803425    Bu�arest     Romanya
1760433     Hamburg     Almanya
1754000   Budape�te  Macaristan
1740119     Var�ova     Polonya
1602386   Barselona     �spanya
1493900       M�nih     Almanya
1350680      Milano     �Italya
14657321   �stanbul     T�rkiye
5731256      Ankara     T�rkiye

Tekrar �ehir endeksli �ehirler �er�evesi:
              n�fus        �lke
Londra      8615246   �ngiltere
Berlin      3562166     Almanya
Madrid      3165235     �spanya
Roma        2874038      �talya
Paris       2273305      Fransa
Viyana      1805681   Avusturya
Bu�arest    1803425     Romanya
Hamburg     1760433     Almanya
Budape�te   1754000  Macaristan
Var�ova     1740119     Polonya
Barselona   1602386     �spanya
M�nih       1493900     Almanya
Milano      1350680     �Italya
�stanbul   14657321     T�rkiye
Ankara      5731256     T�rkiye
"""