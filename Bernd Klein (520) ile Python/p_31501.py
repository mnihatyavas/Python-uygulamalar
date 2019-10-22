# coding:iso-8859-9 T�rk�e
# p_31501.py: Bir grafik penceresini 4 altpencereye b�lme �rne�i.

import matplotlib.pyplot as mp

import numpy as np
mp.style.use ('dark_background')
mp.plot (np.sin (np.linspace (0, 2 * np.pi)), 'r-o')
mp.show()
#-----------------------------------------------------------------------------------------------------

mp.figure (figsize=(8, 4) ) # Altpencerelerin en ve boyu...
mp.subplot (221).set_facecolor ('lightslategray') # Sat�r, s�tun ve aktifno virg�ll� de verilebilir: mp.subplot (2, 2, 1)
mp.fill_between ([0,1], [0,1], 1, color='orange', alpha=.9)
mp.fill_between ([0,1], [0,1], 0, color='orange', alpha=.9)
mp.text (# Altpencere i�ine yaz�lacak metin �zellikleri...
    0.5, # Metnin x yatay konumu [0, 1]...
    0.5, # Metnin y dikey konumu [0, 1]...
    'subplot (2, 2, 1)', # Yaz�lacak metin...
    horizontalalignment='center', # Yatay hizalama (k�saca: 'ha')...
    verticalalignment='center', # Dikey hizalama (k�saca: "va")...
    fontsize=20, # Metnin ebat�...
    color="Cyan", # Metnin yaz� rengi...
    alpha=.5, # �effaf-->Opak �l�e�i [0, 1]...
    backgroundcolor="Brown" # Metnin zemin rengi...
    )

mp.subplot (2, 2, 4).set_facecolor ('lightslategray') # G�sterilecek son altpencere...
#mp.subplot(224, axisbg="Green") # axisbg yerine: set_facecolor...
mp.fill_between ([0,1], [0,1], color='orange', alpha=.9)
mp.text (0.5, 0.5, 'altpencere (224)', ha='center', va='center', fontsize=20,
    color="r", backgroundcolor="b")

mp.show()
#-----------------------------------------------------------------------------------------------------

mp.figure (figsize=(7,4) )
mp.subplot (221).set_facecolor ("Tan")
mp.xticks ( () ) # Yatay ve dikey eksen �entikleri olmas�n...
mp.yticks ( () )
mp.text (0.5, 0.5, 'subplot (2, 2, 1)', ha='center', va='center',
    fontsize=20, color="Cyan", alpha=.8, backgroundcolor="Brown")

mp.subplot (2, 2, 4).set_facecolor ("Teal")
mp.xticks(())
mp.yticks(())
mp.text (0.5, 0.5, 'altpencere (224)', ha='center', va='center', fontsize=20,
    color="r", backgroundcolor="b")

mp.show()
#-----------------------------------------------------------------------------------------------------

�ekil = mp.figure (figsize=(7,2) )
�ekil.set_facecolor ("Navy") # �ekil nesnesine, alt�ekilleri ekleyelim...
alt�ekil1 = �ekil.add_subplot (221)
alt�ekil1.set_facecolor ("Salmon")
alt�ekil1.text (0.5, 0.5, 'subplot (2, 2, 1)', ha='center', va='center',
    fontsize=20, color="Cyan", alpha=.95, backgroundcolor="Brown")
alt�ekil1.set_xticks(()) # set_xticks kullan�lmal� (veya mp.xticks)...
alt�ekil1.set_yticks(())

alt�ekil2 = �ekil.add_subplot (2, 2, 4)
alt�ekil2.set_facecolor ("Brown")
alt�ekil2.text (0.5, 0.5, 'altpencere (224)', ha='center', va='center', fontsize=20,
    color="r", backgroundcolor="b")
alt�ekil2.set_xticks(())
alt�ekil2.set_yticks(())

mp.show()
#-----------------------------------------------------------------------------------------------------

# 4 alt�ekli de etkinle�tirelim...
�ekil = mp.figure (figsize=(7,5) )
#�ekil.set_facecolor ("Gold") # S�tun ve sat�r geni�li�ini de�i�tirelim...
alt�ekil1 = �ekil.add_subplot (221)
alt�ekil1.set_facecolor ("Green")
alt�ekil1.text (0.5, 0.5, 'subplot (2, 2, 1)', ha='center', va='center',
    fontsize=15, color="Cyan", alpha=.55, backgroundcolor="Brown")
mp.fill_between ([0,1], [0,1], 0, color='orange')
mp.fill_between ([0,1], [0,1], 1, color='orange')
mp.xlim (0,1)
mp.ylim (0,1)

alt�ekil2 = �ekil.add_subplot (222)
alt�ekil2.set_facecolor ("Blue")
alt�ekil2.text (0.5, 0.5, 'subplot (2, 2, 2)', ha='center', va='center',
    fontsize=15, color="Cyan", alpha=.75, backgroundcolor="Brown")
mp.fill_between ([0,1], [0,1], 0, color='Brown')
mp.fill_between ([0,1], [0,1], 1, color='Brown')
mp.xlim (0,1)
mp.ylim (0,1)

alt�ekil3 = �ekil.add_subplot (223)
alt�ekil3.set_facecolor ("Pink")
alt�ekil3.text (0.5, 0.5, 'subplot (2, 2, 3)', ha='center', va='center',
    fontsize=15, color="Cyan", alpha=.95, backgroundcolor="Brown")
mp.fill_between ([0,1], [0,1], 0, color='Brown', alpha="0.5")
mp.fill_between ([0,1], [0,1], 1, color='Brown', alpha="0.5")
mp.xlim (0,1)
mp.ylim (0,1)

alt�ekil4 = �ekil.add_subplot (2, 2, 4)
alt�ekil4.set_facecolor ("Magenta")
alt�ekil4.text (0.5, 0.5, 'altpencere (224)', ha='center', va='center',
    fontsize=15, color="r", backgroundcolor="b")
mp.fill_between ([0,1], [0,1], 0, color='blue', alpha="0.1")
mp.fill_between ([0,1], [0,1], 1, color='blue', alpha="0.7")
mp.xlim (0,1)
mp.ylim (0,1)

mp.show()
