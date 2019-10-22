# coding:iso-8859-9 Türkçe
# Python 3 - Multithreaded Programming
# Yeni yöntemle sicim yaratma: Thread altsınıfı, override __init__ ve run metodları,
# sicim tip nesneleri yaratma, start ile run'ı koşturma, ve  icabında join ile sicimlerin
# çalışması tamamlanmadan alttaki kodlamaya geçmemenin sağlanması

import threading
import time

çıkışBayrağı = 0 # Zamanı göstererek (0=False) sicimleri tamamlar...

class sicimim (threading.Thread):
    def __init__ (self, sicimNo, sicimAdı, geciktir): #Sicim kurucu metodu...
        threading.Thread.__init__ (self)
        self.sicimNo = sicimNo
        self.sicimAdı = sicimAdı
        self.geciktir = geciktir
    def run (self):
        print ("Başlatılıyor: " + self.sicimAdı)
        zamanıYaz (self.sicimAdı, self.geciktir, 10)
        print ("Sonlandırılıyor: " + self.sicimAdı)

def zamanıYaz (ipAdı, tehir, sayaç):
    while sayaç: # sayaç sayısı kadar döngü tekrarı...
        if çıkışBayrağı: # Zamanı göstermeden (1=True) sicimleri tamamlar...
            break
        time.sleep (tehir)
        print ("[%s: Sayaç(%d) Tarih: %s]" % (ipAdı, sayaç, time.ctime (time.time())))
        sayaç -= 1

# 3 adet sicim tip nesnesi yaratalım...
sicim1 = sicimim (10, "Sicim-1", 3) # Tehir ençok, sonuncu olur...
sicim2 = sicimim (25, "Sicim-2", 1) # Tehir enaz, önce tamamlanır...
sicim3 = sicimim (15, "Sicim-3", 2)

# Sicimleri başlatalım...
sicim1.start()
sicim2.start()
sicim3.start()

# Sicimleri tamamlamadan alttaki kodlamaya geçmesin...
sicim1.join()
sicim2.join()
sicim3.join()

print ("\nSicimler tamamlandı. Programdan çıkılıyor!")
