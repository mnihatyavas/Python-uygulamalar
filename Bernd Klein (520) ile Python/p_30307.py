# coding:iso-8859-9 Türkçe
# p_30307.py: Bazı dünya şehirlerinde zaman farklarını dosyadan okuma yazma gösterme örneği.

import numpy as np
import pickle

satırlar = open ("p_30307x.txt").readlines()
print ("Düzensiz yan-yana p_30307x.txt dosya listesi:", satırlar)

şehirler = []
print ("\nŞehirler ve gün-saat:dakika zaman farkları:\n", "-"*43, sep="")
for satır in satırlar:
    şehir, gün, saat, dakika = satır.split (",")
    print ("{}==>{}->{:d}:{:d}" .format (şehir [1:-1], gün [2:-1], int (saat), int (dakika)) )
    şehirler.append (" ".join ((şehir, gün, str (saat), str (dakika)) ))

dosya = open ("şehirlerdeZaman.turşu", "bw+")
pickle.dump (şehirler, dosya) # Okunamaz dosya olarak kaydet...
dosya.close()

print ("\nşehirlerdeZaman.turşu dosyası içerikleri:\n", "-"*41, sep="")
dosya = open ("şehirlerdeZaman.turşu", "br")
liste = pickle.load (dosya) # Okunabilir kayıtlar olarak al...
liste1 = []
for satır in liste:
    şehir, gün, saat, dakika = satır.split ("  ")
    liste1 +=[tuple ((şehir [1:-1], gün [1:-1], (saat, dakika [:-1])))]
print (liste1)

tip = [('şehir', "U15"), ('gün', "U10"), ("zaman", [('saat', int), ('dakika', int)] ) ]
şehirZamanları = np.array (liste1, dtype=tip)

print ("\nBazı dünya şehirlerindeki zaman farkları listesi yan-yana:\n", "-"*58, "\n", şehirZamanları, sep="")
print ("\nBazı dünya şehirleri listesi:\n", şehirZamanları ["şehir"], sep="")
print ("\nBazı dünya zaman farkları listesi:\n", şehirZamanları ["zaman"], sep="")

x = şehirZamanları [27]
print ("\n28.şehir ve zaman farkı: ", x[0], " / ", x [1], " = ", x [2] [0], ":", x [2] [1], sep="")

print ("\nBazı dünya şehirlerindeki zaman farklarının alt-alta düzenli listesi:\n", "-"*69,
    "\nNo Şehir        Gün       St:Dk\n", "-"*31, sep="")
for i in range (len (şehirZamanları)):
    print ("{:2d} {:12s} {:9s} {:02d}:{:02d}" .format ((i+1), şehirZamanları [i] [0], şehirZamanları [i] [1], şehirZamanları [i] [2] [0], şehirZamanları [i] [2] [1]))
print ("-"*31)



