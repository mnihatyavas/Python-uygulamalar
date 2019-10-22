# coding:iso-8859-9 Türkçe
# p_20502.py: Linux fork'la tutulan sayının tahmini oyunu örneği.

import os, sys, random

def gizliSayı (azami):
    dosya = open ("gizliSayı.kütük", "w")
    gizliSayı = int (azami * random.random() ) + 1

    tahmin = 0
    while tahmin != gizliSayı:
        tahmin = int (input ("Tahminini gir: ") )
        dosya.write (str (tahmin) + " ")
        if tahmin > 0:
            if tahmin > gizliSayı: print (1)
            elif tahmin < gizliSayı: print (-1)
            else: print (0)
            sys.stdout.flush()       
        else: break # - sayıda çık..
    dosya.close()

def tahminci (azami):
    dosya = open ("tahminci.kütük", "w")
    alt = 0
    üst = azami
    sonuç = 1
    while sonuç != 0:
        tahmin = (alt + üst) / 2
        print ("Tavsiye tahmin:", tahmin)
        sys.stdout.flush()       
        dosya.write (str (tahmin) + " ")
        sonuç = int (input ("Tahmininiz: ") )
        if sonuç == -1: alt = tahmin
        elif sonuç == 1: üst = tahmin
        elif sonuç == 0:
            mesaj = "Aranan sayı [%d[ bulundu!.." % tahmin
            dosya.write (mesaj)
        else:
            print ("[0/1/-1] dışında yanlış bir veri girdiniz")
            dosya.write ("Hatalı giriş")


n = 100
stdin  = sys.stdin.fileno() # Genelde 0: klavye
stdout = sys.stdout.fileno() # Genelde 1: ekran

ebeveynGirdi, yavruÇıktı  = os.pipe()
yavruGirdi,  ebeveynÇıktı = os.pipe()
kimlik = os.fork() # Unix-Linux için geçerlidir...
if kimlik:
    # ebeveyn işlemi...
    os.close (yavruÇıktı)
    os.close (yavruGirdi)
    os.dup2 (ebeveynGirdi,  stdin)
    os.dup2 (ebeveynÇıktı, stdout)
    gizliSayı (n)
else:
    # yavru işlemi...
    os.close (ebeveynGirdi)
    os.close (ebeveynÇıktı)
    os.dup2 (yavruGirdi,  stdin)
    os.dup2 (yavruÇıktı, stdout)
    tahminci (n)
