#coding:iso-8859-9 T�rk�e
# p_32505c.py: Programlama dilleri kullan�m y�zdesi v� b�rek grafi�i �rne�i.

import matplotlib.pyplot as mp
import pandas as pd
from p_315 import Renk

dillerV� = pd.read_csv ("p_32504x.txt", encoding="iso-8859-9", index_col=0)
print ("Programlama dilleri ve kullan�m y�zdeleri v�:\n", dillerV�, sep="")

mp.style.use ("dark_background")
dillerV�.plot.pie (figsize=(7, 5), subplots=True, legend=False, colors=[Renk.renk() for _ in range (len (dillerV�.index))] ) # V� i�in varsay�l� legend=True...
# �lk kolon x=index=Dil, ikincisi ise y=veriler= Y�zde (subplots=True)...
# B�re�in ilk-->son dilimi = 0-->360 dereceyi takip eder...
mp.show()


dillerV�.plot.pie (figsize=(11, 4), subplots=True, legend=False, colors=[Renk.renk() for _ in range (len (dillerV�.index))] )
mp.ylabel ("")
y�zdeler = [dillerV� ["Y�zde"] [i].round (3) for i in range (len (dillerV�.index))]
mp.xlabel ("%: " + str (y�zdeler) )
mp.show()



"""��kt�:
>python p_32505c.py
Programlama dilleri ve kullan�m y�zdeleri v�:
                       Y�zde
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