# coding:iso-8859-9 T�rk�e

c�mle = input ("Herhangibir c�mle girin: ")

print ("C�mlenizdeki bo�luklar�n say�s�:", c�mle.count (' '))
s1 = c�mle.upper()
print ("C�mlenizin b�y�k harflisi:", s1)
s1 = c�mle.replace ('a','�')
print ("C�mlenizdeki a'lar � olunca:", s1)
if ' ' in c�mle: print ("C�mlenizdeki ilk bo�luk endeksi:", c�mle.index (' '))
if len(c�mle) > 0 and c�mle[0].isalpha(): print ('C�mleniz bir harfle ba�lamaktad�r.')
if not c�mle.isalpha(): print ('C�mlenizde harf olamayan karakter-ler var.')

print ("\nT�m String/dizge metodlar� listesi==>\n", dir (str))

��kt�="""
Herhangibir c�mle girin: M. Nihat Yava�
C�mlenizdeki bo�luklar�n say�s�: 2
C�mlenizin b�y�k harflisi: M. NIHAT YAVA�
C�mlenizdeki a'lar � olunca: M. Nih�t Y�v��
C�mlenizdeki ilk bo�luk endeksi: 2
C�mleniz bir harfle ba�lamaktad�r.
C�mlenizde harf olamayan karakter-ler var.

T�m String/dizge metodlar� listesi==>
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