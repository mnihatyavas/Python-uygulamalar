# coding:iso-8859-9 Türkçe
# p_40801.py: Canvas tuvalinde çoklu çizgiler örneği.

from tkinter import *

kök = Tk()
kök.title ("Tuval'de Çizgiler")

tuvalEni = 250
tuvalBoyu = 100
tuval = Canvas (kök,
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

kök.mainloop()
