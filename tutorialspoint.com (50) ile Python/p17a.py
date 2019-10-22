# coding:iso-8859-9 Türkçe
# Python 3 - Regular Expressions

import re

dizge = "Kediler köpeklerden daha zekidirler"

sonuç1 = re.match ( r"(.*) (.*?) .*", dizge, re.M|re.I ) # Multiline ve Ignorecase...

if sonuç1:
    print ("sonuç1.groups() : ", sonuç1.groups())
    print ("sonuç1.group(1) : ", sonuç1.group (1))
    print ("sonuç1.group(2) : ", sonuç1.group (2))
else:
    print ("Eşleşme yok!!")

print()
sonuç2 = re.search ( r"(.*) (.*?) .*", dizge, re.M|re.I ) # Multiline ve Ignorecase...

if sonuç2:
    print ("sonuç2.groups() : ", sonuç2.groups())
    print ("sonuç2.group(1) : ", sonuç2.group (1))
    print ("sonuç2.group(2) : ", sonuç2.group (2))
else:
    print ("Eşleşme yok!!")
