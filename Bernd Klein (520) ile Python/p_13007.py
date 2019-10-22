# coding:iso-8859-9 T�rk�e
# p_13007.py: re.search'le listeden telno-soyad-g�bekadl�ad gruplar�n� aray�p d�kme �rne�i.

import re

liste = ["555-8396 Nur, Abdullah", 
    "Feyza, C.Muhammed", 
    "555-5299 Pullu, Aslan",
    "555-7334 Sevimli, H.Caner",
    "555-6385 Resul, Abdi Faruk"]

# 3 grup; ilki sonunda bo�luklu rakam ve tire, ikincisi sonu virg�l ve bo�luklu soyad,
# ���nc�s� de nokta ve karakterli ilk ve g�bek ad�.
# Bunlar aralar� birer bo�lukla "ad-g�bekad soyad telefonno" �eklinde yazd�r�lacak.

for i in liste:
    sonu� = re.search (r"([0-9-]*)\s*([A-Za-z]+),\s+(.*)", i)
    print (sonu�.group (3) + " " + sonu�.group (2) + " " + sonu�.group(1) )

"""��kt�:
>python p_13007.py
Abdullah Nur 555-8396
C.Muhammed Feyza
Aslan Pullu 555-5299
H.Caner Sevimli 555-7334
Abdi Faruk Resul 555-6385
"""