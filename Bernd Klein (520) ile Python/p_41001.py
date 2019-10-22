# coding:iso-8859-9 T�rk�e
# p_41001.py: Metin bile�eninin sade, kayd�ra�l� ve resimli �rne�i

from tkinter import *
from p_315 import Renk

k�k = Tk()
k�k.title ("Metin Bile�eni-1")

metin = Text (k�k, height=2, width=30)
metin.pack()

metin.insert (END, "Bu, sadece iki sat�rl�k k���k\nbir metin bile�enidir.\n")

k�k.mainloop()
#---------------------------------------------------------------------------------------------------------

k�k = Tk()
k�k.title ("Metin Bile�eni-2")

metin = Text (k�k, height=2, width=30)
metin.pack()

al�nt� = """HAMLET: Olmak yada olmamak--Esas mesele budur:
Hangisi daha soyludur, acaba �irkin baht�n
Ok ve m�zraklar�n�n an�lar eziyeti mi,
Yoksa bir acun s�k�nt�ya g���s germek,
Ve sonunda hepsiyle z�tla�mak m�? �lmek, uyumak--
Fazlas� de�il--ve uyuyunca deriz ki sonland�rd�k
Kalp s�z�s�n�, ve binlerce do�al �oklar�
Bedenin mirasland���. Bu'dur kemale erme
Sofucas�na arzulanan."""

metin.insert (END, al�nt�)

k�k.mainloop()
#---------------------------------------------------------------------------------------------------------

k�k = Tk()
k�k.title ("Kayd�ra�l� Metin Bile�eni")

kayd�ra� = Scrollbar (k�k)
kayd�ra�.pack (side=RIGHT, fill=Y)

metin = Text (k�k, height=4, width=50)
metin.pack(side=LEFT)

kayd�ra�.config (command=metin.yview)
metin.config (yscrollcommand=kayd�ra�.set)

metin.insert (END, al�nt�)

k�k.mainloop()
#---------------------------------------------------------------------------------------------------------

k�k = Tk()
k�k.title ("Resimli ve Kayd�ra�l� Metin")

metin1 = Text (k�k, height=15, width=25, background=Renk.renk() )
metin1.pack (side=LEFT)
# k�k renklendirmesi bg ve fg ile de�il, background ve foreground iledir...
resim = PhotoImage (file='resim/shakespeare.png')
metin1.image_create (END, image=resim)

metin2 = Text (k�k, height=15, width=45, background=Renk.renk() )
metin2.pack (side=LEFT)

kayd�ra� = Scrollbar (k�k, command=metin2.yview)
kayd�ra�.pack (side=RIGHT, fill=Y)

metin2.configure (yscrollcommand=kayd�ra�.set)

metin2.tag_configure ('koyu-yat�k', foreground="blue", font=('Arial', 10, 'bold', 'italic'))
metin2.tag_configure ('b�y�k', foreground="Brown", font=('Verdana', 20, 'bold'))
metin2.tag_configure ('koyu-renkli', foreground='#476042', background="Tan", font=('Tempus Sans ITC', 12, 'bold'))
metin2.tag_bind ('devam', "<1>", lambda olay, t=metin2: t.insert (END, "�imdi de�il, belki daha sonra!\n", "koyu-yat�k") )
# tag_configure ve tag_bind'lar sonradan metin.insert(END, metin, tag) olarak kullan�lacakt�r...

metin2.insert (END,'William Shakespeare\n', 'b�y�k')

al�nt� = """
Olmak yada olmamak--Esas mesele budur:
Hangisi daha soyludur, acaba �irkin baht�n
Ok ve m�zraklar�n�n an�lar eziyeti mi,
Yoksa bir acun s�k�nt�ya g���s germek,
"""

metin2.insert (END, al�nt�, 'koyu-renkli')
metin2.insert (END, 'devam� var...\n', 'devam')

k�k.mainloop()