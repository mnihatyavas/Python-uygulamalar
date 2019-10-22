# coding:iso-8859-9 Türkçe
# p_30211.py: numpy.array asıl ve kopya diziler arasında order/sıralama F-C-A-K çeşitleri örneği.

import numpy as np

x = np.array ([[42,22,12], [44,53,66]], order='F') # order=F/C/A/K
y = x.copy() # Kopyanın order='C' (varsayılı)...
x[0,0] = 1001

print ("x[0,0]=1001 değiştirilen  ve order='F' olan orijinal dizi:\n", x, sep="")
print ("\nKopyası:\n", y, sep="")

print ("\nOrijinal dizi için order='C' mi?", x.flags['C_CONTIGUOUS'])
print ("Kopyası için order='C' mi?", y.flags['C_CONTIGUOUS'])
print ("-"*40)
#------------------------------------------------------------------------------------------------------

x = np.array ([[42,22,12], [44,53,66]]) # order='C' (varsayılı)...
y = x.copy()

print ("\nVarsayılı order='C' olan orijinal dizi:\n", x, sep="")
print ("\nKopyası:\n", y, sep="")

print ("\nOrijinal dizi için order='C' mi?", x.flags['C_CONTIGUOUS'])
print ("Kopyası için order='C' mi?", y.flags['C_CONTIGUOUS'])
print ("-"*40)
#------------------------------------------------------------------------------------------------------

x = np.array ([[42,22,12], [44,53,66]], order="F")
y = x.copy (order='C')
x[0][0] = 1001

print ("\norder='F' olan orijinal dizi:\n", x, sep="")
print ("\norder='C' olan kopyası:\n", y, sep="")

print ("\nOrijinal dizi için order='F' mi?", x.flags['F_CONTIGUOUS'])
print ("Kopyası için order='C' mi?", y.flags['C_CONTIGUOUS'])



"""Çıktı:
>python p_30211.py
x[0,0]=1001 değiştirilen ve order='F' olan orijinal dizi:
[[1001   22   12]
 [  44   53   66]]

Kopyası:
[[42 22 12]
 [44 53 66]]

Orijinal dizi için order='C' mi? False
Kopyası için order='C' mi? True
----------------------------------------

Varsayılı order='C' olan orijinal dizi:
[[42 22 12]
 [44 53 66]]

Kopyası:
[[42 22 12]
 [44 53 66]]

Orijinal dizi için order='C' mi? True
Kopyası için order='C' mi? True
----------------------------------------

order='F' olan orijinal dizi:
[[1001   22   12]
 [  44   53   66]]

order='C' olan kopyası:
[[42 22 12]
 [44 53 66]]

Orijinal dizi için order='F' mi? True
Kopyası için order='C' mi? True
"""