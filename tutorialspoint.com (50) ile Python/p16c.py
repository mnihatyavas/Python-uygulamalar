# coding:iso-8859-9 Türkçe
# Python 3 - Object Oriented

import p16c_sınıf # p16c_sınıf.py

nesne1 = p16c_sınıf.Sınıf()
nesne2 = nesne1
nesne3 = nesne1

print (id (nesne1), id (nesne2), id (nesne3));   # Nesne id kimlik referans numaraları...

del nesne1
del nesne2
del nesne3
