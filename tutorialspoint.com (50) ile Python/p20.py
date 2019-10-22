# coding:iso8859-9 Türkçe
# Python 3 - GUI Programming (Tkinter)

import tkinter

# Ana program kodlaması buraya eklenmeli...
pencere = tkinter.Tk()
pencere.mainloop()


çıktı = """
Pencere aletleri -araç, komponent, parça- (Button, Canvas, Checkbutton, Entry,
Frame, Label, Listbox, Menubutton, Menu, Message, Radiobutton, Scale, Scrollbar,
Text, Toplevel, Spinbox, PanedWindow, LabelFrame, tkMessageBox)

Bazı komponent özellikleri: Dimension, Color, Font, Anchor, Relief stilleri, Bitmap, Cursor vb...

Komponentleri pencereye serimleme yöntemleri:
   1. pack(): Komponentleri blok olarak kurar
   2. grid(): Parçalar tablo hücreleri benzeri ızgaraya yerleştirilir
   3. place(): Parçaların mutlak konumları belirlenir
"""