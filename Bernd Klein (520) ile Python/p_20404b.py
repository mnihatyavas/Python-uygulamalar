# coding:iso-8859-9 T�rk�e
# p_20404b.py: �nternet ip adresleriyle haberle�me kontrol� �rne�i.

import os, re, threading

class ipKontrolu (threading.Thread):
   def __init__ (self,ip):
      threading.Thread.__init__ (self)
      self.ip = ip
      self.__ba�ar�l���nlatma = -1

   def run (self):
      kontrol = os.popen ("ping -q -c2 " + self.ip, "r")
      while True:
        sat�r = kontrol.readsat�r()
        if not sat�r: break
        al�nan = re.findall (al�nanPaketler, sat�r)
        if al�nan: self.__ba�ar�l���nlatma = int (al�nan[0])

   def durum (self):
      if self.__ba�ar�l���nlatma == 0: return "cevap yok"
      elif self.__ba�ar�l���nlatma == 1: return "canl�, ancak % 50 paket kayb�"
      elif self.__ba�ar�l���nlatma == 2: return "canl�"
      else: return "adres bulunamad�"


al�nanPaketler = re.compile (r"(\d) al�nd�")
kontrolSonu�lar� = []

for sonek in range(20,70): # A��k internetle ip=192.168.178.20->192.168.178.69 adresleri kontrol edilir...
   ip = "192.168.178." + str (sonek)
   akt�el = ipKontrolu (ip)
   kontrolSonu�lar�.append (akt�el)
   akt�el.start() # run() �al��t�r�l�r...

for ba�lant� in kontrolSonu�lar�:
   ba�lant�.join()
   print (ba�lant�.ip,"adresindeki durum:", ba�lant�.durum() )

# �nternete ba�lan�p bu ip adreslerini kontrol edin...



"""��kt�:
>python p_2-4-4b.py
192.168.178.66 adresindeki durum: adres bulunamad�
192.168.178.67 adresindeki durum: adres bulunamad�
192.168.178.68 adresindeki durum: adres bulunamad�
192.168.178.69 adresindeki durum: adres bulunamad�
"""