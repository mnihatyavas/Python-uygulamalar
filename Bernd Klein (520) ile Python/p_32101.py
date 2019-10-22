# coding:iso-8859-9 Türkçe
# p_32101.py: Pandas'la excel tabloları DataFrame oluşturma örneği.

import pandas as pd

yıllar = range (2014, 2018)

mağaza1 = pd.Series ([2409.14, 2941.01, 3496.83, 3119.55], index=yıllar)
mağaza2 = pd.Series ([1203.45, 3441.62, 3007.83, 3619.53], index=yıllar)
mağaza3 = pd.Series ([3412.12, 3491.16, 3457.19, 1963.10], index=yıllar)

print ("1.Mağazanın yıllık satış cirosu:\n", mağaza1, sep="")
print ("\n2.Mağazanın yıllık satış cirosu:\n", mağaza2, sep="")
print ("\n3.Mağazanın yıllık satış cirosu:\n", mağaza3, sep="")
print ("-"*45)
#------------------------------------------------------------------------------------------------------

print ("\nHer üç mağazanın DİKEY yıllık satış cirosu:\n", pd.concat ([mağaza1, mağaza2, mağaza3]), sep="") # axis=0

mağazalar1= pd.concat ([mağaza1, mağaza2, mağaza3], axis=1)
print ("\nHer üç mağazanın YATAY yıllık satış cirosu:\n", mağazalar1, sep="")

mağazalar1.columns = ["Ankara", "İstanbul", "İzmir"]
print ("\nHer üç ŞEHİR mağazanın YATAY yıllık satış cirosu:\n", mağazalar1, sep="")
print ("-"*45)
#------------------------------------------------------------------------------------------------------

mağaza1.name = "Bursa"
mağaza2.name = "Balıkesir"
mağaza3.name = "Bandırma"
mağazalar2 = pd.concat ([mağaza1, mağaza2, mağaza3], axis=1)
print ("\nHer üç ŞEHİR mağazanın YATAY yıllık satış cirosu:\n", mağazalar2, sep="")

print ("\nmağaza1'in veri tipi:", type (mağaza1))
print ("mağazalar1'in veri tipi:", type (mağazalar1))



"""Çıktı:
>python p_32101.py
1.Mağazanın yıllık satış cirosu:
2014    2409.14
2015    2941.01
2016    3496.83
2017    3119.55
dtype: float64

2.Mağazanın yıllık satış cirosu:
2014    1203.45
2015    3441.62
2016    3007.83
2017    3619.53
dtype: float64

3.Mağazanın yıllık satış cirosu:
2014    3412.12
2015    3491.16
2016    3457.19
2017    1963.10
dtype: float64
---------------------------------------------

Her üç mağazanın DİKEY yıllık satış cirosu:
2014    2409.14
2015    2941.01
2016    3496.83
2017    3119.55
2014    1203.45
2015    3441.62
2016    3007.83
2017    3619.53
2014    3412.12
2015    3491.16
2016    3457.19
2017    1963.10
dtype: float64

Her üç mağazanın YATAY yıllık satış cirosu:
            0        1        2
2014  2409.14  1203.45  3412.12
2015  2941.01  3441.62  3491.16
2016  3496.83  3007.83  3457.19
2017  3119.55  3619.53  1963.10

Her üç ŞEHİR mağazanın YATAY yıllık satış cirosu:
       Ankara  İstanbul    İzmir
2014  2409.14   1203.45  3412.12
2015  2941.01   3441.62  3491.16
2016  3496.83   3007.83  3457.19
2017  3119.55   3619.53  1963.10
---------------------------------------------

Her üç ŞEHİR mağazanın YATAY yıllık satış cirosu:
        Bursa  Balıkesir  Bandırma
2014  2409.14    1203.45   3412.12
2015  2941.01    3441.62   3491.16
2016  3496.83    3007.83   3457.19
2017  3119.55    3619.53   1963.10

mağaza1'in veri tipi: <class 'pandas.core.series.Series'>
mağazalar1'in veri tipi: <class 'pandas.core.frame.DataFrame'>
"""