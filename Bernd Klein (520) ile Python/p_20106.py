# coding:iso-8859-9 T�rk�e
# p_20106.py: Hatalar�n sys.stderr'le ekrana ve dosyaya y�nlendirilmesi �rne�i.

import sys

try: x = 10 / 0 # Hatalar ekrana yans�t�l�r...
except Exception as ist: print ("Hata:", ist)

ekran = sys.stderr

dosya = open ("hatalar.txt", "w")
sys.stderr = dosya
x = 10 / 0 # Hatalar hatalar.txt dosyas�na y�nlendirilir...
dosya.close()

sys.stderr = ekran

try: x = 10 / 0 # Hatalar tekrar ekrana yans�t�l�r...
except Exception as ist: print ("Hata:", ist)



"""��kt�:
>python p_20106.py
Hata: division by zero

hatalar.txt dosyas�:
Traceback (most recent call last):
  File "p_20106.py", line 12, in <module>
    x = 10 / 0 # Hatalar hatalar.txt dosyas�na y�nlendirilir...
ZeroDivisionError: division by zero
"""