# coding:iso-8859-9 T�rk�e
# p_31202.py: mathplotlib.pyplot etiket adlar�, eksen limitleri ve �ift grafik �izimi �rne�i.

import matplotlib.pyplot as mp

g�nlerX = list (range (1, 31+1, 3) )
derecelerY = [25.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1, 31.76, 34, 35.8]

mp.plot (g�nlerX, derecelerY)
mp.xlabel ('Temmuz G�nleri')
mp.ylabel ('Selsiy�s Dereceleri')
mp.show()
#---------------------------------------------------------------------------------------------

g�n�nEns�caklar�Y = [25.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1, 31.76, 34, 35.8]
g�n�nEnso�uklar�Y = [21.2, 20.7, 21.37, 25.13, 22.3, 26.15, 28.38, 27.61, 27.36, 31, 32.38]

mp.plot (
    g�nlerX, g�n�nEnso�uklar�Y,
    g�nlerX, g�n�nEnso�uklar�Y, "oy",
    g�nlerX, g�n�nEns�caklar�Y,
    g�nlerX, g�n�nEns�caklar�Y, "or")
mp.xlabel ('Temmuz G�nleri')
mp.ylabel ('Selsiy�s Dereceleri')
mp.show()
#---------------------------------------------------------------------------------------------

mp.plot (
    g�nlerX, g�n�nEnso�uklar�Y,
    g�nlerX, g�n�nEnso�uklar�Y, "oy",
    g�nlerX, g�n�nEns�caklar�Y,
    g�nlerX, g�n�nEns�caklar�Y, "or")
mp.xlabel ('Temmuz G�nleri')
mp.ylabel ('Selsiy�s Dereceleri')
print ("Temmuz ay� g�nleri:\n", g�nlerX,
    "\n\nSelsiy�s asgari s�cakl�k dereceleri:\n", g�n�nEnso�uklar�Y,
    "\nSelsiy�s azami s�cakl�k dereceleri:\n", g�n�nEns�caklar�Y, sep="")

print ("X-Y eksenlerinin akt�el limitleri:", mp.axis() )
asgariX, azamiX, asgariY, azamiY = 0, 32, 20, 37
mp.axis ([asgariX, azamiX, asgariY, azamiY])
print ("X-Y eksenlerinin yeni limitleri:", mp.axis() )
mp.show()
#---------------------------------------------------------------------------------------------

mp.plot (
    g�nlerX, g�n�nEnso�uklar�Y, "--",
    g�nlerX, g�n�nEnso�uklar�Y, "db",
    g�nlerX, g�n�nEns�caklar�Y, "--",
    g�nlerX, g�n�nEns�caklar�Y, "dm")
mp.xlabel ('Temmuz G�nleri')
mp.ylabel ('Selsiy�s Dereceleri')

print ("\nX-Y eksenlerinin akt�el limitleri:", mp.axis() )
asgariX, azamiX, asgariY, azamiY = -1, 35, 0, 50
mp.axis ([asgariX, azamiX, asgariY, azamiY])
print ("X-Y eksenlerinin yeni limitleri:", mp.axis() )
mp.show()



"""��kt�:
>python p_31202.py
Temmuz ay� g�nleri:
[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31]

Selsiy�s asgari s�cakl�k dereceleri:
[21.2, 20.7, 21.37, 25.13, 22.3, 26.15, 28.38, 27.61, 27.36, 31, 32.38]
Selsiy�s azami s�cakl�k dereceleri:
[25.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1, 31.76, 34, 35.8]
X-Y eksenlerinin akt�el limitleri: (-0.5, 32.5, 19.945, 36.555)
X-Y eksenlerinin yeni limitleri: (0.0, 32.0, 20.0, 37.0)

X-Y eksenlerinin akt�el limitleri: (-0.5, 32.5, 19.945, 36.555)
X-Y eksenlerinin yeni limitleri: (-1.0, 35.0, 0.0, 50.0)
"""