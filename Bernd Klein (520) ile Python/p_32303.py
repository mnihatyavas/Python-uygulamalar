#coding:iso-8859-9 Türkçe
# p_32303.py: Sıcaklık veri çerçevesinde NaN eksik bilgi yönetimi örneği.

import numpy as np
import pandas as pd

vçSıcaklık = pd.read_csv ("p_32301x.txt", sep=";", decimal=",", encoding="iso:8859-9", index_col=0)
print ("6 sensör değerli sıcaklık disk dosyası veri çerçevesi (ilk 5):\n", vçSıcaklık [:5], sep="")

vçTesadüfi = pd.DataFrame (np.random.random (size=vçSıcaklık.shape),
    columns=vçSıcaklık.columns.values,
    index=vçSıcaklık.index)
print ("\nZaman ve 6 sensör kolonlu tesadüfi vç (ilk 5):\n", vçTesadüfi.head(), sep="")

vçNaN = pd.DataFrame (np.nan,
    columns=vçSıcaklık.columns.values,
    index=vçSıcaklık.index)
print ("\nZaman ve 6 sensör kolonlu NaN vç (ilk 5):\n", vçNaN.head(), sep="")

vçİkili = vçTesadüfi < 0.8 # %20 false...
print ("\nZaman ve 6 sensör kolonlu tesadüfi<0.8=True vç (ilk 5):\n", vçİkili.head(), sep="")

vçBozuk = vçSıcaklık.where (vçİkili, vçNaN)
print ("\nZaman ve 6 sensör kolonlu bozuk vç (ilk 5):\n", vçBozuk.head(), sep="")

if (input ("\nBozuk vç saklansın mı [e/h]? ") == "e"): vçBozuk.to_csv ("p_32303x.txt", encoding="iso:8859-9")



"""Çıktı:
>python p_32303.py
6 sensör değerli sıcaklık disk dosyası veri çerçevesi (ilk 5):
          sensör1  sensör2  sensör3  sensör4  sensör5  sensör6
zaman
06:00:00     14.3     13.7     14.2     14.3     13.5     13.6
06:15:00     14.5     14.5     14.0     15.0     14.5     14.7
06:30:00     14.6     15.1     14.8     15.3     14.0     14.2
06:45:00     14.8     14.5     15.6     15.2     14.7     14.6
07:00:00     15.0     14.9     15.7     15.6     14.0     15.3

Zaman ve 6 sensör kolonlu tesadüfi vç (ilk 5):
           sensör1   sensör2   sensör3   sensör4   sensör5   sensör6
zaman
06:00:00  0.749406  0.592442  0.031924  0.360691  0.215435  0.335362
06:15:00  0.562676  0.566898  0.505368  0.814021  0.046357  0.255013
06:30:00  0.420957  0.086341  0.208879  0.462696  0.880438  0.737635
06:45:00  0.108853  0.110036  0.137326  0.375487  0.023736  0.318667
07:00:00  0.333200  0.475804  0.747325  0.453620  0.807202  0.656185

Zaman ve 6 sensör kolonlu NaN vç (ilk 5):
          sensör1  sensör2  sensör3  sensör4  sensör5  sensör6
zaman
06:00:00      NaN      NaN      NaN      NaN      NaN      NaN
06:15:00      NaN      NaN      NaN      NaN      NaN      NaN
06:30:00      NaN      NaN      NaN      NaN      NaN      NaN
06:45:00      NaN      NaN      NaN      NaN      NaN      NaN
07:00:00      NaN      NaN      NaN      NaN      NaN      NaN

Zaman ve 6 sensör kolonlu tesadüfi<0.8=True vç (ilk 5):
          sensör1  sensör2  sensör3  sensör4  sensör5  sensör6
zaman
06:00:00     True     True     True     True     True     True
06:15:00     True     True     True    False     True     True
06:30:00     True     True     True     True    False     True
06:45:00     True     True     True     True     True     True
07:00:00     True     True     True     True    False     True

Zaman ve 6 sensör kolonlu bozuk vç (ilk 5):
          sensör1  sensör2  sensör3  sensör4  sensör5  sensör6
zaman
06:00:00     14.3     13.7     14.2     14.3     13.5     13.6
06:15:00     14.5     14.5     14.0      NaN     14.5     14.7
06:30:00     14.6     15.1     14.8     15.3      NaN     14.2
06:45:00     14.8     14.5     15.6     15.2     14.7     14.6
07:00:00     15.0     14.9     15.7     15.6      NaN     15.3

Bozuk vç saklansın mı [e/h]? e
"""