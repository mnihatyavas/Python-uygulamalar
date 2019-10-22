# coding:iso-8859-9 Türkçe
# p_21405.py: Karşılaştırmalı kelime matrisi varsayılı 1-1-1 sil-sok-değiştir maliyetini değiştirme örneği.

# maliyetler=(1,1,1): Varsayılan 1 olan sil, sok, değiş maliyetleri kullanıcı tarafından belirlenebilir...

def LM (d1, d2, maliyetler = (1, 1, 1) ):
    satırlar = len (d1)+1
    sütunlar = len (d2)+1
    silmeler, sokmalar, değiştirmeler = maliyetler

    mesafe = [[0 for x in range (sütunlar)] for x in range (satırlar)]
    for satır in range (1, satırlar): mesafe [satır] [0] = satır * silmeler
    for sütun in range (1, sütunlar): mesafe [0] [sütun] = sütun * sokmalar

    for sütun in range (1, sütunlar):
        for satır in range (1, satırlar):
            if d1 [satır-1] == d2 [sütun-1]: maliyet = 0
            else: maliyet = değiştirmeler
            mesafe [satır] [sütun] = min (mesafe [satır-1] [sütun] + silmeler,
                    mesafe [satır] [sütun-1] + sokmalar,
                    mesafe [satır-1] [sütun-1] + maliyet) # değiştirmeler...
    for r in range (satırlar): print (mesafe [r])

    return mesafe [satır] [sütun]


# Varsayılan (sil, sok, değiştir) = (1, 1, 1):
print ('LM("abc-","xyz-",maliyetler=(1,1,1)) için fark:', LM ("abc-", "xyz-"), "\n")

# Maliyetler (sil, sok, değiştir) = (1, 1, 2):
print ('LM("abc-q","xyz-",maliyetler=(1,1,2)) için fark:', LM ("abc-q", "xyz-", maliyetler=(1, 1, 2)), "\n")

# Maliyetler (sil, sok, değiştir) = (2, 2, 1):
print ('LM("abc-","xyz-w",maliyetler=(2,2,1)) için fark:', LM ("abc-", "xyz-w", maliyetler=(2, 2, 1)), "\n")

# Maliyetler (sil, sok, değiştir) = (1, 2, 3):
print ('LM("abc","xyz-",maliyetler=(1,2,3)) için fark:', LM ("abc", "xyz-", maliyetler=(1, 2, 3)), "\n")

# Maliyetler (sil, sok, değiştir) = (1, 2, 3):
print ('LM("abc-","xyz",maliyetler=(1,2,3)) için fark:', LM ("abc-", "xyz", maliyetler=(1, 2, 3)), "\n")



"""Çıktı:
>python p_21405.py
[0, 1, 2, 3, 4]
[1, 1, 2, 3, 4]
[2, 2, 2, 3, 4]
[3, 3, 3, 3, 4]
[4, 4, 4, 4, 3]
LM("abc-","xyz-",maliyetler=(1,1,1)) için fark: 3
==>3 değişiklik=2

[0, 1, 2, 3, 4]
[1, 2, 3, 4, 5]
[2, 3, 4, 5, 6]
[3, 4, 5, 6, 7]
[4, 5, 6, 7, 6]
[5, 6, 7, 8, 7]
LM("abc-q","xyz-",maliyetler=(1,1,2)) için fark: 7
==>3 değişiklik ve 1 sok=7

[0, 2, 4, 6, 8, 10]
[2, 1, 3, 5, 7, 9]
[4, 3, 2, 4, 6, 8]
[6, 5, 4, 3, 5, 7]
[8, 7, 6, 5, 3, 5]
LM("abc-","xyz-w",maliyetler=(2,2,1)) için fark: 5
==>3 değişiklik ve 1 sil=5

[0, 2, 4, 6, 8]
[1, 3, 5, 7, 9]
[2, 4, 6, 8, 10]
[3, 5, 7, 9, 11]
LM("abc","xyz-",maliyetler=(1,2,3)) için fark: 11
==>3 değişiklik ve 1 sok=11

[0, 2, 4, 6]
[1, 3, 5, 7]
[2, 4, 6, 8]
[3, 5, 7, 9]
[4, 6, 8, 10]
LM("abc-","xyz",maliyetler=(1,2,3)) için fark: 10
==>3 değişiklik ve 1 ekle=10
"""