# coding:iso-8859-9 T�rk�e

from tkinter import *
k�k1 = Tk()

def g�ster1():
    etiket1.configure (text="Girilen Veriler==>\n" + metinKutusu1.get (1.0, END) )
    metinKutusu1.delete (1.0, END)

metinKutusu1 = Text (k�k1, font=('Verdana', 16), height=6, width=40, undo=True)
metinKutusu1.grid (row=0, column=0)
metinKutusu1.insert (1.0, "Merhaba, istedi�iniz uzunlukta veri girebilirsiniz.\n"+
        "Ayr�ca ^z_undo:iptal ve ^y_redo:yinele aktifdir.")

etiket1 = Label (k�k1)
etiket1.grid (row=2, column=0, pady=10)

d��me1 = Button (k�k1, text="Yaz�lan� G�ster-1", bg="black", fg="yellow", command=g�ster1)
d��me1.grid (row=1, column=0)
#-------------------------------------------------------------------------------------------------

from tkinter.scrolledtext import ScrolledText
k�k2 = Tk()

def g�ster2():
    etiket2.configure (text="Girilen Veriler==>\n" + metinKutusu2.get (1.0, END) )
    metinKutusu2.delete (1.0, END)

metinKutusu2 = ScrolledText (k�k2, font=('Verdana', 16), height=6, width=40, undo=True)
metinKutusu2.grid (row=0, column=0)
metinKutusu2.insert (1.0, "KAYDIRMA �UBUKLU MET�N_KUTUSU\n"+
        "Merhaba, istedi�iniz uzunlukta veri girebilirsiniz.\n"+
        "Ayr�ca ^z_undo:iptal ve ^y_redo:yinele aktifdir.")

etiket2 = Label (k�k2)
etiket2.grid (row=2, column=0, pady=10)

d��me2 = Button (k�k2, text="Yaz�lan� G�ster-2", bg="black", fg="yellow", command=g�ster2)
d��me2.grid (row=1, column=0)

mainloop()
