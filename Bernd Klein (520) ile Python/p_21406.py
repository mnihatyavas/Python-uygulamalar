# coding:iso-8859-9 Türkçe
# p_21406.py: Karşılaştırılan kelimelerin herbir harf maliyetini belirleme örneği.

# Herbir karakterin (sil,sok,değiştir) puanları tek tek belirlenebilir (varsayılan 1'dir)...

def LM (d1, d2, **puan):
    str = len (d1) + 1
    stn = len (d2) + 1

    karakterler = "abcdefghijklmnopqrstuvwxyz-019"
    w = dict ( (x, (1, 1, 1)) for x in karakterler + karakterler.upper())
    if puan: w.update (puan)

    fark = [[0 for x in range (stn)] for x in range (str)]
    for st in range (1, str): fark [st] [0] = fark [st-1] [0] + w [d1 [st-1]] [0]
    for sn in range (1, stn): fark [0] [sn] = fark [0] [sn-1] + w [d2 [sn-1]] [1]

    for sn in range (1, stn):
        for st in range (1, str):
            sil = w [d1 [st-1]] [0]
            sok = w [d2 [sn-1]] [1]
            değiş = max (w [d1 [st-1]] [2], w [d2 [sn-1]] [2])
            if d1 [st-1] == d2 [sn-1]: değiş = 0
            else: değiş = değiş
            fark [st] [sn] = min (fark [st-1] [sn] + sil,
                    fark [st] [sn-1] + sok,
                    fark [st-1] [sn-1] + değiş) # değiş...
    for s in range (str): print (fark [s])

    return fark [st] [sn]


# Varsayılan:
print ('LM("abc-1","xyz-0",maliyetler=(1,1,1)) için fark:', LM ("abc-1", "xyz-0"), "\n")

# Her karakterin (sil,sok,değiş) puanlamaları ayrıca girilmektedir (belirtilmemişse 1'dir):
print ('LM("abx","xya",a=(7, 6, 6),x=(3, 2, 8),y=(4, 5, 4)) için fark:',
        LM ("abx", "xya",
            a=(7, 6, 6),
            x=(3, 2, 8),
            y=(4, 5, 4) ), "\n")

print ('LM("9abc-1","9xyz-0",a=(7, 6, 6),b=(3, 2, 8),c=(4, 5, 4), x=(1,3,5),z=(3,5,7)) için fark:',
       LM ("9abc-1", "9xyz-0",
            a=(7, 6, 6),
            b=(3, 2, 8),
            c=(4, 5, 4),
            x=(1, 3, 5),
            z=(3, 5, 7) ), "\n")



"""Çıktı:
>python p_21406.py
[0, 1, 2, 3, 4, 5]
[1, 1, 2, 3, 4, 5]
[2, 2, 2, 3, 4, 5]
[3, 3, 3, 3, 4, 5]
[4, 4, 4, 4, 3, 4]
[5, 5, 5, 5, 4, 4]
LM("abc-1","xyz-0",maliyetler=(1,1,1)) için fark: 4

[0, 2, 7, 13]
[7, 8, 8, 7]
[8, 9, 9, 8]
[11, 8, 12, 11]
LM("abx","xya",a=(7, 6, 6),x=(3, 2, 8),y=(4, 5, 4)) için fark: 11

[0, 1, 4, 5, 10, 11, 12]
[1, 0, 3, 4, 9, 10, 11]
[8, 7, 6, 7, 11, 12, 13]
[11, 10, 9, 10, 14, 15, 16]
[15, 14, 13, 13, 17, 18, 19]
[16, 15, 14, 14, 18, 17, 18]
[17, 16, 15, 15, 19, 18, 18]
LM("9abc-1","9xyz-0",a=(7, 6, 6),b=(3, 2, 8),c=(4, 5, 4), x=(1,3,5),z=(3,5,7)) için fark: 18
"""