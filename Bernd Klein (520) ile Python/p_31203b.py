# coding:iso-8859-9 T�rk�e
# p_31203b.py: Ayn� linspace() ile 4 farkl� mathplotlib.pyplot �rne�i.

import numpy as np
import matplotlib.pyplot as mp


X = np.linspace (-2 * np.pi, 2 * np.pi, 100, endpoint=True)
F1 = 3 * np.sin (X)
F2 = 0.3 * np.sin (X)
F3 = 3 * np.sin (2 * X)
F4 = 0.3 * np.sin (3 * X)

ilkX, sonX = -2 * np.pi - 0.1, 2 * np.pi + 0.1
ilkY, sonY = -3.1, 3.1
mp.axis ([ilkX, sonX, ilkY, sonY])
mp.plot (X, F1) # mavi
mp.plot (X, F2) # turuncu
mp.plot (X, F3) # ye�il
mp.plot (X, F4) # k�rm�z�
mp.show()
#-----------------------------------------------------------------------------------------------

mp.plot (X, F1, "r--d") # k�rm�z�
mp.plot (X, F2, "bx") # mavi
mp.plot (X, F3, "g--*") # ye�il
mp.plot (X, F4, "y.") # sar�
mp.show()
