# coding:iso-8859-9 T�rk�e
# p_40801.py: Canvas tuvalinde �oklu �izgiler �rne�i.

from tkinter import *

k�k = Tk()
k�k.title ("Tuval'de �izgiler")

tuvalEni = 250
tuvalBoyu = 100
tuval = Canvas (k�k,
    bg="#476042",
    width=tuvalEni,
    height=tuvalBoyu)
tuval.pack()

x = int (tuvalEni / 2)
y = int (tuvalBoyu / 2)

tuval.create_line (0,y, tuvalEni,y, fill="Red")
tuval.create_line (0,0, tuvalEni,tuvalBoyu, fill="Red")
tuval.create_line (0,tuvalBoyu, tuvalEni,0, fill="Red")
tuval.create_line (x,0, x,tuvalBoyu, fill="Red")

k�k.mainloop()
