# coding:iso-8859-9 Türkçe
# Python 3 - Multithreaded Programming
# Eski yöntemle sicim yaratma...

import _thread
import time

# Sicim için bir fonksiyon tanımlayalım...
def zamanıYaz (sicimAdı, tehir):
    sayaç = 0
    while sayaç < 10:
        time.sleep (tehir)
        sayaç += 1
        print ("[%s: Sayaç(%d) Tarih: %s]" % (sicimAdı, sayaç, time.ctime (time.time())))
        if sayaç == 10:
            print ("-->%s sonlandı" % sicimAdı)

# 3 farklı sicim yaratalım...
try:
     _thread.start_new_thread (zamanıYaz, ("Sicim-1", 1, ))
     _thread.start_new_thread (zamanıYaz, ("Sicim-2", 3, ))
     _thread.start_new_thread (zamanıYaz, ("Sicim-3", 2, ))
except:
    print ("HATA: Sicim başlatma hatası")

while True: # Sonsuz döngü; ^C ile çıkın...
    pass