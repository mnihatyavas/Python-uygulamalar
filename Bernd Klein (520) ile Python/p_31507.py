# coding:iso-8859-9 Türkçe
# p_31507.py: Izgaralık ile çoklu altşekilleri konumlandırma ve renklendirme örneği.

import matplotlib.pyplot as mp
import matplotlib.gridspec as mg
from p_315 import Renk

mp.figure (figsize=(6, 4))
ızgara = mg.GridSpec (3, 3) # 3 satır ve 3 sütunluk...

altşekil1 = mp.subplot (ızgara [0, :])
mp.xticks(())
mp.yticks(())
mp.text (0.5, 0.5, 'Altşekil 1', ha='center', va='center', size=24, alpha=.5)

altşekil2 = mp.subplot (ızgara [1, :-1])
mp.xticks(())
mp.yticks(())
mp.text (0.5, 0.5, 'Altşekil 2', ha='center', va='center', size=24, alpha=.5)

altşekil3 = mp.subplot (ızgara [1:, -1])
mp.xticks(())
mp.yticks(())
mp.text (0.5, 0.5, 'Altşekil 3', ha='center', va='center', size=24, alpha=.5)

altşekil4 = mp.subplot (ızgara [-1, 0])
mp.xticks(())
mp.yticks(())
mp.text (0.5, 0.5, 'Altşekil 4', ha='center', va='center', size=24, alpha=.5)

altşekil5 = mp.subplot (ızgara [-1, -2])
mp.xticks(())
mp.yticks(())
mp.text (0.5, 0.5, 'Altşekil 5', ha='center', va='center', size=24, alpha=.5)

mp.tight_layout()
mp.show()
#-------------------------------------------------------------------------------------------------------

mp.style.use ("dark_background")
şekil = mp.figure (figsize=(7, 4))
ızgara = mg.GridSpec (3, 3) # 3 satır ve 3 sütunluk...

altşekil1 = şekil.add_subplot (ızgara [0, :])
altşekil1.text (0.5, 0.5, 'Altşekil 1', ha='center', va='center', size=24, alpha=.5)

altşekil2 = şekil.add_subplot (ızgara [1, :-1])
altşekil2.text (0.5, 0.5, 'Altşekil 2', ha='center', va='center', size=24, alpha=.5)

altşekil3 = şekil.add_subplot (ızgara [1:, -1])
altşekil3.text (0.5, 0.5, 'Altşekil 3', ha='center', va='center', size=24, alpha=.5)

altşekil4 = şekil.add_subplot (ızgara [-1, 0])
altşekil4.text (0.5, 0.5, 'Altşekil 4', ha='center', va='center', size=24, alpha=.5)

altşekil5 = şekil.add_subplot (ızgara [-1, -2])
altşekil5.text (0.5, 0.5, 'Altşekil 5', ha='center', va='center', size=24, alpha=.5)

şekil.tight_layout()
mp.show()
#-------------------------------------------------------------------------------------------------------

şekil = mp.figure (figsize=(7, 4))
şekil.set_facecolor (Renk.renk())
ızgara = mg.GridSpec (3, 3) # 3 satır ve 3 sütunluk...

altşekil1 = şekil.add_subplot (ızgara [0, :])
altşekil1.text (0.5, 0.5, 'Altşekil 1', ha='center', va='center', size=24, alpha=.5)
altşekil1.set_facecolor (Renk.renk())

altşekil2 = şekil.add_subplot (ızgara [1, :-1])
altşekil2.text (0.5, 0.5, 'Altşekil 2', ha='center', va='center', size=24, alpha=.5)
altşekil2.set_facecolor (Renk.renk())

altşekil3 = şekil.add_subplot (ızgara [1:, -1])
altşekil3.text (0.5, 0.5, 'Altşekil 3', ha='center', va='center', size=24, alpha=.5)
altşekil3.set_facecolor (Renk.renk())

altşekil4 = şekil.add_subplot (ızgara [-1, 0])
altşekil4.text (0.5, 0.5, 'Altşekil 4', ha='center', va='center', size=24, alpha=.5)
altşekil4.set_facecolor (Renk.renk())

altşekil5 = şekil.add_subplot (ızgara [-1, -2])
altşekil5.text (0.5, 0.5, 'Altşekil 5', ha='center', va='center', size=24, alpha=.5)
altşekil5.set_facecolor (Renk.renk())

