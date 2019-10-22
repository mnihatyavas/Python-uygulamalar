# coding:iso-8859-9 Türkçe
# p_31804.py: Bir resmi tümden veya kademeli ağartma ve karartma örneği.

import numpy as np
import matplotlib.pyplot as mp
from p_315 import Renk

mp.style.use ("dark_background")
mp.title ("Hollanda Roterdam'da bir Yeldeğirmeni", color="r", fontsize=15)
mp.axis ("off")
Resim = mp.imread ('resim/yelDeğirmeni.png')
mp.imshow (Resim)
mp.tight_layout()
mp.show()
#------------------------------------------------------------------------------------------------------

def ağart (resim, oran): return resim + (np.ones (resim.shape) - resim) * oran

mp.figure().set_facecolor (Renk.renk())
mp.title ("Roterdam'da %60 Ağartılan bir Yeldeğirmeni", color=Renk.renk(), fontsize=15)
mp.axis ("off")

ağaranResim = ağart (Resim, 0.6)
mp.imshow (ağaranResim)
mp.show()
#------------------------------------------------------------------------------------------------------

def karart (resim, oran): return resim * (1 - oran)

mp.figure().set_facecolor (Renk.renk())
mp.title ("Roterdam'da %55 Karartılan bir Yeldeğirmeni", color=Renk.renk(), fontsize=15)
mp.axis ("off")

kararanResim = karart (Resim, 0.55)
mp.imshow (kararanResim)
mp.show()
#------------------------------------------------------------------------------------------------------

def yatayKademeleme (resim, reverse=False):
    kolonAdedi = resim.shape [1] # 384...
    if reverse: X = np.linspace (1, 0, kolonAdedi) # Ağartma sağdan sola artar...
    else: X = np.linspace (0, 1, kolonAdedi) #==> Ağartma soldan sağa artar...
    X = np.dstack ((X, X, X, X))
    return X

mp.figure().set_facecolor (Renk.renk())
mp.title ("Roterdam'da Soldan-sağa Ağaran bir Yeldeğirmeni", color=Renk.renk(), fontsize=15)
mp.axis ("off")

sağaAğaranResim =  yatayKademeleme (Resim) * Resim
mp.imshow (sağaAğaranResim)
mp.show()
#------------------------------------------------------------------------------------------------------

def yatayKademeleme (resim, reverse=False):
    kolonAdedi = resim.shape [1] # 384...
    if reverse: X = np.linspace (1, 0, kolonAdedi) #==> Ağartma sağdan sola artar...
    else: X = np.linspace (0, 1, kolonAdedi) # Ağartma soldan sağa artar...
    X = np.dstack ((X, X, X, X))
    return X

mp.figure().set_facecolor (Renk.renk())
mp.title ("Roterdam'da Sağdan-sola Ağaran bir Yeldeğirmeni", color=Renk.renk(), fontsize=15)
mp.axis ("off")

solaAğaranResim =  Resim * yatayKademeleme (Resim, reverse=True)
mp.imshow (solaAğaranResim)
mp.show()
#------------------------------------------------------------------------------------------------------

def yatayKademeleme (resim):
    satırSayısı, sütunSayısı = resim.shape [0], resim.shape [1]
    X = np.linspace (1, 0, satırSayısı)
    X = X [np.newaxis, :]
    X = np.concatenate ((X, X, X, X)).transpose()
    X = X [:, np.newaxis]
    return X

mp.figure().set_facecolor (Renk.renk())
mp.title ("Roterdam'da Alttan-üste Ağaran bir Yeldeğirmeni", color=Renk.renk(), fontsize=15)
mp.axis ("off")

üsteAğaranResim =  yatayKademeleme (Resim) * Resim
mp.imshow (üsteAğaranResim)
mp.show()
