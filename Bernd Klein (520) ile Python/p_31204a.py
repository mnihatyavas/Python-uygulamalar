# coding:iso-8859-9 T�rk�e
# p_31204a.py: ��-alan� g�lgeli sin�s mathplotlib.pyplot �rne�i.

import numpy as np
import matplotlib.pyplot as mp

n = 256
X = np.linspace (-np.pi, np.pi, n, endpoint=True)
Y = np.sin (2 * X)
mp.plot (X, Y, color='blue',  linewidth= 3, alpha=1.00)
mp.fill_between (X, 0, Y, color='red', alpha=.3)
mp.show()