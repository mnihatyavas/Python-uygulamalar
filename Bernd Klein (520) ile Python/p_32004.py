# coding:iso-8859-9 Türkçe
# p_32004.py: Pandas serisinde aranan mevcut ve namevcutlar örneği.

import pandas as pd

sözlük = {
    "Berlin":3562166,
    "İstanbul":7167203,
    "Madrid":3165235,
    "Roma":2874038,
    "Paris":2273305,
    "Vienna":1805681,
    "Buçarest":1803425,
    "Hamburg":1760433,
    "Budapeşte":1754000,
    "Varşova":1740119,
    "Barselona":1602386,
    "Münih":1493900,
    "Londra":8615246,
    "Milano":1350680}

seri = pd.Series (sözlük)

print ("Şehirler ve merkez nüfuslarını göster:\n", seri, sep="")
print ("\n2 milyon ve üzeri şehirleri göster:\n", seri [seri >= 2000000], sep="")
print ("\nListede 'İstanbul' var mı?", ("İstanbul" in seri) )
print ("Listede 'Ankara' yok mu?", ("Ankara" not in seri) )
print ("-"*40)
#-----------------------------------------------------------------------------------------------------

print ("\nAranan hepsi listede mevcutsa dype=int64:\n", pd.Series (sözlük, index=["Londra", "İstanbul", "Hamburg", "Milano", "Paris"]), sep="")

aranan = pd.Series (sözlük, index=["Londra", "İstanbul", "Zürih", "Milano", "Şututgard"])

print ("\nListede namevcutsa dype=float64:\n", aranan, sep="")
print ("\nNamevcutları listeden ayıkla:\n", aranan.dropna(), sep="")
print ("\nNamevcutsa NaN yerine sıfırla:\n", aranan.fillna (0), sep="")
print ("\nEksikleri tamamla:\n", aranan.fillna ({"Şututgard":597939, "Zürih":378884}), sep="")
print ("\nEksikleri tamamla ve dtype=int32 yap:\n", aranan.fillna ({"Şututgard":597939, "Zürih":378884}).astype (int), sep="")



"""Çıktı:
>python p_32004.py
Şehirler ve merkez nüfuslarını göster:
Berlin       3562166
İstanbul     7167203
Madrid       3165235
Roma         2874038
Paris        2273305
Vienna       1805681
Buçarest     1803425
Hamburg      1760433
Budapeşte    1754000
Varşova      1740119
Barselona    1602386
Münih        1493900
Londra       8615246
Milano       1350680
dtype: int64

2 milyon ve üzeri şehirleri göster:
Berlin      3562166
İstanbul    7167203
Madrid      3165235
Roma        2874038
Paris       2273305
Londra      8615246
dtype: int64

Listede 'İstanbul' var mı? True
Listede 'Ankara' yok mu? True
----------------------------------------

Aranan hepsi listede mevcutsa dype=int64:
Londra      8615246
İstanbul    7167203
Hamburg     1760433
Milano      1350680
Paris       2273305
dtype: int64

Listede namevcutsa dype=float64:
Londra       8615246.0
İstanbul     7167203.0
Zürih              NaN
Milano       1350680.0
Şututgard          NaN
dtype: float64

Namevcutları listeden ayıkla:
Londra      8615246.0
İstanbul    7167203.0
Milano      1350680.0
dtype: float64

Namevcutsa NaN yerine sıfırla:
Londra       8615246.0
İstanbul     7167203.0
Zürih              0.0
Milano       1350680.0
Şututgard          0.0
dtype: float64

Eksikleri tamamla:
Londra       8615246.0
İstanbul     7167203.0
Zürih         378884.0
Milano       1350680.0
Şututgard     597939.0
dtype: float64

Eksikleri tamamla ve dtype=int32 yap:
Londra       8615246
İstanbul     7167203
Zürih         378884
Milano       1350680
Şututgard     597939
dtype: int32
"""