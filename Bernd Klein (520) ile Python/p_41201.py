# coding:iso-8859-9 Türkçe
# p_41201.py: Tkinter serilim yönetiminde pack kullanımı örneği.

from tkinter import *

kök = Tk()
kök.title ("pack()'le Varsayılı Serilim")

Label (kök, text="Kızıl Güneş", bg="red", fg="Yellow").pack()
Label (kök, text="Yeşil Otlak", bg="green", fg="Cyan").pack()
Label (kök, text="Mavi Gök", bg="blue", fg="Lime").pack()

kök.mainloop()
#-----------------------------------------------------------------------------------------------------------

kök = Tk()
kök.title ("pack()'le Enlemesine Serilim")

Label (kök, text="Kızıl Güneş", bg="red", fg="Yellow").pack (fill=X)
Label (kök, text="Yeşil Otlak", bg="green", fg="Cyan").pack (fill=X)
Label (kök, text="Mavi Gök", bg="blue", fg="Lime").pack (fill=X)

kök.mainloop()
#-----------------------------------------------------------------------------------------------------------

kök = Tk()
kök.title ("pack()'le Dış pad'li Serilim")

Label (kök, text="Kızıl Güneş", bg="red", fg="Yellow").pack (fill=X, padx=10, pady=10)
Label (kök, text="Yeşil Otlak", bg="green", fg="Cyan").pack (fill=X, padx=10, pady=10)
Label (kök, text="Mavi Gök", bg="blue", fg="Lime").pack (fill=X, padx=10, pady=10)

kök.mainloop()
#-----------------------------------------------------------------------------------------------------------

kök = Tk()
kök.title ("pack()'le İç pad'li Serilim")

Label (kök, text="Kızıl Güneş", bg="red", fg="Yellow").pack (ipadx=20) # ipad/internalpad=dahili tampon...
Label (kök, text="Yeşil Otlak", bg="green", fg="Cyan").pack (ipady=20)
Label (kök, text="Mavi Gök", bg="blue", fg="Lime").pack (ipadx=20, ipady=20)

kök.mainloop()
#-----------------------------------------------------------------------------------------------------------

kök = Tk()
kök.title ("pack()'le Sol'dan Yanyana Serilim")

Label (kök, text="Kızıl Güneş", bg="red", fg="Yellow").pack (padx=5, pady=10, side=LEFT) # Etiketler sola yanaşık...
Label (kök, text="Yeşil Otlak", bg="green", fg="Cyan").pack (padx=5, pady=10, side=LEFT)
Label (kök, text="Mavi Gök", bg="blue", fg="Lime").pack (padx=5, pady=10, side=LEFT)

kök.mainloop()
#-----------------------------------------------------------------------------------------------------------

kök = Tk()
kök.title ("pack()'le Sağ'dan Yanyana Serilim")

Label (kök, text="Kızıl Güneş", bg="red", fg="Yellow").pack (padx=5, pady=10, side=RIGHT) # Etiketler sağa yanaşık...
Label (kök, text="Yeşil Otlak", bg="green", fg="Cyan").pack (padx=5, pady=10, side=RIGHT)
Label (kök, text="Mavi Gök", bg="blue", fg="Lime").pack (padx=5, pady=10, side=RIGHT)

kök.mainloop()
