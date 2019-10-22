# coding:iso-8859-9 T�rk�e
# p_20502.py: Linux fork'la tutulan say�n�n tahmini oyunu �rne�i.

import os, sys, random

def gizliSay� (azami):
    dosya = open ("gizliSay�.k�t�k", "w")
    gizliSay� = int (azami * random.random() ) + 1

    tahmin = 0
    while tahmin != gizliSay�:
        tahmin = int (input ("Tahminini gir: ") )
        dosya.write (str (tahmin) + " ")
        if tahmin > 0:
            if tahmin > gizliSay�: print (1)
            elif tahmin < gizliSay�: print (-1)
            else: print (0)
            sys.stdout.flush()       
        else: break # - say�da ��k..
    dosya.close()

def tahminci (azami):
    dosya = open ("tahminci.k�t�k", "w")
    alt = 0
    �st = azami
    sonu� = 1
    while sonu� != 0:
        tahmin = (alt + �st) / 2
        print ("Tavsiye tahmin:", tahmin)
        sys.stdout.flush()       
        dosya.write (str (tahmin) + " ")
        sonu� = int (input ("Tahmininiz: ") )
        if sonu� == -1: alt = tahmin
        elif sonu� == 1: �st = tahmin
        elif sonu� == 0:
            mesaj = "Aranan say� [%d[ bulundu!.." % tahmin
            dosya.write (mesaj)
        else:
            print ("[0/1/-1] d���nda yanl�� bir veri girdiniz")
            dosya.write ("Hatal� giri�")


n = 100
stdin  = sys.stdin.fileno() # Genelde 0: klavye
stdout = sys.stdout.fileno() # Genelde 1: ekran

ebeveynGirdi, yavru��kt�  = os.pipe()
yavruGirdi,  ebeveyn��kt� = os.pipe()
kimlik = os.fork() # Unix-Linux i�in ge�erlidir...
if kimlik:
    # ebeveyn i�lemi...
    os.close (yavru��kt�)
    os.close (yavruGirdi)
    os.dup2 (ebeveynGirdi,  stdin)
    os.dup2 (ebeveyn��kt�, stdout)
    gizliSay� (n)
else:
    # yavru i�lemi...
    os.close (ebeveynGirdi)
    os.close (ebeveyn��kt�)
    os.dup2 (yavruGirdi,  stdin)
    os.dup2 (yavru��kt�, stdout)
    tahminci (n)
