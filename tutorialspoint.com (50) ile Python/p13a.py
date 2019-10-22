# coding:iso-8859-9 Türkçe
# Python 3 - Modules

import p13a_modül1 # p13_modül1.py

# Modülümüzdeki selam fonksiyonunu çağıralım...
p13a_modül1.selam ("M.Nihat Yavaş")

# Başka bir modülden tanımlı bir fonksiyonu çağıralım...
from p13a_modül2 import fib # p13a_modül2.py

print (fib (100))
