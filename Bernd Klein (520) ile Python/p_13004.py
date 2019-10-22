# coding:iso-8859-9 T�rk�e
# p_13004.py: re.search ile hi�/tek/�ok rakam veya karakterle ba�layan/sonra-gelen arama �rne�i.

import re

print (re.search (r"[0-9]*", "Enaz 0 rakamla ba�layan, bo� da olabilen dizge.") )
print (re.search (r"[0-9]*", "5 gibi enaz 0 rakamla ba�layan, bo� da olabilen dizge.") )
print (re.search (r".*", "") ) # Enaz 0 karakterli, bo� da olabilen dizge...
print (re.search (r"^[0-9][0-9]* ", "543 gibi enaz 1 rakamla ba�layan, sonra bir bo�lu�u olan dizge.") )
print (re.search (r"^[0-9]+ ", "543 gibi enaz 1 rakamla ba�layan, sonra bir bo�lu�u olan dizge.") ) # Bir�ncekinin ayn�s�...
print (re.search (r"^[0-9][0-9][0-9][0-9] [A-Za-z]+", "5432 gibi enaz 4 rakamla ve bo�lukla ba�layan, sonra enaz 1 k���k/b�y�k harfli kelimesi olan dizge.") )
print (re.search (r"^[0-9]{4} [A-Za-z]+", "5432 gibi enaz 4 rakamla ve bo�lukla ba�layan, sonra enaz 1 k���k/b�y�k harfli kelimesi olan dizge.") ) # Bir�ncenin ayn�s�...
print (re.search (r"^[0-9]{4,5} [A-Z][a-z]{2,}", "54321 Mnyava� gibi enaz 4 veya 5 rakamla ve bo�lukla ba�layan, sonra 1 b�y�k ve 2 veya daha fazla k���k harfli kelimesi olan dizge.") ) # re utf-8 harici � gibi karakterleri g�rm�yor...
print (re.search (r"^[0-9]{4,5} [A-Z][a-z]{2,}", "54321 M������ gibi enaz 4 veya 5 rakamla ve bo�lukla ba�layan, sonra 1 b�y�k ve 2 veya daha fazla k���k harfli kelimesi olan dizge.") )

"""��kt�:
>python p_13004.py
<re.Match object; span=(0, 0), match=''>
<re.Match object; span=(0, 1), match='5'>
<re.Match object; span=(0, 0), match=''>
<re.Match object; span=(0, 4), match='543 '>
<re.Match object; span=(0, 4), match='543 '>
<re.Match object; span=(0, 9), match='5432 gibi'>
<re.Match object; span=(0, 9), match='5432 gibi'>
<re.Match object; span=(0, 12), match='54321 Mnyava'>
None
"""