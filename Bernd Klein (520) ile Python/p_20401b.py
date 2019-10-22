# coding:iso-8859-9 Türkçe
# p_20401b.py: Sicimlerin tamamlanmasını Ent değil while döngü kontrolüyle sağlama örneği.

from _thread import start_new_thread as ip, allocate_lock as kilitle

sicimNo = 0
sicimBaşladı = False
kilit = kilitle()

def karekök (a):
    global sicimNo, sicimBaşladı

    kilit.acquire()
    sicimNo += 1
    sicimBaşladı = True
    kilit.release()

    fark = 0.0000001
    eski = 1
    yeni = 1
    while True:
        eski, yeni = yeni, (yeni + a / yeni) / 2.0
        print (eski, yeni)
        if abs (yeni - eski) < fark: break

    kilit.acquire()
    sicimNo -= 1
    kilit.release()

    return yeni

print ("Karekök (9, 99, 999, 1733):\n")
ip (karekök, (99,) )
ip (karekök, (999,) )
ip (karekök, (1733,) )

# input ("Ent:") ==>Ent yerine alttaki döngülerle sicimlerin tamamlanması beklenir...

while not sicimBaşladı: pass # sicimBaşladı=False ise döngü sürer...
while sicimNo > 0: pass # sicimNo>0 ise döngü sürer...
print ("\nKarekökler:", 9**0.5, 99**0.5, 999**0.5, 1733**0.5)

"""Çıktı:
>python p_20401b.py
Karekök (9, 99, 999, 1733):

1 867.0
1 50.0
1 500.0
867.0 434.49942329873124
50.0 25.99
500.0 250.999
434.49942329873124 219.24396055635268
25.99 14.899578684109272
250.999 127.48954776911462
219.24396055635268 113.57419860976081
14.899578684109272 10.772030933542913
127.48954776911462 67.66274213168452
113.57419860976081 64.41647297078916
10.772030933542913 9.98124920731545
67.66274213168452 41.21357261818075
64.41647297078916 45.65976464330739
45.65976464330739 41.80720309343319
41.21357261818075 32.72658006314248
9.98124920731545 9.949923682546618
41.80720309343319 41.62969503982818
32.72658006314248 31.626113065211403
9.949923682546618 9.949874371188393
41.62969503982818 41.62931659471749
31.626113065211403 31.60696705743235
9.949874371188393 9.9498743710662
41.62931659471749 41.6293165929973
31.60696705743235 31.606961258558748
31.606961258558748 31.606961258558215

Karekökler: 3.0 9.9498743710662 31.606961258558215 41.6293165929973
"""