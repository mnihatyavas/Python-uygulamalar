# coding:iso-8859-9 T�rk�e
# p_13003.py: re.search ve re.match ile tek/�ok sat�rl� dizge ba��nda/sonunda arama �rne�i.

import re

sat�r = "O ki�i Mayer ad�nda bir Alman'd�r."
if re.search (r"M[ae][iy]er", sat�r): print ("Bir Mayer olarak okunan ad buldum!")
if re.search (r"M[ae][iy]e?r", "O ki�i Mair ad�nda bir �ngiliz'dir."): print ("Mair olarak okunan bir ad buldum!")

if re.search (r"�ub(at)? 2019", "Bu �ubat 2019 ay� 28 �ekiyor."): print ("�ubat veya �ub olarak okunan ay ad� buldum!")
print ("-"*75, "\n")
#-----------------------------------------------------------------------------------------------------

dizge1 = "Mayer �ok genel olarak kullan�lan bir add�r."
dizge2 = "Onun ad� Meyer ama kendisi bir Alman de�ildir."
print ("re.search'le 1.dizge i�inde var m�?", re.search (r"M[ae][iy]er", dizge1) )
print ("re.search'le 2.dizge i�inde var m�?", re.search (r"M[ae][iy]er", dizge2) )

print ("\nre.match'le 1.dizge ba��nda var m�?", re.match (r"M[ae][iy]er", dizge1) ) # Sadece dizge ba�� kontrolu yapar...
print ("re.match'le 2.dizge ba��nda var m�?", re.match (r"M[ae][iy]er", dizge2) )
print ("-"*75, "\n")
#-----------------------------------------------------------------------------------------------------

# ^ ile dizge ba�� kontrolu...
print ("^re.search'le tek sat�rl� 1.dizgenin dizge ba��nda var m�?", re.search (r"^M[ae][iy]er", dizge1) )
print ("^re.search'le tek sat�rl� 2.dizgenin dizge ba��nda var m�?", re.search (r"^M[ae][iy]er", dizge2) )

dizge = dizge2 + "\n" + dizge1
print ("\nM'siz ^re.search'le �ok sat�rl� dizgenin dizge ba��nda var m�?", re.search (r"^M[ae][iy]er", dizge) )

print ("M'li ^re.search'le �ok sat�rl� dizgenin herhangibir sat�r ba��nda var m�?", re.search (r"^M[ae][iy]er", dizge, re.MULTILINE) )
print ("M'li ^re.search'le �ok sat�rl� dizgenin herhangibir sat�r ba��nda var m�?", re.search (r"^M[ae][iy]er", dizge, re.M) )

print ("\nM'li ^re.match'le �ok sat�rl� dizgenin herhangibir sat�r ba��nda var m�?", re.match (r"^M[ae][iy]er", dizge, re.M) )
print ("-"*75, "\n")
#-----------------------------------------------------------------------------------------------------

# $ ile dizge sonu kontrolu...
print ("'Python.' dizge sonunda var m�?", re.search (r"Python\.$", "En sevdi�im programlama dili: Python.") )
print ("'Python.' dizge sonunda var m�?", re.search (r"Python\.$", "En sevdi�im programlama dilleri: Python ve Perl.") )
print ("'Python.' M'siz �oklu sat�rl� dizgenin herhangibir sat�r sonunda var m�?", re.search (r"Python\.$", "En sevdi�im programlama dili Python.\nBaz�lar�n�n tercihleri ise Java veya Perl.") )
print ("'Python.' M'li �oklu sat�rl� dizgenin herhangibir sat�r sonunda var m�?", re.search (r"Python\.$", "En sevdi�im programlama dili Python.\nBaz�lar�n�n tercihleri ise Java veya Perl.", re.M) )



"""��kt�:
>python p_13003.py
Bir Mayer olarak okunan ad buldum!
Mair olarak okunan bir ad buldum!
�ubat veya �ub olarak okunan ay ad� buldum!
---------------------------------------------------------------------------

re.search'le 1.dizge i�inde var m�? <re.Match object; span=(0, 5), match='Mayer'>
re.search'le 2.dizge i�inde var m�? <re.Match object; span=(9, 14), match='Meyer'>

re.match'le 1.dizge ba��nda var m�? <re.Match object; span=(0, 5), match='Mayer'>
re.match'le 2.dizge ba��nda var m�? None
---------------------------------------------------------------------------

^re.search'le tek sat�rl� 1.dizgenin dizge ba��nda var m�? <re.Match object; span=(0, 5), match='Mayer'>
^re.search'le tek sat�rl� 2.dizgenin dizge ba��nda var m�? None

M'siz ^re.search'le �ok sat�rl� dizgenin dizge ba��nda var m�? None
M'li ^re.search'le �ok sat�rl� dizgenin herhangibir sat�r ba��nda var m�? <re.Match object; span=(47, 52), match='Mayer'>
M'li ^re.search'le �ok sat�rl� dizgenin herhangibir sat�r ba��nda var m�? <re.Match object; span=(47, 52), match='Mayer'>

M'li ^re.match'le �ok sat�rl� dizgenin herhangibir sat�r ba��nda var m�? None
---------------------------------------------------------------------------

'Python.' dizge sonunda var m�? <re.Match object; span=(30, 37), match='Python.'>
'Python.' dizge sonunda var m�? None
'Python.' M'siz �oklu sat�rl� dizgenin herhangibir sat�r sonunda var m�? None
'Python.' M'li �oklu sat�rl� dizgenin herhangibir sat�r sonunda var m�? <re.Match object; span=(29, 36), match='Python.'>
"""