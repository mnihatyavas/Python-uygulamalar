# coding:iso-8859-9 T�rk�e

import re

print ("re'yi 3 kez i�let:", re.sub (r'a', '*', 'abababababa', count=3) )

print ("\nUyanlar�n listesi:", re.findall (r'[AB�]\d', 'A3 + B2 + Ba * A9 - �7 * Xy') )

dizge = "Bu re �rne�i dizge.split(" ")'den daha kullan��l�d�r, zira noktay� da ay�rteder."
print ("T�m kelimelerin listesi:", re.findall (r'\w+', dizge) )

denklem = '3x+4y-12x^2+7*5.2/3-2.5**7'
print ("\nre.split listesi:", re.split (r'\+|\-|\*|\/', denklem) )

print()
if (re.match (r'zzz', 'abc...xyzzz!..')): print ('C�mle ba��nda match ile uyan bulundu.')
else: print ('C�mle ba��nda match ile uyan bulunmad�!')

if (re.search (r'zzz', 'abc...xyzzz!..')): print ('C�mlede search ile uyan bulundu.')
else: print ('C�mlede search ile uyan bulunmad�!')

a=re.search (r'([ABC])(\d)', '= AA-BA-A3+B2+C8')
print ("\nsearch ile bulunan ilk grup bilgileri:", a.group(), a.group (1), a.group (2) )

print()
for bul in re.finditer (r'([ABC])(\d)', '= AA-BA-A3+B2+C8'):
    print ("Bulunan grup, ilk ve ikinci i�erikleri:", bul.group(), bul.group (1), bul.group (2) )

kal�p = re.compile (r'[ABC]\d')
print ("\nDerlenen kal�ba uyanlar:", kal�p.sub ('X', '= AA-BA-A3+B2+C8') )
print ("Derlenen kal�ba uyanlar:", kal�p.sub ('Y1', '= AA-BA-A3+B2+C8') )
print ("Derlenen kal�ba uyanlar:", kal�p.sub ('ZZ', '= AA-BA-A3+B2+C8') )

print ("\nDerlenen kal�ba [8->16).endekslerde uyanlar�n listesi:", kal�p.findall ('= AA-BA-A3+B2+C8+C7', 8,16) )