# coding:iso-8859-9 Türkçe
# p_40603.py: Çoklu çentik kutuları ve değerlerine pratik yöntemler örneği.

from tkinter import *

kök=Tk()
kök.title ("Çentikkutuları ve Değerleri")

def değerler(): 
    değerler = "  [";
    for i in range (uz):
        değerler += str (değer [i].get()) + " "
        etiket.config (text=değerler + "]")

Label (kök, text="Cinsiyet, yaş ve medeni durumlarınızı çentikleyin", pady=5).grid (row=0)

liste = ["Eril", "Dişil", "Çocuk", "Genç", "Kamil", "Yaşlı", "Bekar", "Evli", "Dul"]
uz = len (liste)
değer = [IntVar() for _ in range (uz)]
çerçeve1 = Frame (kök)
çerçeve1.grid (row=1)
çerçeve1.config (relief=RAISED, bd=4)
for i in range (uz): Checkbutton (çerçeve1, text=liste[i], variable=değer [i]).pack (side=LEFT)

çerçeve2 = Frame (kök)
çerçeve2.grid (row=2)
Button (çerçeve2, text='GÖSTER', command=değerler).pack (side=LEFT)
etiket = Label (çerçeve2)
etiket.pack (side=LEFT)

Label (kök, text="="*60).grid (row=3)
#-------------------------------------------------------------------------------------------------

class Çentik (Frame):
    def __init__ (self, ata=None, argümanlar=[], yön=LEFT, çapa=W):
        Frame.__init__ (self, ata)
        self.değerler = []
        for argüman in argümanlar:
            değer = IntVar()
            çentik = Checkbutton (self, text=argüman, variable=değer)
            çentik.pack (side=yön, anchor=çapa, expand=YES)
            self.değerler.append (değer)
    def durum (self): return map ((lambda x: x.get()), self.değerler)

def göster(): etiket3.config (text=(str (list (dil.durum())) + str (list (lisan.durum())) + "   ")  )

Label (kök, text="Programlama ve yabancı dillerinizi çentikleyin").grid (row=4, pady=5)

dil = Çentik (kök, ['Python', 'Java', 'JS', 'C++', 'MASM', "HTML", "CSS"])
lisan = Çentik (kök, ['İngilizce', 'Almanca', 'Fransızca', 'Rusça', "Türkçe"])
dil.grid (row=5)
lisan.grid (row=6)
dil.config (relief=GROOVE, bd=4)
lisan.config (relief=RIDGE, bd=4)

çerçeve3 = Frame (kök)
çerçeve3.grid (row=7, pady=5)
etiket3 = Label (çerçeve3)
etiket3.pack (side=LEFT)
Button (çerçeve3, text='GÖSTER', command=göster).pack (side=LEFT)
Button (çerçeve3, text='ÇIK', command=kök.quit).pack (side=LEFT)

kök.mainloop()
