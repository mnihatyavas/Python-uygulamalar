# coding:iso-8859-9 Türkçe

from tkinter import *
kök = Tk()

def selam(): etiket.config (text="Merhaba Pythoncular")
def göster(): etiket.config (text=str (düğme1.cget ("state") ) )

def değiştir():
    if düğme1.cget ("state") == DISABLED: düğme1.config (state=NORMAL)
    else: düğme1.config (state=DISABLED)

def başlık():
    etiket.config (text="Şimdi 'Tkinter GUI' başlığını pencere üstünde görebilirsiniz")
    kök.title ("Tkinter GUI Başlığı")

if __name__ == "__main__":
    düğme1 = Button (kök, text="Selam Ver", state=DISABLED, command=selam)
    düğme1.pack()
    düğme2 = Button (kök, text="Durum Değiştir", command=değiştir).pack()
    düğme3 = Button (kök, text="Durum Göster", command=göster).pack()
    düğme4 = Button (kök, text="Başlık At", command=başlık).pack()
    düğme5 = Button (kök, text="Çık", command=kök.quit).pack()

    etiket = Label (kök)
    etiket.pack()

mainloop()
