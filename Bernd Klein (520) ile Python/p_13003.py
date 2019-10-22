# coding:iso-8859-9 Türkçe
# p_13003.py: re.search ve re.match ile tek/çok satırlı dizge başında/sonunda arama örneği.

import re

satır = "O kişi Mayer adında bir Alman'dır."
if re.search (r"M[ae][iy]er", satır): print ("Bir Mayer olarak okunan ad buldum!")
if re.search (r"M[ae][iy]e?r", "O kişi Mair adında bir İngiliz'dir."): print ("Mair olarak okunan bir ad buldum!")

if re.search (r"Şub(at)? 2019", "Bu Şubat 2019 ayı 28 çekiyor."): print ("Şubat veya Şub olarak okunan ay adı buldum!")
print ("-"*75, "\n")
#-----------------------------------------------------------------------------------------------------

dizge1 = "Mayer çok genel olarak kullanılan bir addır."
dizge2 = "Onun adı Meyer ama kendisi bir Alman değildir."
print ("re.search'le 1.dizge içinde var mı?", re.search (r"M[ae][iy]er", dizge1) )
print ("re.search'le 2.dizge içinde var mı?", re.search (r"M[ae][iy]er", dizge2) )

print ("\nre.match'le 1.dizge başında var mı?", re.match (r"M[ae][iy]er", dizge1) ) # Sadece dizge başı kontrolu yapar...
print ("re.match'le 2.dizge başında var mı?", re.match (r"M[ae][iy]er", dizge2) )
print ("-"*75, "\n")
#-----------------------------------------------------------------------------------------------------

# ^ ile dizge başı kontrolu...
print ("^re.search'le tek satırlı 1.dizgenin dizge başında var mı?", re.search (r"^M[ae][iy]er", dizge1) )
print ("^re.search'le tek satırlı 2.dizgenin dizge başında var mı?", re.search (r"^M[ae][iy]er", dizge2) )

dizge = dizge2 + "\n" + dizge1
print ("\nM'siz ^re.search'le çok satırlı dizgenin dizge başında var mı?", re.search (r"^M[ae][iy]er", dizge) )

print ("M'li ^re.search'le çok satırlı dizgenin herhangibir satır başında var mı?", re.search (r"^M[ae][iy]er", dizge, re.MULTILINE) )
print ("M'li ^re.search'le çok satırlı dizgenin herhangibir satır başında var mı?", re.search (r"^M[ae][iy]er", dizge, re.M) )

print ("\nM'li ^re.match'le çok satırlı dizgenin herhangibir satır başında var mı?", re.match (r"^M[ae][iy]er", dizge, re.M) )
print ("-"*75, "\n")
#-----------------------------------------------------------------------------------------------------

# $ ile dizge sonu kontrolu...
print ("'Python.' dizge sonunda var mı?", re.search (r"Python\.$", "En sevdiğim programlama dili: Python.") )
print ("'Python.' dizge sonunda var mı?", re.search (r"Python\.$", "En sevdiğim programlama dilleri: Python ve Perl.") )
print ("'Python.' M'siz çoklu satırlı dizgenin herhangibir satır sonunda var mı?", re.search (r"Python\.$", "En sevdiğim programlama dili Python.\nBazılarının tercihleri ise Java veya Perl.") )
print ("'Python.' M'li çoklu satırlı dizgenin herhangibir satır sonunda var mı?", re.search (r"Python\.$", "En sevdiğim programlama dili Python.\nBazılarının tercihleri ise Java veya Perl.", re.M) )



"""Çıktı:
>python p_13003.py
Bir Mayer olarak okunan ad buldum!
Mair olarak okunan bir ad buldum!
Şubat veya Şub olarak okunan ay adı buldum!
---------------------------------------------------------------------------

re.search'le 1.dizge içinde var mı? <re.Match object; span=(0, 5), match='Mayer'>
re.search'le 2.dizge içinde var mı? <re.Match object; span=(9, 14), match='Meyer'>

re.match'le 1.dizge başında var mı? <re.Match object; span=(0, 5), match='Mayer'>
re.match'le 2.dizge başında var mı? None
---------------------------------------------------------------------------

^re.search'le tek satırlı 1.dizgenin dizge başında var mı? <re.Match object; span=(0, 5), match='Mayer'>
^re.search'le tek satırlı 2.dizgenin dizge başında var mı? None

M'siz ^re.search'le çok satırlı dizgenin dizge başında var mı? None
M'li ^re.search'le çok satırlı dizgenin herhangibir satır başında var mı? <re.Match object; span=(47, 52), match='Mayer'>
M'li ^re.search'le çok satırlı dizgenin herhangibir satır başında var mı? <re.Match object; span=(47, 52), match='Mayer'>

M'li ^re.match'le çok satırlı dizgenin herhangibir satır başında var mı? None
---------------------------------------------------------------------------

'Python.' dizge sonunda var mı? <re.Match object; span=(30, 37), match='Python.'>
'Python.' dizge sonunda var mı? None
'Python.' M'siz çoklu satırlı dizgenin herhangibir satır sonunda var mı? None
'Python.' M'li çoklu satırlı dizgenin herhangibir satır sonunda var mı? <re.Match object; span=(29, 36), match='Python.'>
"""