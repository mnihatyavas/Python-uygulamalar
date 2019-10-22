# coding:iso-8859-9 T�rk�e
# p_30606.py: Numpy.random.randint(1,6,size=(5, 4)) ile tesad�fi zar at��l� (5,4) �ekilli matris �rne�i.

import random

zarAt = random.randint (1,6)
print ("At�lan normal tek zar sonucu:", zarAt)

print ("At�lan normal 10 zar listesi:", [random.randint (1, 6) for _ in range (10)] )
#-------------------------------------------------------------------------------------------------

print ("\nAt�lan g�venli 10 zar listesi:", [random.SystemRandom().randint (1, 6) for _ in range (10)] )
#-------------------------------------------------------------------------------------------------

import numpy as np

print ("\nAt�lan Numpy tek zar skalar sonucu:", np.random.randint (1, 7) )
print ("At�lan Numpy tek zar dizisi:", np.random.randint (1, 7, size=1) )
print ("At�lan Numpy 10 zar dizisi:", np.random.randint (1, 7, size=10) )
print ("At�lan Numpy 10 zar dizisi:", np.random.randint (1, 7, size=(10,)) ) # �ncekiyle ayn�....

A = np.random.randint (1, 7, size=(5, 4))
print ("\nAt�lan Numpy (5,4) matrisi:\n", A, "==>", A.shape, sep="")



"""��kt�:
>python p_30605.py
At�lan normal tek zar sonucu: 3
At�lan normal 10 zar listesi: [3, 4, 6, 3, 1, 4, 3, 3, 4, 5]

At�lan g�venli 10 zar listesi: [6, 5, 3, 6, 6, 5, 5, 6, 2, 5]

At�lan Numpy tek zar skalar sonucu: 2
At�lan Numpy tek zar dizisi: [3]
At�lan Numpy 10 zar dizisi: [6 2 2 2 4 4 1 5 6 2]
At�lan Numpy 10 zar dizisi: [5 4 2 1 4 6 3 6 3 3]

At�lan Numpy (5,4) matrisi:
[[6 6 2 3]
 [2 3 4 3]
 [1 3 1 4]
 [5 5 3 2]
 [2 2 5 5]]==>(5, 4)
"""