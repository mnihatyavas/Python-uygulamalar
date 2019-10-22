# coding:iso-8859-9 Türkçe
# p_20503.py: Linux fork'la ebeveyn/yavru klonlamalı borulama örneği.

import os, time, sys
boruAdı = 'borulama'

def yavru( ):
    yaz = os.open (boruAdı, os.O_WRONLY)
    sayaç = 0
    while True:
        time.sleep (1)
        os.write (yaz, 'Sayı %03d\n' % sayaç)
        sayaç = (sayaç+1) % 5

def ebeveyn( ):
    oku = open (boruAdı, 'r')
    while True:
        satır = oku.readline()[:-1]
        print ('Ebeveyn no: %d aldı "%s" saat %s' % (os.getpid(), satır, time.time( )) )


if not os.path.exists (boruAdı): os.mkfifo (boruAdı)  
kimlik = os.fork() # Unix, Linux için geçerli...
if kimlik != 0: ebeveyn()
else: yavru()
