#coding:iso-8859-9 Türkçe
# p_32505a.py: Pandas serisiyle çizgi, çubuk ve börek grafikler kind/çeşitlemesi örneği.

import matplotlib.pyplot as mp
import pandas as pd
from p_315 import Renk

liste = [100, 120, 140, 180, 200, 210, 214]
seri = pd.Series (liste, index=range (len (liste)))

mp.style.use ("dark_background")
seri.plot (kind="line", color=Renk.renk() )
mp.show()

seri.plot (kind="bar", color=Renk.renk() ) # Tüm çubuklar aynı renkte...
mp.show()

seri.plot (kind="bar", color=[Renk.renk() for _ in range (len (liste))] ) # Her çubuk farklı renkte...
mp.show()

seri.plot (kind="pie", colors=[Renk.renk() for _ in range (len (liste))] )
mp.show()
