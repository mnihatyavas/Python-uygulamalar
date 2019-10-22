# coding:iso-8859-9 T�rk�e
# p_40201.py: Message bile�eni ve parametrik i�erikleri �rne�i.

from tkinter import *

k�k = Tk()
�zs�z = "Ne yapt���n �nemli de�ildir, �nemli olan senin yapm�� olmand�r.\n(Mahatma Gandhi)"
mesaj = Message (k�k, text = �zs�z)
mesaj.config (bg='DarkGreen', fg="SpringGreen", font=('times', 10, 'italic') )
mesaj.pack()
#--------------------------------------------------------------------------------------------------------

Message (k�k, text=�zs�z, width=1000, anchor=SW, bg="Navy", fg="SpringGreen", font=('times', 10) ).pack()
# anchor/demirat: N/north/kuzey, NE, E, SE, S, SW, W, NW veya CENTER (varsay�l�).

Message (k�k, text=�zs�z, aspect=400, bg='DarkGreen', fg="SpringGreen", font=('times', 10) ).pack()
# aspect/g�r�n��: Mesaj geni�li�inin y�ksekli�e oran� (varsay�l� 150).

Message (k�k, text=�zs�z, width=1000, bd=3, bg="Brown", fg="Lime", font=('times', 10) ).pack()
# bd/borderwidth/s�n�rgeni�li�i (varsay�l� 2).

Message (k�k, text=�zs�z, width=1000, cursor="arrow", bg="Tan", fg="Lime", font=('times', 10) ).pack()
# cursor/imle�: Fare �zerindeyken imle� bi�imi (varsay�l� "arrow"/ok).

Message (k�k, text=�zs�z, width=1000, highlightthickness=10, highlightbackground="black", highlightcolor="yellow", bg="Sienna", fg="Lime", font=('times', 10) ).pack()
# highlightthickness-background-color/���ldakkal�nl���-zemini-rengi.

Message (k�k, text=�zs�z, width=1000, bd=10, relief=GROOVE, bg="Brown", fg="Lime", font=('times', 10) ).pack()
# relief/kabartma: FLAT/d�z (varsay�l�), SUNKEN/g�m�l�, RAISED/kabar�k, GROOVE/oluk ve RIDGE/s�rt.

Message (k�k, text=�zs�z, width=1000, bd=10, relief=SUNKEN, takefocus="true", bg="Olive", fg="Lime", font=('times', 10) ).pack()
# takefocus/odaklan: True ise bile�en odaklan�l�r (varsay�l� false).

isim = "M.Nihat Yava�"
Message (k�k, text=�zs�z, textvariable=isim, width=1000, bd=10, relief=RAISED, bg="Coral", fg="Lime", font=('times', 10) ).pack()
# textvariable/dizgede�i�keni: Mesaj� bir de�i�kenle ili�kilendirir; de�i�ken i�eri�i de�i�irse mesaj� g�nceller.

mainloop()