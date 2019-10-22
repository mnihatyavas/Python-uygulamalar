# coding:iso-8859-9 Türkçe
# Python 3 - Regular Expressions

import re

telefon = "+90-551-555-94-64 # Bu benim numaramdır..."
print ("Orijinal telefon numaram:", telefon)

# Önce yorumu silelim...
sonuç = re.sub (r'#.*$', "", telefon) # sub-->substitute: ile değiştir...
print ("Yorumsuz telefon numaram:", sonuç)

# -/+'ler yerine boşluk bırakalım...
sonuç = re.sub (r'\D', " ", telefon)    
print ("-/+'lardan arınık telefon numaram:", sonuç)
