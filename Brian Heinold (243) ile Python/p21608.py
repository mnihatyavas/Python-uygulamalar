# coding:iso-8859-9 Türkçe

from math import *
from tkinter import *
kök = Tk()

def hesapla (olay):
    değer = eval (gir.get() )
    print ("Sonuç =", değer)
    etiket.config (text="Sonuç: "+str (değer) )

def göster (olay): print (olay.keysym, "tuşuna bastınız")

Label (kök, text="İşlem gir ve [Ent] bas").pack()

gir = Entry (kök, width=20)
gir.pack() #Örn. [log(123)/sin(76)*1e-7**78] gir, dene...
gir.focus_set()

gir.bind ("<Key>", göster)
gir.bind ("<Return>", hesapla)

etiket = Label (kök, pady=10)
etiket.pack()

mainloop()

"""
1) Bazı bağlanabilecek olaylar:
<Button-1> Fare sol düğmesi tıklandı
<Double-Button-1> Fare sol düğmesi çift-tıklandı
Farenin, 1:sol, 2:orta, 3:sağ düğmesi...
<Button-Release-1> Fare sol düğmesi bırakıldı
<B1-Motion> Fare sol düğmesiyle tıklanıp sürüklendi
<MouseWheel> Fare tekeri oynadı
<Motion> Fare oynadı
<Enter> Fare bileşke üzerinde
<Leave> Fare bileşkeden ayrıldı
<Key> Bir tuşa basıldı
<"tuş adı"> Adı belirtilen tuşa basıldı

2) Event olay nesne özellikleri:
keysym: tuş sembolleri
x,y: farenin (x,y) kordinatı
delta: fare teker değeri

3) Bazı bind olay yakalayıcı/bağlayıcı keysym: key symbol = tuş sembolleri
<Return>, <Tab>, <Space>, <F1>, . . . , <F12> F1, . . . , F12
<Next>, <Prior> Page up, Page down
<Up>, <Down>, <Left>, <Right> Arrow keys
<Home>, <End>, <Insert>, <Delete>, <Caps_Lock>, <Num_Lock>
<Control_L>, <Control_R>, <Alt_L>, <Alt_R>, <Shift_L>, <Shift_R>
"a", "A", "-", <Space>, <Less>, <Greater>,
<Shift-F5>, <Control-Next>, <Alt-2>, <Control-Shift-F1>.
"""