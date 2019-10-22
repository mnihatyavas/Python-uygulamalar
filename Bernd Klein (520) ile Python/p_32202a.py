# coding:iso-8859-9 Türkçe
# p_32202a.py: Pandas'la dünya erkek ve kadın nüfuslarını okuma, çıkarma ve yazdırma örneği.

import pandas as pd

kolonAdları = ["Ülke"] + list (range (2002, 2013))
erkekNüfusu = pd.read_csv ("p_32202x1.txt", sep=",",
     header=None, index_col=0, names=kolonAdları)
toplamNüfus = pd.read_csv ("p_32202x2.txt", sep="\t",
    header=None, index_col=0, names=kolonAdları)
kadınNüfusu = toplamNüfus - erkekNüfusu
#kadınNüfusu.to_csv ("p_32202x3.txt", sep=",", header=0)

print ("Dünya kadın nüfusu veri çerçevesi:\n", kadınNüfusu, sep="")



"""Çıktı:
>python p_32202.py
Dünya kadın nüfusu veri çerçevesi:
                        2002       2003  ...       2011       2012
Ülke                                     ...
Australia          9887846.0    9999199  ...   11359807   11402769
Austria            4179743.0    4158169  ...    4308915    4324983
Belgium            5267437.0    5288959  ...    4996609    5622157
Canada                   NaN   15829173  ...   17101813   17379104
Czech Republic     5264218.0    5236563  ...    5363971    5347235
Denmark            2714208.0    2721084  ...    2804046    2813740
Finland            2657304.0    2661379  ...    2736860    2748733
France            30510073.0   30655533  ...   33598633   33723892
Germany           42165633.0   42191801  ...   41639177   41637080
Greece             5547887.0    5557795  ...    5709818    5699936
Hungary            5337873.0    5323906  ...    5241821    5226007
Iceland             143125.0     144184  ...     158446     159211
Ireland            1954407.0    1994513  ...    2301435    2312938
Italy             29406500.0   29554847  ...   31213168   31308292
Japan             65047000.0   65185000  ...   65730000   65615000
Korea             23655780.0   23799133  ...   24837101   24964884
Luxembourg          225230.0     227291  ...     257221     263033
Mexico            51143166.0   51765793  ...   55166362   59163070
Netherlands        8133318.0    8177101  ...    8412317    8447477
New Zealand        2005120.0    2037900  ...    2240560    2253000
Norway             2282132.0    2296145  ...    2459456    2486999
Poland            19871665.0   19711782  ...   19755664   19883870
Portugal           5343969.0    5377218  ...    5490336    5511961
Slovak Republic    2767030.0    2767855  ...    2793033    2772570
Spain             20629952.0   21163499  ...   23428062   23719209
Sweden             4500683.0    4513681  ...    4725326    4756021
Switzerland        3712121.0    3738824  ...    3992708    4032409
Turkey                   NaN   34753495  ...   36679806   37191315
United Kingdom    29753779.0   30331409  ...   31726030   32115485
United States    141943484.0  146817188  ...  157539944  158635141

[30 rows x 11 columns]
"""