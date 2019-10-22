# coding:iso-8859-9 T�rk�e
# p_41201.py: Tkinter serilim y�netiminde pack kullan�m� �rne�i.

from tkinter import *

k�k = Tk()
k�k.title ("pack()'le Varsay�l� Serilim")

Label (k�k, text="K�z�l G�ne�", bg="red", fg="Yellow").pack()
Label (k�k, text="Ye�il Otlak", bg="green", fg="Cyan").pack()
Label (k�k, text="Mavi G�k", bg="blue", fg="Lime").pack()

k�k.mainloop()
#-----------------------------------------------------------------------------------------------------------

k�k = Tk()
k�k.title ("pack()'le Enlemesine Serilim")

Label (k�k, text="K�z�l G�ne�", bg="red", fg="Yellow").pack (fill=X)
Label (k�k, text="Ye�il Otlak", bg="green", fg="Cyan").pack (fill=X)
Label (k�k, text="Mavi G�k", bg="blue", fg="Lime").pack (fill=X)

k�k.mainloop()
#-----------------------------------------------------------------------------------------------------------

k�k = Tk()
k�k.title ("pack()'le D�� pad'li Serilim")

Label (k�k, text="K�z�l G�ne�", bg="red", fg="Yellow").pack (fill=X, padx=10, pady=10)
Label (k�k, text="Ye�il Otlak", bg="green", fg="Cyan").pack (fill=X, padx=10, pady=10)
Label (k�k, text="Mavi G�k", bg="blue", fg="Lime").pack (fill=X, padx=10, pady=10)

k�k.mainloop()
#-----------------------------------------------------------------------------------------------------------

k�k = Tk()
k�k.title ("pack()'le �� pad'li Serilim")

Label (k�k, text="K�z�l G�ne�", bg="red", fg="Yellow").pack (ipadx=20) # ipad/internalpad=dahili tampon...
Label (k�k, text="Ye�il Otlak", bg="green", fg="Cyan").pack (ipady=20)
Label (k�k, text="Mavi G�k", bg="blue", fg="Lime").pack (ipadx=20, ipady=20)

k�k.mainloop()
#-----------------------------------------------------------------------------------------------------------

k�k = Tk()
k�k.title ("pack()'le Sol'dan Yanyana Serilim")

Label (k�k, text="K�z�l G�ne�", bg="red", fg="Yellow").pack (padx=5, pady=10, side=LEFT) # Etiketler sola yana��k...
Label (k�k, text="Ye�il Otlak", bg="green", fg="Cyan").pack (padx=5, pady=10, side=LEFT)
Label (k�k, text="Mavi G�k", bg="blue", fg="Lime").pack (padx=5, pady=10, side=LEFT)

k�k.mainloop()
#-----------------------------------------------------------------------------------------------------------

k�k = Tk()
k�k.title ("pack()'le Sa�'dan Yanyana Serilim")

Label (k�k, text="K�z�l G�ne�", bg="red", fg="Yellow").pack (padx=5, pady=10, side=RIGHT) # Etiketler sa�a yana��k...
Label (k�k, text="Ye�il Otlak", bg="green", fg="Cyan").pack (padx=5, pady=10, side=RIGHT)
Label (k�k, text="Mavi G�k", bg="blue", fg="Lime").pack (padx=5, pady=10, side=RIGHT)

k�k.mainloop()
