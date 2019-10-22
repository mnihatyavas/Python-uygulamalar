# coding:iso-8859-9 Türkçe

import re

print ("re'yi 3 kez işlet:", re.sub (r'a', '*', 'abababababa', count=3) )

print ("\nUyanların listesi:", re.findall (r'[ABÜ]\d', 'A3 + B2 + Ba * A9 - Ü7 * Xy') )

dizge = "Bu re örneği dizge.split(" ")'den daha kullanışlıdır, zira noktayı da ayırteder."
print ("Tüm kelimelerin listesi:", re.findall (r'\w+', dizge) )

denklem = '3x+4y-12x^2+7*5.2/3-2.5**7'
print ("\nre.split listesi:", re.split (r'\+|\-|\*|\/', denklem) )

print()
if (re.match (r'zzz', 'abc...xyzzz!..')): print ('Cümle başında match ile uyan bulundu.')
else: print ('Cümle başında match ile uyan bulunmadı!')

if (re.search (r'zzz', 'abc...xyzzz!..')): print ('Cümlede search ile uyan bulundu.')
else: print ('Cümlede search ile uyan bulunmadı!')

a=re.search (r'([ABC])(\d)', '= AA-BA-A3+B2+C8')
print ("\nsearch ile bulunan ilk grup bilgileri:", a.group(), a.group (1), a.group (2) )

print()
for bul in re.finditer (r'([ABC])(\d)', '= AA-BA-A3+B2+C8'):
    print ("Bulunan grup, ilk ve ikinci içerikleri:", bul.group(), bul.group (1), bul.group (2) )

kalıp = re.compile (r'[ABC]\d')
print ("\nDerlenen kalıba uyanlar:", kalıp.sub ('X', '= AA-BA-A3+B2+C8') )
print ("Derlenen kalıba uyanlar:", kalıp.sub ('Y1', '= AA-BA-A3+B2+C8') )
print ("Derlenen kalıba uyanlar:", kalıp.sub ('ZZ', '= AA-BA-A3+B2+C8') )

print ("\nDerlenen kalıba [8->16).endekslerde uyanların listesi:", kalıp.findall ('= AA-BA-A3+B2+C8+C7', 8,16) )