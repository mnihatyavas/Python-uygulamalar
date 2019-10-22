# coding:iso-8859-9 T�rk�e

# python -m pip install Pillow
# easy_install Pillow

from PIL import Image, ImageFilter

print ("PIL mod�l�n� kurma ve resmi varsay�l� g�stericiyle net/bulan�k g�r�nt�lrme")
try:
    orijinalResim = Image.open ("resim/nissan.png")
    orijinalResim.show()
    bulan�kResim = orijinalResim.filter (ImageFilter.BLUR)
    bulan�kResim.show()
    #bulan�kResim.save ("bulan�k.png")
except:
    print ("HATA: Bulan�k resmi saklayam�yorum!..")
