# coding:iso-8859-9 T�rk�e
# p_31507.py: Izgaral�k ile �oklu alt�ekilleri konumland�rma ve renklendirme �rne�i.

import matplotlib.pyplot as mp
import matplotlib.gridspec as mg
from p_315 import Renk

mp.figure (figsize=(6, 4))
�zgara = mg.GridSpec (3, 3) # 3 sat�r ve 3 s�tunluk...

alt�ekil1 = mp.subplot (�zgara [0, :])
mp.xticks(())
mp.yticks(())
mp.text (0.5, 0.5, 'Alt�ekil 1', ha='center', va='center', size=24, alpha=.5)

alt�ekil2 = mp.subplot (�zgara [1, :-1])
mp.xticks(())
mp.yticks(())
mp.text (0.5, 0.5, 'Alt�ekil 2', ha='center', va='center', size=24, alpha=.5)

alt�ekil3 = mp.subplot (�zgara [1:, -1])
mp.xticks(())
mp.yticks(())
mp.text (0.5, 0.5, 'Alt�ekil 3', ha='center', va='center', size=24, alpha=.5)

alt�ekil4 = mp.subplot (�zgara [-1, 0])
mp.xticks(())
mp.yticks(())
mp.text (0.5, 0.5, 'Alt�ekil 4', ha='center', va='center', size=24, alpha=.5)

alt�ekil5 = mp.subplot (�zgara [-1, -2])
mp.xticks(())
mp.yticks(())
mp.text (0.5, 0.5, 'Alt�ekil 5', ha='center', va='center', size=24, alpha=.5)

mp.tight_layout()
mp.show()
#-------------------------------------------------------------------------------------------------------

mp.style.use ("dark_background")
�ekil = mp.figure (figsize=(7, 4))
�zgara = mg.GridSpec (3, 3) # 3 sat�r ve 3 s�tunluk...

alt�ekil1 = �ekil.add_subplot (�zgara [0, :])
alt�ekil1.text (0.5, 0.5, 'Alt�ekil 1', ha='center', va='center', size=24, alpha=.5)

alt�ekil2 = �ekil.add_subplot (�zgara [1, :-1])
alt�ekil2.text (0.5, 0.5, 'Alt�ekil 2', ha='center', va='center', size=24, alpha=.5)

alt�ekil3 = �ekil.add_subplot (�zgara [1:, -1])
alt�ekil3.text (0.5, 0.5, 'Alt�ekil 3', ha='center', va='center', size=24, alpha=.5)

alt�ekil4 = �ekil.add_subplot (�zgara [-1, 0])
alt�ekil4.text (0.5, 0.5, 'Alt�ekil 4', ha='center', va='center', size=24, alpha=.5)

alt�ekil5 = �ekil.add_subplot (�zgara [-1, -2])
alt�ekil5.text (0.5, 0.5, 'Alt�ekil 5', ha='center', va='center', size=24, alpha=.5)

�ekil.tight_layout()
mp.show()
#-------------------------------------------------------------------------------------------------------

�ekil = mp.figure (figsize=(7, 4))
�ekil.set_facecolor (Renk.renk())
�zgara = mg.GridSpec (3, 3) # 3 sat�r ve 3 s�tunluk...

alt�ekil1 = �ekil.add_subplot (�zgara [0, :])
alt�ekil1.text (0.5, 0.5, 'Alt�ekil 1', ha='center', va='center', size=24, alpha=.5)
alt�ekil1.set_facecolor (Renk.renk())

alt�ekil2 = �ekil.add_subplot (�zgara [1, :-1])
alt�ekil2.text (0.5, 0.5, 'Alt�ekil 2', ha='center', va='center', size=24, alpha=.5)
alt�ekil2.set_facecolor (Renk.renk())

alt�ekil3 = �ekil.add_subplot (�zgara [1:, -1])
alt�ekil3.text (0.5, 0.5, 'Alt�ekil 3', ha='center', va='center', size=24, alpha=.5)
alt�ekil3.set_facecolor (Renk.renk())

alt�ekil4 = �ekil.add_subplot (�zgara [-1, 0])
alt�ekil4.text (0.5, 0.5, 'Alt�ekil 4', ha='center', va='center', size=24, alpha=.5)
alt�ekil4.set_facecolor (Renk.renk())

alt�ekil5 = �ekil.add_subplot (�zgara [-1, -2])
alt�ekil5.text (0.5, 0.5, 'Alt�ekil 5', ha='center', va='center', size=24, alpha=.5)
alt�ekil5.set_facecolor (Renk.renk())

�ekil.tight_layout()
mp.show()
#-------------------------------------------------------------------------------------------------------

