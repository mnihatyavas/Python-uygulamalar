# coding:iso-8859-9 Türkçe
# p_13004.py: re.search ile hiç/tek/çok rakam veya karakterle başlayan/sonra-gelen arama örneği.

import re

print (re.search (r"[0-9]*", "Enaz 0 rakamla başlayan, boş da olabilen dizge.") )
print (re.search (r"[0-9]*", "5 gibi enaz 0 rakamla başlayan, boş da olabilen dizge.") )
print (re.search (r".*", "") ) # Enaz 0 karakterli, boş da olabilen dizge...
print (re.search (r"^[0-9][0-9]* ", "543 gibi enaz 1 rakamla başlayan, sonra bir boşluğu olan dizge.") )
print (re.search (r"^[0-9]+ ", "543 gibi enaz 1 rakamla başlayan, sonra bir boşluğu olan dizge.") ) # Biröncekinin aynısı...
print (re.search (r"^[0-9][0-9][0-9][0-9] [A-Za-z]+", "5432 gibi enaz 4 rakamla ve boşlukla başlayan, sonra enaz 1 küçük/büyük harfli kelimesi olan dizge.") )
print (re.search (r"^[0-9]{4} [A-Za-z]+", "5432 gibi enaz 4 rakamla ve boşlukla başlayan, sonra enaz 1 küçük/büyük harfli kelimesi olan dizge.") ) # Biröncenin aynısı...
print (re.search (r"^[0-9]{4,5} [A-Z][a-z]{2,}", "54321 Mnyavaş gibi enaz 4 veya 5 rakamla ve boşlukla başlayan, sonra 1 büyük ve 2 veya daha fazla küçük harfli kelimesi olan dizge.") ) # re utf-8 harici ş gibi karakterleri görmüyor...
print (re.search (r"^[0-9]{4,5} [A-Z][a-z]{2,}", "54321 Mıçğüöş gibi enaz 4 veya 5 rakamla ve boşlukla başlayan, sonra 1 büyük ve 2 veya daha fazla küçük harfli kelimesi olan dizge.") )

"""Çıktı:
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