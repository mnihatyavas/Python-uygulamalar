# coding:iso-8859-9 Türkçe
# p_31204a.py: Karma-alan gölgeli kosinüs mathplotlib.pyplot örneği.

import numpy as np
import matplotlib.pyplot as mp

n = 256
X = np.linspace (-np.pi, np.pi, n, endpoint=True)
Y = - np.cos (3 * X)
mp.plot (X, Y, color='blue', linewidth=3, alpha=1.00)
mp.fill_between (X, Y, 1, color='orange', alpha=.2)
mp.fill_between (X, Y, -1, color='green', alpha=.2)
mp.fill_between (X, 0, Y, color='magenta', alpha=.5)
mp.xlabel ("X=[-pi, pi]")
mp.ylabel ("Y=-Cos(3X)")
mp.show()