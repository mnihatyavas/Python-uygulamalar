# coding:iso-8859-9 Türkçe

from tkinter import *
from p21601 import Renk
kök = Tk()
kök.title ("grid yerine pack")

if __name__ == "__main__":
    Button (kök, text="Pencere Ebatlarını\nEsnetin\nGörün", bg=Renk.renk(), fg=Renk.renk(), width=50, height=5).pack()
    Button (kök, text="Merhaba-1", bg=Renk.renk(), fg=Renk.renk()).pack()
    Button (kök, text="Merhaba-2", bg=Renk.renk(), fg=Renk.renk()).pack (fill=X, expand=YES)
    Button (kök, text="Merhaba-3", bg=Renk.renk(), fg=Renk.renk()).pack (fill=Y, expand=YES)
    Button (kök, text="TIKLAYIN", bg=Renk.renk(), fg=Renk.renk()).pack (fill=BOTH, expand=YES)
    Button (kök, text="Merhaba-4", bg=Renk.renk(), fg=Renk.renk()).pack (side=LEFT)
    Button (kök, text="Merhaba-5", bg=Renk.renk(), fg=Renk.renk()).pack (side="right")
    Button (kök, text="Merhaba-6", bg=Renk.renk(), fg=Renk.renk()).pack (side=TOP)
    Button (kök, text="Merhaba-7", bg=Renk.renk(), fg=Renk.renk()).pack (side="bottom")
    Button (kök, text="ÇIK", font=("verdana", 25, "bold"), bg=Renk.renk(), fg=Renk.renk(), command=kök.quit).pack (fill=BOTH, expand=NO)

mainloop()
