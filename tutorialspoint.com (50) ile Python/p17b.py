# coding:iso-8859-9 Türkçe
# Python 3 - Regular Expressions

import re

dizge = "Kediler köpeklerden daha zekidirler"

sonuç1 = re.match ( r"zeki", dizge, re.M|re.I ) # Multiline ve Ignorecase...

if sonuç1:
    print ("sonuç1.groups() : ", sonuç1.groups())
else:
    print ("Eşleşme yok!!")

print()
sonuç2 = re.search ( r"zeki", dizge, re.M|re.I ) # Multiline ve Ignorecase...

if sonuç2:
    print ("sonuç2.groups() : ", sonuç2.groups())
else:
    print ("Eşleşme yok!!")
