# coding:iso-8859-9 T�rk�e

from tkinter import *
from p21601 import Renk
k�k = Tk()
k�k.title ("grid yerine pack")

if __name__ == "__main__":
    Button (k�k, text="Pencere Ebatlar�n�\nEsnetin\nG�r�n", bg=Renk.renk(), fg=Renk.renk(), width=50, height=5).pack()
    Button (k�k, text="Merhaba-1", bg=Renk.renk(), fg=Renk.renk()).pack()
    Button (k�k, text="Merhaba-2", bg=Renk.renk(), fg=Renk.renk()).pack (fill=X, expand=YES)
    Button (k�k, text="Merhaba-3", bg=Renk.renk(), fg=Renk.renk()).pack (fill=Y, expand=YES)
    Button (k�k, text="TIKLAYIN", bg=Renk.renk(), fg=Renk.renk()).pack (fill=BOTH, expand=YES)
    Button (k�k, text="Merhaba-4", bg=Renk.renk(), fg=Renk.renk()).pack (side=LEFT)
    Button (k�k, text="Merhaba-5", bg=Renk.renk(), fg=Renk.renk()).pack (side="right")
    Button (k�k, text="Merhaba-6", bg=Renk.renk(), fg=Renk.renk()).pack (side=TOP)
    Button (k�k, text="Merhaba-7", bg=Renk.renk(), fg=Renk.renk()).pack (side="bottom")
    Button (k�k, text="�IK", font=("verdana", 25, "bold"), bg=Renk.renk(), fg=Renk.renk(), command=k�k.quit).pack (fill=BOTH, expand=NO)

mainloop()
