# coding:iso-8859-9 Türkçe
# p_31802.py: Scipy misc face veri dosyasından rakun resmi tarama örneği.

from scipy import misc as spm
import matplotlib.pyplot as mp
from p_315 import Renk

mp.figure().set_facecolor (Renk.renk())
mp.title ("Rakun Sansarı Data Resmi", color=Renk.renk(), fontsize=18)
rakunSansarı = spm.face()
mp.axis ("off")
#mp.gray()
mp.imshow (rakunSansarı)
mp.tight_layout()
mp.show()
#-----------------------------------------------------------------------------------------------------

print ("Rakun sansarı matris şekli:", rakunSansarı.shape)
print ("Matris azami:", rakunSansarı.max)
print ("Matris tipi:", rakunSansarı.dtype)



"""Çıktı:
>python p_31802.py
Rakun sansarı matris şekli: (768, 1024, 3)
Matris azami: <built-in method max of numpy.ndarray object at 0x0532ECF0>
Matris tipi: uint8
"""