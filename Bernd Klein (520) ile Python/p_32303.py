#coding:iso-8859-9 T�rk�e
# p_32303.py: S�cakl�k veri �er�evesinde NaN eksik bilgi y�netimi �rne�i.

import numpy as np
import pandas as pd

v�S�cakl�k = pd.read_csv ("p_32301x.txt", sep=";", decimal=",", encoding="iso:8859-9", index_col=0)
print ("6 sens�r de�erli s�cakl�k disk dosyas� veri �er�evesi (ilk 5):\n", v�S�cakl�k [:5], sep="")

v�Tesad�fi = pd.DataFrame (np.random.random (size=v�S�cakl�k.shape),
    columns=v�S�cakl�k.columns.values,
    index=v�S�cakl�k.index)
print ("\nZaman ve 6 sens�r kolonlu tesad�fi v� (ilk 5):\n", v�Tesad�fi.head(), sep="")

v�NaN = pd.DataFrame (np.nan,
    columns=v�S�cakl�k.columns.values,
    index=v�S�cakl�k.index)
print ("\nZaman ve 6 sens�r kolonlu NaN v� (ilk 5):\n", v�NaN.head(), sep="")

v��kili = v�Tesad�fi < 0.8 # %20 false...
print ("\nZaman ve 6 sens�r kolonlu tesad�fi<0.8=True v� (ilk 5):\n", v��kili.head(), sep="")

v�Bozuk = v�S�cakl�k.where (v��kili, v�NaN)
print ("\nZaman ve 6 sens�r kolonlu bozuk v� (ilk 5):\n", v�Bozuk.head(), sep="")

if (input ("\nBozuk v� saklans�n m� [e/h]? ") == "e"): v�Bozuk.to_csv ("p_32303x.txt", encoding="iso:8859-9")



"""��kt�:
>python p_32303.py
6 sens�r de�erli s�cakl�k disk dosyas� veri �er�evesi (ilk 5):
          sens�r1  sens�r2  sens�r3  sens�r4  sens�r5  sens�r6
zaman
06:00:00     14.3     13.7     14.2     14.3     13.5     13.6
06:15:00     14.5     14.5     14.0     15.0     14.5     14.7
06:30:00     14.6     15.1     14.8     15.3     14.0     14.2
06:45:00     14.8     14.5     15.6     15.2     14.7     14.6
07:00:00     15.0     14.9     15.7     15.6     14.0     15.3

Zaman ve 6 sens�r kolonlu tesad�fi v� (ilk 5):
           sens�r1   sens�r2   sens�r3   sens�r4   sens�r5   sens�r6
zaman
06:00:00  0.749406  0.592442  0.031924  0.360691  0.215435  0.335362
06:15:00  0.562676  0.566898  0.505368  0.814021  0.046357  0.255013
06:30:00  0.420957  0.086341  0.208879  0.462696  0.880438  0.737635
06:45:00  0.108853  0.110036  0.137326  0.375487  0.023736  0.318667
07:00:00  0.333200  0.475804  0.747325  0.453620  0.807202  0.656185

Zaman ve 6 sens�r kolonlu NaN v� (ilk 5):
          sens�r1  sens�r2  sens�r3  sens�r4  sens�r5  sens�r6
zaman
06:00:00      NaN      NaN      NaN      NaN      NaN      NaN
06:15:00      NaN      NaN      NaN      NaN      NaN      NaN
06:30:00      NaN      NaN      NaN      NaN      NaN      NaN
06:45:00      NaN      NaN      NaN      NaN      NaN      NaN
07:00:00      NaN      NaN      NaN      NaN      NaN      NaN

Zaman ve 6 sens�r kolonlu tesad�fi<0.8=True v� (ilk 5):
          sens�r1  sens�r2  sens�r3  sens�r4  sens�r5  sens�r6
zaman
06:00:00     True     True     True     True     True     True
06:15:00     True     True     True    False     True     True
06:30:00     True     True     True     True    False     True
06:45:00     True     True     True     True     True     True
07:00:00     True     True     True     True    False     True

Zaman ve 6 sens�r kolonlu bozuk v� (ilk 5):
          sens�r1  sens�r2  sens�r3  sens�r4  sens�r5  sens�r6
zaman
06:00:00     14.3     13.7     14.2     14.3     13.5     13.6
06:15:00     14.5     14.5     14.0      NaN     14.5     14.7
06:30:00     14.6     15.1     14.8     15.3      NaN     14.2
06:45:00     14.8     14.5     15.6     15.2     14.7     14.6
07:00:00     15.0     14.9     15.7     15.6      NaN     15.3

Bozuk v� saklans�n m� [e/h]? e
"""