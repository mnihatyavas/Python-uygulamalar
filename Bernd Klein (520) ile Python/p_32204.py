#coding:iso-8859-9 T�rk�e
# p_32204.py: Veri-�er�evesi yayg�n-sayfaya kolon ekleme ve s�zge�li ��kt� alma �rne�i.

import pandas as pd

�ehirler = pd.read_csv ('p_32204x.txt', sep=" ", header=0, encoding="iso-8859-9",
    names=["�ehir", "alan", "erkek", "kad�n"], index_col=0)
# encoding="ISO-8859-1", veya varsay�l� encoding="utf-8"

print ("�ehir alanlar� ve erkek-kad�n n�fusu veri �er�evesi:\n", �ehirler, sep="")
print ("-"*60)
#-----------------------------------------------------------------------------------------------------

�ehirler.insert (loc=len (�ehirler.columns), column='n�fus',
    value=�ehirler['kad�n'] + �ehirler['erkek'])
print ("\nSona n�fus kolonu ekli veri �er�evesi:\n", �ehirler, sep="")
print ("-"*70)
#-----------------------------------------------------------------------------------------------------

�ehirler.insert (loc=len (�ehirler.columns), column='yo�unluk',
    value=(�ehirler ['n�fus'] / �ehirler ['alan']).round (0) )
print ("\nSona yo�unluk kolonu ekli veri �er�evesi:\n", �ehirler, sep="")
print ("-"*70)
#-----------------------------------------------------------------------------------------------------

print ("\nAlan 35B ve n�fus 10M'dan fazla �ehirler:\n",
    �ehirler.loc [(�ehirler.alan > 35000) & (�ehirler.n�fus > 10000000)], sep="")
print ("-"*70)
#-----------------------------------------------------------------------------------------------------

print ("\nAlan < 30B, n�fus < 5M ve yo�unluk < 500 olan �ehirler:\n",
    �ehirler.loc [(�ehirler.alan < 30000) & (�ehirler.n�fus < 5000000) & (�ehirler.yo�unluk < 500)], sep="")
print ("-"*70)
#-----------------------------------------------------------------------------------------------------

print ("\nYo�unluk > 1000 olan �ehirler:\n", �ehirler.loc [�ehirler.yo�unluk > 1000], sep="")



"""��kt�:
>python p_32204.py
�ehir alanlar� ve erkek-kad�n n�fusu veri �er�evesi:
                            alan    erkek    kad�n
�ehir
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

Sona n�fus kolonu ekli veri �er�evesi:
                            alan    erkek    kad�n     n�fus
�ehir
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

Sona yo�unluk kolonu ekli veri �er�evesi:
                            alan    erkek    kad�n     n�fus  yo�unluk
�ehir
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

Alan 35B ve n�fus 10M'dan fazla �ehirler:
                       alan    erkek    kad�n     n�fus  yo�unluk
�ehir
Baden-Wurttemberg  35751.65  5271000  5465000  10736000     300.0
Bayern             70551.57  6103000  6366000  12469000     177.0
----------------------------------------------------------------------

Alan < 30B, n�fus < 5M ve yo�unluk < 500 olan �ehirler:
                            alan    erkek    kad�n    n�fus  yo�unluk
�ehir
Brandenburg             29478.61  1267000  1293000  2560000      87.0
Mecklenburg-Vorpommern  23180.14   846000   861000  1707000      74.0
Rheinland-Pfalz         19853.36  1990000  2069000  4059000     204.0
Saarland                 2568.70   510000   540000  1050000     409.0
Sachsen                 18415.51  2083000  2191000  4274000     232.0
Sachsen-Anhalt          20446.31  1206000  1264000  2470000     121.0
Schleswig-Holstein      15799.38  1385000  1448000  2833000     179.0
Thuringen               16172.10  1150000  1185000  2335000     144.0
----------------------------------------------------------------------

Yo�unluk > 1000 olan �ehirler:
           alan    erkek    kad�n    n�fus  yo�unluk
�ehir
Berlin   891.85  1660000  1736000  3396000    3808.0
Bremen   404.28   321000   342000   663000    1640.0
Hamburg  755.16   849000   894000  1743000    2308.0
"""