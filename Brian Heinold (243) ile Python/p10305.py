# coding:iso-8859-9 Türkçe

from math import sin, asin, pi

print ('p:', pi, end="\n")
print()
for i in range (0, 91, 15): print ("sin(", i*pi/180, ") = ", sin (i*pi/180), sep="")
print()
for i in range (0, 91, 15): print ("asin(", i/90, ") = ", asin (i/90), sep="")

# Modülsüz hazır-iç matematik fonksiyonlar...
print ("\nabs(-4.3):", abs (-4.3))
print()
for i in range (4, -5, -1): print ("round(345.228,", i, "): ", round (345.228, i), sep="")
