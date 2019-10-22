# coding:iso-8859-9 T�rk�e
# p_20104.py: Kontroll� try-except-else sonsuz d�ng�l� say�sal veri giri�i �rne�i.

import sys

while True:
    print ("\n�stisna veya break [^z] olu�uncaya dek sonsuz d�ng�...")
    try: say� = int (input ("Bir say� girin: "))
    except Exception as ist:
        print ("\nVeri giri� sonu:", ist)
        break
    else:
        if say� == 0: print (sys.stderr, "0 say�s�n�n tersi sonsuzdur!")
        else: print ("Girilen %d say�s�n�n tersi: %f" % (say�, 1.0/say�) )



"""��kt�:
>python p_20104.py
�stisna veya break [^Z] olu�uncaya dek sonsuz d�ng�...
Bir say� girin: 12
Girilen 12 say�s�n�n tersi: 0.083333

�stisna veya break [^Z] olu�uncaya dek sonsuz d�ng�...
Bir say� girin: 0
<_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'> 0 say�s�n�n tersi sonsuzdur!

�stisna veya break [^Z] olu�uncaya dek sonsuz d�ng�...
Bir say� girin: ^Z
Veri giri� sonu:
"""