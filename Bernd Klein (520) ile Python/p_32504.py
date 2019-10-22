#coding:iso-8859-9 Türkçe
# p_32504.py: Dünya programlama dilleri kullanım yüzdeleri vç grafiği örneği.

import matplotlib.pyplot as mp
import pandas as pd
from p_315 import Renk

"""İnternetten dosya okuma:
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

dillerVÇ = pd.read_csv ("p_32504x.txt", encoding="iso-8859-9", index_col=0)
print ("Kasım 2018 tarihli dünya programlama dilleri kullanım yüzdeleri vç:\n", dillerVÇ, sep="")

#dillerVÇ.set_index ("Dil", inplace=True)

şekil = mp.figure()
şekil.suptitle ("Dillerin kullanım yüzdeleri")
şekil.set_facecolor (Renk.renk())

altşekil = şekil.subplots()
altşekil.set_ylabel ("Kullanım yüzdesi")
altşekil.set_facecolor (Renk.renk())

dillerVÇ.plot (
    ax=altşekil,
    xticks=range (1, len (dillerVÇ.index)),
    use_index=True,
    style="--d", color=Renk.renk() )
altşekil.set_xlabel ("Programlama dilleri")
mp.show()

#X-exsen dil adları için grafikte configure_subplots->bottom artırılır, pencere tam açılır...



"""Çıktı:
>python p_32504.py
Kasım 2018 tarihli dünya programlama dilleri kullanım yüzdeleri vç:
                     Dil   Yüzde
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