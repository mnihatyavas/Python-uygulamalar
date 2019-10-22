# coding:iso-8859-9 Türkçe
# p_31501.py: Bir grafik penceresini 4 altpencereye bölme örneği.

import matplotlib.pyplot as mp

import numpy as np
mp.style.use ('dark_background')
mp.plot (np.sin (np.linspace (0, 2 * np.pi)), 'r-o')
mp.show()
#-----------------------------------------------------------------------------------------------------

mp.figure (figsize=(8, 4) ) # Altpencerelerin en ve boyu...
mp.subplot (221).set_facecolor ('lightslategray') # Satır, sütun ve aktifno virgüllü de verilebilir: mp.subplot (2, 2, 1)
mp.fill_between ([0,1], [0,1], 1, color='orange', alpha=.9)
mp.fill_between ([0,1], [0,1], 0, color='orange', alpha=.9)
mp.text (# Altpencere içine yazılacak metin özellikleri...
    0.5, # Metnin x yatay konumu [0, 1]...
    0.5, # Metnin y dikey konumu [0, 1]...
    'subplot (2, 2, 1)', # Yazılacak metin...
    horizontalalignment='center', # Yatay hizalama (kısaca: 'ha')...
    verticalalignment='center', # Dikey hizalama (kısaca: "va")...
    fontsize=20, # Metnin ebatı...
    color="Cyan", # Metnin yazı rengi...
    alpha=.5, # Şeffaf-->Opak ölçeği [0, 1]...
    backgroundcolor="Brown" # Metnin zemin rengi...
    )

mp.subplot (2, 2, 4).set_facecolor ('lightslategray') # Gösterilecek son altpencere...
#mp.subplot(224, axisbg="Green") # axisbg yerine: set_facecolor...
mp.fill_between ([0,1], [0,1], color='orange', alpha=.9)
mp.text (0.5, 0.5, 'altpencere (224)', ha='center', va='center', fontsize=20,
    color="r", backgroundcolor="b")

mp.show()
#-----------------------------------------------------------------------------------------------------

mp.figure (figsize=(7,4) )
mp.subplot (221).set_facecolor ("Tan")
mp.xticks ( () ) # Yatay ve dikey eksen çentikleri olmasın...
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

şekil = mp.figure (figsize=(7,2) )
şekil.set_facecolor ("Navy") # şekil nesnesine, altşekilleri ekleyelim...
altşekil1 = şekil.add_subplot (221)
altşekil1.set_facecolor ("Salmon")
altşekil1.text (0.5, 0.5, 'subplot (2, 2, 1)', ha='center', va='center',
    fontsize=20, color="Cyan", alpha=.95, backgroundcolor="Brown")
altşekil1.set_xticks(()) # set_xticks kullanılmalı (veya mp.xticks)...
altşekil1.set_yticks(())

altşekil2 = şekil.add_subplot (2, 2, 4)
altşekil2.set_facecolor ("Brown")
altşekil2.text (0.5, 0.5, 'altpencere (224)', ha='center', va='center', fontsize=20,
    color="r", backgroundcolor="b")
altşekil2.set_xticks(())
altşekil2.set_yticks(())

mp.show()
#-----------------------------------------------------------------------------------------------------

# 4 altşekli de etkinleştirelim...
şekil = mp.figure (figsize=(7,5) )
#şekil.set_facecolor ("Gold") # Sütun ve satır genişliğini değiştirelim...
altşekil1 = şekil.add_subplot (221)
altşekil1.set_facecolor ("Green")
altşekil1.text (0.5, 0.5, 'subplot (2, 2, 1)', ha='center', va='center',
    fontsize=15, color="Cyan", alpha=.55, backgroundcolor="Brown")
mp.fill_between ([0,1], [0,1], 0, color='orange')
mp.fill_between ([0,1], [0,1], 1, color='orange')
mp.xlim (0,1)
mp.ylim (0,1)

altşekil2 = şekil.add_subplot (222)
altşekil2.set_facecolor ("Blue")
altşekil2.text (0.5, 0.5, 'subplot (2, 2, 2)', ha='center', va='center',
    fontsize=15, color="Cyan", alpha=.75, backgroundcolor="Brown")
mp.fill_between ([0,1], [0,1], 0, color='Brown')
mp.fill_between ([0,1], [0,1], 1, color='Brown')
mp.xlim (0,1)
mp.ylim (0,1)

altşekil3 = şekil.add_subplot (223)
altşekil3.set_facecolor ("Pink")
altşekil3.text (0.5, 0.5, 'subplot (2, 2, 3)', ha='center', va='center',
    fontsize=15, color="Cyan", alpha=.95, backgroundcolor="Brown")
mp.fill_between ([0,1], [0,1], 0, color='Brown', alpha="0.5")
mp.fill_between ([0,1], [0,1], 1, color='Brown', alpha="0.5")
mp.xlim (0,1)
mp.ylim (0,1)

altşekil4 = şekil.add_subplot (2, 2, 4)
altşekil4.set_facecolor ("Magenta")
altşekil4.text (0.5, 0.5, 'altpencere (224)', ha='center', va='center',
    fontsize=15, color="r", backgroundcolor="b")
mp.fill_between ([0,1], [0,1], 0, color='blue', alpha="0.1")
mp.fill_between ([0,1], [0,1], 1, color='blue', alpha="0.7")
mp.xlim (0,1)
mp.ylim (0,1)

mp.show()
