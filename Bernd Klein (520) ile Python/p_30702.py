# coding:iso-8859-9 T�rk�e
# p_30702.py: De�erler listesinin mesafeler listesinde hangi aral�klara uydu�unun tespiti �rne�i.

def ka��nc�Arada (de�erim, mesafe):
    for i in range (0, len (mesafe)):
        if de�erim < mesafe [i]: return i-1
    return -1

mesafeler = [0, 3, 5, 7.8, 9, 12, 13.8, 16]
print ("Mesafeler:", mesafeler); print()
for de�erim in [-1.3, 0, 0.1, 3.2, 5, 6.2, 7.9, 10.8, 13.9, 15, 16, 16.5]:
    print (de�erim, " �l�e�i: ", ka��nc�Arada (de�erim, mesafeler), ".aral�kdad�r", sep="")
print ("-"*40)
#----------------------------------------------------------------------------------------------------------

def ka��nc�_arada (de�erim, b�l�mler, u�lar_1Mi=True):
    for i in range (0, len (b�l�mler)):
        if de�erim < b�l�mler [i]: return i-1 if u�lar_1Mi else i
    return -1 if u�lar_1Mi else len (b�l�mler)

aral�klar = [0, 3, 5, 7.8, 9, 12, 13.8, 16]
print ("\n-1'li u� kontrollu:")
for de�erim in [-1.3, 0, 0.1, 3.2, 5, 6.2, 7.9, 10.8, 13.9, 15, 16, 16.5]:
    print (ka��nc�_arada (de�erim, aral�klar), end=", ")

print ("\n\n-/+ sonsuz u�lu:") # -~/0, 1/0,..,7/16, 8/+~
for de�erim in [-1.3, 0, 0.1, 3.2, 5, 6.2, 7.9, 10.8, 13.9, 15, 16, 16.5]:
    print (ka��nc�_arada (de�erim, aral�klar, u�lar_1Mi=False), end=", ")



"""��kt�:
>python p_30702.py
Mesafeler: [0, 3, 5, 7.8, 9, 12, 13.8, 16]

-1.3 �l�e�i: -1.aral�kdad�r
0 �l�e�i: 0.aral�kdad�r
0.1 �l�e�i: 0.aral�kdad�r
3.2 �l�e�i: 1.aral�kdad�r
5 �l�e�i: 2.aral�kdad�r
6.2 �l�e�i: 2.aral�kdad�r
7.9 �l�e�i: 3.aral�kdad�r
10.8 �l�e�i: 4.aral�kdad�r
13.9 �l�e�i: 6.aral�kdad�r
15 �l�e�i: 6.aral�kdad�r
16 �l�e�i: -1.aral�kdad�r
16.5 �l�e�i: -1.aral�kdad�r
----------------------------------------

-1'li u� kontrollu:
-1, 0, 0, 1, 2, 2, 3, 4, 6, 6, -1, -1,

-/+ sonsuz u�lu:
0, 1, 1, 2, 3, 3, 4, 5, 7, 7, 8, 8,
"""