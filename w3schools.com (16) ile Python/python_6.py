# coding: iso-8859-9 "Türkçe"
import os, sys

import pymongo

müşterim = pymongo.MongoClient ('mongodb://localhost:27017/')

veritabanı = müşterim['veritabanım']
# python -m pip install --upgrade pip

vtlistesi = müşterim.list_database_names()

if "veritabanım" in vtlistesi:
    print ("Yarattığım veritabanım mevcutmuş!")
