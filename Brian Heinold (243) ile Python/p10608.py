# coding:iso-8859-9 Türkçe

cümle = input ("Herhangibir cümle girin: ")

print ("Cümlenizdeki boşlukların sayısı:", cümle.count (' '))
s1 = cümle.upper()
print ("Cümlenizin büyük harflisi:", s1)
s1 = cümle.replace ('a','ö')
print ("Cümlenizdeki a'lar ö olunca:", s1)
if ' ' in cümle: print ("Cümlenizdeki ilk boşluk endeksi:", cümle.index (' '))
if len(cümle) > 0 and cümle[0].isalpha(): print ('Cümleniz bir harfle başlamaktadır.')
if not cümle.isalpha(): print ('Cümlenizde harf olamayan karakter-ler var.')

print ("\nTüm String/dizge metodları listesi==>\n", dir (str))

Çıktı="""
Herhangibir cümle girin: M. Nihat Yavaş
Cümlenizdeki boşlukların sayısı: 2
Cümlenizin büyük harflisi: M. NIHAT YAVAŞ
Cümlenizdeki a'lar ö olunca: M. Nihöt Yövöş
Cümlenizdeki ilk boşluk endeksi: 2
Cümleniz bir harfle başlamaktadır.
Cümlenizde harf olamayan karakter-ler var.

Tüm String/dizge metodları listesi==>
 ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__',
'__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
'__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__',
'__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__',
'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__',
'__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs',
'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal',
'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle',
'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind',
'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip'
, 'swapcase', 'title', 'translate', 'upper', 'zfill']
"""