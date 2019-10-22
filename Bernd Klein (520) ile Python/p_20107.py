# coding:iso-8859-9 Türkçe
# p_20107.py: sys modülünün muhtelif metod ve vasıfları dökümü örneği.

import sys

print (sys.byteorder)
print (sys.executable)
print (sys.maxsize)
#print (sys.unicode)
print(); print (sys.modules)
print(); print (sys.path)
print(); print (sys.platform)
print (sys.version)
print (sys.version_info)
print (sys.stdin)
print (sys.stdout)
print (sys.stderr)
print (sys.getrecursionlimit())



"""Çıktı:
>python p_20107.py
little
C:\\Users\\pc\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe
2147483647

{'sys': <module 'sys' (built-in)>, 'builtins': <module 'builtins' (built-in)>,
'_frozen_importlib': <module '_frozen_importlib' (frozen)>, '_imp':<module '_imp' (built-in)>,
'_thread': <module '_thread' (built-in)>, '_warnings': <module '_warnings' (built-in)>,
'_weakref': <module '_weakref' (built-in)>, 'zipimport':<module 'zipimport' (built-in)>,
 '_frozen_importlib_external': <module '_frozen_importlib_external' (frozen)>, 
'_io': <module 'io' (built-in)>, 'marshal': <module 'marshal' (built-in)>,
 'nt': <module 'nt' (built-in)>, 'winreg': <module 'winreg' (built-in)>,
 'encodings': <module 'encodings' from 'C:\\Users\\pc\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\encodings\\__init__.py'>,
 'codecs':<module 'codecs' from 'C:\\Users\\pc\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\codecs.py'>,
 '_codecs': <module '_codecs' (built-in)>,
 'encodings.aliases': <module 'encodings.aliases' from 'C:\\Users\\pc\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\encodings\\aliases.py'>,
 'encodings.utf_8': <module 'encodings.utf_8' from 'C:\\Users\\pc\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\encodings\\utf_8.py'>, 
'_signal': <module '_signal' (built-in)>, '__main__': <module '__main__' from 'p_20107.py'>,
 'encodings.latin_1': <module 'encodings.latin_1' from 'C:\\Users\\pc\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\encodings\\latin_1.py'>,
 'io': <module 'io' from 'C:\\Users\\pc\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\io.py'>,
 'abc': <module 'abc' from'C:\\Users\\pc\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\abc.py'>,
 '_abc': <module '_abc' (built-in)>, 'site': <module 'site' from 'C:\\Users\\pc\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\site.py'>,
 'os': <module 'os'from 'C:\\Users\\pc\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\os.py'>,
 'stat': <module 'stat' from 'C:\\Users\\pc\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\stat.py'>, 
'_stat': <module '_stat' (built-in)>, 'ntpath': <module 'ntpath' from 'C:\\Users\\pc\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\ntpath.py'>,
 'genericpath': <module 'genericpath' from 'C:\\Users\\pc\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\genericpath.py'>,
 'os.path': <module 'ntpath' from 'C:\\Users\\pc\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\ntpath.py'>,
 '_collections_abc': <module '_collections_abc' from 'C:\\Users\\pc\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\_collections_abc.py'>,
 '_sitebuiltins': <module '_sitebuiltins' from 'C:\\Users\\pc\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\_sitebuiltins.py'>,
 'encodings.iso8859_9': <module 'encodings.iso8859_9' from 'C:\\Users\\pc\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\encodings\\iso8859_9.py'>}

['C:\\Users\\pc\\Desktop\\MyFiles\\4. Dersler\\python', 'C:\\Users\\pc\\AppData\\Local\\Programs\\Python\\Python37-32\\python37.zip',
 'C:\\Users\\pc\\AppData\\Local\\Programs\\Python\\Python37-32\\DLLs', 'C:\\Users\\pc\\AppData\\Local\\Programs\\Python\\Python37-32\\lib',
 'C:\\Users\\pc\\AppData\\Local\\Programs\\Python\\Python37-32', 'C:\\Users\\pc\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\site-packages']

win32
3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)]
sys.version_info(major=3, minor=7, micro=0, releaselevel='final', serial=0)
<_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>
<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>
<_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>
1000
"""