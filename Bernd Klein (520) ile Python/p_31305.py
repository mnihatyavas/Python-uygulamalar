# coding:iso-8859-9 Türkçe
# p_31305.py: Dikey ve yatay etiketleri ve başlığı tasarlama örneği.

import numpy as np
import matplotlib.pyplot as mp

X = np.linspace (-2 * np.pi, 2 * np.pi, 200, endpoint=True)
F1 = np.sin (X**3 / 2)
F2 = np.sin (X)

eksenler = mp.gca() # GetCurrentAxis...
eksenler.spines ['top'].set_color ('none') # İptal...
eksenler.spines ['right'].set_color ('none') # İptal...

#eksenler.xaxis.set_ticks_position ('bottom') # Varsayılan...
eksenler.spines ['bottom'].set_position (('data',0))
#eksenler.yaxis.set_ticks_position ('left') # Varsayılan...
eksenler.spines ['left'].set_position (('data',0))

mp.xticks ( # LaTeX $-+\pi$
    [-6.28, -4.71, -3.14, -1.57, 1.57, 3.14, 4.71, 6.28],
    ["$-2\pi$", "$-3\pi/2$", "$-\pi$", "$-\pi/2$", "$+\pi/2$", "$+\pi$", "$+3\pi/2$", r"$+\pi/2$"])
mp.yticks ([-1, -0.5, 0, +0.5, 1])

for çentikX in eksenler.get_xticklabels(): # Yatay çentik ebat ve renkleri...
    çentikX.set_fontsize (10)
    çentikX.set_bbox (dict (facecolor='Yellow', edgecolor='red', alpha=.5 ))
for çentikY in eksenler.get_yticklabels(): # Dikey çentik ebat ve renkleri...
    çentikY.set_fontsize (14)
    çentikY.set_bbox (dict (facecolor='green', edgecolor='Red', alpha=0.5 ))

mp.plot (X, F1, label="f=sin(x**3/2)")
mp.plot (X, F2, label="f=sin(x)")
mp.legend (loc='lower left')
"""Mümkün "loc" konumları:
best, upper right, upper left, lower left, lower right, right, center left,
center right, lower center, upper center, center
"""
mp.show()
#----------------------------------------------------------------------------------------------------
etiketlerY = eksenler.get_xticklabels()
print (etiketlerY)
print()
for xÇentik in etiketlerY: print (xÇentik)
print()
liste = [çentikX.get_text() for çentikX in etiketlerY]
print (liste)
print()
for eleman in liste: print (eleman, end=" ")



"""Çıktı:
>python p_31305.py
<a list of 8 Text xticklabel objects>

Text(-6.28, 0, '$-2\\pi$')
Text(-4.71, 0, '$-3\\pi/2$')
Text(-3.14, 0, '$-\\pi$')
Text(-1.57, 0, '$-\\pi/2$')
Text(1.57, 0, '$+\\pi/2$')
Text(3.14, 0, '$+\\pi$')
Text(4.71, 0, '$+3\\pi/2$')
Text(6.28, 0, '$+\\pi/2$')

['$-2\\pi$', '$-3\\pi/2$', '$-\\pi$', '$-\\pi/2$', '$+\\pi/2$', '$+\\pi$', '$+3\\pi/2$', '$+\\pi/2$']

$-2\pi$ $-3\pi/2$ $-\pi$ $-\pi/2$ $+\pi/2$ $+\pi$ $+3\pi/2$ $+\pi/2$
"""