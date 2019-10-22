# coding:iso-8859-9 Türkçe
# p_30103a.py: Aynı dizisel toplamın python ve numpy işlem süratlerinin time modülüyle karşılaştırılması örneği.

import numpy as np
import time

elemanSayısı = 1000001

def pythonFonksiyonu():
    t1 = time.time() # ilk zaman...
    X = range (elemanSayısı)
    Y = range (elemanSayısı)
    Z = [X [i] + Y [i] for i in range (len (X)) ]
    #print (X[0],Y[0],Z[0])
    #print (X[1000000],Y[1000000],Z[1000000])
    return time.time() - t1 # işlem zamanı...

def numpyFonksiyonu():
    t1 = time.time() # başlangıç zamanı...
    X = np.arange (elemanSayısı)
    Y = np.arange (elemanSayısı)
    Z = X + Y
    #print (X[0],Y[0],Z[0])
    #print (X[0001000],Y[1000000],Z[1000000])
    return time.time() - t1 # işlem için geçen zaman...

t1 = pythonFonksiyonu()
t2 = numpyFonksiyonu()

print ("Python ve numpy işlem zamanları:", t1, t2)
print ("Bu örnekte numpy python'dan tam [" + str ( t1 / t2) + "] misli hızlıdır!")



"""Çıktı:
>python p_30103a.py
Python ve numpy işlem zamanları: 3.322805643081665 0.031200170516967773
Bu örnekte numpy python'dan tam [106.49959881708351] misli hızlıdır!

>python p_30103a.py  ** TEKRAR **
Python ve numpy işlem zamanları: 2.7300047874450684 0.015599966049194336
Bu örnekte numpy python'dan tam [175.00068774739802] misli hızlıdır!

>python p_30103a.py  ** TEKRAR **
Python ve numpy işlem zamanları: 2.88600492477417 0.015600204467773438
Bu örnekte numpy python'dan tam [184.99789094021273] misli hızlıdır!

>python p_30103a.py  ** TEKRAR **
Python ve numpy işlem zamanları: 5.038808822631836 0.015599727630615234
Bu örnekte numpy python'dan tam [323.006205104692] misli hızlıdır!
"""