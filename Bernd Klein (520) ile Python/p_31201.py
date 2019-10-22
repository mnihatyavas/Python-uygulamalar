# coding:iso-8859-9 Türkçe
# p_31201.py: Python mathplotlib.pyplot altmodüllü grafik çizim örneği.

import matplotlib.pyplot as mp

mp.plot ([-1, -4.5, 16, 23]) # x değerleri endekslerdir: (0, 1, 2, 3)
mp.show() # .png dosyası olarak save/saklanabilir...
#input ("Ent: ") # Üstteki grafiği kaparsanız...
#----------------------------------------------------------------------------------------------

mp.plot ([-1, -4.5, 16, 23], "Dr") # Mavi çubuk grafik yerine elmas-kırmızı işaretler...
mp.show()
#input ("Ent: ")
#----------------------------------------------------------------------------------------------

günlerX = list (range (0, 31, 3) )
derecelerY = [25.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1, 32, 34.87, 36]
print ("Temmuz ayı günleri:\n", günlerX, "\n\nSelsiyüs sıcaklık dereceleri:\n", derecelerY, sep="")

mp.plot (günlerX, derecelerY)
mp.show()
#----------------------------------------------------------------------------------------------

mp.plot (günlerX, derecelerY, "--*g") # Yeşil tireli yıldız ...
mp.show()



"""Format parametreleri:
'-'             solid line style
'--'            dashed line style
'-.'            dash-dot line style
':'             dotted line style
'.'             point marker
','             pixel marker
'o'             circle marker
'v'             triangle_down marker
'^'             triangle_up marker
'<'             triangle_left marker
'>'             triangle_right marker
'1'             tri_down marker
'2'             tri_up marker
'3'             tri_left marker
'4'             tri_right marker
's'             square marker
'p'             pentagon marker
'*'             star marker
'h'             hexagon1 marker
'H'             hexagon2 marker
'+'             plus marker
'x'             x marker
'D'             diamond marker
'd'             thin_diamond marker
'|'             vline marker
'_'             hline marker
"""

"""Renk parametreleri:
'b'         blue
'g'         green
'r'         red
'c'         cyan
'm'         magenta
'y'         yellow
'k'         black
'w'         white
"""


"""Çıktı (Herbir grafiğin de .png çıktısı alınabilir):
>python p_31201.py
Temmuz ayı günleri:
[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

Selsiyüs sıcaklık dereceleri:
[25.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1, 32, 34.87, 36]
"""