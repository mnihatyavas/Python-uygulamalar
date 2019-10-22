# coding:iso-8859-9 Türkçe
# p_40501a.py: Radyo düğmeleri ve onlara variable-value ile değişken-değer atanması örneği.

import tkinter as tk
from p_315 import Renk

kök = tk.Tk()
kök.title ("Radyo Düğmeleri-1")

def seçiminiz(): etiket.config (text="Seçtiğiniz programlama dili: " + liste [değer.get()], bg=Renk.renk(), fg=Renk.renk() )
liste = ["Pyton", "JavaScript", "Java", "HTML", "CSS"]

değer = tk.IntVar()
değer.set (1) # İlk açılışta varsayılı seçilen 1=JavaScript
# variable=değer: StringVar(),  IntVar(), DoubleVar() veya BooleanVar() olabilir...

çerçeve = tk.Frame (kök, bg=Renk.renk() )
çerçeve.pack()

tk.Label (çerçeve,
    text="""Aşağıdaki programlama dillerinden\nsadece birini seçebilirsiniz:""",
    justify=tk.LEFT,
    bg=Renk.renk(),
    fg=Renk.renk(),
    padx = 20).pack()

tk.Radiobutton (çerçeve, text="Python", bg=Renk.renk(), fg=Renk.renk(), padx = 20, variable=değer, value=0, command=seçiminiz).pack (anchor=tk.W)
tk.Radiobutton (çerçeve, text="JavaScript", bg=Renk.renk(), fg=Renk.renk(), padx = 20, variable=değer, value=1, command=seçiminiz).pack (anchor=tk.W)
tk.Radiobutton (çerçeve, text="Java", bg=Renk.renk(), fg=Renk.renk(), padx = 20, variable=değer, value=2, command=seçiminiz).pack (anchor=tk.W)
tk.Radiobutton (çerçeve, text="HTML", bg=Renk.renk(), fg=Renk.renk(), padx = 20, variable=değer, value=3, command=seçiminiz).pack (anchor=tk.W)
tk.Radiobutton (çerçeve, text="CSS", bg=Renk.renk(), fg=Renk.renk(), padx = 20, variable=değer, value=4, command=seçiminiz).pack (anchor=tk.W)

etiket = tk.Label (çerçeve, text="Seçtiğiniz programlama dili: " + liste [değer.get()], justify=tk.LEFT, bg=Renk.renk(), fg=Renk.renk(), padx = 20, pady=20)
etiket.pack (anchor=tk.W)

kök.mainloop()
#------------------------------------------------------------------------------------------------------

from tkinter import *

kök = Tk()
kök.title ("Radyo Düğmeleri-2")

def seçiminiz(): etiket.config (text="Seçtiğiniz programlama dili: " + liste [değer.get()], bg=Renk.renk(), fg=Renk.renk() )

değer = IntVar()
değer.set (1) # İlk açılışta varsayılı seçilen 1=JavaScript
# variable=değer: StringVar(),  IntVar(), DoubleVar() veya BooleanVar() olabilir...

çerçeve = Frame (kök, bg=Renk.renk() )
çerçeve.pack()

Label (çerçeve,
    text="""Aşağıdaki programlama dillerinden\nsadece birini seçebilirsiniz:""",
    justify=LEFT,
    bg=Renk.renk(),
    fg=Renk.renk(),
    width=30,
    padx = 16).pack()

dillerListesi = ["Pyton", "JavaScript", "Java", "HTML", "CSS"]
for i, dil in enumerate (dillerListesi): Radiobutton (çerçeve, text=dil, bg=Renk.renk(), fg=Renk.renk(), padx = 20, variable=değer, value=i, command=seçiminiz).pack() # Varsayılı: CENTER

Label (çerçeve, text="-"*48).pack()
etiket = Label (çerçeve, text="Seçtiğiniz programlama dili: " + liste [değer.get()], justify=LEFT, bg=Renk.renk(), fg=Renk.renk(), padx = 20, pady=20)
etiket.pack()

mainloop() # Varsayılı: kök.mainloop()
#------------------------------------------------------------------------------------------------------

kök = Tk()
kök.title ("Radyo Düğmeleri-3")

def seçiminiz(): etiket.config (text="Seçtiğiniz programlama dili: " + liste [değer.get()], bg=Renk.renk(), fg=Renk.renk() )

değer = IntVar()
değer.set (0) # İlk açılışta varsayılı seçilen 0=Python
# variable=değer: StringVar(),  IntVar(), DoubleVar() veya BooleanVar() olabilir...

çerçeve = Frame (kök, bg=Renk.renk() )
çerçeve.pack()

Label (çerçeve,
    text="""Aşağıdaki programlama dillerinden\nsadece birini seçebilirsiniz:""",
    justify=LEFT,
    bg=Renk.renk(),
    fg=Renk.renk(),
    width=30,
    padx = 16).pack()

diller = ["Pyton", "JavaScript", "Java", "HTML", "CSS"]
for i in range (len (diller) ): Radiobutton (çerçeve, text=diller [i], indicatoron=0, bg=Renk.renk(), fg=Renk.renk(), width=20, variable=değer, value=i, command=seçiminiz).pack()
# Varsayılı indicatoron=1 (radyo düğme yuvarlak ikon görünür)...
# Seçilen buton gömülüdür...

Label (çerçeve, text="-"*48, bg="Black", fg="Yellow").pack()
etiket = Label (çerçeve, text="Seçtiğiniz programlama dili: " + liste [değer.get()], justify=LEFT, bg=Renk.renk(), fg=Renk.renk(), padx = 20, pady=20)
etiket.pack()

kök.mainloop()
