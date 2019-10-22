# coding:iso-8859-9 Türkçe
# p_10802.py: Listelerde =atamalı, +=toplamalı, append'li ve extend'li işlem süreleri kıyaslaması örneği.

import time

n= 20000

başla = time.time()
L= []
for i in range (n): L = L+ [i * 2]
print ("L = L+ [i * 2] yöntemi:", time.time() - başla)

başla = time.time()
L= []
for i in range(n): L += [i * 2]
print ("L += [i * 2] yöntemi:", time.time() - başla)

başla = time.time()
L= []
for i in range(n): L.append (i * 2)
print ("L.append (i * 2) yöntemi:", time.time() - başla)

başla = time.time()
L= []
for i in range(n): L.extend ([i * 2])
print ("L.extend ([i * 2]) yöntemi:", time.time() - başla)


"""Çıktı:
>python p_10802.py
L = L+ [i * 2] yöntemi: 4.684612274169922
L += [i * 2] yöntemi: 0.04679989814758301
L.append (i * 2) yöntemi: 0.031200170516967773
L.extend ([i * 2]) yöntemi: 0.031199932098388672
"""