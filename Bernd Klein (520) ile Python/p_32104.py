# coding:iso-8859-9 T�rk�e
# p_32104.py: ��-i�e s�zl�kten veri �er�evesinin sat�r ve s�tunlar�n� yerde�i�tirme �rne�i.

import pandas as pd

y�ll�kB�y�me = {# ��-i�e s�zl�k...
    "�svi�re": {"2010": 3.0, "2011": 1.8, "2012": 1.1, "2013": 1.9},
    "Almanya": {"2010": 4.1, "2011": 3.6, "2012": 0.4, "2013": 0.1},
    "Fransa": {"2010":2.0,  "2011":2.1, "2012": 0.3, "2013": 0.3},
    "Yunanistan": {"2010":-5.4, "2011":-8.9, "2012":-6.6, "2013":	-3.3},
    "�talya": {"2010":1.7, "2011":	0.6, "2012":-2.3, "2013":-1.9},
    "T�rkiye": {"2010": 3.2, "2011": 4.1, "2012": 3.8, "2013":6.5} }

b� = pd.DataFrame (y�ll�kB�y�me) # B�y�me �er�evesi...
print ("Y�la endeksli �lkelerin b�y�me oranlar� y�zdesi:\n", b�, sep="")

b�1 = b�.T
print ("\n�lkeye endeksli y�ll�k b�y�me oranlar� y�zdesi:\n", b�, sep="") # T:transpose

print ("\n3 �lkeye endeksli y�ll�k b�y�me oranlar� y�zdesi:\n", b�1.reindex (["T�rkiye", "�talya", "Yunanistan"]), sep="")



"""��kt�:
>python p_32104.py
Y�la endeksli �lkelerin b�y�me oranlar� y�zdesi:
      �svi�re  Almanya  Fransa  Yunanistan  �talya  T�rkiye
2010      3.0      4.1     2.0        -5.4     1.7      3.2
2011      1.8      3.6     2.1        -8.9     0.6      4.1
2012      1.1      0.4     0.3        -6.6    -2.3      3.8
2013      1.9      0.1     0.3        -3.3    -1.9      6.5

�lkeye endeksli y�ll�k b�y�me oranlar� y�zdesi:
      �svi�re  Almanya  Fransa  Yunanistan  �talya  T�rkiye
2010      3.0      4.1     2.0        -5.4     1.7      3.2
2011      1.8      3.6     2.1        -8.9     0.6      4.1
2012      1.1      0.4     0.3        -6.6    -2.3      3.8
2013      1.9      0.1     0.3        -3.3    -1.9      6.5

3 �lkeye endeksli y�ll�k b�y�me oranlar� y�zdesi:
            2010  2011  2012  2013
T�rkiye      3.2   4.1   3.8   6.5
�talya       1.7   0.6  -2.3  -1.9
Yunanistan  -5.4  -8.9  -6.6  -3.3
"""