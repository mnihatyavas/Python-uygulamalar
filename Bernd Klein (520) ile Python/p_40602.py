# coding:iso-8859-9 T�rk�e
# p_40602.py: Programlama ve yabanc� diller �okse�meli �entik kutular� �rne�i.

from tkinter import *

class �entik�ubu�u (Frame):
    def __init__ (self, ebeveyn=None, liste=[], y�n=LEFT, demirle=W):
        Frame.__init__ (self, ebeveyn)
        self.de�i�kenler = []
        for eleman in liste:
            de�i�ken = IntVar()
            �entik = Checkbutton (self, text=eleman, variable=de�i�ken)
            �entik.pack (side=y�n, anchor=demirle, expand=YES)
            self.de�i�kenler.append (de�i�ken)
    def durum (self): return map ((lambda de�i�ken: de�i�ken.get() ), self.de�i�kenler)

if __name__ == '__main__':
    k�k = Tk()
    diller = �entik�ubu�u (k�k, ['Python', 'Java', 'JS', 'HTML', "CSS"])
    lisanlar = �entik�ubu�u (k�k, ['�ngilizce', 'Almanca', "Frans�zca", "Rusca"])
    diller.pack (side=TOP,  fill=X)
    lisanlar.pack (side=TOP, anchor=W)
    diller.config (relief=GROOVE, bd=2)
    lisanlar.config (relief=GROOVE, bd=2)

    def durumlar(): etiket.config (text=("[" + str (list (diller.durum())) + str (list (lisanlar.durum())) + "]"))

    Button (k�k, text='G�STER', command=durumlar).pack (side=LEFT, anchor=W)
    Button (k�k, text='�IK', command=k�k.quit).pack (side=RIGHT)


    etiket = Label (k�k)
    etiket.pack()

k�k.mainloop()