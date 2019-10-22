# coding:iso-8859-9 Türkçe
# p_30103b.py: Aynı dizisel toplamın python ve numpy işlem süratlerinin timeit modülüyle karşılaştırılması örneği.

import numpy as np
from timeit import Timer as T

elemanSayısı = 1000
listeX = range (elemanSayısı) # [0, 1,..., 999]
listeY = range (elemanSayısı) # [0, 1,..., 999]
npDiziX = np.arange (elemanSayısı) # [0 1 ... 999]
npDiziY = np.arange (elemanSayısı) # [0 1 ... 999]

def pythonFonksiyonu(): listeZ = [listeX [i] + listeY [i] for i in range (len (listeX))] # [0, 2,..., 1998]
def numpyFonksiyonu(): npDiziZ = npDiziX + npDiziY # [0 2 ... 1998]

nesneTimer1 = T ("pythonFonksiyonu()", "from __main__ import pythonFonksiyonu")
nesneTimer2 = T ("numpyFonksiyonu()", "from __main__ import numpyFonksiyonu")

print ("10 kez yinelenen python ve numpy fonksiyonları için geçen zaman\n", "-"*63, sep="")
t1 = nesneTimer1.timeit (10)
t2 = nesneTimer2.timeit (10)
print (t1, t2)
print ("Numpy python'dan [", (t1 / t2), "] misli hızlıdır!", sep="")

print ("\n10 kez yinelenen python ve numpy fonksiyonları için 3 ayrı geçen zamanları\n", "-"*74, sep="")
print (nesneTimer1.repeat (repeat=3, number=10))
print (nesneTimer2.repeat (repeat=3, number=10))



"""Çıktı:
>python p_30103b.py
10 kez yinelenen python ve numpy fonksiyonları için geçen zaman
---------------------------------------------------------------
0.024860263000000105 0.0002556769999999542
Numpy python'dan [97.23308314789581] misli hızlıdır!

10 kez yinelenen python ve numpy fonksiyonları için 3 ayrı geçen zamanları
--------------------------------------------------------------------------
[0.02480827699999999, 0.024741168000000036, 0.024732660999999823]
[0.00022732099999989153, 0.0007259159999999376, 0.0005260049999999961]

>python p_30103b.py  ** TEKRAR **
10 kez yinelenen python ve numpy fonksiyonları için geçen zaman
---------------------------------------------------------------
0.029651971000000055 0.00029395799999987204
Numpy python'dan [100.87145442550623] misli hızlıdır!

10 kez yinelenen python ve numpy fonksiyonları için 3 ayrı geçen zamanları
--------------------------------------------------------------------------
[0.029742237999999865, 0.02953949300000014, 0.02938022600000001]
[0.00027032800000004187, 0.00024953400000016224, 0.00025000699999999654]

>python p_30103b.py  ** TEKRAR **
10 kez yinelenen python ve numpy fonksiyonları için geçen zaman
---------------------------------------------------------------
0.023877251999999904 0.0002296850000000905
Numpy python'dan [103.95651435657747] misli hızlıdır!

10 kez yinelenen python ve numpy fonksiyonları için 3 ayrı geçen zamanları
--------------------------------------------------------------------------
[0.022350748999999892, 0.021839394000000123, 0.021825688000000065]
[0.0002065270000000119, 0.00018573299999991022, 0.00018289699999995968]
"""