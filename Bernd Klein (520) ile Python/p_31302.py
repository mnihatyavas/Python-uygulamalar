# coding:iso-8859-9 Türkçe
# p_31302.py: Yatay ve dikey çentikleri alma veya değiştirme örneği.

import numpy as np
import matplotlib.pyplot as mp

eksenler = mp.gca()

çentikler, değerleri = mp.xticks()
print ("Yatay çentikler ve değerleri:\n", çentikler, "\n", değerleri, sep="")

çentikler, değerleri = mp.yticks()
print ("\nDikey çentikler ve değerleri:\n", çentikler, "\n", değerleri[:], sep="")

mp.xlabel ("X=[0.0, 1.0]")
mp.ylabel ("Y=[0.0, 1.0]")
mp.plot()
mp.show()
print ("-"*50)
#------------------------------------------------------------------------------------------------------

mp.yticks (np.arange (0, 3001, 1000) )
çentikler, değerleri = mp.yticks()
print ("\nDikey çentikler ve değerleri:\n", çentikler, "\n", değerleri, sep="")

mp.xticks (np.arange (4), ('Berlin', 'Hamburg', 'Paris', 'Londra') )
çentikler, değerleri = mp.xticks()
print ("\nYatay çentikler ve değerleri:\n", çentikler, "\n", değerleri [:], sep="")

mp.xlabel ("Şehirler")
mp.ylabel ("İstanbul'a Mesafeler (km)")
mp.plot()
mp.show()



"""Çıktı:
>python p_31302.py
Yatay çentikler ve değerleri:
[0.  0.2 0.4 0.6 0.8 1. ]
<a list of 6 Text xticklabel objects>

Dikey çentikler ve değerleri:
[0.  0.2 0.4 0.6 0.8 1. ]
[Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, '')]
--------------------------------------------------

Dikey çentikler ve değerleri:
[   0 1000 2000 3000]
<a list of 4 Text yticklabel objects>

Yatay çentikler ve değerleri:
[0 1 2 3]
[Text(0, 0, 'Berlin'), Text(0, 0, 'Hamburg'), Text(0, 0, 'Paris'), Text(0, 0, 'Londra')]
"""