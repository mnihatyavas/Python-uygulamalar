# coding:iso-8859-9 Türkçe
# p_20301.py: Linux'la çatallama yöntemli klonlama/kopyalama örneği.

import os # os modülünde fork() metodu mevcut değil...

def yavru():
   print ('\nYeni bir çocuk ',  os.getpid())
   os._exit (0)  

def ebeveyn():
   while True:
      yeniKimlik = os.fork() # fork/çatal bir işlemin aynen kolonlanması/kopyalanmasıdır (yavru()=ebeveyn() )...
      if yeniKimlik == 0: yavru()
      else:
         kimlikler = (os.getpid(), yeniKimlik)
         print ("ebeveyn: %d, çocuk: %d\n" % kimlikler)
      cevap = input ("Çıkmak için q/ Yeni çatal için c")
      if cevap == 'c': continue
      else: break

ebeveyn()

"""Çıktı:
>python p_20301.py
Traceback (most recent call last):
  File "p_20301.py", line 20, in <module>
    ebeveyn()
  File "p_20301.py", line 11, in ebeveyn
    yeniKimlik = os.fork()
AttributeError: module 'os' has no attribute 'fork' # HATA: "os.fork()" metodu mevcut değil...
"""
