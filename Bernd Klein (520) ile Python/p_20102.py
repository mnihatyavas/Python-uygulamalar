# coding:iso-8859-9 Türkçe
# p_20102.py: Komut iletisinden girilen argümanların yönetilmesi örneği.

import sys

print ("Komut satırı iletileri listesi:", sys.argv)

for i in range (len (sys.argv) ):
    if i == 0: print ("\nÇalıştırılan programın adı: %s" % sys.argv [0] )
    else: print ("%d.argüman: %s" % (i, sys.argv [i]) )



"""Çıktı:
>python p_20102.py "M.Nihat Yavaş"
1957 Yeşilyurt-Malatya TR
Komut satırı iletileri listesi: ['p_20102.py', 'M.Nihat Yavaş', '1957', 'Yeşilyurt-Malatya', 'TR']

Çalıştırılan programın adı: p_20102.py
1.argüman: M.Nihat Yavaş
2.argüman: 1957
3.argüman: Yeşilyurt-Malatya
4.argüman: TR
"""