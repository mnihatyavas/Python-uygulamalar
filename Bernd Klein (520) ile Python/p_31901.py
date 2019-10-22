# coding:iso-8859-9 T�rk�e
# p_31901.py: Resmi �oklu sat�r s�tunlu �r�nt� kal�b� olarak kullanma �rne�i.

import numpy as np
import matplotlib.pyplot as mp
import matplotlib.image as mi
from p_315 import Renk

def resim�r�nt�s� (resim, n, m=1): # (n,m): (sat�r x s�tun)
    if n == 1: �r�nt�Resimler = resim
    else:
        dikey�r�nt� = []
        for i in range (n): dikey�r�nt�.append (resim)  
        �r�nt�Resimler = np.concatenate (dikey�r�nt�, axis=0) # Dikey y-ekseni...
    if m > 1:
        yatay�r�nt� = []
        for i in range (m): yatay�r�nt�.append (�r�nt�Resimler)  
        �r�nt�Resimler = np.concatenate (yatay�r�nt�, axis=1 ) # Yatay x-ekseni
    return �r�nt�Resimler

mp.style.use ("dark_background")
boyac�larKal�b� = mi.imread ('resim/boyac�larKal�b�.png')
duvarDekorasyonu = resim�r�nt�s� (boyac�larKal�b�, 3, 4)

mp.title ("(3x4) �r�nt�l� 4'er Avatarl� Resimli Kal�p")
mp.axis ("off")
mp.imshow (duvarDekorasyonu)
mp.show()
#-----------------------------------------------------------------------------------------------------

duvarDekorasyonu = resim�r�nt�s� (boyac�larKal�b�, 4, 5)

mp.figure().set_facecolor (Renk.renk())
mp.title ("(4x5) �r�nt�l� 4'er Avatarl� Resimli Kal�p", color=Renk.renk())
mp.axis ("off")
mp.imshow (duvarDekorasyonu)
mp.show()