# coding:iso-8859-9 T�rk�e
# p_32101.py: Pandas'la excel tablolar� DataFrame olu�turma �rne�i.

import pandas as pd

y�llar = range (2014, 2018)

ma�aza1 = pd.Series ([2409.14, 2941.01, 3496.83, 3119.55], index=y�llar)
ma�aza2 = pd.Series ([1203.45, 3441.62, 3007.83, 3619.53], index=y�llar)
ma�aza3 = pd.Series ([3412.12, 3491.16, 3457.19, 1963.10], index=y�llar)

print ("1.Ma�azan�n y�ll�k sat�� cirosu:\n", ma�aza1, sep="")
print ("\n2.Ma�azan�n y�ll�k sat�� cirosu:\n", ma�aza2, sep="")
print ("\n3.Ma�azan�n y�ll�k sat�� cirosu:\n", ma�aza3, sep="")
print ("-"*45)
#------------------------------------------------------------------------------------------------------

print ("\nHer �� ma�azan�n D�KEY y�ll�k sat�� cirosu:\n", pd.concat ([ma�aza1, ma�aza2, ma�aza3]), sep="") # axis=0

ma�azalar1= pd.concat ([ma�aza1, ma�aza2, ma�aza3], axis=1)
print ("\nHer �� ma�azan�n YATAY y�ll�k sat�� cirosu:\n", ma�azalar1, sep="")

ma�azalar1.columns = ["Ankara", "�stanbul", "�zmir"]
print ("\nHer �� �EH�R ma�azan�n YATAY y�ll�k sat�� cirosu:\n", ma�azalar1, sep="")
print ("-"*45)
#------------------------------------------------------------------------------------------------------

ma�aza1.name = "Bursa"
ma�aza2.name = "Bal�kesir"
ma�aza3.name = "Band�rma"
ma�azalar2 = pd.concat ([ma�aza1, ma�aza2, ma�aza3], axis=1)
print ("\nHer �� �EH�R ma�azan�n YATAY y�ll�k sat�� cirosu:\n", ma�azalar2, sep="")

print ("\nma�aza1'in veri tipi:", type (ma�aza1))
print ("ma�azalar1'in veri tipi:", type (ma�azalar1))



"""��kt�:
>python p_32101.py
1.Ma�azan�n y�ll�k sat�� cirosu:
2014    2409.14
2015    2941.01
2016    3496.83
2017    3119.55
dtype: float64

2.Ma�azan�n y�ll�k sat�� cirosu:
2014    1203.45
2015    3441.62
2016    3007.83
2017    3619.53
dtype: float64

3.Ma�azan�n y�ll�k sat�� cirosu:
2014    3412.12
2015    3491.16
2016    3457.19
2017    1963.10
dtype: float64
---------------------------------------------

Her �� ma�azan�n D�KEY y�ll�k sat�� cirosu:
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

Her �� ma�azan�n YATAY y�ll�k sat�� cirosu:
            0        1        2
2014  2409.14  1203.45  3412.12
2015  2941.01  3441.62  3491.16
2016  3496.83  3007.83  3457.19
2017  3119.55  3619.53  1963.10

Her �� �EH�R ma�azan�n YATAY y�ll�k sat�� cirosu:
       Ankara  �stanbul    �zmir
2014  2409.14   1203.45  3412.12
2015  2941.01   3441.62  3491.16
2016  3496.83   3007.83  3457.19
2017  3119.55   3619.53  1963.10
---------------------------------------------

Her �� �EH�R ma�azan�n YATAY y�ll�k sat�� cirosu:
        Bursa  Bal�kesir  Band�rma
2014  2409.14    1203.45   3412.12
2015  2941.01    3441.62   3491.16
2016  3496.83    3007.83   3457.19
2017  3119.55    3619.53   1963.10

ma�aza1'in veri tipi: <class 'pandas.core.series.Series'>
ma�azalar1'in veri tipi: <class 'pandas.core.frame.DataFrame'>
"""