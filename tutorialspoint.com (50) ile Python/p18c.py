# coding:iso-8859-9 T�rk�e
# Python 3 - Multithreaded Programming
# Yeni y�ntemle sicim yaratma: Thread alts�n�f�, override __init__ ve run metodlar�,
# sicim tip nesneleri yaratma, start ile run'� ko�turma, icab�nda join ile sicimlerin
# �al��mas� tamamlanmadan alttaki kodlamaya ge�memenin sa�lanmas� ve
# lock ile bir sicim tamamlanmadan (senkronizasyon) di�erine ge�ilmemesi

import threading
import time

class sicimim (threading.Thread):
    def __init__ (self, sicimNo, sicimAd�, tehir): # Kurucu metod...
        threading.Thread.__init__ (self)
        self.sicimNo = sicimNo
        self.sicimAd� = sicimAd�
        self.tehir = tehir
    def run (self):
        print ("Ba�lat�l�yor: " + self.sicimAd�)
        # Sicim kilidi kapat�l�p, sicimin tamamlanma b�t�nl��� sa�lan�yor...
        sicimKilidi.acquire()
        zaman�G�ster (self.sicimAd�, self.tehir, 5)
        print ("Sonland�r�l�yor: " + self.sicimAd�)
        # Kilidi a��p birsonraki sicime ge�i� veriliyor...
        sicimKilidi.release()

def zaman�G�ster (ipAd�, beklet, tekrarla):
    while tekrarla:
        time.sleep (beklet)
        print ("%s: Saya�(%d) Zaman: %s" % (ipAd�, tekrarla, time.ctime (time.time())))
        tekrarla -= 1

sicimKilidi = threading.Lock()
sicimler = []

# Yeni sicimlerimizi yaratal�m...
sicim1 = sicimim (1001, "Sicim-1", 2)
sicim2 = sicimim (250, "Sicim-2", 3)
sicim3 = sicimim (1957, "Sicim-3", 1)

# Sicimleri run i�in ba�latal�m...
sicim3.start()
sicim1.start()
sicim2.start()

# Sicim listesi yap�p birlikte join (alt koda ge�i� bekletmesi) edelim...
sicimler.append (sicim1)
sicimler.append (sicim3)
sicimler.append (sicim2)

for ip in sicimler: ip.join()

print ("\nSicimler tamamland�; alt kodlamalara ge�ilebilir...")
