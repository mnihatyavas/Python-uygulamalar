# coding:iso-8859-9 T�rk�e
# Python 3 - Regular Expressions

import re

dizge = "Kediler k�peklerden daha zekidirler"

sonu�1 = re.match ( r"zeki", dizge, re.M|re.I ) # Multiline ve Ignorecase...

if sonu�1:
    print ("sonu�1.groups() : ", sonu�1.groups())
else:
    print ("E�le�me yok!!")

print()
sonu�2 = re.search ( r"zeki", dizge, re.M|re.I ) # Multiline ve Ignorecase...

if sonu�2:
    print ("sonu�2.groups() : ", sonu�2.groups())
else:
    print ("E�le�me yok!!")
