# coding:iso-8859-9 Türkçe
# p_20106.py: Hataların sys.stderr'le ekrana ve dosyaya yönlendirilmesi örneği.

import sys

try: x = 10 / 0 # Hatalar ekrana yansıtılır...
except Exception as ist: print ("Hata:", ist)

ekran = sys.stderr

dosya = open ("hatalar.txt", "w")
sys.stderr = dosya
x = 10 / 0 # Hatalar hatalar.txt dosyasına yönlendirilir...
dosya.close()

sys.stderr = ekran

try: x = 10 / 0 # Hatalar tekrar ekrana yansıtılır...
except Exception as ist: print ("Hata:", ist)



"""Çıktı:
>python p_20106.py
Hata: division by zero

hatalar.txt dosyası:
Traceback (most recent call last):
  File "p_20106.py", line 12, in <module>
    x = 10 / 0 # Hatalar hatalar.txt dosyasına yönlendirilir...
ZeroDivisionError: division by zero
"""