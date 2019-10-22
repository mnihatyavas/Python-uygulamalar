# coding:iso-8859-9 T�rk�e
# p_13001.py: in ve re.search ile bir dizgede ibare aranmas� �rne�i.

dizge = "Regular expressions regexp/regex/re d�zenli ibareler kolayca izah edilebilir."
print (dizge)
print ("Dizgemizde 'kolayca' ibaresi var m�?", "kolayca" in dizge)
print ("-"*75, "\n")
#-------------------------------------------------------------------------------------------------------

import re

x = re.search ("kedi", "Bir kediyle bir fare asla arkada� olamazlar.")
print ("'kedi' uyumu var m�?", x)

x = re.search ("inek", "Bir kediyle bir fare asla arkada� olamazlar.")
print ("'inek' uyumu var m�?", x)
print ("-"*75, "\n")
#-------------------------------------------------------------------------------------------------------

if re.search ("kedi", "Bir kediyle bir fare asla arkada� olamazlar."):
    print ("Bir 'kedi' �e�idi bulundu :-)" )
else: print ("Hi� bir kedi bulunamad� :-)" )

if re.search ("inek", "Bir kediyle bir fare asla arkada� olamazlar."):
    print ("Kediler ve fareler, ayr�ca bir de inek.")
else: print ("Etrafta hi� ine�e rastlanmad�.")



"""��kt�:
>python p_13001.py

Regular expressions regexp/regex/re d�zenli ibareler kolayca izah edilebilir.

Dizgemizde 'kolayca' ibaresi var m�? True
---------------------------------------------------------------------------

'kedi' uyumu var m�? <re.Match object; span=(4, 8), match='kedi'>
'inek' uyumu var m�? None
---------------------------------------------------------------------------

Bir 'kedi' �e�idi bulundu :-)
Etrafta hi� ine�e rastlanmad�.
"""