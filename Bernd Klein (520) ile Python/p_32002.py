# coding:iso-8859-9 Türkçe
# p_32002.py: Panda serilerinin toplanması ve aritmetik işlemler örneği.

import pandas as pd
import numpy as np

meyveler = ['Elma', 'Portakal', 'Kiraz', "Armut", 'Şeftali']
kiloları = [20, 33, 52, 10, 19]

seri1 = pd.Series (kiloları, index=meyveler)
print ("Meyve adları endeksli kiloları (seri1):\n", seri1, sep="")
print ("\nMeyvelerin kilo değerleri:", seri1.values)
print ("Meyvelerin isim endeksleri:", seri1.index)
print ("Endeksle ilk ve son meyve kiloları:", seri1 [0], seri1 [len (seri1) - 1])
print ("Anahtarkelimeyle ilk ve son meyve kiloları:", seri1 ["Elma"], seri1 ["Şeftali"])
print ("-"*70)
#-----------------------------------------------------------------------------------------------------

seri2 = pd.Series ([17, 13, 31, 32, 9], index=meyveler)
print ("\nMeyve adları endeksli kiloları (seri2):\n", seri2, sep="")

seriA = seri1 + seri2
print ("\nHer iki serinin toplamı (seriA):\n", seriA, sep="")
print ("\nTüm meyvelerin toplam kilosu:", sum (seriA) )
print ("-"*70)
#-----------------------------------------------------------------------------------------------------

seri3 = pd.Series ([17, 13, 31, 32, 9], index=['Ahududu', 'Portakal', 'Kiraz', "Armut", 'Şeftali'])
print ("\nMeyve adları endeksli kiloları (seri3):\n", seri3, sep="")

seriB = seri1 + seri3
print ("\nHer iki serinin (A->Z) toplamı (seriB):\n", seriB, sep="")
print ("-"*70)
#-----------------------------------------------------------------------------------------------------

seri4 = pd.Series ([17, 13, 31, 32, 9], index=['Mere', 'Portokale', 'Cireşe', "Pere", 'Çefteli']) #Romanya...
print ("\nRoman meyve adları endeksli kiloları (seri4):\n", seri4, sep="")

seriC = seri1 + seri4
print ("\nHer iki serinin (A->Z) toplamı (seriC):\n", seriC, sep="")
print ("-"*70)
#-----------------------------------------------------------------------------------------------------

print ("\nTek elemana erişim:", seri1 ["Armut"])
print ("Üç elemana tek-tek erişim:", seri1 ["Armut"], seri1 ["Elma"], seri1 ["Kiraz"])
print ("\nÜç elemana toplu erişim:\n", seri1 [ ["Armut", "Elma", "Kiraz"] ], sep="")
print ("-"*70)
#-----------------------------------------------------------------------------------------------------

print ("\n(seri1*3-9)**0.5:\n", ( (seri1 * 3 - 9) ** (0.75) ), sep="")
print ("\nnp.sin(seri1):\n", np.sin (seri1), sep="")



"""Çıktı:
>python p_32002.py
Meyve adları endeksli kiloları (seri1):
Elma        20
Portakal    33
Kiraz       52
Armut       10
Şeftali     19
dtype: int64

Meyvelerin kilo değerleri: [20 33 52 10 19]
Meyvelerin isim endeksleri: Index(['Elma', 'Portakal', 'Kiraz', 'Armut', 'Şeftal
i'], dtype='object')
Endeksle ilk ve son meyve kiloları: 20 19
Anahtarkelimeyle ilk ve son meyve kiloları: 20 19
----------------------------------------------------------------------

Meyve adları endeksli kiloları (seri2):
Elma        17
Portakal    13
Kiraz       31
Armut       32
Şeftali      9
dtype: int64

Her iki serinin toplamı (seriA):
Elma        37
Portakal    46
Kiraz       83
Armut       42
Şeftali     28
dtype: int64

Tüm meyvelerin toplam kilosu: 236
----------------------------------------------------------------------

Meyve adları endeksli kiloları (seri3):
Ahududu     17
Portakal    13
Kiraz       31
Armut       32
Şeftali      9
dtype: int64

Her iki serinin (A->Z) toplamı (seriB):
Ahududu      NaN
Armut       42.0
Elma         NaN
Kiraz       83.0
Portakal    46.0
Şeftali     28.0
dtype: float64
----------------------------------------------------------------------

Roman meyve adları endeksli kiloları (seri4):
Mere         17
Portokale    13
Cireşe       31
Pere         32
Çefteli       9
dtype: int64

Her iki serinin (A->Z) toplamı (seriC):
Armut       NaN
Cireşe      NaN
Elma        NaN
Kiraz       NaN
Mere        NaN
Pere        NaN
Portakal    NaN
Portokale   NaN
Çefteli     NaN
Şeftali     NaN
dtype: float64
----------------------------------------------------------------------

Tek elemana erişim: 10
Üç elemana tek-tek erişim: 10 20 52

Üç elemana toplu erişim:
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
Şeftali     18.236056
dtype: float64

np.sin(seri1):
Elma        0.912945
Portakal    0.999912
Kiraz       0.986628
Armut      -0.544021
Şeftali     0.149877
dtype: float64
"""