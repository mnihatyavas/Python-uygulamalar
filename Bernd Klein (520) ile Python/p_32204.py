#coding:iso-8859-9 Türkçe
# p_32204.py: Veri-çerçevesi yaygın-sayfaya kolon ekleme ve süzgeçli çıktı alma örneği.

import pandas as pd

şehirler = pd.read_csv ('p_32204x.txt', sep=" ", header=0, encoding="iso-8859-9",
    names=["şehir", "alan", "erkek", "kadın"], index_col=0)
# encoding="ISO-8859-1", veya varsayılı encoding="utf-8"

print ("Şehir alanları ve erkek-kadın nüfusu veri çerçevesi:\n", şehirler, sep="")
print ("-"*60)
#-----------------------------------------------------------------------------------------------------

şehirler.insert (loc=len (şehirler.columns), column='nüfus',
    value=şehirler['kadın'] + şehirler['erkek'])
print ("\nSona nüfus kolonu ekli veri çerçevesi:\n", şehirler, sep="")
print ("-"*70)
#-----------------------------------------------------------------------------------------------------

şehirler.insert (loc=len (şehirler.columns), column='yoğunluk',
    value=(şehirler ['nüfus'] / şehirler ['alan']).round (0) )
print ("\nSona yoğunluk kolonu ekli veri çerçevesi:\n", şehirler, sep="")
print ("-"*70)
#-----------------------------------------------------------------------------------------------------

print ("\nAlan 35B ve nüfus 10M'dan fazla şehirler:\n",
    şehirler.loc [(şehirler.alan > 35000) & (şehirler.nüfus > 10000000)], sep="")
print ("-"*70)
#-----------------------------------------------------------------------------------------------------

print ("\nAlan < 30B, nüfus < 5M ve yoğunluk < 500 olan şehirler:\n",
    şehirler.loc [(şehirler.alan < 30000) & (şehirler.nüfus < 5000000) & (şehirler.yoğunluk < 500)], sep="")
print ("-"*70)
#-----------------------------------------------------------------------------------------------------

print ("\nYoğunluk > 1000 olan şehirler:\n", şehirler.loc [şehirler.yoğunluk > 1000], sep="")



"""Çıktı:
>python p_32204.py
Şehir alanları ve erkek-kadın nüfusu veri çerçevesi:
                            alan    erkek    kadın
şehir
Baden-Wurttemberg       35751.65  5271000  5465000
Bayern                  70551.57  6103000  6366000
Berlin                    891.85  1660000  1736000
Brandenburg             29478.61  1267000  1293000
Bremen                    404.28   321000   342000
Hamburg                   755.16   849000   894000
Hessen                  21114.79  2983000  3109000
Mecklenburg-Vorpommern  23180.14   846000   861000
Niedersachsen           47624.20  3918000  4076000
Nordrhein-Westfalen     34085.29  8797000  9261000
Rheinland-Pfalz         19853.36  1990000  2069000
Saarland                 2568.70   510000   540000
Sachsen                 18415.51  2083000  2191000
Sachsen-Anhalt          20446.31  1206000  1264000
Schleswig-Holstein      15799.38  1385000  1448000
Thuringen               16172.10  1150000  1185000
------------------------------------------------------------

Sona nüfus kolonu ekli veri çerçevesi:
                            alan    erkek    kadın     nüfus
şehir
Baden-Wurttemberg       35751.65  5271000  5465000  10736000
Bayern                  70551.57  6103000  6366000  12469000
Berlin                    891.85  1660000  1736000   3396000
Brandenburg             29478.61  1267000  1293000   2560000
Bremen                    404.28   321000   342000    663000
Hamburg                   755.16   849000   894000   1743000
Hessen                  21114.79  2983000  3109000   6092000
Mecklenburg-Vorpommern  23180.14   846000   861000   1707000
Niedersachsen           47624.20  3918000  4076000   7994000
Nordrhein-Westfalen     34085.29  8797000  9261000  18058000
Rheinland-Pfalz         19853.36  1990000  2069000   4059000
Saarland                 2568.70   510000   540000   1050000
Sachsen                 18415.51  2083000  2191000   4274000
Sachsen-Anhalt          20446.31  1206000  1264000   2470000
Schleswig-Holstein      15799.38  1385000  1448000   2833000
Thuringen               16172.10  1150000  1185000   2335000
----------------------------------------------------------------------

Sona yoğunluk kolonu ekli veri çerçevesi:
                            alan    erkek    kadın     nüfus  yoğunluk
şehir
Baden-Wurttemberg       35751.65  5271000  5465000  10736000     300.0
Bayern                  70551.57  6103000  6366000  12469000     177.0
Berlin                    891.85  1660000  1736000   3396000    3808.0
Brandenburg             29478.61  1267000  1293000   2560000      87.0
Bremen                    404.28   321000   342000    663000    1640.0
Hamburg                   755.16   849000   894000   1743000    2308.0
Hessen                  21114.79  2983000  3109000   6092000     289.0
Mecklenburg-Vorpommern  23180.14   846000   861000   1707000      74.0
Niedersachsen           47624.20  3918000  4076000   7994000     168.0
Nordrhein-Westfalen     34085.29  8797000  9261000  18058000     530.0
Rheinland-Pfalz         19853.36  1990000  2069000   4059000     204.0
Saarland                 2568.70   510000   540000   1050000     409.0
Sachsen                 18415.51  2083000  2191000   4274000     232.0
Sachsen-Anhalt          20446.31  1206000  1264000   2470000     121.0
Schleswig-Holstein      15799.38  1385000  1448000   2833000     179.0
Thuringen               16172.10  1150000  1185000   2335000     144.0
----------------------------------------------------------------------

Alan 35B ve nüfus 10M'dan fazla şehirler:
                       alan    erkek    kadın     nüfus  yoğunluk
şehir
Baden-Wurttemberg  35751.65  5271000  5465000  10736000     300.0
Bayern             70551.57  6103000  6366000  12469000     177.0
----------------------------------------------------------------------

Alan < 30B, nüfus < 5M ve yoğunluk < 500 olan şehirler:
                            alan    erkek    kadın    nüfus  yoğunluk
şehir
Brandenburg             29478.61  1267000  1293000  2560000      87.0
Mecklenburg-Vorpommern  23180.14   846000   861000  1707000      74.0
Rheinland-Pfalz         19853.36  1990000  2069000  4059000     204.0
Saarland                 2568.70   510000   540000  1050000     409.0
Sachsen                 18415.51  2083000  2191000  4274000     232.0
Sachsen-Anhalt          20446.31  1206000  1264000  2470000     121.0
Schleswig-Holstein      15799.38  1385000  1448000  2833000     179.0
Thuringen               16172.10  1150000  1185000  2335000     144.0
----------------------------------------------------------------------

Yoğunluk > 1000 olan şehirler:
           alan    erkek    kadın    nüfus  yoğunluk
şehir
Berlin   891.85  1660000  1736000  3396000    3808.0
Bremen   404.28   321000   342000   663000    1640.0
Hamburg  755.16   849000   894000  1743000    2308.0
"""