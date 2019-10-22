# coding:iso-8859-9 T�rk�e
# p_20401b.py: Sicimlerin tamamlanmas�n� Ent de�il while d�ng� kontrol�yle sa�lama �rne�i.

from _thread import start_new_thread as ip, allocate_lock as kilitle

sicimNo = 0
sicimBa�lad� = False
kilit = kilitle()

def karek�k (a):
    global sicimNo, sicimBa�lad�

    kilit.acquire()
    sicimNo += 1
    sicimBa�lad� = True
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

print ("Karek�k (9, 99, 999, 1733):\n")
ip (karek�k, (99,) )
ip (karek�k, (999,) )
ip (karek�k, (1733,) )

# input ("Ent:") ==>Ent yerine alttaki d�ng�lerle sicimlerin tamamlanmas� beklenir...

while not sicimBa�lad�: pass # sicimBa�lad�=False ise d�ng� s�rer...
while sicimNo > 0: pass # sicimNo>0 ise d�ng� s�rer...
print ("\nKarek�kler:", 9**0.5, 99**0.5, 999**0.5, 1733**0.5)

"""��kt�:
>python p_20401b.py
Karek�k (9, 99, 999, 1733):

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

Karek�kler: 3.0 9.9498743710662 31.606961258558215 41.6293165929973
"""