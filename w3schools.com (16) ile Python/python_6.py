# coding: iso-8859-9 "T�rk�e"
import os, sys

import pymongo

m��terim = pymongo.MongoClient ('mongodb://localhost:27017/')

veritaban� = m��terim['veritaban�m']
# python -m pip install --upgrade pip

vtlistesi = m��terim.list_database_names()

if "veritaban�m" in vtlistesi:
    print ("Yaratt���m veritaban�m mevcutmu�!")
