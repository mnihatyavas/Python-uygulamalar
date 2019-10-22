# coding:iso-8859-9 Türkçe
# p_31202.py: mathplotlib.pyplot etiket adları, eksen limitleri ve çift grafik çizimi örneği.

import matplotlib.pyplot as mp

günlerX = list (range (1, 31+1, 3) )
derecelerY = [25.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1, 31.76, 34, 35.8]

mp.plot (günlerX, derecelerY)
mp.xlabel ('Temmuz Günleri')
mp.ylabel ('Selsiyüs Dereceleri')
mp.show()
#---------------------------------------------------------------------------------------------

gününEnsıcaklarıY = [25.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1, 31.76, 34, 35.8]
gününEnsoğuklarıY = [21.2, 20.7, 21.37, 25.13, 22.3, 26.15, 28.38, 27.61, 27.36, 31, 32.38]

mp.plot (
    günlerX, gününEnsoğuklarıY,
    günlerX, gününEnsoğuklarıY, "oy",
    günlerX, gününEnsıcaklarıY,
    günlerX, gününEnsıcaklarıY, "or")
mp.xlabel ('Temmuz Günleri')
mp.ylabel ('Selsiyüs Dereceleri')
mp.show()
#---------------------------------------------------------------------------------------------

mp.plot (
    günlerX, gününEnsoğuklarıY,
    günlerX, gününEnsoğuklarıY, "oy",
    günlerX, gününEnsıcaklarıY,
    günlerX, gününEnsıcaklarıY, "or")
mp.xlabel ('Temmuz Günleri')
mp.ylabel ('Selsiyüs Dereceleri')
print ("Temmuz ayı günleri:\n", günlerX,
    "\n\nSelsiyüs asgari sıcaklık dereceleri:\n", gününEnsoğuklarıY,
    "\nSelsiyüs azami sıcaklık dereceleri:\n", gününEnsıcaklarıY, sep="")

print ("X-Y eksenlerinin aktüel limitleri:", mp.axis() )
asgariX, azamiX, asgariY, azamiY = 0, 32, 20, 37
mp.axis ([asgariX, azamiX, asgariY, azamiY])
print ("X-Y eksenlerinin yeni limitleri:", mp.axis() )
mp.show()
#---------------------------------------------------------------------------------------------

mp.plot (
    günlerX, gününEnsoğuklarıY, "--",
    günlerX, gününEnsoğuklarıY, "db",
    günlerX, gününEnsıcaklarıY, "--",
    günlerX, gününEnsıcaklarıY, "dm")
mp.xlabel ('Temmuz Günleri')
mp.ylabel ('Selsiyüs Dereceleri')

print ("\nX-Y eksenlerinin aktüel limitleri:", mp.axis() )
asgariX, azamiX, asgariY, azamiY = -1, 35, 0, 50
mp.axis ([asgariX, azamiX, asgariY, azamiY])
print ("X-Y eksenlerinin yeni limitleri:", mp.axis() )
mp.show()



"""Çıktı:
>python p_31202.py
Temmuz ayı günleri:
[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31]

Selsiyüs asgari sıcaklık dereceleri:
[21.2, 20.7, 21.37, 25.13, 22.3, 26.15, 28.38, 27.61, 27.36, 31, 32.38]
Selsiyüs azami sıcaklık dereceleri:
[25.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1, 31.76, 34, 35.8]
X-Y eksenlerinin aktüel limitleri: (-0.5, 32.5, 19.945, 36.555)
X-Y eksenlerinin yeni limitleri: (0.0, 32.0, 20.0, 37.0)

X-Y eksenlerinin aktüel limitleri: (-0.5, 32.5, 19.945, 36.555)
X-Y eksenlerinin yeni limitleri: (-1.0, 35.0, 0.0, 50.0)
"""