"""Çıktı:
>python p_30307.py
Düzensiz yan-yana p_30307x.txt dosya listesi: ["'Amsterdam', 'Pazar', 8, 52\n",
"'Anchorage', 'Cumartesi', 23, 52\n", "'Ankara', 'Pazar', 10, 52\n", "'Athens',
'Pazar', 9, 52\n", "'Atlanta', 'Pazar', 2, 52\n", "'Auckland', 'Pazar', 20, 52\n
", "'Barcelona', 'Pazar', 8, 52\n", "'Beirut', 'Pazar', 9, 52\n", "'Berlin', 'Pa
zar', 8, 52\n", "'Boston', 'Pazar', 2, 52\n", "'Brasilia', 'Pazar', 5, 52\n", "'
Brussels', 'Pazar', 8, 52\n", "'Bucharest', 'Pazar', 9, 52\n", "'Budapest', 'Paz
ar', 8, 52\n", "'Cairo', 'Pazar', 9, 52\n", "'Calgary', 'Pazar', 1, 52\n", "'Cap
eTown', 'Pazar', 9, 52\n", "'Casablanca', 'Pazar', 7, 52\n", "'Chicago', 'Pazar'
, 1, 52\n", "'Columbus', 'Pazar', 2, 52\n", "'Copenhagen', 'Pazar', 8, 52\n", "'
Dallas', 'Pazar', 1, 52\n", "'Denver', 'Pazar', 1, 52\n", "'Detroit', 'Pazar', 2
, 52\n", "'Dubai', 'Pazar', 11, 52\n", "'Dublin', 'Pazar', 7, 52\n", "'Edmonton'
, 'Pazar', 1, 52\n", "'Frankfurt', 'Pazar', 8, 52\n", "'Halifax', 'Pazar', 3, 52
\n", "'Helsinki', 'Pazar', 9, 52\n", "'Toronto', 'Pazar', 2, 52\n", "'Vancouver'
, 'Pazar', 0, 52\n", "'Vienna', 'Pazar', 8, 52\n", "'Warsaw', 'Pazar', 8, 52\n",
 "'WashingtonDC', 'Pazar', 2, 52\n", "'Winnipeg', 'Pazar', 1, 52\n", "'Zurich',
'Pazar', 8, 52\n"]

Şehirler ve gün-saat:dakika zaman farkları:
-------------------------------------------
Amsterdam==>Pazar->8:52
Anchorage==>Cumartesi->23:52
Ankara==>Pazar->10:52
Athens==>Pazar->9:52
Atlanta==>Pazar->2:52
Auckland==>Pazar->20:52
Barcelona==>Pazar->8:52
Beirut==>Pazar->9:52
Berlin==>Pazar->8:52
Boston==>Pazar->2:52
Brasilia==>Pazar->5:52
Brussels==>Pazar->8:52
Bucharest==>Pazar->9:52
Budapest==>Pazar->8:52
Cairo==>Pazar->9:52
Calgary==>Pazar->1:52
CapeTown==>Pazar->9:52
Casablanca==>Pazar->7:52
Chicago==>Pazar->1:52
Columbus==>Pazar->2:52
Copenhagen==>Pazar->8:52
Dallas==>Pazar->1:52
Denver==>Pazar->1:52
Detroit==>Pazar->2:52
Dubai==>Pazar->11:52
Dublin==>Pazar->7:52
Edmonton==>Pazar->1:52
Frankfurt==>Pazar->8:52
Halifax==>Pazar->3:52
Helsinki==>Pazar->9:52
Toronto==>Pazar->2:52
Vancouver==>Pazar->0:52
Vienna==>Pazar->8:52
Warsaw==>Pazar->8:52
WashingtonDC==>Pazar->2:52
Winnipeg==>Pazar->1:52
Zurich==>Pazar->8:52

şehirlerdeZaman.turşu dosyası içerikleri:
-----------------------------------------
[('Amsterdam', 'Pazar', ('8', '52')), ('Anchorage', 'Cumartesi', ('23', '52')),
('Ankara', 'Pazar', ('10', '52')), ('Athens', 'Pazar', ('9', '52')), ('Atlanta',
 'Pazar', ('2', '52')), ('Auckland', 'Pazar', ('20', '52')), ('Barcelona', 'Paza
r', ('8', '52')), ('Beirut', 'Pazar', ('9', '52')), ('Berlin', 'Pazar', ('8', '5
2')), ('Boston', 'Pazar', ('2', '52')), ('Brasilia', 'Pazar', ('5', '52')), ('Br
ussels', 'Pazar', ('8', '52')), ('Bucharest', 'Pazar', ('9', '52')), ('Budapest'
, 'Pazar', ('8', '52')), ('Cairo', 'Pazar', ('9', '52')), ('Calgary', 'Pazar', (
'1', '52')), ('CapeTown', 'Pazar', ('9', '52')), ('Casablanca', 'Pazar', ('7', '
52')), ('Chicago', 'Pazar', ('1', '52')), ('Columbus', 'Pazar', ('2', '52')), ('
Copenhagen', 'Pazar', ('8', '52')), ('Dallas', 'Pazar', ('1', '52')), ('Denver',
 'Pazar', ('1', '52')), ('Detroit', 'Pazar', ('2', '52')), ('Dubai', 'Pazar', ('
11', '52')), ('Dublin', 'Pazar', ('7', '52')), ('Edmonton', 'Pazar', ('1', '52')
), ('Frankfurt', 'Pazar', ('8', '52')), ('Halifax', 'Pazar', ('3', '52')), ('Hel
sinki', 'Pazar', ('9', '52')), ('Toronto', 'Pazar', ('2', '52')), ('Vancouver',
'Pazar', ('0', '52')), ('Vienna', 'Pazar', ('8', '52')), ('Warsaw', 'Pazar', ('8
', '52')), ('WashingtonDC', 'Pazar', ('2', '52')), ('Winnipeg', 'Pazar', ('1', '
52')), ('Zurich', 'Pazar', ('8', '52'))]

Bazı dünya şehirlerindeki zaman farkları listesi yan-yana:
----------------------------------------------------------
[('Amsterdam', 'Pazar', ( 8, 52)) ('Anchorage', 'Cumartesi', (23, 52))
 ('Ankara', 'Pazar', (10, 52)) ('Athens', 'Pazar', ( 9, 52))
 ('Atlanta', 'Pazar', ( 2, 52)) ('Auckland', 'Pazar', (20, 52))
 ('Barcelona', 'Pazar', ( 8, 52)) ('Beirut', 'Pazar', ( 9, 52))
 ('Berlin', 'Pazar', ( 8, 52)) ('Boston', 'Pazar', ( 2, 52))
 ('Brasilia', 'Pazar', ( 5, 52)) ('Brussels', 'Pazar', ( 8, 52))
 ('Bucharest', 'Pazar', ( 9, 52)) ('Budapest', 'Pazar', ( 8, 52))
 ('Cairo', 'Pazar', ( 9, 52)) ('Calgary', 'Pazar', ( 1, 52))
 ('CapeTown', 'Pazar', ( 9, 52)) ('Casablanca', 'Pazar', ( 7, 52))
 ('Chicago', 'Pazar', ( 1, 52)) ('Columbus', 'Pazar', ( 2, 52))
 ('Copenhagen', 'Pazar', ( 8, 52)) ('Dallas', 'Pazar', ( 1, 52))
 ('Denver', 'Pazar', ( 1, 52)) ('Detroit', 'Pazar', ( 2, 52))
 ('Dubai', 'Pazar', (11, 52)) ('Dublin', 'Pazar', ( 7, 52))
 ('Edmonton', 'Pazar', ( 1, 52)) ('Frankfurt', 'Pazar', ( 8, 52))
 ('Halifax', 'Pazar', ( 3, 52)) ('Helsinki', 'Pazar', ( 9, 52))
 ('Toronto', 'Pazar', ( 2, 52)) ('Vancouver', 'Pazar', ( 0, 52))
 ('Vienna', 'Pazar', ( 8, 52)) ('Warsaw', 'Pazar', ( 8, 52))
 ('WashingtonDC', 'Pazar', ( 2, 52)) ('Winnipeg', 'Pazar', ( 1, 52))
 ('Zurich', 'Pazar', ( 8, 52))]

Bazı dünya şehirleri listesi:
['Amsterdam' 'Anchorage' 'Ankara' 'Athens' 'Atlanta' 'Auckland'
 'Barcelona' 'Beirut' 'Berlin' 'Boston' 'Brasilia' 'Brussels' 'Bucharest'
 'Budapest' 'Cairo' 'Calgary' 'CapeTown' 'Casablanca' 'Chicago' 'Columbus'
 'Copenhagen' 'Dallas' 'Denver' 'Detroit' 'Dubai' 'Dublin' 'Edmonton'
 'Frankfurt' 'Halifax' 'Helsinki' 'Toronto' 'Vancouver' 'Vienna' 'Warsaw'
 'WashingtonDC' 'Winnipeg' 'Zurich']

Bazı dünya zaman farkları listesi:
[( 8, 52) (23, 52) (10, 52) ( 9, 52) ( 2, 52) (20, 52) ( 8, 52) ( 9, 52)
 ( 8, 52) ( 2, 52) ( 5, 52) ( 8, 52) ( 9, 52) ( 8, 52) ( 9, 52) ( 1, 52)
 ( 9, 52) ( 7, 52) ( 1, 52) ( 2, 52) ( 8, 52) ( 1, 52) ( 1, 52) ( 2, 52)
 (11, 52) ( 7, 52) ( 1, 52) ( 8, 52) ( 3, 52) ( 9, 52) ( 2, 52) ( 0, 52)
 ( 8, 52) ( 8, 52) ( 2, 52) ( 1, 52) ( 8, 52)]

28.şehir ve zaman farkı: Frankfurt / Pazar = 8:52

Bazı dünya şehirlerindeki zaman farklarının alt-alta düzenli listesi:
---------------------------------------------------------------------
No Şehir        Gün       St:Dk
-------------------------------
 1 Amsterdam    Pazar     08:52
 2 Anchorage    Cumartesi 23:52
 3 Ankara       Pazar     10:52
 4 Athens       Pazar     09:52
 5 Atlanta      Pazar     02:52
 6 Auckland     Pazar     20:52
 7 Barcelona    Pazar     08:52
 8 Beirut       Pazar     09:52
 9 Berlin       Pazar     08:52
10 Boston       Pazar     02:52
11 Brasilia     Pazar     05:52
12 Brussels     Pazar     08:52
13 Bucharest    Pazar     09:52
14 Budapest     Pazar     08:52
15 Cairo        Pazar     09:52
16 Calgary      Pazar     01:52
17 CapeTown     Pazar     09:52
18 Casablanca   Pazar     07:52
19 Chicago      Pazar     01:52
20 Columbus     Pazar     02:52
21 Copenhagen   Pazar     08:52
22 Dallas       Pazar     01:52
23 Denver       Pazar     01:52
24 Detroit      Pazar     02:52
25 Dubai        Pazar     11:52
26 Dublin       Pazar     07:52
27 Edmonton     Pazar     01:52
28 Frankfurt    Pazar     08:52
29 Halifax      Pazar     03:52
30 Helsinki     Pazar     09:52
31 Toronto      Pazar     02:52
32 Vancouver    Pazar     00:52
33 Vienna       Pazar     08:52
34 Warsaw       Pazar     08:52
35 WashingtonDC Pazar     02:52
36 Winnipeg     Pazar     01:52
37 Zurich       Pazar     08:52
-------------------------------
"""