# coding:iso-8859-9 T�rk�e
# p_20105.py: print ��kt�s�n� sys.stdout'la ekrana ve dosyaya y�nlendirme �rne�i.

import sys

��kt� = sys.stdout
print ("��kt�lar ekrana geliyor.")

dosya = open ("test.txt", "a")
sys.stdout = dosya
print ("Bu ��kt� sat�r� test.txt dosyas�na y�nlendirilmi�tir.")
dosya.close()

sys.stdout = ��kt�
print ("��kt�lar tekrar ekrana geliyor.")



"""��kt�:
>python p_20105.py
��kt�lar ekrana geliyor.
��kt�lar tekrar ekrana geliyor.
"""