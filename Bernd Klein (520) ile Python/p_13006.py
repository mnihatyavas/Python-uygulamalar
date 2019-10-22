# coding:iso-8859-9 T�rk�e
# p_13006.py: Bir XML html dosyas�ndan film gruplar�n� re.search'le aray�p d�kme �rne�i.

import re

dosya = open ("p_13006x.xml")
i = 1
print ("\nVizyondaki filimleri gururla takdirlerinize sunuyoruz==>\nFilm No:", i, "\n", "-"*40, sep="")
for sat�r in dosya:
    sonu� = re.search (r"<([a-z]+)>(.*)</\1>", sat�r)
    try: print (sonu�.group (1) + ": " + sonu�.group (2) )
    except: continue
    if (sonu�.group (1) == "aciklama" and i < 5):
        i +=1
        print ("\nFilm No:", i, "\n", "-"*40, sep="")

"""��kt�:
>python p_13006.py

Vizyondaki filimleri takdirlerinize gururla sunuyoruz==>
Film No:1
----------------------------------------
katagori: Savas, Heyecan
bicim: DVD
yil: 2003
itibar: PG
yildizlar: 10
aciklama: Amerika-Japonya savasi hakkinda

Film No:2
----------------------------------------
katagori: Canlandirma, Bilim Kurgu
bicim: DVD
yil: 1989
itibar: R
yildizlar: 8
aciklama: Bir bilim kurgu filmi

Film No:3
----------------------------------------
katagori: Canlandirma, Aksiyon
bicim: DVD
bolumler: 4
itibar: PG
yildizlar: 10
aciklama: Korkmaya kendinizi hazirlayin!

Film No:4
----------------------------------------
katagori: Komedi
bicim: VHS
itibar: PG
yildizlar: 2
aciklama: Izlemesi sikici

Film No:5
----------------------------------------
katagori: Bilim Kurgu
bicim: VHS
itibar: PG
yildizlar: 8
aciklama: New York'ta canavarlar
"""