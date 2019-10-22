# coding:iso-8859-9 T�rk�e

import re

dizge = "abcdef abcxyz"
print ("replace ile:", dizge.replace ("abc", "*") )
print ("re'abc' ile:", re.sub (r"abc", "*", dizge) ) # Her abc'yi *'la de�i�tir...
print ("re'[adx]' ile:", re.sub (r"[adx]", "*", dizge) ) # Her a veya d veya x'i *'la de�i�tir...
print ("re'[abc][123]' ile:", re.sub (r'[abc][123]', '*', 'a + a1 + c2 + b5 + x2 - a3') ) # Her a veya b veya c'yi takipeden 1 veya 2 veya 3'� * ile de�i�tir...

# Kapsam: [A-Z], [0-9]=\d, [A-Za-z0-9]

print (".=herhangi B�R karakter ile:", re.sub (r'A.B', '*', 'A2B AxB AxxB A$B') ) # ? = . ve [Ent]
print ("B+ bir ve dada �ok B ile:", re.sub(r'AB+', '*', 'ABC ABBBBBBC AC') )

"""
+: 1 veya daha �ok
* 0 veya daha �ok
? 0 veya 1
{m} tam� tam�na m adet
{m,n} eanza m, en�ok n adet
"""
print ("enaz 3 ve en�ok 6 B ile:", re.sub (r'AB{3,6}', '*', 'ABB ABBB ABBBB ABBBBBBBBB') )
print ("Ta�mada enaz� ile:", re.sub (r'AB{3,6}?', '*', 'ABB ABBB ABBBB ABBBBBBBBB'))
print ("| veya ile:", re.sub (r'abc|xyz', '*', 'abcdefxyz123abc') )
print ("^ ilk 'abc' ile:", re.sub ('^abc', '*', 'abcdefgabc'))
print ("$ son 'abc' ile:", re.sub ('abc$', '*', 'abcdefgabc'))
print ("+'y� \+ ile:", re.sub (r'AB\+|AB\*|AB\?', '*', 'AB+C123AB?mny'))
print ("Her rakam * ile:", re.sub (r'\d', '*', '3 + 14 = 17') )
print ("Her rakam_olmayan * ile:", re.sub (r'\D', '*', '3 + 14 = 17') )
print ("Her harf veya rakam * ile:", re.sub (r'\w', '*', 'Bu deneme no: 1 mi acaba?!..'))
print ("Her harf veya rakam olmayan * ile:", re.sub (r'\W', '*', 'Bu deneme no: 1 mi acaba?!..'))
print ("Her bo�luk * ile:", re.sub (r'\s', '*', 'Bu deneme no: 1 mi acaba?!..'))
print ("Her bo�luk olmayan * ile:", re.sub (r'\S', '*', 'Bu deneme no: 1 mi acaba?!..'))

"""
(?=) sonras�nda �u gelirse
(?!) sonras�nda �u gelmezse
(?<=) �ncesinde �u gelirse
(?<!) �ncesinde �u gelmezse
"""
print ("bir sonras� kedi'yse:", re.sub (r'bir(?= kedi)', '*', 'bir k�pek, bir kedi ve bir fare') )
print ("bir �ncesi bo�luksa:", re.sub (r'(?<= )bir', '*', 'Ankara bir ba��ehirdir.') )
print ("[B/b]ir �ncesiz ve sonras�zsa:", re.sub (r'(?<!\w)[Bb]ir(?!\w)', '*', "Bir bira Birol'a ve bir de Birsen'e verilecek!") )
print ("B�y�k/k���k harfle farketmez:", re.sub ('(?i)ab', '*', 'ab AB') )

kal�p = r"(?x)[ABCD]\d+" # A veya B veya C veya D'yi birka� rakam takip ederse
print ("A, B, C, D'den sonra birka� rakamsa:", re.sub (kal�p, '*', 'A3C9, C1B17, ve ABC') )
print ("S�ral� kontrol:", re.sub ('aba', '*', 'abababa') )