�ekil = mp.figure (figsize=(7, 4))
�ekil.set_facecolor (Renk.renk())
�zgara = mg.GridSpec (3, 3) # 3 sat�r ve 3 s�tunluk...

alt�ekil1 = �ekil.add_subplot (�zgara [0, :])
alt�ekil1.text (0.5, 0.5, 'Alt�ekil 1', ha='center', va='center', size=24, color=Renk.renk(), backgroundcolor=Renk.renk(), alpha=.2)
alt�ekil1.set_facecolor (Renk.renk())
alt�ekil1.set_xticks(())
alt�ekil1.set_yticks(())

alt�ekil2 = �ekil.add_subplot (�zgara [1, :-1])
alt�ekil2.text (0.5, 0.5, 'Alt�ekil 2', ha='center', va='center', size=24, color=Renk.renk(), backgroundcolor=Renk.renk(), alpha=.4)
alt�ekil2.set_facecolor (Renk.renk())
alt�ekil2.set_xticks(())
alt�ekil2.set_yticks(())

alt�ekil3 = �ekil.add_subplot (�zgara [1:, -1])
alt�ekil3.text (0.5, 0.5, 'Alt�ekil 3', ha='center', va='center', size=24, color=Renk.renk(), backgroundcolor=Renk.renk(), alpha=.6)
alt�ekil3.set_facecolor (Renk.renk())

alt�ekil4 = �ekil.add_subplot (�zgara [-1, 0])
alt�ekil4.text (0.5, 0.5, 'Alt�ekil 4', ha='center', va='center', size=24, color=Renk.renk(), backgroundcolor=Renk.renk(), alpha=.8)
alt�ekil4.set_facecolor (Renk.renk())
alt�ekil4.set_xticks(())
alt�ekil4.set_yticks(())

alt�ekil5 = �ekil.add_subplot (�zgara [-1, -2])
alt�ekil5.text (0.5, 0.5, 'Alt�ekil 5', ha='center', va='center', size=24, color=Renk.renk(), backgroundcolor=Renk.renk(), alpha=.99)
alt�ekil5.set_facecolor (Renk.renk())
alt�ekil5.set_xticks(())
alt�ekil5.set_yticks(())

�ekil.tight_layout()
mp.show()
#-------------------------------------------------------------------------------------------------------

�ekil = mp.figure (figsize=(7, 4))
�ekil.set_facecolor (Renk.renk())
�zgara = mg.GridSpec (3, 3) # 3 sat�r ve 3 s�tunluk...

alt�ekil1 = �ekil.add_subplot (�zgara [0, 0:3]) # Farkl� konumland�rma y�ntemi...
alt�ekil1.text (0.5, 0.5, 'Alt�ekil 1', ha='center', va='center', size=24, color=Renk.renk(), backgroundcolor=Renk.renk())
alt�ekil1.set_facecolor (Renk.renk())
alt�ekil1.set_xticks(())
alt�ekil1.set_yticks(())

alt�ekil2 = �ekil.add_subplot (�zgara [1, 0:2])
alt�ekil2.text (0.5, 0.5, 'Alt�ekil 2', ha='center', va='center', size=24, color=Renk.renk(), backgroundcolor=Renk.renk())
alt�ekil2.set_facecolor (Renk.renk())
alt�ekil2.set_xticks(())
alt�ekil2.set_yticks(())

alt�ekil3 = �ekil.add_subplot (�zgara [1:3, 2])
alt�ekil3.text (0.5, 0.5, 'Alt�ekil 3', ha='center', va='center', size=24, color=Renk.renk(), backgroundcolor=Renk.renk())
alt�ekil3.set_facecolor (Renk.renk())
alt�ekil3.set_xticks(())
alt�ekil3.set_yticks(())

alt�ekil4 = �ekil.add_subplot (�zgara [2, 0])
alt�ekil4.text (0.5, 0.5, 'Alt�ekil 4', ha='center', va='center', size=24, color=Renk.renk(), backgroundcolor=Renk.renk())
alt�ekil4.set_facecolor (Renk.renk())
alt�ekil4.set_xticks(())
alt�ekil4.set_yticks(())

alt�ekil5 = �ekil.add_subplot (�zgara [2, 1])
alt�ekil5.text (0.5, 0.5, 'Alt�ekil 5', ha='center', va='center', size=24, color=Renk.renk(), backgroundcolor=Renk.renk())
alt�ekil5.set_facecolor (Renk.renk())
alt�ekil5.set_xticks(())
alt�ekil5.set_yticks(())

�ekil.tight_layout()
mp.show()
