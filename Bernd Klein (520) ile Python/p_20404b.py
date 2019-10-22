# coding:iso-8859-9 Türkçe
# p_20404b.py: İnternet ip adresleriyle haberleşme kontrolü örneği.

import os, re, threading

class ipKontrolu (threading.Thread):
   def __init__ (self,ip):
      threading.Thread.__init__ (self)
      self.ip = ip
      self.__başarılıÇınlatma = -1

   def run (self):
      kontrol = os.popen ("ping -q -c2 " + self.ip, "r")
      while True:
        satır = kontrol.readsatır()
        if not satır: break
        alınan = re.findall (alınanPaketler, satır)
        if alınan: self.__başarılıÇınlatma = int (alınan[0])

   def durum (self):
      if self.__başarılıÇınlatma == 0: return "cevap yok"
      elif self.__başarılıÇınlatma == 1: return "canlı, ancak % 50 paket kaybı"
      elif self.__başarılıÇınlatma == 2: return "canlı"
      else: return "adres bulunamadı"


alınanPaketler = re.compile (r"(\d) alındı")
kontrolSonuçları = []

for sonek in range(20,70): # Açık internetle ip=192.168.178.20->192.168.178.69 adresleri kontrol edilir...
   ip = "192.168.178." + str (sonek)
   aktüel = ipKontrolu (ip)
   kontrolSonuçları.append (aktüel)
   aktüel.start() # run() çalıştırılır...

for bağlantı in kontrolSonuçları:
   bağlantı.join()
   print (bağlantı.ip,"adresindeki durum:", bağlantı.durum() )

# İnternete bağlanıp bu ip adreslerini kontrol edin...



"""Çıktı:
>python p_2-4-4b.py
192.168.178.66 adresindeki durum: adres bulunamadı
192.168.178.67 adresindeki durum: adres bulunamadı
192.168.178.68 adresindeki durum: adres bulunamadı
192.168.178.69 adresindeki durum: adres bulunamadı
"""