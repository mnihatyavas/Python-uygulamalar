# coding:iso-8859-9 Türkçe

from random import randint
L1 = [randint (0,100) for i in range (10)]
L2 = [randint (0,100) for i in range (20)]
i = 0
bayrak = True
while i < len (L1) and bayrak:
    if L1[i] in L2: bayrak = False
    else: i +=1
if not bayrak: print ("İlk ortak değer: ", i, ".endeksteki: ", L1[i], "'dir.", sep="")
else: print ("Hiç ortak değere rastlanmadı!")

print ("\n1 adet tamsayı 1'den 20 adet tamsayı 1'e artan liste:")
L = [int ("1"*i) for i in range (1, 21)]
print (L)

print ("\n[1->1000] arası sayılardan 7'ye bölünebilen ve sonu 6 olanların yanyana dökümü:\n==>", end="")
for i in range (1, 1001):
    if (i % 7 == 0) and (i - ((i // 10) * 10) == 6): print (i, end=" ")

print ("\n\n[1->10000] arası sayılardan enaz bir 3 içerenlerin yanyana dökümü:")
sayaç = 0
for i in range (1, 10001):
    if "3" in str (i): print (i, end=" "); sayaç +=1
print ("\n==>Toplam:", sayaç, "adet 3 içeren bulundu.")

print ("\n[10->99] arası palindromik (ters=düz) sayıların (azami 20 aşamalı) listesi==>")
for i in range (10, 100):
    bayrak = True
    j = 0
    r1 = i
    while j < 21 and bayrak:
        j += 1
        r2 = str (r1)[::-1]
        r3 = r1 + int (r2)
        if str (r3) == str (r3)[::-1]:
            print ("Sayı: {:2d}, Aşama sayısı: {:2d}, Palindromik sayı: {:5d}" .format (i, j, r3) )
            bayrak = False
        else: r1 = r3

print ("\n[100->500] arası 6 haneli palindromik sayıların listesi==>")
for i in range (100, 500):
    bayrak = True
    j = 0
    r1 = i
    while j < 21 and bayrak:
        j += 1
        r2 = str (r1)[::-1]
        r3 = r1 + int (r2)
        if str (r3) == str (r3)[::-1] and len (str (r3)) == 6:
            print ("Sayı: {:3d}, Aşama sayısı: {:2d}, Palindromik sayı: {:6d}" .format (i, j, r3) )
            bayrak = False
        else: r1 = r3

print ("\n[1->10000000:on_milyon] arası alttan=üstten sayıların listesi==>")
for i in range (1, 10000000):
    d = str (i)
    e = len (d)
    if "2" in d or "3" in d or "4" in d or "5" in d or "7" in d: continue
    if d[0] == "0" or d[e-1] == "0": continue
    if (d[0] == "1" and d[e-1] != "1") \
            or (d[0] == "8" and d[e-1] != "8") \
            or (d[0] == "6" and d[e-1] != "9") \
            or (d[0] == "9" and d[e-1] != "6"): continue
    if (e+1) % 2 == 0:
        if d[e//2] != "0" and d[e//2] != "1" and d[e//2] != "8": continue
    if e < 4: print (i)
    else:
        yaz = True
        for j in range (1, e//2):
            if d[j] == "0" and d[e-j-1] == "0": continue
            elif d[j] == "1" and d[e-j-1] == "1": continue
            elif d[j] == "8" and d[e-j-1] == "8": continue
            elif d[j] == "6" and d[e-j-1] == "9": continue
            elif d[j] == "9" and d[e-j-1] == "6": continue
            else: yaz = False
        if yaz: print (i)
