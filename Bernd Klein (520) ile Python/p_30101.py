# coding:iso-8859-9 Türkçe
# p_30101.py: Derece fahrenhayt çevrimlerinin numpy dizisi ve mathplotlib grafiği örneği.

import numpy as np

selsiyüs = [20.1, 20.8, 21.9, 22.5, 22.7, 22.3, 21.8, 21.2, 20.9, 20.0]
SD = np.array (selsiyüs)

print ("Python selsiyüs listesi:\n", selsiyüs)
print ("Fahrenhayt'a çevrimleri:\n", end=" ")
for i in range (len (selsiyüs)): print ("{:.2f}" .format (selsiyüs[i] * 9 / 5 + 32), end=" ")
print ("\nVeya:\n", end=" ")
fahrenhayt = [ int ((x * 9 / 5 + 32) * 100)  / 100.0 for x in selsiyüs] 
print (fahrenhayt)

print ("\nNumpy selsiyüs liste dizisi:\n", SD)
print ("Fahrenhayt'a çevrimleri:\n", end=" ")
print (SD * 9 / 5 + 32)

print ("\ntype(selsiyüs): ", type (selsiyüs), "\ntype(SD): ", type (SD), sep="")

import matplotlib.pyplot as mp
mp.style.use ("dark_background")
mp.plot (SD)
mp.show()



"""Çıktı:
>python p_30101.py
Python selsiyüs listesi:
 [20.1, 20.8, 21.9, 22.5, 22.7, 22.3, 21.8, 21.2, 20.9, 20.1]
Fahrenhayt'a çevrimleri:
 68.18 69.44 71.42 72.50 72.86 72.14 71.24 70.16 69.62 68.18
Veya:
 [68.18, 69.44, 71.42, 72.5, 72.86, 72.14, 71.24, 70.16, 69.62, 68.18]

Numpy selsiyüs liste dizisi:
 [20.1 20.8 21.9 22.5 22.7 22.3 21.8 21.2 20.9 20.1]
Fahrenhayt'a çevrimleri:
 [68.18 69.44 71.42 72.5  72.86 72.14 71.24 70.16 69.62 68.18]

type(selsiyüs): <class 'list'>
type(SD): <class 'numpy.ndarray'>
"""