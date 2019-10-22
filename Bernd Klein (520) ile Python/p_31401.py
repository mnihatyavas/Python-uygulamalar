# coding:iso-8859-9 Türkçe
# p_31401.py:  Legend söylencelerle grafiklerde fonksiyonların başlık kutuları örneği.

import numpy as np
import matplotlib.pyplot as mp

eksenler = mp.gca()
eksenler.plot ([1, 2, 3, 4]) # mp.plot ([1, 2, 3, 4])
eksenler.legend (['Basit bir çizgi']) # mp.legend (['Basit bir çizgi'])
mp.show()
#------------------------------------------------------------------------------------------------------

X = np.linspace (0, 25, 200)
y1 = np.sin (X)
y2 = np.cos (X)
y3 = np.tan (X)

mp.plot (X, y1, '-b', label='sinüs') # plot label'leri legend'a dah'lolur...
mp.plot (X, y2, '-r', label='kosinüs')
mp.plot (X, y3, '-g', label='tanjant')

mp.legend (loc='upper center')
mp.ylim (-1.5, 2.0) # dikey tam hudutlar...
mp.xlim (0, 25) # yatay tam hudutlar...
mp.show()
#------------------------------------------------------------------------------------------------------

F1 = np.sin (0.5 * X)
F2 = 3 * np.cos (0.8 * X)

mp.plot (X, F1, label="$sin(0.5X)$") #LaTeX legend/söylence...
mp.plot (X, F2, label="$3cos(0.8X)$")

mp.legend (loc='best')
mp.ylim (-3, 3.03)
mp.xlim (0, 25)
mp.show()
#------------------------------------------------------------------------------------------------------

X = np.linspace (-2 * np.pi, 2 * np.pi, 200, endpoint=True)
F1 = np.sin (0.5 * X)
F2 = -3 * np.cos (0.8 * X)

mp.xticks (
    [-6.28, -3.14, 0, 3.14, 6.28],
    ["$-2\pi$", "$-\pi$", "$0$", "$+\pi$", "$+2\pi$"])
mp.yticks ([-3, -2, -1, 0, 1, 2, 3])

mp.plot (X, F1, label="$sin(0.5x)$")
mp.plot (X, F2, label="$-3cos(0.8x)$")

mp.legend (loc='best')
mp.ylim (-3.01, 3.03)
mp.xlim (-6.28, 6.28)
mp.show()