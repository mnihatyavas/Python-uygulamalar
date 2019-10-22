# coding:iso-8859-9 Türkçe

import re

dizge = "abcdef abcxyz"
print ("replace ile:", dizge.replace ("abc", "*") )
print ("re'abc' ile:", re.sub (r"abc", "*", dizge) ) # Her abc'yi *'la değiştir...
print ("re'[adx]' ile:", re.sub (r"[adx]", "*", dizge) ) # Her a veya d veya x'i *'la değiştir...
print ("re'[abc][123]' ile:", re.sub (r'[abc][123]', '*', 'a + a1 + c2 + b5 + x2 - a3') ) # Her a veya b veya c'yi takipeden 1 veya 2 veya 3'ü * ile değiştir...

# Kapsam: [A-Z], [0-9]=\d, [A-Za-z0-9]

print (".=herhangi BİR karakter ile:", re.sub (r'A.B', '*', 'A2B AxB AxxB A$B') ) # ? = . ve [Ent]
print ("B+ bir ve dada çok B ile:", re.sub(r'AB+', '*', 'ABC ABBBBBBC AC') )

"""
+: 1 veya daha çok
* 0 veya daha çok
? 0 veya 1
{m} tamı tamına m adet
{m,n} eanza m, ençok n adet
"""
print ("enaz 3 ve ençok 6 B ile:", re.sub (r'AB{3,6}', '*', 'ABB ABBB ABBBB ABBBBBBBBB') )
print ("Taşmada enazı ile:", re.sub (r'AB{3,6}?', '*', 'ABB ABBB ABBBB ABBBBBBBBB'))
print ("| veya ile:", re.sub (r'abc|xyz', '*', 'abcdefxyz123abc') )
print ("^ ilk 'abc' ile:", re.sub ('^abc', '*', 'abcdefgabc'))
print ("$ son 'abc' ile:", re.sub ('abc$', '*', 'abcdefgabc'))
print ("+'yı \+ ile:", re.sub (r'AB\+|AB\*|AB\?', '*', 'AB+C123AB?mny'))
print ("Her rakam * ile:", re.sub (r'\d', '*', '3 + 14 = 17') )
print ("Her rakam_olmayan * ile:", re.sub (r'\D', '*', '3 + 14 = 17') )
print ("Her harf veya rakam * ile:", re.sub (r'\w', '*', 'Bu deneme no: 1 mi acaba?!..'))
print ("Her harf veya rakam olmayan * ile:", re.sub (r'\W', '*', 'Bu deneme no: 1 mi acaba?!..'))
print ("Her boşluk * ile:", re.sub (r'\s', '*', 'Bu deneme no: 1 mi acaba?!..'))
print ("Her boşluk olmayan * ile:", re.sub (r'\S', '*', 'Bu deneme no: 1 mi acaba?!..'))

"""
(?=) sonrasında şu gelirse
(?!) sonrasında şu gelmezse
(?<=) öncesinde şu gelirse
(?<!) öncesinde şu gelmezse
"""
print ("bir sonrası kedi'yse:", re.sub (r'bir(?= kedi)', '*', 'bir köpek, bir kedi ve bir fare') )
print ("bir öncesi boşluksa:", re.sub (r'(?<= )bir', '*', 'Ankara bir başşehirdir.') )
print ("[B/b]ir öncesiz ve sonrasızsa:", re.sub (r'(?<!\w)[Bb]ir(?!\w)', '*', "Bir bira Birol'a ve bir de Birsen'e verilecek!") )
print ("Büyük/küçük harfle farketmez:", re.sub ('(?i)ab', '*', 'ab AB') )

kalıp = r"(?x)[ABCD]\d+" # A veya B veya C veya D'yi birkaç rakam takip ederse
print ("A, B, C, D'den sonra birkaç rakamsa:", re.sub (kalıp, '*', 'A3C9, C1B17, ve ABC') )
print ("Sıralı kontrol:", re.sub ('aba', '*', 'abababa') )
