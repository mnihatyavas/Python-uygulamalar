# coding:iso-8859-9 T�rk�e
# p_40501a.py: Radyo d��meleri ve onlara variable-value ile de�i�ken-de�er atanmas� �rne�i.

import tkinter as tk
from p_315 import Renk

k�k = tk.Tk()
k�k.title ("Radyo D��meleri-1")

def se�iminiz(): etiket.config (text="Se�ti�iniz programlama dili: " + liste [de�er.get()], bg=Renk.renk(), fg=Renk.renk() )
liste = ["Pyton", "JavaScript", "Java", "HTML", "CSS"]

de�er = tk.IntVar()
de�er.set (1) # �lk a��l��ta varsay�l� se�ilen 1=JavaScript
# variable=de�er: StringVar(),  IntVar(), DoubleVar() veya BooleanVar() olabilir...

�er�eve = tk.Frame (k�k, bg=Renk.renk() )
�er�eve.pack()

tk.Label (�er�eve,
    text="""A�a��daki programlama dillerinden\nsadece birini se�ebilirsiniz:""",
    justify=tk.LEFT,
    bg=Renk.renk(),
    fg=Renk.renk(),
    padx = 20).pack()

tk.Radiobutton (�er�eve, text="Python", bg=Renk.renk(), fg=Renk.renk(), padx = 20, variable=de�er, value=0, command=se�iminiz).pack (anchor=tk.W)
tk.Radiobutton (�er�eve, text="JavaScript", bg=Renk.renk(), fg=Renk.renk(), padx = 20, variable=de�er, value=1, command=se�iminiz).pack (anchor=tk.W)
tk.Radiobutton (�er�eve, text="Java", bg=Renk.renk(), fg=Renk.renk(), padx = 20, variable=de�er, value=2, command=se�iminiz).pack (anchor=tk.W)
tk.Radiobutton (�er�eve, text="HTML", bg=Renk.renk(), fg=Renk.renk(), padx = 20, variable=de�er, value=3, command=se�iminiz).pack (anchor=tk.W)
tk.Radiobutton (�er�eve, text="CSS", bg=Renk.renk(), fg=Renk.renk(), padx = 20, variable=de�er, value=4, command=se�iminiz).pack (anchor=tk.W)

etiket = tk.Label (�er�eve, text="Se�ti�iniz programlama dili: " + liste [de�er.get()], justify=tk.LEFT, bg=Renk.renk(), fg=Renk.renk(), padx = 20, pady=20)
etiket.pack (anchor=tk.W)

k�k.mainloop()
#------------------------------------------------------------------------------------------------------

from tkinter import *

k�k = Tk()
k�k.title ("Radyo D��meleri-2")

def se�iminiz(): etiket.config (text="Se�ti�iniz programlama dili: " + liste [de�er.get()], bg=Renk.renk(), fg=Renk.renk() )

de�er = IntVar()
de�er.set (1) # �lk a��l��ta varsay�l� se�ilen 1=JavaScript
# variable=de�er: StringVar(),  IntVar(), DoubleVar() veya BooleanVar() olabilir...

�er�eve = Frame (k�k, bg=Renk.renk() )
�er�eve.pack()

Label (�er�eve,
    text="""A�a��daki programlama dillerinden\nsadece birini se�ebilirsiniz:""",
    justify=LEFT,
    bg=Renk.renk(),
    fg=Renk.renk(),
    width=30,
    padx = 16).pack()

dillerListesi = ["Pyton", "JavaScript", "Java", "HTML", "CSS"]
for i, dil in enumerate (dillerListesi): Radiobutton (�er�eve, text=dil, bg=Renk.renk(), fg=Renk.renk(), padx = 20, variable=de�er, value=i, command=se�iminiz).pack() # Varsay�l�: CENTER

Label (�er�eve, text="-"*48).pack()
etiket = Label (�er�eve, text="Se�ti�iniz programlama dili: " + liste [de�er.get()], justify=LEFT, bg=Renk.renk(), fg=Renk.renk(), padx = 20, pady=20)
etiket.pack()

mainloop() # Varsay�l�: k�k.mainloop()
#------------------------------------------------------------------------------------------------------

k�k = Tk()
k�k.title ("Radyo D��meleri-3")

def se�iminiz(): etiket.config (text="Se�ti�iniz programlama dili: " + liste [de�er.get()], bg=Renk.renk(), fg=Renk.renk() )

de�er = IntVar()
de�er.set (0) # �lk a��l��ta varsay�l� se�ilen 0=Python
# variable=de�er: StringVar(),  IntVar(), DoubleVar() veya BooleanVar() olabilir...

�er�eve = Frame (k�k, bg=Renk.renk() )
�er�eve.pack()

Label (�er�eve,
    text="""A�a��daki programlama dillerinden\nsadece birini se�ebilirsiniz:""",
    justify=LEFT,
    bg=Renk.renk(),
    fg=Renk.renk(),
    width=30,
    padx = 16).pack()

diller = ["Pyton", "JavaScript", "Java", "HTML", "CSS"]
for i in range (len (diller) ): Radiobutton (�er�eve, text=diller [i], indicatoron=0, bg=Renk.renk(), fg=Renk.renk(), width=20, variable=de�er, value=i, command=se�iminiz).pack()
# Varsay�l� indicatoron=1 (radyo d��me yuvarlak ikon g�r�n�r)...
# Se�ilen buton g�m�l�d�r...

Label (�er�eve, text="-"*48, bg="Black", fg="Yellow").pack()
etiket = Label (�er�eve, text="Se�ti�iniz programlama dili: " + liste [de�er.get()], justify=LEFT, bg=Renk.renk(), fg=Renk.renk(), padx = 20, pady=20)
etiket.pack()

k�k.mainloop()
