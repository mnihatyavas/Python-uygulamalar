# coding:iso-8859-9 T�rk�e
# p_31301.py: �st'le sa� omurgan�n iptali ve s�f�r eksenli grafik �rne�i.

import numpy as np
import matplotlib.pyplot as mp

X = np.linspace (-2 * np.pi, 2 * np.pi, 200, endpoint=True)
F1 = np.sin (2 * X)
F2 = (2*X**5 + 4*X**4 - 4.8*X**3 + 1.2*X**2 + X + 1) * np.exp (-X**2)

mp.plot (X, F1)
mp.plot (X, F2)
mp.show()


# gca:GetCurrentAxes/CariEksenleriAl...
eksenler = mp.gca()

# �st ve sa� omurga eksenlerini g�r�nmez/renksiz yap...
eksenler.spines ['top'].set_color ('none')
eksenler.spines ['right'].set_color ('none')

# Alt eksen omurgas�n� y=0'a y�kselt...
#eksenler.xaxis.set_ticks_position ('bottom')
eksenler.spines ['bottom'].set_position (('data', 0))

# Sol omurgay� x=0'a ta��...
#eksenler.yaxis.set_ticks_position ('left')
eksenler.spines ['left'].set_position (('data', 0))

mp.plot (X, F1)
mp.plot (X, F2)
mp.show()