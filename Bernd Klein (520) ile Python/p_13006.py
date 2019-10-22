# coding:iso-8859-9 Türkçe
# p_13006.py: Bir XML html dosyasından film gruplarını re.search'le arayıp dökme örneği.

import re

dosya = open ("p_13006x.xml")
i = 1
print ("\nVizyondaki filimleri gururla takdirlerinize sunuyoruz==>\nFilm No:", i, "\n", "-"*40, sep="")
for satır in dosya:
    sonuç = re.search (r"<([a-z]+)>(.*)</\1>", satır)
    try: print (sonuç.group (1) + ": " + sonuç.group (2) )
    except: continue
    if (sonuç.group (1) == "aciklama" and i < 5):
        i +=1
        print ("\nFilm No:", i, "\n", "-"*40, sep="")

"""Çıktı:
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