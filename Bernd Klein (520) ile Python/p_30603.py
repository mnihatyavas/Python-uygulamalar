# coding:iso-8859-9 Türkçe
# p_30603.py: 1000 adet numpy tesadüfi sayının ardışık toplamı ve birlemeli normalleştirilmiş toplamı örneği.

import numpy as np

randomDizi = np.random.random (1000)
toplam = randomDizi.sum()
print ("1000 adet randomDizi'nin toplamı:", toplam)

birlemeliDizi = randomDizi / toplam # İhtimal işlemlerinde kullanılabilir...
print ("1000 adet birlemeliDizi'nin normalleştirilmiş toplamı:", birlemeliDizi.sum())



"""Çıktı:
>python p_30603.py
1000 adet randomDizi'nin toplamı: 504.0364770246135
1000 adet birlemeliDizi'nin normalleştirilmiş toplamı: 1.0
"""