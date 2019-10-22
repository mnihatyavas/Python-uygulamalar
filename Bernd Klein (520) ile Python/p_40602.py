# coding:iso-8859-9 Türkçe
# p_40602.py: Programlama ve yabancı diller çokseçmeli çentik kutuları örneği.

from tkinter import *

class Çentikçubuğu (Frame):
    def __init__ (self, ebeveyn=None, liste=[], yön=LEFT, demirle=W):
        Frame.__init__ (self, ebeveyn)
        self.değişkenler = []
        for eleman in liste:
            değişken = IntVar()
            çentik = Checkbutton (self, text=eleman, variable=değişken)
            çentik.pack (side=yön, anchor=demirle, expand=YES)
            self.değişkenler.append (değişken)
    def durum (self): return map ((lambda değişken: değişken.get() ), self.değişkenler)

if __name__ == '__main__':
    kök = Tk()
    diller = Çentikçubuğu (kök, ['Python', 'Java', 'JS', 'HTML', "CSS"])
    lisanlar = Çentikçubuğu (kök, ['İngilizce', 'Almanca', "Fransızca", "Rusca"])
    diller.pack (side=TOP,  fill=X)
    lisanlar.pack (side=TOP, anchor=W)
    diller.config (relief=GROOVE, bd=2)
    lisanlar.config (relief=GROOVE, bd=2)

    def durumlar(): etiket.config (text=("[" + str (list (diller.durum())) + str (list (lisanlar.durum())) + "]"))

    Button (kök, text='GÖSTER', command=durumlar).pack (side=LEFT, anchor=W)
    Button (kök, text='ÇIK', command=kök.quit).pack (side=RIGHT)


    etiket = Label (kök)
    etiket.pack()

kök.mainloop()