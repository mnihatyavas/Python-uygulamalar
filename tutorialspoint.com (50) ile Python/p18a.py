# coding:iso-8859-9 T�rk�e
# Python 3 - Multithreaded Programming
# Eski y�ntemle sicim yaratma...

import _thread
import time

# Sicim i�in bir fonksiyon tan�mlayal�m...
def zaman�Yaz (sicimAd�, tehir):
    saya� = 0
    while saya� < 10:
        time.sleep (tehir)
        saya� += 1
        print ("[%s: Saya�(%d) Tarih: %s]" % (sicimAd�, saya�, time.ctime (time.time())))
        if saya� == 10:
            print ("-->%s sonland�" % sicimAd�)

# 3 farkl� sicim yaratal�m...
try:
     _thread.start_new_thread (zaman�Yaz, ("Sicim-1", 1, ))
     _thread.start_new_thread (zaman�Yaz, ("Sicim-2", 3, ))
     _thread.start_new_thread (zaman�Yaz, ("Sicim-3", 2, ))
except:
    print ("HATA: Sicim ba�latma hatas�")

while True: # Sonsuz d�ng�; ^C ile ��k�n...
    pass