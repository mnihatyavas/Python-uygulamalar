# coding:iso-8859-9 Türkçe

import os
import zipfile

try: os.mkdir ("C:/Users/pc/Desktop/MyFiles/4. Dersler/python/mny")
except Exception: a=0

fermuar = zipfile.ZipFile ("C:/Users/pc/Desktop/MyFiles/4. Dersler/python/Dersler/pgame tutorial/00_00_minimalprog/00_00_minimalprog.zip")
fermuar.extractall ("C:/Users/pc/Desktop/MyFiles/4. Dersler/python/mny/")
