# coding:iso-8859-9 T�rk�e
# p_31201.py: Python mathplotlib.pyplot altmod�ll� grafik �izim �rne�i.

import matplotlib.pyplot as mp

mp.plot ([-1, -4.5, 16, 23]) # x de�erleri endekslerdir: (0, 1, 2, 3)
mp.show() # .png dosyas� olarak save/saklanabilir...
#input ("Ent: ") # �stteki grafi�i kaparsan�z...
#----------------------------------------------------------------------------------------------

mp.plot ([-1, -4.5, 16, 23], "Dr") # Mavi �ubuk grafik yerine elmas-k�rm�z� i�aretler...
mp.show()
#input ("Ent: ")
#----------------------------------------------------------------------------------------------

g�nlerX = list (range (0, 31, 3) )
derecelerY = [25.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1, 32, 34.87, 36]
print ("Temmuz ay� g�nleri:\n", g�nlerX, "\n\nSelsiy�s s�cakl�k dereceleri:\n", derecelerY, sep="")

mp.plot (g�nlerX, derecelerY)
mp.show()
#----------------------------------------------------------------------------------------------

mp.plot (g�nlerX, derecelerY, "--*g") # Ye�il tireli y�ld�z ...
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


"""��kt� (Herbir grafi�in de .png ��kt�s� al�nabilir):
>python p_31201.py
Temmuz ay� g�nleri:
[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

Selsiy�s s�cakl�k dereceleri:
[25.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1, 32, 34.87, 36]
"""