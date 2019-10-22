#coding:iso-8859-9 T�rk�e
# p_32504.py: D�nya programlama dilleri kullan�m y�zdeleri v� grafi�i �rne�i.

import matplotlib.pyplot as mp
import pandas as pd
from p_315 import Renk

"""�nternetten dosya okuma:
data_path = "https://www.python-course.eu/data1/programming_language_usage.txt"
def strip_percentage_sign(x): return float(x.strip('%'))
progs = pd.read_csv(data_path,
                   quotechar='"',
                   thousands=",",
                   index_col=1,
                   converters={'Percentage':strip_percentage_sign},
                   delimiter=r"\s+")
progs.to_csv ("p_32504x.txt")
"""

dillerV� = pd.read_csv ("p_32504x.txt", encoding="iso-8859-9", index_col=0)
print ("Kas�m 2018 tarihli d�nya programlama dilleri kullan�m y�zdeleri v�:\n", dillerV�, sep="")

#dillerV�.set_index ("Dil", inplace=True)

�ekil = mp.figure()
�ekil.suptitle ("Dillerin kullan�m y�zdeleri")
�ekil.set_facecolor (Renk.renk())

alt�ekil = �ekil.subplots()
alt�ekil.set_ylabel ("Kullan�m y�zdesi")
alt�ekil.set_facecolor (Renk.renk())

dillerV�.plot (
    ax=alt�ekil,
    xticks=range (1, len (dillerV�.index)),
    use_index=True,
    style="--d", color=Renk.renk() )
alt�ekil.set_xlabel ("Programlama dilleri")
mp.show()

#X-exsen dil adlar� i�in grafikte configure_subplots->bottom art�r�l�r, pencere tam a��l�r...



"""��kt�:
>python p_32504.py
Kas�m 2018 tarihli d�nya programlama dilleri kullan�m y�zdeleri v�:
                     Dil   Y�zde
0                   Java  16.384
1                      C   7.742
2                    C++   5.184
3                     C#   4.409
4                 Python   3.919
5      Visual Basic .NET   3.174
6                    PHP   3.009
7             JavaScript   2.667
8   Delphi/Object Pascal   2.544
9                  Swift   2.268
10                  Perl   2.261
11                  Ruby   2.254
12     Assembly language   2.232
13                     R   2.016
14          Visual Basic   2.008
15           Objective-C   1.997
16                    Go   1.982
17                MATLAB   1.854
18                PL/SQL   1.672
19               Scratch   1.472
"""