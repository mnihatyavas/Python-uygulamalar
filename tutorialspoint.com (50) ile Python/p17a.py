# coding:iso-8859-9 T�rk�e
# Python 3 - Regular Expressions

import re

dizge = "Kediler k�peklerden daha zekidirler"

sonu�1 = re.match ( r"(.*) (.*?) .*", dizge, re.M|re.I ) # Multiline ve Ignorecase...

if sonu�1:
    print ("sonu�1.groups() : ", sonu�1.groups())
    print ("sonu�1.group(1) : ", sonu�1.group (1))
    print ("sonu�1.group(2) : ", sonu�1.group (2))
else:
    print ("E�le�me yok!!")

print()
sonu�2 = re.search ( r"(.*) (.*?) .*", dizge, re.M|re.I ) # Multiline ve Ignorecase...

if sonu�2:
    print ("sonu�2.groups() : ", sonu�2.groups())
    print ("sonu�2.group(1) : ", sonu�2.group (1))
    print ("sonu�2.group(2) : ", sonu�2.group (2))
else:
    print ("E�le�me yok!!")
