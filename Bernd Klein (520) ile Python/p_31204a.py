# coding:iso-8859-9 Türkçe
# p_31204a.py: İç-alanı gölgeli sinüs mathplotlib.pyplot örneği.

import numpy as np
import matplotlib.pyplot as mp

n = 256
X = np.linspace (-np.pi, np.pi, n, endpoint=True)
Y = np.sin (2 * X)
mp.plot (X, Y, color='blue',  linewidth= 3, alpha=1.00)
mp.fill_between (X, 0, Y, color='red', alpha=.3)
mp.show()