# coding:iso-8859-9 T�rk�e
# Python 3 - Regular Expressions

import re

telefon = "+90-551-555-94-64 # Bu benim numaramd�r..."
print ("Orijinal telefon numaram:", telefon)

# �nce yorumu silelim...
sonu� = re.sub (r'#.*$', "", telefon) # sub-->substitute: ile de�i�tir...
print ("Yorumsuz telefon numaram:", sonu�)

# -/+'ler yerine bo�luk b�rakal�m...
sonu� = re.sub (r'\D', " ", telefon)    
print ("-/+'lardan ar�n�k telefon numaram:", sonu�)
