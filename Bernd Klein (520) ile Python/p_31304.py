# coding:iso-8859-9 T�rk�e
# p_31304.py: Omurgay� ortalama ve LaTeX'le eksen de�erlerini tan�mlama �rne�i.

import numpy as np
import matplotlib.pyplot as mp

X = np.linspace (-2 * np.pi, 2 * np.pi, 100, endpoint=True)
F1 = X * np.sin (X)

eksenler = mp.gca()
eksenler.spines ['top'].set_color ('none')
eksenler.spines ['right'].set_color ('none')

#eksenler.xaxis.set_ticks_position ('bottom') # Varsay�lan...
eksenler.spines ['bottom'].set_position (('data', 0))
#eksenler.yaxis.set_ticks_position ('left') # Varsay�lan...
eksenler.spines ['left'].set_position (('data', 0))

mp.xlabel ("X = [$-2\pi$, $+2\pi$]")
mp.ylabel ("F = X * Sin (X)")

mp.xticks ( # LaTeX r"$-+\pi$" kurallar� kullan�lacak...
    [-6.28, -4.71, -3.14, -1.57, 1.57, 3.14, 4.71, 6.28],
    ["$-2\pi$", "$-3\pi/2$", "$-\pi$", "$-\pi/2$", "$+\pi/2$", "$+\pi$", "$+3\pi/2$", r"$+\pi/2$"])
mp.yticks ([-5, -4, -3, -2, -1, 0, +1, 2])

mp.plot (X, F1)
mp.show()
