# coding:iso-8859-9 T�rk�e

import os
import sys

# os.chdir ("C:/Users/pc/Desktop/MyFiles/4. Dersler/python/")

while True:
    os.system ("%windir%/system32/calc.exe")
    #L = ["mny"]; os.execv ("C:\Program Files\JET XP\JET_XP.exe", L)

    cevap = input ('Programdan ��k�yor musun [e/h]? ').lower()
    if cevap == 'e': sys.exit()
