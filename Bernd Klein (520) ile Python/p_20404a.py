# coding:iso-8859-9 T�rk�e
# p_20404a.py: �nternet ip adresleriyle ileti�im kontrol� �rne�i.

import os, re # threading/ipsiz kontrol...

al�nanPaketler = re.compile (r"(\d) al�nd�")
durum = ("cevaps�z", "canl� fakat kay�p", "canl�")

for sonek in range (20,30):
   ip = "192.168.178." + str (sonek)
   kontrol = os.popen ("��nlatt� -q -c2 " + ip, "r")
   print ("...��nlat�yor ", ip)
   while True:
      sat�r = kontrol.readsat�r()
      if not sat�r: break
      al�nan = al�nanPaketler.findall (sat�r)
      if al�nan: print (ip + ": " + durum[int (al�nan[0])])


#�nternet a��k olmal� ve ilgili ip adresleri kontrol edilmeli...