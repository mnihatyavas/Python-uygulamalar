# coding:iso-8859-9 Türkçe
# Python 3 - Multithreaded Programming
# Yeni yöntemle sicim yaratma: Thread altsınıfı, override __init__ ve run metodları,
# sicim tip nesneleri yaratma, start ile run'ı koşturma, icabında join ile sicimlerin
# çalışması tamamlanmadan alttaki kodlamaya geçmemenin sağlanması,
# lock ile bir sicim tamamlanmadan (senkronizasyon) diğerine geçilmemesi,
# liste ile çoklu sicimlerde döngüyle işlem kolaylığı sağlanması

import threading
import time
#import queue ==> Sorunlu, sadece son sicimi işliyor, tüm sicimleri değil...

class sicimim (threading.Thread):
    def __init__ (self, sicimNo, sicimAdı):
        threading.Thread.__init__ (self)
        self.sicimNo = sicimNo
        self.sicimAdı = sicimAdı
    def run (self):
        print ("Başlıyor: " + self.sicimAdı)
        kilit.acquire()
        veriİşleme (self.sicimAdı)
        print ("Sonlanıyor: " + self.sicimAdı)
        kilit.release()

def veriİşleme (ipAdı):
    for i in range (8):
        print ("%s: (%s)inci kez işleniyor [Zaman: %s]" % (ipAdı, işlemAdı[i], time.ctime (time.time()) ))
    time.sleep (2)

sicimAdlarıListesi = ["Sicim-1", "Sicim-2", "Sicim-3", "Sicim-4", "Sicim-5"]
işlemAdı= ["Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz"]
sicimler = []
sicimNo = 1
kilit = threading.Lock()

# Sicimleri yaratıp başlatalım...
for ad in sicimAdlarıListesi:
    sicim = sicimim (sicimNo, ad)
    sicim.start()
    sicimler.append (sicim)
    sicimNo += 1

# Tüm sicimler tamamlanınca alt kodlamaya geçsin...
for ip in sicimler: ip.join()

print ("Sicimler tamamlandı; program sonlanıyor...")
