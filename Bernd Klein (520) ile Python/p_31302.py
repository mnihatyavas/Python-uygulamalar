# coding:iso-8859-9 T�rk�e
# p_31302.py: Yatay ve dikey �entikleri alma veya de�i�tirme �rne�i.

import numpy as np
import matplotlib.pyplot as mp

eksenler = mp.gca()

�entikler, de�erleri = mp.xticks()
print ("Yatay �entikler ve de�erleri:\n", �entikler, "\n", de�erleri, sep="")

�entikler, de�erleri = mp.yticks()
print ("\nDikey �entikler ve de�erleri:\n", �entikler, "\n", de�erleri[:], sep="")

mp.xlabel ("X=[0.0, 1.0]")
mp.ylabel ("Y=[0.0, 1.0]")
mp.plot()
mp.show()
print ("-"*50)
#------------------------------------------------------------------------------------------------------

mp.yticks (np.arange (0, 3001, 1000) )
�entikler, de�erleri = mp.yticks()
print ("\nDikey �entikler ve de�erleri:\n", �entikler, "\n", de�erleri, sep="")

mp.xticks (np.arange (4), ('Berlin', 'Hamburg', 'Paris', 'Londra') )
�entikler, de�erleri = mp.xticks()
print ("\nYatay �entikler ve de�erleri:\n", �entikler, "\n", de�erleri [:], sep="")

mp.xlabel ("�ehirler")
mp.ylabel ("�stanbul'a Mesafeler (km)")
mp.plot()
mp.show()



"""��kt�:
>python p_31302.py
Yatay �entikler ve de�erleri:
[0.  0.2 0.4 0.6 0.8 1. ]
<a list of 6 Text xticklabel objects>

Dikey �entikler ve de�erleri:
[0.  0.2 0.4 0.6 0.8 1. ]
[Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, '')]
--------------------------------------------------

Dikey �entikler ve de�erleri:
[   0 1000 2000 3000]
<a list of 4 Text yticklabel objects>

Yatay �entikler ve de�erleri:
[0 1 2 3]
[Text(0, 0, 'Berlin'), Text(0, 0, 'Hamburg'), Text(0, 0, 'Paris'), Text(0, 0, 'Londra')]
"""