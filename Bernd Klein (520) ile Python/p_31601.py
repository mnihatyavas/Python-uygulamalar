# coding:iso-8859-9 T�rk�e
# p_31601.py: S�f�r yo�u�mal� -3/+3 da��l�ml� tesad�fi gauss histogram� �rne�i.

import numpy as np
import matplotlib.pyplot as mp
#from p_315 import Renk

gaussSay�lar� = np.random.normal (size=10000)

mp.title ("Gauss Histogram'�")
mp.xlabel ("Gauss Say�lar�")
mp.ylabel ("Say�lar�n Tekrarlanma S�kl���")
mp.hist (gaussSay�lar�)

mp.show()
#-------------------------------------------------------------------------------------------------------

mp.style.use ("dark_background")

mp.title ("Gauss Histogram'�")
mp.xlabel ("Gauss Say�lar�")
mp.ylabel ("Say�lar�n Tekrarlanma S�kl���")
n, kutular, yamalar = mp.hist (gaussSay�lar�)

mp.show()

print ("Y=n (kutu boyu-tekrar s�kl���) ve toplam frekans:\n", n, " +=", sum(n), sep="")
print ("\nX=kutular:\n", kutular, sep="")
print ("kutular aras� fark (kutu geni�li�i):", (kutular [1] - kutular [0]) )
print ("\nyamalar:", yamalar)
for i in range (len (yamalar)): print ("yama[", i, "]: ", yamalar [i], sep="")


"""��kt�:
>python p_31601.py
Y=n (kutu boyu-tekrar s�kl���) ve toplam frekans:
[  19.  159.  639. 1844. 2871. 2518. 1393.  459.   89.    9.] +=10000.0

X=kutular:
[-3.64670043 -2.89409171 -2.14148299 -1.38887427 -0.63626555  0.11634317
  0.86895189  1.62156061  2.37416933  3.12677805  3.87938677]
kutular aras� fark (kutu geni�li�i): 0.7526087198614606

yamalar: <a list of 10 Patch objects>
yama[0]: Rectangle(xy=(-3.6467, 0), width=0.752609, height=19, angle=0)
yama[1]: Rectangle(xy=(-2.89409, 0), width=0.752609, height=159, angle=0)
yama[2]: Rectangle(xy=(-2.14148, 0), width=0.752609, height=639, angle=0)
yama[3]: Rectangle(xy=(-1.38887, 0), width=0.752609, height=1844, angle=0)
yama[4]: Rectangle(xy=(-0.636266, 0), width=0.752609, height=2871, angle=0)
yama[5]: Rectangle(xy=(0.116343, 0), width=0.752609, height=2518, angle=0)
yama[6]: Rectangle(xy=(0.868952, 0), width=0.752609, height=1393, angle=0)
yama[7]: Rectangle(xy=(1.62156, 0), width=0.752609, height=459, angle=0)
yama[8]: Rectangle(xy=(2.37417, 0), width=0.752609, height=89, angle=0)
yama[9]: Rectangle(xy=(3.12678, 0), width=0.752609, height=9, angle=0)
"""