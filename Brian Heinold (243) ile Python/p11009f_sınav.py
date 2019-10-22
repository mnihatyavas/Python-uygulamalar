# coding:iso-8859-9 Türkçe

from random import randint
L = []
for i in range (1000):
    gün = randint (1, 365)
    if gün <= 31: L = L + [0 + gün / 100] # Ocak-31
    elif gün <= 59: L = L + [1 + (gün-31) / 100] # Şubat-28
    elif gün <= 90: L = L + [2 + (gün-59) / 100] # Mart-31
    elif gün <= 120: L = L + [3 + (gün-90) / 100] # Nisan-30
    elif gün <= 151: L = L + [4 + (gün-120) / 100] # Mayıs-31
    elif gün <= 181: L = L + [5 + (gün-151) / 100] # Haziran-30
    elif gün <= 212: L = L + [6 + (gün-181) / 100] # Temmuz-31
    elif gün <= 243: L = L + [7 + (gün-212) / 100] # Ağustos-31
    elif gün <= 273: L = L + [8 + (gün-243) / 100] # Eylül-30
    elif gün <= 304: L = L + [9 + (gün-273) / 100] # Ekim-31
    elif gün <= 334: L = L + [10 + (gün-304) / 100] # Kasım-30
    else: L = L + [11 + (gün-334) / 100] # Aralık-31
L.sort()
print ("Aylık doğumgünü frekans tablosu==>")
ay = int (L[0])
gün = (L[0] - int (L[0])) * 100
aySayaç = günSayaç = 0
for i in range (len (L)):
    if ay != int (L[i]):
        print ("=" * 18)
        print ("   Ay toplamı:", aySayaç)
        aySayaç = 0
        ay = int (L[i])
    if gün != (L[i] - int (L[i])) * 100:
        print ("-" * 18)
        print ("   Gün toplamı:", günSayaç)
        gün = (L[i] - int (L[i])) * 100
        günSayaç = 0
    print ("Ay: {:2.0f}, Gün: {:2.0f}" .format (int (L[i])+1, (L[i] - int (L[i])) * 100))
    günSayaç += 1
    aySayaç += 1
print ("-" * 18)
print ("   Gün toplamı:", günSayaç)
print ("=" * 18)
print ("   Ay toplamı:", aySayaç)

ay=gün=-1
while not (0 < ay < 13): ay = abs (eval (input ("\nAy girin [1->12]: ")))
while not (0 < gün < 32): gün = abs (eval (input ("Gün girin [1->32]: ")))
sayaç = len ([L[i] for i in range (len (L)) if L[i] == ((ay-1)+(gün/100))])
print (ay, ".ay ve ", gün, ".güne ait doğumgünü toplamı: ", sayaç, sep="")