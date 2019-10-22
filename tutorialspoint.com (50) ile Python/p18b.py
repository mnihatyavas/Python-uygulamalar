# coding:iso-8859-9 T�rk�e
# Python 3 - Multithreaded Programming
# Yeni y�ntemle sicim yaratma: Thread alts�n�f�, override __init__ ve run metodlar�,
# sicim tip nesneleri yaratma, start ile run'� ko�turma, ve  icab�nda join ile sicimlerin
# �al��mas� tamamlanmadan alttaki kodlamaya ge�memenin sa�lanmas�

import threading
import time

��k��Bayra�� = 0 # Zaman� g�stererek (0=False) sicimleri tamamlar...

class sicimim (threading.Thread):
    def __init__ (self, sicimNo, sicimAd�, geciktir): #Sicim kurucu metodu...
        threading.Thread.__init__ (self)
        self.sicimNo = sicimNo
        self.sicimAd� = sicimAd�
        self.geciktir = geciktir
    def run (self):
        print ("Ba�lat�l�yor: " + self.sicimAd�)
        zaman�Yaz (self.sicimAd�, self.geciktir, 10)
        print ("Sonland�r�l�yor: " + self.sicimAd�)

def zaman�Yaz (ipAd�, tehir, saya�):
    while saya�: # saya� say�s� kadar d�ng� tekrar�...
        if ��k��Bayra��: # Zaman� g�stermeden (1=True) sicimleri tamamlar...
            break
        time.sleep (tehir)
        print ("[%s: Saya�(%d) Tarih: %s]" % (ipAd�, saya�, time.ctime (time.time())))
        saya� -= 1

# 3 adet sicim tip nesnesi yaratal�m...
sicim1 = sicimim (10, "Sicim-1", 3) # Tehir en�ok, sonuncu olur...
sicim2 = sicimim (25, "Sicim-2", 1) # Tehir enaz, �nce tamamlan�r...
sicim3 = sicimim (15, "Sicim-3", 2)

# Sicimleri ba�latal�m...
sicim1.start()
sicim2.start()
sicim3.start()

# Sicimleri tamamlamadan alttaki kodlamaya ge�mesin...
sicim1.join()
sicim2.join()
sicim3.join()

print ("\nSicimler tamamland�. Programdan ��k�l�yor!")
