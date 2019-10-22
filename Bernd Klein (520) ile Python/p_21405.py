# coding:iso-8859-9 T�rk�e
# p_21405.py: Kar��la�t�rmal� kelime matrisi varsay�l� 1-1-1 sil-sok-de�i�tir maliyetini de�i�tirme �rne�i.

# maliyetler=(1,1,1): Varsay�lan 1 olan sil, sok, de�i� maliyetleri kullan�c� taraf�ndan belirlenebilir...

def LM (d1, d2, maliyetler = (1, 1, 1) ):
    sat�rlar = len (d1)+1
    s�tunlar = len (d2)+1
    silmeler, sokmalar, de�i�tirmeler = maliyetler

    mesafe = [[0 for x in range (s�tunlar)] for x in range (sat�rlar)]
    for sat�r in range (1, sat�rlar): mesafe [sat�r] [0] = sat�r * silmeler
    for s�tun in range (1, s�tunlar): mesafe [0] [s�tun] = s�tun * sokmalar

    for s�tun in range (1, s�tunlar):
        for sat�r in range (1, sat�rlar):
            if d1 [sat�r-1] == d2 [s�tun-1]: maliyet = 0
            else: maliyet = de�i�tirmeler
            mesafe [sat�r] [s�tun] = min (mesafe [sat�r-1] [s�tun] + silmeler,
                    mesafe [sat�r] [s�tun-1] + sokmalar,
                    mesafe [sat�r-1] [s�tun-1] + maliyet) # de�i�tirmeler...
    for r in range (sat�rlar): print (mesafe [r])

    return mesafe [sat�r] [s�tun]


# Varsay�lan (sil, sok, de�i�tir) = (1, 1, 1):
print ('LM("abc-","xyz-",maliyetler=(1,1,1)) i�in fark:', LM ("abc-", "xyz-"), "\n")

# Maliyetler (sil, sok, de�i�tir) = (1, 1, 2):
print ('LM("abc-q","xyz-",maliyetler=(1,1,2)) i�in fark:', LM ("abc-q", "xyz-", maliyetler=(1, 1, 2)), "\n")

# Maliyetler (sil, sok, de�i�tir) = (2, 2, 1):
print ('LM("abc-","xyz-w",maliyetler=(2,2,1)) i�in fark:', LM ("abc-", "xyz-w", maliyetler=(2, 2, 1)), "\n")

# Maliyetler (sil, sok, de�i�tir) = (1, 2, 3):
print ('LM("abc","xyz-",maliyetler=(1,2,3)) i�in fark:', LM ("abc", "xyz-", maliyetler=(1, 2, 3)), "\n")

# Maliyetler (sil, sok, de�i�tir) = (1, 2, 3):
print ('LM("abc-","xyz",maliyetler=(1,2,3)) i�in fark:', LM ("abc-", "xyz", maliyetler=(1, 2, 3)), "\n")



"""��kt�:
>python p_21405.py
[0, 1, 2, 3, 4]
[1, 1, 2, 3, 4]
[2, 2, 2, 3, 4]
[3, 3, 3, 3, 4]
[4, 4, 4, 4, 3]
LM("abc-","xyz-",maliyetler=(1,1,1)) i�in fark: 3
==>3 de�i�iklik=2

[0, 1, 2, 3, 4]
[1, 2, 3, 4, 5]
[2, 3, 4, 5, 6]
[3, 4, 5, 6, 7]
[4, 5, 6, 7, 6]
[5, 6, 7, 8, 7]
LM("abc-q","xyz-",maliyetler=(1,1,2)) i�in fark: 7
==>3 de�i�iklik ve 1 sok=7

[0, 2, 4, 6, 8, 10]
[2, 1, 3, 5, 7, 9]
[4, 3, 2, 4, 6, 8]
[6, 5, 4, 3, 5, 7]
[8, 7, 6, 5, 3, 5]
LM("abc-","xyz-w",maliyetler=(2,2,1)) i�in fark: 5
==>3 de�i�iklik ve 1 sil=5

[0, 2, 4, 6, 8]
[1, 3, 5, 7, 9]
[2, 4, 6, 8, 10]
[3, 5, 7, 9, 11]
LM("abc","xyz-",maliyetler=(1,2,3)) i�in fark: 11
==>3 de�i�iklik ve 1 sok=11

[0, 2, 4, 6]
[1, 3, 5, 7]
[2, 4, 6, 8]
[3, 5, 7, 9]
[4, 6, 8, 10]
LM("abc-","xyz",maliyetler=(1,2,3)) i�in fark: 10
==>3 de�i�iklik ve 1 ekle=10
"""