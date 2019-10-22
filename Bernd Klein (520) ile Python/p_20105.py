# coding:iso-8859-9 Türkçe
# p_20105.py: print çıktısını sys.stdout'la ekrana ve dosyaya yönlendirme örneği.

import sys

çıktı = sys.stdout
print ("Çıktılar ekrana geliyor.")

dosya = open ("test.txt", "a")
sys.stdout = dosya
print ("Bu çıktı satırı test.txt dosyasına yönlendirilmiştir.")
dosya.close()

sys.stdout = çıktı
print ("Çıktılar tekrar ekrana geliyor.")



"""Çıktı:
>python p_20105.py
Çıktılar ekrana geliyor.
Çıktılar tekrar ekrana geliyor.
"""