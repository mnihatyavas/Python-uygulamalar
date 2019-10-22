# coding:iso-8859-9 T�rk�e
# p_30103a.py: Ayn� dizisel toplam�n python ve numpy i�lem s�ratlerinin time mod�l�yle kar��la�t�r�lmas� �rne�i.

import numpy as np
import time

elemanSay�s� = 1000001

def pythonFonksiyonu():
    t1 = time.time() # ilk zaman...
    X = range (elemanSay�s�)
    Y = range (elemanSay�s�)
    Z = [X [i] + Y [i] for i in range (len (X)) ]
    #print (X[0],Y[0],Z[0])
    #print (X[1000000],Y[1000000],Z[1000000])
    return time.time() - t1 # i�lem zaman�...

def numpyFonksiyonu():
    t1 = time.time() # ba�lang�� zaman�...
    X = np.arange (elemanSay�s�)
    Y = np.arange (elemanSay�s�)
    Z = X + Y
    #print (X[0],Y[0],Z[0])
    #print (X[0001000],Y[1000000],Z[1000000])
    return time.time() - t1 # i�lem i�in ge�en zaman...

t1 = pythonFonksiyonu()
t2 = numpyFonksiyonu()

print ("Python ve numpy i�lem zamanlar�:", t1, t2)
print ("Bu �rnekte numpy python'dan tam [" + str ( t1 / t2) + "] misli h�zl�d�r!")



"""��kt�:
>python p_30103a.py
Python ve numpy i�lem zamanlar�: 3.322805643081665 0.031200170516967773
Bu �rnekte numpy python'dan tam [106.49959881708351] misli h�zl�d�r!

>python p_30103a.py  ** TEKRAR **
Python ve numpy i�lem zamanlar�: 2.7300047874450684 0.015599966049194336
Bu �rnekte numpy python'dan tam [175.00068774739802] misli h�zl�d�r!

>python p_30103a.py  ** TEKRAR **
Python ve numpy i�lem zamanlar�: 2.88600492477417 0.015600204467773438
Bu �rnekte numpy python'dan tam [184.99789094021273] misli h�zl�d�r!

>python p_30103a.py  ** TEKRAR **
Python ve numpy i�lem zamanlar�: 5.038808822631836 0.015599727630615234
Bu �rnekte numpy python'dan tam [323.006205104692] misli h�zl�d�r!
"""