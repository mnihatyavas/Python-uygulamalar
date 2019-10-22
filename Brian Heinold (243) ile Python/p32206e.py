# coding:iso-8859-9 Türkçe

# python -m pip install Pillow
# easy_install Pillow

from PIL import Image, ImageFilter

print ("PIL modülünü kurma ve resmi varsayılı göstericiyle net/bulanık görüntülrme")
try:
    orijinalResim = Image.open ("resim/nissan.png")
    orijinalResim.show()
    bulanıkResim = orijinalResim.filter (ImageFilter.BLUR)
    bulanıkResim.show()
    #bulanıkResim.save ("bulanık.png")
except:
    print ("HATA: Bulanık resmi saklayamıyorum!..")
