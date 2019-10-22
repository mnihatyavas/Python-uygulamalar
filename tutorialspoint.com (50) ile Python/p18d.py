# coding:iso-8859-9 T�rk�e
# Python 3 - Multithreaded Programming
# Yeni y�ntemle sicim yaratma: Thread alts�n�f�, override __init__ ve run metodlar�,
# sicim tip nesneleri yaratma, start ile run'� ko�turma, icab�nda join ile sicimlerin
# �al��mas� tamamlanmadan alttaki kodlamaya ge�memenin sa�lanmas�,
# lock ile bir sicim tamamlanmadan (senkronizasyon) di�erine ge�ilmemesi,
# liste ile �oklu sicimlerde d�ng�yle i�lem kolayl��� sa�lanmas�

import threading
import time
#import queue ==> Sorunlu, sadece son sicimi i�liyor, t�m sicimleri de�il...

class sicimim (threading.Thread):
    def __init__ (self, sicimNo, sicimAd�):
        threading.Thread.__init__ (self)
        self.sicimNo = sicimNo
        self.sicimAd� = sicimAd�
    def run (self):
        print ("Ba�l�yor: " + self.sicimAd�)
        kilit.acquire()
        veri��leme (self.sicimAd�)
        print ("Sonlan�yor: " + self.sicimAd�)
        kilit.release()

def veri��leme (ipAd�):
    for i in range (8):
        print ("%s: (%s)inci kez i�leniyor [Zaman: %s]" % (ipAd�, i�lemAd�[i], time.ctime (time.time()) ))
    time.sleep (2)

sicimAdlar�Listesi = ["Sicim-1", "Sicim-2", "Sicim-3", "Sicim-4", "Sicim-5"]
i�lemAd�= ["Bir", "�ki", "��", "D�rt", "Be�", "Alt�", "Yedi", "Sekiz"]
sicimler = []
sicimNo = 1
kilit = threading.Lock()

# Sicimleri yarat�p ba�latal�m...
for ad in sicimAdlar�Listesi:
    sicim = sicimim (sicimNo, ad)
    sicim.start()
    sicimler.append (sicim)
    sicimNo += 1

# T�m sicimler tamamlan�nca alt kodlamaya ge�sin...
for ip in sicimler: ip.join()

print ("Sicimler tamamland�; program sonlan�yor...")
