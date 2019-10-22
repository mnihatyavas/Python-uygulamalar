# coding:iso-8859-9 Türkçe
# p_41001.py: Metin bileşeninin sade, kaydıraçlı ve resimli örneği

from tkinter import *
from p_315 import Renk

kök = Tk()
kök.title ("Metin Bileşeni-1")

metin = Text (kök, height=2, width=30)
metin.pack()

metin.insert (END, "Bu, sadece iki satırlık küçük\nbir metin bileşenidir.\n")

kök.mainloop()
#---------------------------------------------------------------------------------------------------------

kök = Tk()
kök.title ("Metin Bileşeni-2")

metin = Text (kök, height=2, width=30)
metin.pack()

alıntı = """HAMLET: Olmak yada olmamak--Esas mesele budur:
Hangisi daha soyludur, acaba çirkin bahtın
Ok ve mızraklarının anılar eziyeti mi,
Yoksa bir acun sıkıntıya göğüs germek,
Ve sonunda hepsiyle zıtlaşmak mı? Ölmek, uyumak--
Fazlası değil--ve uyuyunca deriz ki sonlandırdık
Kalp sızısını, ve binlerce doğal şokları
Bedenin miraslandığı. Bu'dur kemale erme
Sofucasına arzulanan."""

metin.insert (END, alıntı)

kök.mainloop()
#---------------------------------------------------------------------------------------------------------

kök = Tk()
kök.title ("Kaydıraçlı Metin Bileşeni")

kaydıraç = Scrollbar (kök)
kaydıraç.pack (side=RIGHT, fill=Y)

metin = Text (kök, height=4, width=50)
metin.pack(side=LEFT)

kaydıraç.config (command=metin.yview)
metin.config (yscrollcommand=kaydıraç.set)

metin.insert (END, alıntı)

kök.mainloop()
#---------------------------------------------------------------------------------------------------------

kök = Tk()
kök.title ("Resimli ve Kaydıraçlı Metin")

metin1 = Text (kök, height=15, width=25, background=Renk.renk() )
metin1.pack (side=LEFT)
# kök renklendirmesi bg ve fg ile değil, background ve foreground iledir...
resim = PhotoImage (file='resim/shakespeare.png')
metin1.image_create (END, image=resim)

metin2 = Text (kök, height=15, width=45, background=Renk.renk() )
metin2.pack (side=LEFT)

kaydıraç = Scrollbar (kök, command=metin2.yview)
kaydıraç.pack (side=RIGHT, fill=Y)

metin2.configure (yscrollcommand=kaydıraç.set)

metin2.tag_configure ('koyu-yatık', foreground="blue", font=('Arial', 10, 'bold', 'italic'))
metin2.tag_configure ('büyük', foreground="Brown", font=('Verdana', 20, 'bold'))
metin2.tag_configure ('koyu-renkli', foreground='#476042', background="Tan", font=('Tempus Sans ITC', 12, 'bold'))
metin2.tag_bind ('devam', "<1>", lambda olay, t=metin2: t.insert (END, "Şimdi değil, belki daha sonra!\n", "koyu-yatık") )
# tag_configure ve tag_bind'lar sonradan metin.insert(END, metin, tag) olarak kullanılacaktır...

metin2.insert (END,'William Shakespeare\n', 'büyük')

alıntı = """
Olmak yada olmamak--Esas mesele budur:
Hangisi daha soyludur, acaba çirkin bahtın
Ok ve mızraklarının anılar eziyeti mi,
Yoksa bir acun sıkıntıya göğüs germek,
"""

metin2.insert (END, alıntı, 'koyu-renkli')
metin2.insert (END, 'devamı var...\n', 'devam')

kök.mainloop()