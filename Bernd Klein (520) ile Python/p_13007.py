# coding:iso-8859-9 Türkçe
# p_13007.py: re.search'le listeden telno-soyad-göbekadlıad gruplarını arayıp dökme örneği.

import re

liste = ["555-8396 Nur, Abdullah", 
    "Feyza, C.Muhammed", 
    "555-5299 Pullu, Aslan",
    "555-7334 Sevimli, H.Caner",
    "555-6385 Resul, Abdi Faruk"]

# 3 grup; ilki sonunda boşluklu rakam ve tire, ikincisi sonu virgül ve boşluklu soyad,
# üçüncüsü de nokta ve karakterli ilk ve göbek adı.
# Bunlar araları birer boşlukla "ad-göbekad soyad telefonno" şeklinde yazdırılacak.

for i in liste:
    sonuç = re.search (r"([0-9-]*)\s*([A-Za-z]+),\s+(.*)", i)
    print (sonuç.group (3) + " " + sonuç.group (2) + " " + sonuç.group(1) )

"""Çıktı:
>python p_13007.py
Abdullah Nur 555-8396
C.Muhammed Feyza
Aslan Pullu 555-5299
H.Caner Sevimli 555-7334
Abdi Faruk Resul 555-6385
"""