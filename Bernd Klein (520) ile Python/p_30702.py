# coding:iso-8859-9 Türkçe
# p_30702.py: Değerler listesinin mesafeler listesinde hangi aralıklara uyduğunun tespiti örneği.

def kaçıncıArada (değerim, mesafe):
    for i in range (0, len (mesafe)):
        if değerim < mesafe [i]: return i-1
    return -1

mesafeler = [0, 3, 5, 7.8, 9, 12, 13.8, 16]
print ("Mesafeler:", mesafeler); print()
for değerim in [-1.3, 0, 0.1, 3.2, 5, 6.2, 7.9, 10.8, 13.9, 15, 16, 16.5]:
    print (değerim, " ölçeği: ", kaçıncıArada (değerim, mesafeler), ".aralıkdadır", sep="")
print ("-"*40)
#----------------------------------------------------------------------------------------------------------

def kaçıncı_arada (değerim, bölümler, uçlar_1Mi=True):
    for i in range (0, len (bölümler)):
        if değerim < bölümler [i]: return i-1 if uçlar_1Mi else i
    return -1 if uçlar_1Mi else len (bölümler)

aralıklar = [0, 3, 5, 7.8, 9, 12, 13.8, 16]
print ("\n-1'li uç kontrollu:")
for değerim in [-1.3, 0, 0.1, 3.2, 5, 6.2, 7.9, 10.8, 13.9, 15, 16, 16.5]:
    print (kaçıncı_arada (değerim, aralıklar), end=", ")

print ("\n\n-/+ sonsuz uçlu:") # -~/0, 1/0,..,7/16, 8/+~
for değerim in [-1.3, 0, 0.1, 3.2, 5, 6.2, 7.9, 10.8, 13.9, 15, 16, 16.5]:
    print (kaçıncı_arada (değerim, aralıklar, uçlar_1Mi=False), end=", ")



"""Çıktı:
>python p_30702.py
Mesafeler: [0, 3, 5, 7.8, 9, 12, 13.8, 16]

-1.3 ölçeği: -1.aralıkdadır
0 ölçeği: 0.aralıkdadır
0.1 ölçeği: 0.aralıkdadır
3.2 ölçeği: 1.aralıkdadır
5 ölçeği: 2.aralıkdadır
6.2 ölçeği: 2.aralıkdadır
7.9 ölçeği: 3.aralıkdadır
10.8 ölçeği: 4.aralıkdadır
13.9 ölçeği: 6.aralıkdadır
15 ölçeği: 6.aralıkdadır
16 ölçeği: -1.aralıkdadır
16.5 ölçeği: -1.aralıkdadır
----------------------------------------

-1'li uç kontrollu:
-1, 0, 0, 1, 2, 2, 3, 4, 6, 6, -1, -1,

-/+ sonsuz uçlu:
0, 1, 1, 2, 3, 3, 4, 5, 7, 7, 8, 8,
"""