# coding:iso-8859-9 T�rk�e

from math import *
from decimal import Decimal
from decimal import getcontext # Decimal'in varsay�l� 28 k�s�rat hassasiyetini de�i�tirir...

print ("1/3 =", 1/3)
print ("\nDecimal(0.3) =", Decimal (0.3) )
print ('Decimal("0.3") =', Decimal ("0.3") )
print ("\nDecimal(.34)+Decimal(.17) =", Decimal (.34) + Decimal (.17) )
print ('Decimal(".34")+Decimal(".17") =', Decimal (".34") + Decimal (".17") )
print ("\n1/17 =", 1 / 17)
print ("Decimal(1)/Decimal(17) =", Decimal (1) / Decimal (17) )

print ("\nStandart 16 hassasiyet==>sqrt(2) =", sqrt (2) )
print ("Varsay�l� 28 hassasiyet==>Decimal(2).sqrt() =", Decimal (2).sqrt() )

getcontext().prec = 200
print ("De�i�tirilen 200 hassasiyet==>Decimal(2).sqrt() =", Decimal (2).sqrt() )