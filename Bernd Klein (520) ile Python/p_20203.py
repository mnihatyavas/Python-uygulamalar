# coding:iso-8859-9 T�rk�e
# p_20203.py: Dizin de�i�tirme, i�eriklerini d�kme, dizin yaratma, ad�n� de�i�tirme ve silme �rne�i.

import os
# cwd/CurrentWorkingDirectory/Akt�el�al���lanDizin
print ("cwd:", os.getcwd() )

os.chdir ("d:\Kiler")
print ("cwd:", os.getcwd() )

os.chdir ("c:\\Users\\pc\Desktop\\MyFiles\\4. Dersler\\python")
print ("\nMevcut dizin i�erikleri:", os.listdir (".") )
print ("\n'\i�lenmi� �rnekler' dizin dosyalar�:", os.listdir (".\i�lenmi� �rnekler") )

try: os.mkdir ("nihat")
except: pass
input ("\n'nihat' dizini yarat�ld� [Ent]: ")

os.rename ("nihat", "mahmut")
input ("'nihat' dizinad� 'mahmut' olarak de�i�tirildi [Ent]: ")

os.rmdir ("mahmut")
print ("'mahmut' dizini silindi...")

# import shutil
# shutil.copyfile (kaynak, hedef)

"""��kt�:
>python p_20203.py
cwd: C:\\Users\\pc\\Desktop\\MyFiles\\4. Dersler\\python
cwd: d:\\Kiler

Mevcut dizin i�erikleri: ['cmd.exe', 'ders', 'i�lenmi� �rnekler', 'metin', 'p_20201a.py',
 'p_20201b.py', 'p_20202.py', 'p_20203.py', 'resim', '__pycache__']

'\i�lenmi� �rnekler' dizin dosyalar�: ['bekle', 'p_10301.py', 'p_10401.py', 'p_10501.py',
'p_10502.py', 'p_10503.py', 'p_10601.py', 'p_10701.py', 'p_10702.py',
....
20104.py', 'p_20105.py', 'p_20106.py', 'p_20107.py',
'__BKlein Python �rnekleri Kodlamas� (adet).html']

'nihat' dizini yarat�ld� [Ent]:
'nihat' dizinad� 'mahmut' olarak de�i�tirildi [Ent]:
'mahmut' dizini silindi...
"""