# coding:iso-8859-9 Türkçe
# p_31203a.py: linspace() ile x-ekseninin tanımlandığı mathplotlib.pyplot örneği.

import numpy as np
import matplotlib.pyplot as mp

X = np.linspace (0, (2 * np.pi), 100, endpoint=True)
F = np.sin(X)
mp.plot (X, F)
mp.show()
#--------------------------------------------------------------------------------------------

ilkX, sonX = -0.1, (2 * np.pi + 0.1)
ilkY, sonY = -1.1, 1.1
mp.axis ([ilkX, sonX, ilkY, sonY])
mp.xlabel ("X=[0, 2.pi]")
mp.ylabel ("Y=Sin (X)")
mp.plot (X, F)
mp.show()