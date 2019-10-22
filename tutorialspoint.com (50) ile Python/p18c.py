# coding:iso-8859-9 Türkçe
# Python 3 - Multithreaded Programming
# Yeni yöntemle sicim yaratma: Thread altsınıfı, override __init__ ve run metodları,
# sicim tip nesneleri yaratma, start ile run'ı koşturma, icabında join ile sicimlerin
# çalışması tamamlanmadan alttaki kodlamaya geçmemenin sağlanması ve
# lock ile bir sicim tamamlanmadan (senkronizasyon) diğerine geçilmemesi

import threading
import time

class sicimim (threading.Thread):
    def __init__ (self, sicimNo, sicimAdı, tehir): # Kurucu metod...
        threading.Thread.__init__ (self)
        self.sicimNo = sicimNo
        self.sicimAdı = sicimAdı
        self.tehir = tehir
    def run (self):
        print ("Başlatılıyor: " + self.sicimAdı)
        # Sicim kilidi kapatılıp, sicimin tamamlanma bütünlüğü sağlanıyor...
        sicimKilidi.acquire()
        zamanıGöster (self.sicimAdı, self.tehir, 5)
        print ("Sonlandırılıyor: " + self.sicimAdı)
        # Kilidi açıp birsonraki sicime geçiş veriliyor...
        sicimKilidi.release()

def zamanıGöster (ipAdı, beklet, tekrarla):
    while tekrarla:
        time.sleep (beklet)
        print ("%s: Sayaç(%d) Zaman: %s" % (ipAdı, tekrarla, time.ctime (time.time())))
        tekrarla -= 1

sicimKilidi = threading.Lock()
sicimler = []

# Yeni sicimlerimizi yaratalım...
sicim1 = sicimim (1001, "Sicim-1", 2)
sicim2 = sicimim (250, "Sicim-2", 3)
sicim3 = sicimim (1957, "Sicim-3", 1)

# Sicimleri run için başlatalım...
sicim3.start()
sicim1.start()
sicim2.start()

# Sicim listesi yapıp birlikte join (alt koda geçiş bekletmesi) edelim...
sicimler.append (sicim1)
sicimler.append (sicim3)
sicimler.append (sicim2)

for ip in sicimler: ip.join()

print ("\nSicimler tamamlandı; alt kodlamalara geçilebilir...")
