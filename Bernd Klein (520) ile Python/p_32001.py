# coding:iso-8859-9 T�rk�e
# p_32001.py: Basit bir pandas serisiyle numpy dizisinin kar��la�t�r�lmas� �rne�i.

#pip install pandas
#Successfully installed pandas-0.24.2 pytz-2019.1

import pandas as pd

seri = pd.Series ([11, 28, 72, 3, 5, 8])
print ("Panda serisinin endeks, de�er ve tipi:\n", seri, sep="")
print ("\nSerinin de�erleri:", seri.values)
print ("Serinin endeks kapsam�:", seri.index)
print ("-"*60)
#------------------------------------------------------------------------------------------------------

import numpy as np

seri2 = np.array ([11, 28, 72, 3, 5, 8])
print ("\nNumpy dizisi:", seri2)
print ("Pandas seri de�erleri:", seri.values)
print ("Pandas seri tipi = Numpy dizi tipi:\n",
    type (seri.values), " = ", type (seri2), sep="")
print ("Serinin ilk ve son de�erleri:", seri [0], seri [len (seri) - 1])



"""��kt�:
>python p_32001.py
Panda serisinin endeks, de�er ve tipi:
0    11
1    28
2    72
3     3
4     5
5     8
dtype: int64

Serinin de�erleri: [11 28 72  3  5  8]
Serinin endeks kapsam�: RangeIndex(start=0, stop=6, step=1)
------------------------------------------------------------

Numpy dizisi: [11 28 72  3  5  8]
Pandas seri de�erleri: [11 28 72  3  5  8]
Pandas seri tipi = Numpy dizi tipi:
<class 'numpy.ndarray'> = <class 'numpy.ndarray'>
Serinin ilk ve son de�erleri: 11 8
"""