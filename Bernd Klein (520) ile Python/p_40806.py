# coding:iso-8859-9 T�rk�e
# p_40806.py: Canvas tuvalinde haz�r ikiliharaitalama �ekilleri �rne�i.

from tkinter import *

k�k = Tk()
k�k.title ("Haz�r �kiliharitalama �ekilleri")

tuvalEni = 300
tuvalBoyu =80

tuval = Canvas (k�k, width=tuvalEni, height=tuvalBoyu, bg="Cyan")
tuval.pack()

ikiliharitalamalar = ["error", "gray75", "gray50", "gray25", "gray12", "hourglass", "info", "questhead", "question", "warning"]
# hata, gri75, gri50, gri25, gri12, kumsaat�, bilgilendirme, sorulukafa, sorui�areti, ikaz

�ekilAdedi = len (ikiliharitalamalar)
mesafeX = int (tuvalEni / �ekilAdedi)

for i in range (0, �ekilAdedi): tuval.create_bitmap ( (i+1)*mesafeX - mesafeX/2,50, bitmap=ikiliharitalamalar [i] )

k�k.mainloop()