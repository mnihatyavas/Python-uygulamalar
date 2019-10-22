# coding:iso-8859-9 Türkçe
# p_40806.py: Canvas tuvalinde hazır ikiliharaitalama şekilleri örneği.

from tkinter import *

kök = Tk()
kök.title ("Hazır İkiliharitalama Şekilleri")

tuvalEni = 300
tuvalBoyu =80

tuval = Canvas (kök, width=tuvalEni, height=tuvalBoyu, bg="Cyan")
tuval.pack()

ikiliharitalamalar = ["error", "gray75", "gray50", "gray25", "gray12", "hourglass", "info", "questhead", "question", "warning"]
# hata, gri75, gri50, gri25, gri12, kumsaatı, bilgilendirme, sorulukafa, soruişareti, ikaz

şekilAdedi = len (ikiliharitalamalar)
mesafeX = int (tuvalEni / şekilAdedi)

for i in range (0, şekilAdedi): tuval.create_bitmap ( (i+1)*mesafeX - mesafeX/2,50, bitmap=ikiliharitalamalar [i] )

kök.mainloop()