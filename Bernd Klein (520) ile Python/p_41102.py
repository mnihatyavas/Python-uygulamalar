# coding:iso-8859-9 Türkçe
# p_41102.py: Python filedialog ile dosya önizleme ve açma örneği.

from tkinter import *
from tkinter.filedialog import askopenfilename

kök = Tk()
kök.title ("Dosya Açma Diyaloğu")

def dosyaAç():
    dosyaAdı = askopenfilename()
    etiket.config (text="Açılan dosya: " + dosyaAdı)

Button (kök, text='ÇIK', command=kök.quit).pack (fill=X)    
Button (kök, text='Önizlemesi yapılıp açılacak dosyayı seç', command=dosyaAç).pack (fill=X)

etiket = Label (kök)
etiket.pack (side=BOTTOM)

kök.mainloop()