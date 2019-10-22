# coding:iso-8859-9 T�rk�e
# p_31802.py: Scipy misc face veri dosyas�ndan rakun resmi tarama �rne�i.

from scipy import misc as spm
import matplotlib.pyplot as mp
from p_315 import Renk

mp.figure().set_facecolor (Renk.renk())
mp.title ("Rakun Sansar� Data Resmi", color=Renk.renk(), fontsize=18)
rakunSansar� = spm.face()
mp.axis ("off")
#mp.gray()
mp.imshow (rakunSansar�)
mp.tight_layout()
mp.show()
#-----------------------------------------------------------------------------------------------------

print ("Rakun sansar� matris �ekli:", rakunSansar�.shape)
print ("Matris azami:", rakunSansar�.max)
print ("Matris tipi:", rakunSansar�.dtype)



"""��kt�:
>python p_31802.py
Rakun sansar� matris �ekli: (768, 1024, 3)
Matris azami: <built-in method max of numpy.ndarray object at 0x0532ECF0>
Matris tipi: uint8
"""