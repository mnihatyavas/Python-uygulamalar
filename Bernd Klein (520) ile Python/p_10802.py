# coding:iso-8859-9 T�rk�e
# p_10802.py: Listelerde =atamal�, +=toplamal�, append'li ve extend'li i�lem s�releri k�yaslamas� �rne�i.

import time

n= 20000

ba�la = time.time()
L= []
for i in range (n): L = L+ [i * 2]
print ("L = L+ [i * 2] y�ntemi:", time.time() - ba�la)

ba�la = time.time()
L= []
for i in range(n): L += [i * 2]
print ("L += [i * 2] y�ntemi:", time.time() - ba�la)

ba�la = time.time()
L= []
for i in range(n): L.append (i * 2)
print ("L.append (i * 2) y�ntemi:", time.time() - ba�la)

ba�la = time.time()
L= []
for i in range(n): L.extend ([i * 2])
print ("L.extend ([i * 2]) y�ntemi:", time.time() - ba�la)


"""��kt�:
>python p_10802.py
L = L+ [i * 2] y�ntemi: 4.684612274169922
L += [i * 2] y�ntemi: 0.04679989814758301
L.append (i * 2) y�ntemi: 0.031200170516967773
L.extend ([i * 2]) y�ntemi: 0.031199932098388672
"""