# coding:iso-8859-9 T�rk�e
# p_20503.py: Linux fork'la ebeveyn/yavru klonlamal� borulama �rne�i.

import os, time, sys
boruAd� = 'borulama'

def yavru( ):
    yaz = os.open (boruAd�, os.O_WRONLY)
    saya� = 0
    while True:
        time.sleep (1)
        os.write (yaz, 'Say� %03d\n' % saya�)
        saya� = (saya�+1) % 5

def ebeveyn( ):
    oku = open (boruAd�, 'r')
    while True:
        sat�r = oku.readline()[:-1]
        print ('Ebeveyn no: %d ald� "%s" saat %s' % (os.getpid(), sat�r, time.time( )) )


if not os.path.exists (boruAd�): os.mkfifo (boruAd�)  
kimlik = os.fork() # Unix, Linux i�in ge�erli...
if kimlik != 0: ebeveyn()
else: yavru()
