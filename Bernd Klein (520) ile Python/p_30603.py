# coding:iso-8859-9 T�rk�e
# p_30603.py: 1000 adet numpy tesad�fi say�n�n ard���k toplam� ve birlemeli normalle�tirilmi� toplam� �rne�i.

import numpy as np

randomDizi = np.random.random (1000)
toplam = randomDizi.sum()
print ("1000 adet randomDizi'nin toplam�:", toplam)

birlemeliDizi = randomDizi / toplam # �htimal i�lemlerinde kullan�labilir...
print ("1000 adet birlemeliDizi'nin normalle�tirilmi� toplam�:", birlemeliDizi.sum())



"""��kt�:
>python p_30603.py
1000 adet randomDizi'nin toplam�: 504.0364770246135
1000 adet birlemeliDizi'nin normalle�tirilmi� toplam�: 1.0
"""