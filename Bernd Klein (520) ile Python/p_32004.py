# coding:iso-8859-9 T�rk�e
# p_32004.py: Pandas serisinde aranan mevcut ve namevcutlar �rne�i.

import pandas as pd

s�zl�k = {
    "Berlin":3562166,
    "�stanbul":7167203,
    "Madrid":3165235,
    "Roma":2874038,
    "Paris":2273305,
    "Vienna":1805681,
    "Bu�arest":1803425,
    "Hamburg":1760433,
    "Budape�te":1754000,
    "Var�ova":1740119,
    "Barselona":1602386,
    "M�nih":1493900,
    "Londra":8615246,
    "Milano":1350680}

seri = pd.Series (s�zl�k)

print ("�ehirler ve merkez n�fuslar�n� g�ster:\n", seri, sep="")
print ("\n2 milyon ve �zeri �ehirleri g�ster:\n", seri [seri >= 2000000], sep="")
print ("\nListede '�stanbul' var m�?", ("�stanbul" in seri) )
print ("Listede 'Ankara' yok mu?", ("Ankara" not in seri) )
print ("-"*40)
#-----------------------------------------------------------------------------------------------------

print ("\nAranan hepsi listede mevcutsa dype=int64:\n", pd.Series (s�zl�k, index=["Londra", "�stanbul", "Hamburg", "Milano", "Paris"]), sep="")

aranan = pd.Series (s�zl�k, index=["Londra", "�stanbul", "Z�rih", "Milano", "�ututgard"])

print ("\nListede namevcutsa dype=float64:\n", aranan, sep="")
print ("\nNamevcutlar� listeden ay�kla:\n", aranan.dropna(), sep="")
print ("\nNamevcutsa NaN yerine s�f�rla:\n", aranan.fillna (0), sep="")
print ("\nEksikleri tamamla:\n", aranan.fillna ({"�ututgard":597939, "Z�rih":378884}), sep="")
print ("\nEksikleri tamamla ve dtype=int32 yap:\n", aranan.fillna ({"�ututgard":597939, "Z�rih":378884}).astype (int), sep="")



"""��kt�:
>python p_32004.py
�ehirler ve merkez n�fuslar�n� g�ster:
Berlin       3562166
�stanbul     7167203
Madrid       3165235
Roma         2874038
Paris        2273305
Vienna       1805681
Bu�arest     1803425
Hamburg      1760433
Budape�te    1754000
Var�ova      1740119
Barselona    1602386
M�nih        1493900
Londra       8615246
Milano       1350680
dtype: int64

2 milyon ve �zeri �ehirleri g�ster:
Berlin      3562166
�stanbul    7167203
Madrid      3165235
Roma        2874038
Paris       2273305
Londra      8615246
dtype: int64

Listede '�stanbul' var m�? True
Listede 'Ankara' yok mu? True
----------------------------------------

Aranan hepsi listede mevcutsa dype=int64:
Londra      8615246
�stanbul    7167203
Hamburg     1760433
Milano      1350680
Paris       2273305
dtype: int64

Listede namevcutsa dype=float64:
Londra       8615246.0
�stanbul     7167203.0
Z�rih              NaN
Milano       1350680.0
�ututgard          NaN
dtype: float64

Namevcutlar� listeden ay�kla:
Londra      8615246.0
�stanbul    7167203.0
Milano      1350680.0
dtype: float64

Namevcutsa NaN yerine s�f�rla:
Londra       8615246.0
�stanbul     7167203.0
Z�rih              0.0
Milano       1350680.0
�ututgard          0.0
dtype: float64

Eksikleri tamamla:
Londra       8615246.0
�stanbul     7167203.0
Z�rih         378884.0
Milano       1350680.0
�ututgard     597939.0
dtype: float64

Eksikleri tamamla ve dtype=int32 yap:
Londra       8615246
�stanbul     7167203
Z�rih         378884
Milano       1350680
�ututgard     597939
dtype: int32
"""