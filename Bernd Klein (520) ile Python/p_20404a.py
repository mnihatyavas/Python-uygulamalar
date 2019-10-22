# coding:iso-8859-9 Türkçe
# p_20404a.py: İnternet ip adresleriyle iletişim kontrolü örneği.

import os, re # threading/ipsiz kontrol...

alınanPaketler = re.compile (r"(\d) alındı")
durum = ("cevapsız", "canlı fakat kayıp", "canlı")

for sonek in range (20,30):
   ip = "192.168.178." + str (sonek)
   kontrol = os.popen ("çınlattı -q -c2 " + ip, "r")
   print ("...çınlatıyor ", ip)
   while True:
      satır = kontrol.readsatır()
      if not satır: break
      alınan = alınanPaketler.findall (satır)
      if alınan: print (ip + ": " + durum[int (alınan[0])])


#İnternet açık olmalı ve ilgili ip adresleri kontrol edilmeli...