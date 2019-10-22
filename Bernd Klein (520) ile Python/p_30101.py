# coding:iso-8859-9 T�rk�e
# p_30101.py: Derece fahrenhayt �evrimlerinin numpy dizisi ve mathplotlib grafi�i �rne�i.

import numpy as np

selsiy�s = [20.1, 20.8, 21.9, 22.5, 22.7, 22.3, 21.8, 21.2, 20.9, 20.0]
SD = np.array (selsiy�s)

print ("Python selsiy�s listesi:\n", selsiy�s)
print ("Fahrenhayt'a �evrimleri:\n", end=" ")
for i in range (len (selsiy�s)): print ("{:.2f}" .format (selsiy�s[i] * 9 / 5 + 32), end=" ")
print ("\nVeya:\n", end=" ")
fahrenhayt = [ int ((x * 9 / 5 + 32) * 100)  / 100.0 for x in selsiy�s] 
print (fahrenhayt)

print ("\nNumpy selsiy�s liste dizisi:\n", SD)
print ("Fahrenhayt'a �evrimleri:\n", end=" ")
print (SD * 9 / 5 + 32)

print ("\ntype(selsiy�s): ", type (selsiy�s), "\ntype(SD): ", type (SD), sep="")

import matplotlib.pyplot as mp
mp.style.use ("dark_background")
mp.plot (SD)
mp.show()



"""��kt�:
>python p_30101.py
Python selsiy�s listesi:
 [20.1, 20.8, 21.9, 22.5, 22.7, 22.3, 21.8, 21.2, 20.9, 20.1]
Fahrenhayt'a �evrimleri:
 68.18 69.44 71.42 72.50 72.86 72.14 71.24 70.16 69.62 68.18
Veya:
 [68.18, 69.44, 71.42, 72.5, 72.86, 72.14, 71.24, 70.16, 69.62, 68.18]

Numpy selsiy�s liste dizisi:
 [20.1 20.8 21.9 22.5 22.7 22.3 21.8 21.2 20.9 20.1]
Fahrenhayt'a �evrimleri:
 [68.18 69.44 71.42 72.5  72.86 72.14 71.24 70.16 69.62 68.18]

type(selsiy�s): <class 'list'>
type(SD): <class 'numpy.ndarray'>
"""