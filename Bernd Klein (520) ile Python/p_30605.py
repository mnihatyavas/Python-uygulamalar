# coding:iso-8859-9 Türkçe
# p_30606.py: Numpy.random.randint(1,6,size=(5, 4)) ile tesadüfi zar atışlı (5,4) şekilli matris örneği.

import random

zarAt = random.randint (1,6)
print ("Atılan normal tek zar sonucu:", zarAt)

print ("Atılan normal 10 zar listesi:", [random.randint (1, 6) for _ in range (10)] )
#-------------------------------------------------------------------------------------------------

print ("\nAtılan güvenli 10 zar listesi:", [random.SystemRandom().randint (1, 6) for _ in range (10)] )
#-------------------------------------------------------------------------------------------------

import numpy as np

print ("\nAtılan Numpy tek zar skalar sonucu:", np.random.randint (1, 7) )
print ("Atılan Numpy tek zar dizisi:", np.random.randint (1, 7, size=1) )
print ("Atılan Numpy 10 zar dizisi:", np.random.randint (1, 7, size=10) )
print ("Atılan Numpy 10 zar dizisi:", np.random.randint (1, 7, size=(10,)) ) # Öncekiyle aynı....

A = np.random.randint (1, 7, size=(5, 4))
print ("\nAtılan Numpy (5,4) matrisi:\n", A, "==>", A.shape, sep="")



"""Çıktı:
>python p_30605.py
Atılan normal tek zar sonucu: 3
Atılan normal 10 zar listesi: [3, 4, 6, 3, 1, 4, 3, 3, 4, 5]

Atılan güvenli 10 zar listesi: [6, 5, 3, 6, 6, 5, 5, 6, 2, 5]

Atılan Numpy tek zar skalar sonucu: 2
Atılan Numpy tek zar dizisi: [3]
Atılan Numpy 10 zar dizisi: [6 2 2 2 4 4 1 5 6 2]
Atılan Numpy 10 zar dizisi: [5 4 2 1 4 6 3 6 3 3]

Atılan Numpy (5,4) matrisi:
[[6 6 2 3]
 [2 3 4 3]
 [1 3 1 4]
 [5 5 3 2]
 [2 2 5 5]]==>(5, 4)
"""