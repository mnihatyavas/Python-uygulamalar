# coding:iso-8859-9 Türkçe

print ("Fatura: {} TL, Bahşiş: {} TL, ve Toplamı: {} TL'dır." .format (23.60, 23.60 * 0.25, 23.60 + 23.6*.25) )
print ("Fatura: {:.2f} TL, Bahşiş: {:.2f} TL, ve Toplamı: {:.2f} TL'dır." .format (23.60, 23.60 * 0.25, 23.60 + 23.6*.25) )

L = [0, 19, 765, 7690, 17851, 432578, 4765345]
print ("\nVarsayılı sağa yanaşık tamsayılar:")
for k in L: print ("{:7d}" .format (k) ) # Veya {:>7d}

print ("\nOrtalanmış tamsayılar:")
for k in L: print ("{:^7d}" .format (k) )

print ("\nSola yanaşık tamsayılar:")
for k in L: print ("{:<7d}" .format (k) )

print ("\nSağa yanaşık binleri ayrık tamsayılar:")
for k in L: print ("{:>9,d}" .format (k) )


from random import random
for i in range (len (L)): L[i] = L[i] + random()
L = L + [3.141592653589793]
print ("Ondalıklı sayılar listesi:", L)

print ("\nVarsayılı sola yanaşık, varsayılı 6 ondalık haneli kayan noktalı sayılar:")
for k in L: print ("{:f}" . format (k) )

print ("\nSağa yanaşık 2 ondalık haneli sayılar:")
for k in L: print ("{:10.2f}" . format (k) )

print ("\nSağa yanaşık binleri ayrık ve 2 ondalık haneli sayılar:")
for k in L: print ("{:12,.2f}" . format (k) )

L = ["Hey", "Oradaki", "Sana", "Sesleniyorum", "Merhabalar"]
print ("\nVarsayılı sola yanaşık dizgeler:")
for k in L: print ("{:s}" .format (k) )

print ("\nSağa yanaşık dizgeler:")
for k in L: print ("{:>12s}" .format (k) )

print ("\nOrtalanmış dizgeler:")
for k in L: print ("{:^12s}" .format (k) )