# coding:iso-8859-9 Türkçe
# p_31402.py: Grafik üzerine scatter/daire ve annotate/şerhle odaklanma örneği.

import numpy as np
import matplotlib.pyplot as mp

print ("Sinüs 135 derece: 3/2^(1/2) =", 3 * np.sin (3 * np.pi / 4) ) # 3*sin(3*45)=3*0.707=3/2**0.5
# Grafikte bu noktaya (3*135=405 derece=360D+ 45) şerh konulacak...

X = np.linspace (-2 * np.pi, 3 * np.pi, 200, endpoint=True)

F1 = np.sin (X)
F2 = 3 * np.sin (X)

#eksenler = mp.gca()
mp.xticks (
    [-6.28, -3.14, 0, 3.14, 6.28, 3*3.14],
    ["$-2\pi$", "$-\pi$", "$0$", "$+\pi$", "$+2\pi$", "$+3\pi$"] )
mp.yticks ([-3, -1, 0, +1, 3])

mp.xlim (-6.28, 3*3.14)

x = 3 * np.pi / 4
mp.scatter ([x,], [3 * np.sin (x),], 1000, color ='red') # Daire çiz/saçımla...

mp.annotate (# Şerh düş...
    r"$(3\sin(\frac{3\pi}{4}), \frac{3}{\sqrt{2}})$",
    xy=(x, 3 * np.sin (x)), 
    xycoords='data',
    xytext=(+20, +20), 
    textcoords='offset points', 
    fontsize=16,
    arrowprops=dict (facecolor='yellow') )

mp.plot (X, F1, label="$y1=sin(x)$", color="blue", linewidth=3, alpha=0.2)
mp.plot (X, F2, label="$y2=3sin(x)$", color="green", linewidth=3, alpha=0.9)
mp.legend (loc='lower center') # Söylence...
mp.show()
#--------------------------------------------------------------------------------------------------------

mp.xticks (
    [-6.28, -3.14, 0, 3.14, 6.28, 3*3.14],
    ["$-2\pi$", "$-\pi$", "$0$", "$+\pi$", "$+2\pi$", "$+3\pi$"] )
mp.yticks ([-3, -2, -1, 0, 1, 2, 3])
mp.xlim (-6.28, 3*3.14)
mp.scatter ([x,], [3 * np.sin (x),], 1000, color ="Teal") # Daire çiz/saçımla...
mp.annotate (# Şerh düş...
    r"$(3\sin(\frac{3\pi}{4}), \frac{3}{\sqrt{2}})$",
    xy=(x, 3 * np.sin (x)), 
    xycoords='data',
    xytext=(+20, +20), 
    textcoords='offset points', 
    fontsize=16,
    arrowprops=dict (facecolor='yellow', headwidth=45, headlength=10, width=15) )

mp.plot (X, F1, label="$y1=sin(x)$", color="green", linewidth=2, alpha=0.55)
mp.plot (X, F2, label="$y2=3sin(x)$", color="maroon", linewidth=3, alpha=0.95)
mp.legend (loc='lower center') # Söylence...
mp.show()



"""Çıktı:
>python p_31402.py
Sinüs 135 derece: 3/2^(1/2) = 2.121320343559643
"""