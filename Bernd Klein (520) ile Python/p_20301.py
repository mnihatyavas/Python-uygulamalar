# coding:iso-8859-9 T�rk�e
# p_20301.py: Linux'la �atallama y�ntemli klonlama/kopyalama �rne�i.

import os # os mod�l�nde fork() metodu mevcut de�il...

def yavru():
   print ('\nYeni bir �ocuk ',  os.getpid())
   os._exit (0)  

def ebeveyn():
   while True:
      yeniKimlik = os.fork() # fork/�atal bir i�lemin aynen kolonlanmas�/kopyalanmas�d�r (yavru()=ebeveyn() )...
      if yeniKimlik == 0: yavru()
      else:
         kimlikler = (os.getpid(), yeniKimlik)
         print ("ebeveyn: %d, �ocuk: %d\n" % kimlikler)
      cevap = input ("��kmak i�in q/ Yeni �atal i�in c")
      if cevap == 'c': continue
      else: break

ebeveyn()

"""��kt�:
>python p_20301.py
Traceback (most recent call last):
  File "p_20301.py", line 20, in <module>
    ebeveyn()
  File "p_20301.py", line 11, in ebeveyn
    yeniKimlik = os.fork()
AttributeError: module 'os' has no attribute 'fork' # HATA: "os.fork()" metodu mevcut de�il...
"""
