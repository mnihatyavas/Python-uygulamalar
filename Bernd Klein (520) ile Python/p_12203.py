# coding:iso-8859-9 T�rk�e
# p_12203.py: Komut sat�r�ndan girilen arg�manlar�n y�netilmesi �rne�i.

import sys                

uz = len (sys.argv)
if uz < 2:
    print ("Bu program i�in ileti komutundan enaz 1 arg�man de�eri girmelisiniz!..")
    sys.exit (-1)

for i in range (1, uz):
    print ("Arg�man no:", i, "==>Arg�man de�eri:", sys.argv[i] )

"""��kt�:
>python p_12203.py
Bu program i�in ileti komutundan enaz 1 arg�man de�eri girmelisiniz!..

>python p_12203.py Nihat  ** TEKRAR ??
Arg�man no: 1 ==>Arg�man de�eri: Nihat

>python p_12203.py M.Nihat Yava� 17 Nisan 1957 Ye�ilyurt-Malatya  ** TEKRAR **
Arg�man no: 1 ==>Arg�man de�eri: M.Nihat
Arg�man no: 2 ==>Arg�man de�eri: Yava�
Arg�man no: 3 ==>Arg�man de�eri: 17
Arg�man no: 4 ==>Arg�man de�eri: Nisan
Arg�man no: 5 ==>Arg�man de�eri: 1957
Arg�man no: 6 ==>Arg�man de�eri: Ye�ilyurt-Malatya

>python p_12203.py "M.Nihat Yava�" "17 Nisan 1957" Ye�ilyurt-Malatya  ** TEKRAR **
Arg�man no: 1 ==>Arg�man de�eri: M.Nihat Yava�
Arg�man no: 2 ==>Arg�man de�eri: 17 Nisan 1957
Arg�man no: 3 ==>Arg�man de�eri: Ye�ilyurt-Malatya
"""