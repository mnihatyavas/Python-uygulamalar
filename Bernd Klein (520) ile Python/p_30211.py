# coding:iso-8859-9 T�rk�e
# p_30211.py: numpy.array as�l ve kopya diziler aras�nda order/s�ralama F-C-A-K �e�itleri �rne�i.

import numpy as np

x = np.array ([[42,22,12], [44,53,66]], order='F') # order=F/C/A/K
y = x.copy() # Kopyan�n order='C' (varsay�l�)...
x[0,0] = 1001

print ("x[0,0]=1001 de�i�tirilen  ve order='F' olan orijinal dizi:\n", x, sep="")
print ("\nKopyas�:\n", y, sep="")

print ("\nOrijinal dizi i�in order='C' mi?", x.flags['C_CONTIGUOUS'])
print ("Kopyas� i�in order='C' mi?", y.flags['C_CONTIGUOUS'])
print ("-"*40)
#------------------------------------------------------------------------------------------------------

x = np.array ([[42,22,12], [44,53,66]]) # order='C' (varsay�l�)...
y = x.copy()

print ("\nVarsay�l� order='C' olan orijinal dizi:\n", x, sep="")
print ("\nKopyas�:\n", y, sep="")

print ("\nOrijinal dizi i�in order='C' mi?", x.flags['C_CONTIGUOUS'])
print ("Kopyas� i�in order='C' mi?", y.flags['C_CONTIGUOUS'])
print ("-"*40)
#------------------------------------------------------------------------------------------------------

x = np.array ([[42,22,12], [44,53,66]], order="F")
y = x.copy (order='C')
x[0][0] = 1001

print ("\norder='F' olan orijinal dizi:\n", x, sep="")
print ("\norder='C' olan kopyas�:\n", y, sep="")

print ("\nOrijinal dizi i�in order='F' mi?", x.flags['F_CONTIGUOUS'])
print ("Kopyas� i�in order='C' mi?", y.flags['C_CONTIGUOUS'])



"""��kt�:
>python p_30211.py
x[0,0]=1001 de�i�tirilen ve order='F' olan orijinal dizi:
[[1001   22   12]
 [  44   53   66]]

Kopyas�:
[[42 22 12]
 [44 53 66]]

Orijinal dizi i�in order='C' mi? False
Kopyas� i�in order='C' mi? True
----------------------------------------

Varsay�l� order='C' olan orijinal dizi:
[[42 22 12]
 [44 53 66]]

Kopyas�:
[[42 22 12]
 [44 53 66]]

Orijinal dizi i�in order='C' mi? True
Kopyas� i�in order='C' mi? True
----------------------------------------

order='F' olan orijinal dizi:
[[1001   22   12]
 [  44   53   66]]

order='C' olan kopyas�:
[[42 22 12]
 [44 53 66]]

Orijinal dizi i�in order='F' mi? True
Kopyas� i�in order='C' mi? True
"""