# coding:iso-8859-9 Türkçe
# p_31604.py: Çubuk grafiklerle yıllara dağınık turist sayısı örneği.

import numpy as np
import matplotlib.pyplot as mp
from p_315 import Renk

yıllar = ("2012", "2013", "2014", "2015", "2016", "2017", "2018")
Y = (1241, 50927, 162242, 222093, 296665 / 8 * 12, 65782, 65782 * 4.55)
X = np.arange (len (Y))
çubukEni = 0.95

şekil = mp.figure()
şekil.set_facecolor (Renk.renk())
mp.title ("Yıllara Göre Kuşadasını Ziyaret Eden Yabancı Turist Sayısı", color=Renk.renk())

altşekil1 = şekil.add_subplot (111)
altşekil1.set_facecolor (Renk.renk())
mp.xticks (X, yıllar) # altşekil.set_xticks yılları yansıtmadı...
altşekil1.set_xlabel ("Yıllar", color=Renk.renk())
altşekil1.set_ylabel ("Kuşadası'na Turist Sayısı", color=Renk.renk())
altşekil1.set_xlim (-0.5, 6.5)
çubuklar = altşekil1.bar (X, Y, çubukEni,  color=Renk.renk())
for çubuk in çubuklar: çubuk.set_color (Renk.renk())

mp.tight_layout()
mp.show()