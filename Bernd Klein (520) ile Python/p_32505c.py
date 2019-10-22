#coding:iso-8859-9 Türkçe
# p_32505c.py: Programlama dilleri kullanım yüzdesi vç börek grafiği örneği.

import matplotlib.pyplot as mp
import pandas as pd
from p_315 import Renk

dillerVÇ = pd.read_csv ("p_32504x.txt", encoding="iso-8859-9", index_col=0)
print ("Programlama dilleri ve kullanım yüzdeleri vç:\n", dillerVÇ, sep="")

mp.style.use ("dark_background")
dillerVÇ.plot.pie (figsize=(7, 5), subplots=True, legend=False, colors=[Renk.renk() for _ in range (len (dillerVÇ.index))] ) # VÇ için varsayılı legend=True...
# İlk kolon x=index=Dil, ikincisi ise y=veriler= Yüzde (subplots=True)...
# Böreğin ilk-->son dilimi = 0-->360 dereceyi takip eder...
mp.show()


dillerVÇ.plot.pie (figsize=(11, 4), subplots=True, legend=False, colors=[Renk.renk() for _ in range (len (dillerVÇ.index))] )
mp.ylabel ("")
yüzdeler = [dillerVÇ ["Yüzde"] [i].round (3) for i in range (len (dillerVÇ.index))]
mp.xlabel ("%: " + str (yüzdeler) )
mp.show()



"""Çıktı:
>python p_32505c.py
Programlama dilleri ve kullanım yüzdeleri vç:
                       Yüzde
Dil
Java                  16.384
C                      7.742
C++                    5.184
C#                     4.409
Python                 3.919
Visual Basic .NET      3.174
PHP                    3.009
JavaScript             2.667
Delphi/Object Pascal   2.544
Swift                  2.268
Perl                   2.261
Ruby                   2.254
Assembly language      2.232
R                      2.016
Visual Basic           2.008
Objective-C            1.997
Go                     1.982
MATLAB                 1.854
PL/SQL                 1.672
Scratch                1.472
"""