şekil.tight_layout()
mp.show()
#-------------------------------------------------------------------------------------------------------

şekil = mp.figure (figsize=(7, 4))
şekil.set_facecolor (Renk.renk())
ızgara = mg.GridSpec (3, 3) # 3 satır ve 3 sütunluk...

altşekil1 = şekil.add_subplot (ızgara [0, :])
altşekil1.text (0.5, 0.5, 'Altşekil 1', ha='center', va='center', size=24, color=Renk.renk(), backgroundcolor=Renk.renk(), alpha=.2)
altşekil1.set_facecolor (Renk.renk())
altşekil1.set_xticks(())
altşekil1.set_yticks(())

altşekil2 = şekil.add_subplot (ızgara [1, :-1])
altşekil2.text (0.5, 0.5, 'Altşekil 2', ha='center', va='center', size=24, color=Renk.renk(), backgroundcolor=Renk.renk(), alpha=.4)
altşekil2.set_facecolor (Renk.renk())
altşekil2.set_xticks(())
altşekil2.set_yticks(())

altşekil3 = şekil.add_subplot (ızgara [1:, -1])
altşekil3.text (0.5, 0.5, 'Altşekil 3', ha='center', va='center', size=24, color=Renk.renk(), backgroundcolor=Renk.renk(), alpha=.6)
altşekil3.set_facecolor (Renk.renk())

altşekil4 = şekil.add_subplot (ızgara [-1, 0])
altşekil4.text (0.5, 0.5, 'Altşekil 4', ha='center', va='center', size=24, color=Renk.renk(), backgroundcolor=Renk.renk(), alpha=.8)
altşekil4.set_facecolor (Renk.renk())
altşekil4.set_xticks(())
altşekil4.set_yticks(())

altşekil5 = şekil.add_subplot (ızgara [-1, -2])
altşekil5.text (0.5, 0.5, 'Altşekil 5', ha='center', va='center', size=24, color=Renk.renk(), backgroundcolor=Renk.renk(), alpha=.99)
altşekil5.set_facecolor (Renk.renk())
altşekil5.set_xticks(())
altşekil5.set_yticks(())

şekil.tight_layout()
mp.show()
#-------------------------------------------------------------------------------------------------------

şekil = mp.figure (figsize=(7, 4))
şekil.set_facecolor (Renk.renk())
ızgara = mg.GridSpec (3, 3) # 3 satır ve 3 sütunluk...

altşekil1 = şekil.add_subplot (ızgara [0, 0:3]) # Farklı konumlandırma yöntemi...
altşekil1.text (0.5, 0.5, 'Altşekil 1', ha='center', va='center', size=24, color=Renk.renk(), backgroundcolor=Renk.renk())
altşekil1.set_facecolor (Renk.renk())
altşekil1.set_xticks(())
altşekil1.set_yticks(())

altşekil2 = şekil.add_subplot (ızgara [1, 0:2])
altşekil2.text (0.5, 0.5, 'Altşekil 2', ha='center', va='center', size=24, color=Renk.renk(), backgroundcolor=Renk.renk())
altşekil2.set_facecolor (Renk.renk())
altşekil2.set_xticks(())
altşekil2.set_yticks(())

altşekil3 = şekil.add_subplot (ızgara [1:3, 2])
altşekil3.text (0.5, 0.5, 'Altşekil 3', ha='center', va='center', size=24, color=Renk.renk(), backgroundcolor=Renk.renk())
altşekil3.set_facecolor (Renk.renk())
altşekil3.set_xticks(())
altşekil3.set_yticks(())

altşekil4 = şekil.add_subplot (ızgara [2, 0])
altşekil4.text (0.5, 0.5, 'Altşekil 4', ha='center', va='center', size=24, color=Renk.renk(), backgroundcolor=Renk.renk())
altşekil4.set_facecolor (Renk.renk())
altşekil4.set_xticks(())
altşekil4.set_yticks(())

altşekil5 = şekil.add_subplot (ızgara [2, 1])
altşekil5.text (0.5, 0.5, 'Altşekil 5', ha='center', va='center', size=24, color=Renk.renk(), backgroundcolor=Renk.renk())
altşekil5.set_facecolor (Renk.renk())
altşekil5.set_xticks(())
altşekil5.set_yticks(())

şekil.tight_layout()
mp.show()
