# coding:iso-8859-9 Türkçe
# p_31303.py: Omurgayı ortalama ve eksen değerlerini tanımlama örneği.

import numpy as np
import matplotlib.pyplot as mp

X = np.linspace (-2 * np.pi, 2 * np.pi, 200, endpoint=True)
F1 = np.sin (X**2)
F2 = X * np.sin (X)

eksenler = mp.gca()
eksenler.spines ['top'].set_color ('none')
eksenler.spines ['right'].set_color ('none')
#eksenler.xaxis.set_ticks_position ('bottom')
eksenler.spines ['bottom'].set_position (('data',0))
#eksenler.yaxis.set_ticks_position ('left')
eksenler.spines ['left'].set_position (('data',0))
mp.xlabel ("X=[-2pi, 2pi]")
mp.ylabel ("F1=Sin(x^2), F2=x.Sin(x)")
mp.xticks ( [-6.28, -4.71, -3.14, -1.57, 1.57, 3.14, 4.71, 6.28])
mp.yticks ([-5, -4, -3, -2, -1, 0, 1, 2, 3])
mp.plot (X, F1)
mp.plot (X, F2)
mp.show()