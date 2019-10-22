# coding:iso-8859-9 Türkçe
# p_20203.py: Dizin değiştirme, içeriklerini dökme, dizin yaratma, adını değiştirme ve silme örneği.

import os
# cwd/CurrentWorkingDirectory/AktüelÇalışılanDizin
print ("cwd:", os.getcwd() )

os.chdir ("d:\Kiler")
print ("cwd:", os.getcwd() )

os.chdir ("c:\\Users\\pc\Desktop\\MyFiles\\4. Dersler\\python")
print ("\nMevcut dizin içerikleri:", os.listdir (".") )
print ("\n'\işlenmiş örnekler' dizin dosyaları:", os.listdir (".\işlenmiş örnekler") )

try: os.mkdir ("nihat")
except: pass
input ("\n'nihat' dizini yaratıldı [Ent]: ")

os.rename ("nihat", "mahmut")
input ("'nihat' dizinadı 'mahmut' olarak değiştirildi [Ent]: ")

os.rmdir ("mahmut")
print ("'mahmut' dizini silindi...")

# import shutil
# shutil.copyfile (kaynak, hedef)

"""Çıktı:
>python p_20203.py
cwd: C:\\Users\\pc\\Desktop\\MyFiles\\4. Dersler\\python
cwd: d:\\Kiler

Mevcut dizin içerikleri: ['cmd.exe', 'ders', 'işlenmiş örnekler', 'metin', 'p_20201a.py',
 'p_20201b.py', 'p_20202.py', 'p_20203.py', 'resim', '__pycache__']

'\işlenmiş örnekler' dizin dosyaları: ['bekle', 'p_10301.py', 'p_10401.py', 'p_10501.py',
'p_10502.py', 'p_10503.py', 'p_10601.py', 'p_10701.py', 'p_10702.py',
....
20104.py', 'p_20105.py', 'p_20106.py', 'p_20107.py',
'__BKlein Python Örnekleri Kodlaması (adet).html']

'nihat' dizini yaratıldı [Ent]:
'nihat' dizinadı 'mahmut' olarak değiştirildi [Ent]:
'mahmut' dizini silindi...
"""