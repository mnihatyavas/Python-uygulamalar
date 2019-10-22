# coding:iso-8859-9 Türkçe
# p_31203c.py: Aynı linspace() ile 4 farklı sin, cos ve tan mathplotlib.pyplot örneği.

import numpy as np
import matplotlib.pyplot as mp

X = np.linspace (-2 * np.pi, 2 * np.pi, 100, endpoint=True)
F1 = 3 * np.sin (X)
F2 = np.cos (X)
F3 = 0.3 * np.cos (3 * X)
F4 = 0.3 / np.tan (3 * X)

ilkX, sonX = -2 * np.pi - 0.1, 2 * np.pi + 0.1
ilkY, sonY = -3.1, 3.1
mp.axis ([ilkX, sonX, ilkY, sonY])
mp.plot (X, F1, color="blue", linewidth=2.5, linestyle="-")
mp.plot (X, F2, color="red", linewidth=1.5, linestyle="--")
mp.plot (X, F3, color="magenta", linewidth=3, linestyle=":")
mp.plot (X, F4, color="cyan", linewidth=2, linestyle="-.")
mp.show()
