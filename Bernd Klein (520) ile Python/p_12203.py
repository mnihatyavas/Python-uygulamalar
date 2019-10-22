# coding:iso-8859-9 Türkçe
# p_12203.py: Komut satırından girilen argümanların yönetilmesi örneği.

import sys                

uz = len (sys.argv)
if uz < 2:
    print ("Bu program için ileti komutundan enaz 1 argüman değeri girmelisiniz!..")
    sys.exit (-1)

for i in range (1, uz):
    print ("Argüman no:", i, "==>Argüman değeri:", sys.argv[i] )

"""Çıktı:
>python p_12203.py
Bu program için ileti komutundan enaz 1 argüman değeri girmelisiniz!..

>python p_12203.py Nihat  ** TEKRAR ??
Argüman no: 1 ==>Argüman değeri: Nihat

>python p_12203.py M.Nihat Yavaş 17 Nisan 1957 Yeşilyurt-Malatya  ** TEKRAR **
Argüman no: 1 ==>Argüman değeri: M.Nihat
Argüman no: 2 ==>Argüman değeri: Yavaş
Argüman no: 3 ==>Argüman değeri: 17
Argüman no: 4 ==>Argüman değeri: Nisan
Argüman no: 5 ==>Argüman değeri: 1957
Argüman no: 6 ==>Argüman değeri: Yeşilyurt-Malatya

>python p_12203.py "M.Nihat Yavaş" "17 Nisan 1957" Yeşilyurt-Malatya  ** TEKRAR **
Argüman no: 1 ==>Argüman değeri: M.Nihat Yavaş
Argüman no: 2 ==>Argüman değeri: 17 Nisan 1957
Argüman no: 3 ==>Argüman değeri: Yeşilyurt-Malatya
"""