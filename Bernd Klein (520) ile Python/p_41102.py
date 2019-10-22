# coding:iso-8859-9 T�rk�e
# p_41102.py: Python filedialog ile dosya �nizleme ve a�ma �rne�i.

from tkinter import *
from tkinter.filedialog import askopenfilename

k�k = Tk()
k�k.title ("Dosya A�ma Diyalo�u")

def dosyaA�():
    dosyaAd� = askopenfilename()
    etiket.config (text="A��lan dosya: " + dosyaAd�)

Button (k�k, text='�IK', command=k�k.quit).pack (fill=X)    
Button (k�k, text='�nizlemesi yap�l�p a��lacak dosyay� se�', command=dosyaA�).pack (fill=X)

etiket = Label (k�k)
etiket.pack (side=BOTTOM)

k�k.mainloop()