# coding:iso-8859-9 Türkçe
# p_20302.py: os.execv ile belirtilen yoldaki .exe programı yürütme örneği.

import os

"""
path = os.environ["PATH"] + ":/home/monty/bin2/" 
env =  {"PATH":path, "XYZ":"BlaBla"}
os.execlpe("test.sh", "test","abc", env)
#-----------------------------------------------------------------------------

env =  {"PATH":"/home/monty/bin2", "XYZ":"BlaBla"}
args = ("test","abc")
os.execvpe("test.sh", args, env)
"""

os.execv ("p_20202.py", ["C:/Users/pc/Desktop/MyFiles/4. Dersler/python/işlenmiş örnekler"] )

"""Çıktı:
>python p_20302.py
Traceback (most recent call last):
  File "p_20302.py", line 16, in <module>
    os.execv ("p_20202.py", ["C:/Users/pc/Desktop/MyFiles/4. Dersler/python/işlenmiş örnekler"] )
FileNotFoundError: [Errno 2] No such file or directory
"""