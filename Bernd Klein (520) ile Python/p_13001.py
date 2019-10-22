# coding:iso-8859-9 Türkçe
# p_13001.py: in ve re.search ile bir dizgede ibare aranması örneği.

dizge = "Regular expressions regexp/regex/re düzenli ibareler kolayca izah edilebilir."
print (dizge)
print ("Dizgemizde 'kolayca' ibaresi var mı?", "kolayca" in dizge)
print ("-"*75, "\n")
#-------------------------------------------------------------------------------------------------------

import re

x = re.search ("kedi", "Bir kediyle bir fare asla arkadaş olamazlar.")
print ("'kedi' uyumu var mı?", x)

x = re.search ("inek", "Bir kediyle bir fare asla arkadaş olamazlar.")
print ("'inek' uyumu var mı?", x)
print ("-"*75, "\n")
#-------------------------------------------------------------------------------------------------------

if re.search ("kedi", "Bir kediyle bir fare asla arkadaş olamazlar."):
    print ("Bir 'kedi' çeşidi bulundu :-)" )
else: print ("Hiç bir kedi bulunamadı :-)" )

if re.search ("inek", "Bir kediyle bir fare asla arkadaş olamazlar."):
    print ("Kediler ve fareler, ayrıca bir de inek.")
else: print ("Etrafta hiç ineğe rastlanmadı.")



"""Çıktı:
>python p_13001.py

Regular expressions regexp/regex/re düzenli ibareler kolayca izah edilebilir.

Dizgemizde 'kolayca' ibaresi var mı? True
---------------------------------------------------------------------------

'kedi' uyumu var mı? <re.Match object; span=(4, 8), match='kedi'>
'inek' uyumu var mı? None
---------------------------------------------------------------------------

Bir 'kedi' çeşidi bulundu :-)
Etrafta hiç ineğe rastlanmadı.
"""