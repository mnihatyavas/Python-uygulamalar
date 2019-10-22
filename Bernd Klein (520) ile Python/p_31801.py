# coding:iso-8859-9 T�rk�e
# p_31801.py: Scipy misc ascent veri dosyas�ndan merdiven t�rman�� resmi tarama �rne�i.

#pip install scipy #scipy-1.3.0

from scipy import misc as spm
import matplotlib.pyplot as mp
from p_315 import Renk

t�rman�� = spm.ascent() # Data dosyas� verileri...
mp.imshow (t�rman��)

mp.figure().set_facecolor (Renk.renk())
mp.title ("Merdiven T�rman��� Data Resmi", fontsize=17)
mp.gray()
mp.show()
#---------------------------------------------------------------------------------------------------

t�rman�� = spm.ascent()
mp.imshow (t�rman��)

mp.figure().set_facecolor (Renk.renk())
mp.title ("Merdiven T�rman��� Data Resmi", color=Renk.renk(), fontsize=17)
mp.gray()
mp.axis ("off")
mp.tight_layout()
mp.show()
#---------------------------------------------------------------------------------------------------

print ("'ascent' veri dosyas� tipi:", t�rman��.dtype)
print ("'ascent' veri dosyas� �ekli:", t�rman��.shape)



"""��kt�:
>python p_31801.py
'ascent' veri dosyas� tipi: int32
'ascent' veri dosyas� �ekli: (512, 512)
"""