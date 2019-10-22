# coding:iso-8859-9 T�rk�e
# p_31804.py: Bir resmi t�mden veya kademeli a�artma ve karartma �rne�i.

import numpy as np
import matplotlib.pyplot as mp
from p_315 import Renk

mp.style.use ("dark_background")
mp.title ("Hollanda Roterdam'da bir Yelde�irmeni", color="r", fontsize=15)
mp.axis ("off")
Resim = mp.imread ('resim/yelDe�irmeni.png')
mp.imshow (Resim)
mp.tight_layout()
mp.show()
#------------------------------------------------------------------------------------------------------

def a�art (resim, oran): return resim + (np.ones (resim.shape) - resim) * oran

mp.figure().set_facecolor (Renk.renk())
mp.title ("Roterdam'da %60 A�art�lan bir Yelde�irmeni", color=Renk.renk(), fontsize=15)
mp.axis ("off")

a�aranResim = a�art (Resim, 0.6)
mp.imshow (a�aranResim)
mp.show()
#------------------------------------------------------------------------------------------------------

def karart (resim, oran): return resim * (1 - oran)

mp.figure().set_facecolor (Renk.renk())
mp.title ("Roterdam'da %55 Karart�lan bir Yelde�irmeni", color=Renk.renk(), fontsize=15)
mp.axis ("off")

kararanResim = karart (Resim, 0.55)
mp.imshow (kararanResim)
mp.show()
#------------------------------------------------------------------------------------------------------

def yatayKademeleme (resim, reverse=False):
    kolonAdedi = resim.shape [1] # 384...
    if reverse: X = np.linspace (1, 0, kolonAdedi) # A�artma sa�dan sola artar...
    else: X = np.linspace (0, 1, kolonAdedi) #==> A�artma soldan sa�a artar...
    X = np.dstack ((X, X, X, X))
    return X

mp.figure().set_facecolor (Renk.renk())
mp.title ("Roterdam'da Soldan-sa�a A�aran bir Yelde�irmeni", color=Renk.renk(), fontsize=15)
mp.axis ("off")

sa�aA�aranResim =  yatayKademeleme (Resim) * Resim
mp.imshow (sa�aA�aranResim)
mp.show()
#------------------------------------------------------------------------------------------------------

def yatayKademeleme (resim, reverse=False):
    kolonAdedi = resim.shape [1] # 384...
    if reverse: X = np.linspace (1, 0, kolonAdedi) #==> A�artma sa�dan sola artar...
    else: X = np.linspace (0, 1, kolonAdedi) # A�artma soldan sa�a artar...
    X = np.dstack ((X, X, X, X))
    return X

mp.figure().set_facecolor (Renk.renk())
mp.title ("Roterdam'da Sa�dan-sola A�aran bir Yelde�irmeni", color=Renk.renk(), fontsize=15)
mp.axis ("off")

solaA�aranResim =  Resim * yatayKademeleme (Resim, reverse=True)
mp.imshow (solaA�aranResim)
mp.show()
#------------------------------------------------------------------------------------------------------

def yatayKademeleme (resim):
    sat�rSay�s�, s�tunSay�s� = resim.shape [0], resim.shape [1]
    X = np.linspace (1, 0, sat�rSay�s�)
    X = X [np.newaxis, :]
    X = np.concatenate ((X, X, X, X)).transpose()
    X = X [:, np.newaxis]
    return X

mp.figure().set_facecolor (Renk.renk())
mp.title ("Roterdam'da Alttan-�ste A�aran bir Yelde�irmeni", color=Renk.renk(), fontsize=15)
mp.axis ("off")

�steA�aranResim =  yatayKademeleme (Resim) * Resim
mp.imshow (�steA�aranResim)
mp.show()
