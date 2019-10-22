# coding:iso-8859-9 Türkçe
# p_31801.py: Scipy misc ascent veri dosyasından merdiven tırmanış resmi tarama örneği.

#pip install scipy #scipy-1.3.0

from scipy import misc as spm
import matplotlib.pyplot as mp
from p_315 import Renk

tırmanış = spm.ascent() # Data dosyası verileri...
mp.imshow (tırmanış)

mp.figure().set_facecolor (Renk.renk())
mp.title ("Merdiven Tırmanışı Data Resmi", fontsize=17)
mp.gray()
mp.show()
#---------------------------------------------------------------------------------------------------

tırmanış = spm.ascent()
mp.imshow (tırmanış)

mp.figure().set_facecolor (Renk.renk())
mp.title ("Merdiven Tırmanışı Data Resmi", color=Renk.renk(), fontsize=17)
mp.gray()
mp.axis ("off")
mp.tight_layout()
mp.show()
#---------------------------------------------------------------------------------------------------

print ("'ascent' veri dosyası tipi:", tırmanış.dtype)
print ("'ascent' veri dosyası şekli:", tırmanış.shape)



"""Çıktı:
>python p_31801.py
'ascent' veri dosyası tipi: int32
'ascent' veri dosyası şekli: (512, 512)
"""