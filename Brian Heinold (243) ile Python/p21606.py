# coding:iso-8859-9 Türkçe

from tkinter import *
kök1 = Tk()

def göster1():
    etiket1.configure (text="Girilen Veriler==>\n" + metinKutusu1.get (1.0, END) )
    metinKutusu1.delete (1.0, END)

metinKutusu1 = Text (kök1, font=('Verdana', 16), height=6, width=40, undo=True)
metinKutusu1.grid (row=0, column=0)
metinKutusu1.insert (1.0, "Merhaba, istediğiniz uzunlukta veri girebilirsiniz.\n"+
        "Ayrıca ^z_undo:iptal ve ^y_redo:yinele aktifdir.")

etiket1 = Label (kök1)
etiket1.grid (row=2, column=0, pady=10)

düğme1 = Button (kök1, text="Yazılanı Göster-1", bg="black", fg="yellow", command=göster1)
düğme1.grid (row=1, column=0)
#-------------------------------------------------------------------------------------------------

from tkinter.scrolledtext import ScrolledText
kök2 = Tk()

def göster2():
    etiket2.configure (text="Girilen Veriler==>\n" + metinKutusu2.get (1.0, END) )
    metinKutusu2.delete (1.0, END)

metinKutusu2 = ScrolledText (kök2, font=('Verdana', 16), height=6, width=40, undo=True)
metinKutusu2.grid (row=0, column=0)
metinKutusu2.insert (1.0, "KAYDIRMA ÇUBUKLU METİN_KUTUSU\n"+
        "Merhaba, istediğiniz uzunlukta veri girebilirsiniz.\n"+
        "Ayrıca ^z_undo:iptal ve ^y_redo:yinele aktifdir.")

etiket2 = Label (kök2)
etiket2.grid (row=2, column=0, pady=10)

düğme2 = Button (kök2, text="Yazılanı Göster-2", bg="black", fg="yellow", command=göster2)
düğme2.grid (row=1, column=0)

mainloop()
