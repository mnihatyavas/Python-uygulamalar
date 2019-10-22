# coding:iso-8859-9 T�rk�e
# p_40603.py: �oklu �entik kutular� ve de�erlerine pratik y�ntemler �rne�i.

from tkinter import *

k�k=Tk()
k�k.title ("�entikkutular� ve De�erleri")

def de�erler(): 
    de�erler = "  [";
    for i in range (uz):
        de�erler += str (de�er [i].get()) + " "
        etiket.config (text=de�erler + "]")

Label (k�k, text="Cinsiyet, ya� ve medeni durumlar�n�z� �entikleyin", pady=5).grid (row=0)

liste = ["Eril", "Di�il", "�ocuk", "Gen�", "Kamil", "Ya�l�", "Bekar", "Evli", "Dul"]
uz = len (liste)
de�er = [IntVar() for _ in range (uz)]
�er�eve1 = Frame (k�k)
�er�eve1.grid (row=1)
�er�eve1.config (relief=RAISED, bd=4)
for i in range (uz): Checkbutton (�er�eve1, text=liste[i], variable=de�er [i]).pack (side=LEFT)

�er�eve2 = Frame (k�k)
�er�eve2.grid (row=2)
Button (�er�eve2, text='G�STER', command=de�erler).pack (side=LEFT)
etiket = Label (�er�eve2)
etiket.pack (side=LEFT)

Label (k�k, text="="*60).grid (row=3)
#-------------------------------------------------------------------------------------------------

class �entik (Frame):
    def __init__ (self, ata=None, arg�manlar=[], y�n=LEFT, �apa=W):
        Frame.__init__ (self, ata)
        self.de�erler = []
        for arg�man in arg�manlar:
            de�er = IntVar()
            �entik = Checkbutton (self, text=arg�man, variable=de�er)
            �entik.pack (side=y�n, anchor=�apa, expand=YES)
            self.de�erler.append (de�er)
    def durum (self): return map ((lambda x: x.get()), self.de�erler)

def g�ster(): etiket3.config (text=(str (list (dil.durum())) + str (list (lisan.durum())) + "   ")  )

Label (k�k, text="Programlama ve yabanc� dillerinizi �entikleyin").grid (row=4, pady=5)

dil = �entik (k�k, ['Python', 'Java', 'JS', 'C++', 'MASM', "HTML", "CSS"])
lisan = �entik (k�k, ['�ngilizce', 'Almanca', 'Frans�zca', 'Rus�a', "T�rk�e"])
dil.grid (row=5)
lisan.grid (row=6)
dil.config (relief=GROOVE, bd=4)
lisan.config (relief=RIDGE, bd=4)

�er�eve3 = Frame (k�k)
�er�eve3.grid (row=7, pady=5)
etiket3 = Label (�er�eve3)
etiket3.pack (side=LEFT)
Button (�er�eve3, text='G�STER', command=g�ster).pack (side=LEFT)
Button (�er�eve3, text='�IK', command=k�k.quit).pack (side=LEFT)

k�k.mainloop()
