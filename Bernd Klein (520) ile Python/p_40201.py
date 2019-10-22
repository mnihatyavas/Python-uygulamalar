# coding:iso-8859-9 Türkçe
# p_40201.py: Message bileşeni ve parametrik içerikleri örneği.

from tkinter import *

kök = Tk()
özsöz = "Ne yaptığın önemli değildir, önemli olan senin yapmış olmandır.\n(Mahatma Gandhi)"
mesaj = Message (kök, text = özsöz)
mesaj.config (bg='DarkGreen', fg="SpringGreen", font=('times', 10, 'italic') )
mesaj.pack()
#--------------------------------------------------------------------------------------------------------

Message (kök, text=özsöz, width=1000, anchor=SW, bg="Navy", fg="SpringGreen", font=('times', 10) ).pack()
# anchor/demirat: N/north/kuzey, NE, E, SE, S, SW, W, NW veya CENTER (varsayılı).

Message (kök, text=özsöz, aspect=400, bg='DarkGreen', fg="SpringGreen", font=('times', 10) ).pack()
# aspect/görünüş: Mesaj genişliğinin yüksekliğe oranı (varsayılı 150).

Message (kök, text=özsöz, width=1000, bd=3, bg="Brown", fg="Lime", font=('times', 10) ).pack()
# bd/borderwidth/sınırgenişliği (varsayılı 2).

Message (kök, text=özsöz, width=1000, cursor="arrow", bg="Tan", fg="Lime", font=('times', 10) ).pack()
# cursor/imleç: Fare üzerindeyken imleç biçimi (varsayılı "arrow"/ok).

Message (kök, text=özsöz, width=1000, highlightthickness=10, highlightbackground="black", highlightcolor="yellow", bg="Sienna", fg="Lime", font=('times', 10) ).pack()
# highlightthickness-background-color/ışıldakkalınlığı-zemini-rengi.

Message (kök, text=özsöz, width=1000, bd=10, relief=GROOVE, bg="Brown", fg="Lime", font=('times', 10) ).pack()
# relief/kabartma: FLAT/düz (varsayılı), SUNKEN/gömülü, RAISED/kabarık, GROOVE/oluk ve RIDGE/sırt.

Message (kök, text=özsöz, width=1000, bd=10, relief=SUNKEN, takefocus="true", bg="Olive", fg="Lime", font=('times', 10) ).pack()
# takefocus/odaklan: True ise bileşen odaklanılır (varsayılı false).

isim = "M.Nihat Yavaş"
Message (kök, text=özsöz, textvariable=isim, width=1000, bd=10, relief=RAISED, bg="Coral", fg="Lime", font=('times', 10) ).pack()
# textvariable/dizgedeğişkeni: Mesajı bir değişkenle ilişkilendirir; değişken içeriği değişirse mesajı günceller.

mainloop()