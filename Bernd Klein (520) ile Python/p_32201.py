# coding:iso-8859-9 T�rk�e
# p_32201.py: Pandas'la veri dosyalar�n� okuma �rne�i.

import pandas as pd

dolarYuroOranlar� = pd.read_csv ("p_32201x.txt", sep="\t")
print ("Y�llara yayg�n Dolar/Yuro �evrim oranlar�:\n", dolarYuroOranlar�, sep="")

dolarYuroOranlar� = pd.read_csv ("p_32201x.txt", sep="\t", header=0,
    names=["Y�llar", "Ortalama", "End���k", "Eny�ksek", "��g�nleri"])
print ("\nY�llara yayg�n Dolar/Yuro �evrim oranlar�:\n", dolarYuroOranlar�, sep="")



"""��kt�:
>python p_32201.py
Y�llara yayg�n Dolar/Yuro �evrim oranlar�:
     Yil  Ortalama  Enaz DL/EU  Encok DL/EU  Mesai Gunleri
0   2016  0.901696    0.864379     0.959785            247
1   2015  0.901896    0.830358     0.947688            256
2   2014  0.753941    0.716692     0.823655            255
3   2013  0.753234    0.723903     0.783208            255
4   2012  0.778848    0.743273     0.827198            256
5   2011  0.719219    0.671953     0.775855            257
6   2010  0.755883    0.686672     0.837381            258
7   2009  0.718968    0.661376     0.796495            256
8   2008  0.683499    0.625391     0.802568            256
9   2007  0.730754    0.672314     0.775615            255
10  2006  0.797153    0.750131     0.845594            255
11  2005  0.805097    0.740357     0.857118            257
12  2004  0.804828    0.733514     0.847314            259
13  2003  0.885766    0.791766     0.963670            255
14  2002  1.060945    0.953562     1.165773            255
15  2001  1.117587    1.047669     1.192748            255
16  2000  1.085899    0.962649     1.211827            255
17  1999  0.939475    0.848176     0.998502            261

Y�llara yayg�n Dolar/Yuro �evrim oranlar�:
    Y�llar  Ortalama   End���k  Eny�ksek  ��g�nleri
0     2016  0.901696  0.864379  0.959785        247
1     2015  0.901896  0.830358  0.947688        256
2     2014  0.753941  0.716692  0.823655        255
3     2013  0.753234  0.723903  0.783208        255
4     2012  0.778848  0.743273  0.827198        256
5     2011  0.719219  0.671953  0.775855        257
6     2010  0.755883  0.686672  0.837381        258
7     2009  0.718968  0.661376  0.796495        256
8     2008  0.683499  0.625391  0.802568        256
9     2007  0.730754  0.672314  0.775615        255
10    2006  0.797153  0.750131  0.845594        255
11    2005  0.805097  0.740357  0.857118        257
12    2004  0.804828  0.733514  0.847314        259
13    2003  0.885766  0.791766  0.963670        255
14    2002  1.060945  0.953562  1.165773        255
15    2001  1.117587  1.047669  1.192748        255
16    2000  1.085899  0.962649  1.211827        255
17    1999  0.939475  0.848176  0.998502        261
"""