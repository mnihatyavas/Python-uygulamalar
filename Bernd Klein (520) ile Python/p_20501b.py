# coding:iso-8859-9 T�rk�e
# p_20501b: Linux fork/�atallamayla ebeveyn-yavru klonlamal� bira oyunu �rne�i.

import os

def yavru (da��t):
    �i�eler = 99
    while True:
        bira = "bira �i�esi"
        duvarda = "duvarda dizilidir."
        biriniAl = "Birini al ve isteyene uzat."
        d�kan = "D�kana git ve tekrar bir kutu bira sat�n al."

        if �i�eler > 0:
            veriler =  (�i�eler, bira, duvarda, biriniAl, �i�eler - 1, bira, duvarda)
            ko�ak = "%2d %s %s\n%2d\n%2d %s %s" % veriler # �lk 99 m�sra i�in ko�ak=117 byte (yeniden hesapla!)...
            os.write (da��t, ko�ak)
            �i�eler -= 1
        else:
            �i�eler = 99
            veriler =  (bira, duvarda, d�kan, �i�eler, bira, duvarda)
            ko�ak = "Maalesef s�f�r %s %s\n%s\n%s\n%2d %s %s" % veriler # D�kandan yenileme m�sras� i�in ko�ak=128 byte (yeniden hesapla!)...
            os.write (da��t, ko�ak)

def ebeveyn():
    yeniden, da��t = os.pipe()
    if os.fork() == 0: # Linux i�indir...
        os.close (yeniden)
        yavru (da��t)
    else:
        os.close (da��t)
        saya� = 1
        yeniden = os.fdopen (yeniden)
        while True:
            print ('Tekerleme no: %d\n%s\n' % (saya�, ko�ak) )
            for i in range (4):
                ko�ak = yeniden.readline()[:-1]
                print ('%s' % (ko�ak) )
            saya� += 1
            print()


ebeveyn()