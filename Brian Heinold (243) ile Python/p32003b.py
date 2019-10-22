# coding:iso-8859-9 Türkçe

import os
import shutil

dizin2 = "C:/Users/pc/Desktop/MyFiles/4. Dersler/python/mny/"

try: os.rmdir (dizin2)
except Exception: a=0

try: os.mkdir (dizin2)
except Exception: a=0
#--------------------------------------------------------------------------------------

dizin1 = "C:/Users/pc/Desktop/MyFiles/4. Dersler/python/"
dosyalar = os.listdir (dizin1)
for d in dosyalar:
    if os.path.isfile (dizin1+d):
        shutil.copy (dizin1+d, dizin2+"Kopya_"+d)
#--------------------------------------------------------------------------------------

os.chdir (dizin2)
dosyalar = os.listdir()
print (dosyalar)
try: os.rename ("Kopya_cmd.exe", "mny.exe")
except Exception: a=0
print()
dosyalar = os.listdir()
print (dosyalar)
try: os.remove ("mny.exe")
except Exception: a=0
#--------------------------------------------------------------------------------------

print()
dosyalar = os.listdir()
for d in dosyalar: os.remove (d)
dosyalar = os.listdir()
print (dosyalar)
#--------------------------------------------------------------------------------------

os.chdir (dizin1)
os.rmdir (dizin2)