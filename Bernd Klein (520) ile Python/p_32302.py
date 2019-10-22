#coding:iso-8859-9 T�rk�e
# p_32302.py: Veri �er�evesinde NaN eksik bilgi y�netimi �rne�i.

import numpy as np
import pandas as pd
import math

n1 = float ("nan") # veya "Nan", "naN", "NaN", "NAN"
n2 = math.nan

print (n1)
print (n2, math.isnan (n2))
print ((n1 == n2), (n1 == 0), (n1 == 10), (n1 > 0), (n1 < 0) )
print ("-"*75)
#----------------------------------------------------------------------------------------------------

seriler = pd.Series (range (5, 16, 2) )
print ("\nrange(5,16,2) serileri:\n", seriler, sep="")
print ("\nseriler > 10 de�erleri:\n", seriler.where (seriler > 10), sep="")
print ("-"*75)
#----------------------------------------------------------------------------------------------------

matris = np.random.randint (1, 99, (5, 3)) # de�eri tesad�fi [1,99] olan (5x3) ebatl� matris...
v� = pd.DataFrame (matris, columns=['A', 'B', "C"])
v�2 = v� % 2 == 0 # �ift de�erleri "true", tekleri "false" boolean matris...
print ("\n(5x3) ebatl� tesad�fi [1,99] de�erler matrisi:\n", v�,
    "\n\nAyn� matrisin �iftler true tekler false boolean'�:\n", v�2, sep="")

v�.where (v�2, -v�, inplace=True)
print ("\nAyn� matrisin �iftler + tekler - kar��l���:\n", v�, sep="")



"""��kt�:
>python p_32301b.py
nan
nan True
False False False False False
---------------------------------------------------------------------------

range(5,16,2) serileri:
0     5
1     7
2     9
3    11
4    13
5    15
dtype: int64

seriler > 10 de�erleri:
0     NaN
1     NaN
2     NaN
3    11.0
4    13.0
5    15.0
dtype: float64
---------------------------------------------------------------------------

(5x3) ebatl� tesad�fi [1,99] de�erler matrisi:
    A   B   C
0  52  24  42
1  41  33  46
2  13  53  68
3  52  15  68
4  86  40  68

Ayn� matrisin �iftler true tekler false boolean'�:
       A      B     C
0   True   True  True
1  False  False  True
2  False  False  True
3   True  False  True
4   True   True  True

Ayn� matrisin �iftler + tekler - kar��l���:
    A   B   C
0  52  24  42
1 -41 -33  46
2 -13 -53  68
3  52 -15  68
4  86  40  68
"""