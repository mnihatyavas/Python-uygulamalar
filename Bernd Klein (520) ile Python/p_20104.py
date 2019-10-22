# coding:iso-8859-9 Türkçe
# p_20104.py: Kontrollü try-except-else sonsuz döngülü sayısal veri girişi örneği.

import sys

while True:
    print ("\nİstisna veya break [^z] oluşuncaya dek sonsuz döngü...")
    try: sayı = int (input ("Bir sayı girin: "))
    except Exception as ist:
        print ("\nVeri giriş sonu:", ist)
        break
    else:
        if sayı == 0: print (sys.stderr, "0 sayısının tersi sonsuzdur!")
        else: print ("Girilen %d sayısının tersi: %f" % (sayı, 1.0/sayı) )



"""Çıktı:
>python p_20104.py
İstisna veya break [^Z] oluşuncaya dek sonsuz döngü...
Bir sayı girin: 12
Girilen 12 sayısının tersi: 0.083333

İstisna veya break [^Z] oluşuncaya dek sonsuz döngü...
Bir sayı girin: 0
<_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'> 0 sayısının tersi sonsuzdur!

İstisna veya break [^Z] oluşuncaya dek sonsuz döngü...
Bir sayı girin: ^Z
Veri giriş sonu:
"""