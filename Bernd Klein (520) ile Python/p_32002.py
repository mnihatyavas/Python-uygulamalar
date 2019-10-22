# coding:iso-8859-9 T�rk�e
# p_32002.py: Panda serilerinin toplanmas� ve aritmetik i�lemler �rne�i.

import pandas as pd
import numpy as np

meyveler = ['Elma', 'Portakal', 'Kiraz', "Armut", '�eftali']
kilolar� = [20, 33, 52, 10, 19]

seri1 = pd.Series (kilolar�, index=meyveler)
print ("Meyve adlar� endeksli kilolar� (seri1):\n", seri1, sep="")
print ("\nMeyvelerin kilo de�erleri:", seri1.values)
print ("Meyvelerin isim endeksleri:", seri1.index)
print ("Endeksle ilk ve son meyve kilolar�:", seri1 [0], seri1 [len (seri1) - 1])
print ("Anahtarkelimeyle ilk ve son meyve kilolar�:", seri1 ["Elma"], seri1 ["�eftali"])
print ("-"*70)
#-----------------------------------------------------------------------------------------------------

seri2 = pd.Series ([17, 13, 31, 32, 9], index=meyveler)
print ("\nMeyve adlar� endeksli kilolar� (seri2):\n", seri2, sep="")

seriA = seri1 + seri2
print ("\nHer iki serinin toplam� (seriA):\n", seriA, sep="")
print ("\nT�m meyvelerin toplam kilosu:", sum (seriA) )
print ("-"*70)
#-----------------------------------------------------------------------------------------------------

seri3 = pd.Series ([17, 13, 31, 32, 9], index=['Ahududu', 'Portakal', 'Kiraz', "Armut", '�eftali'])
print ("\nMeyve adlar� endeksli kilolar� (seri3):\n", seri3, sep="")

seriB = seri1 + seri3
print ("\nHer iki serinin (A->Z) toplam� (seriB):\n", seriB, sep="")
print ("-"*70)
#-----------------------------------------------------------------------------------------------------

seri4 = pd.Series ([17, 13, 31, 32, 9], index=['Mere', 'Portokale', 'Cire�e', "Pere", '�efteli']) #Romanya...
print ("\nRoman meyve adlar� endeksli kilolar� (seri4):\n", seri4, sep="")

seriC = seri1 + seri4
print ("\nHer iki serinin (A->Z) toplam� (seriC):\n", seriC, sep="")
print ("-"*70)
#-----------------------------------------------------------------------------------------------------

print ("\nTek elemana eri�im:", seri1 ["Armut"])
print ("�� elemana tek-tek eri�im:", seri1 ["Armut"], seri1 ["Elma"], seri1 ["Kiraz"])
print ("\n�� elemana toplu eri�im:\n", seri1 [ ["Armut", "Elma", "Kiraz"] ], sep="")
print ("-"*70)
#-----------------------------------------------------------------------------------------------------

print ("\n(seri1*3-9)**0.5:\n", ( (seri1 * 3 - 9) ** (0.75) ), sep="")
print ("\nnp.sin(seri1):\n", np.sin (seri1), sep="")



"""��kt�:
>python p_32002.py
Meyve adlar� endeksli kilolar� (seri1):
Elma        20
Portakal    33
Kiraz       52
Armut       10
�eftali     19
dtype: int64

Meyvelerin kilo de�erleri: [20 33 52 10 19]
Meyvelerin isim endeksleri: Index(['Elma', 'Portakal', 'Kiraz', 'Armut', '�eftal
i'], dtype='object')
Endeksle ilk ve son meyve kilolar�: 20 19
Anahtarkelimeyle ilk ve son meyve kilolar�: 20 19
----------------------------------------------------------------------

Meyve adlar� endeksli kilolar� (seri2):
Elma        17
Portakal    13
Kiraz       31
Armut       32
�eftali      9
dtype: int64

Her iki serinin toplam� (seriA):
Elma        37
Portakal    46
Kiraz       83
Armut       42
�eftali     28
dtype: int64

T�m meyvelerin toplam kilosu: 236
----------------------------------------------------------------------

Meyve adlar� endeksli kilolar� (seri3):
Ahududu     17
Portakal    13
Kiraz       31
Armut       32
�eftali      9
dtype: int64

Her iki serinin (A->Z) toplam� (seriB):
Ahududu      NaN
Armut       42.0
Elma         NaN
Kiraz       83.0
Portakal    46.0
�eftali     28.0
dtype: float64
----------------------------------------------------------------------

Roman meyve adlar� endeksli kilolar� (seri4):
Mere         17
Portokale    13
Cire�e       31
Pere         32
�efteli       9
dtype: int64

Her iki serinin (A->Z) toplam� (seriC):
Armut       NaN
Cire�e      NaN
Elma        NaN
Kiraz       NaN
Mere        NaN
Pere        NaN
Portakal    NaN
Portokale   NaN
�efteli     NaN
�eftali     NaN
dtype: float64
----------------------------------------------------------------------

Tek elemana eri�im: 10
�� elemana tek-tek eri�im: 10 20 52

�� elemana toplu eri�im:
Armut    10
Elma     20
Kiraz    52
dtype: int64
----------------------------------------------------------------------

(seri1*3-9)**0.5:
Elma        19.084361
Portakal    29.220112
Kiraz       42.217061
Armut        9.809898
�eftali     18.236056
dtype: float64

np.sin(seri1):
Elma        0.912945
Portakal    0.999912
Kiraz       0.986628
Armut      -0.544021
�eftali     0.149877
dtype: float64
"""