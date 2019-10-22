#coding:iso-8859-9 Türkçe
# p_11801.py: Print ile ekrana, dosyaya ve hataya yazdırma örneği.

import sys

"""print(..) fonksiyonu argümanları:
print (değer1, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
"""
print ("Künyem:\n", "-"*25, "\nMemet ve Hanım Yavaş oğlu", sep="", end="\n")
print ("M.Nihat Yavaş\n", 4, "/", 17, "/", 1957, "\nYeşilyurt-Malatya", sep="", file=sys.stdout)

#-------------------------------------------------------------------------------------------------------

dosya = open ("mny1.txt", "w")
print ("Cevap tabi ki 42 olacaktır; fakat affedersiniz unuttum, sorunuz neydi acaba?..", file=dosya, flush=True)
dosya.close()
print ("\nVeriler 'mny1.txt' dosyasına yazıldı ve dosya da flush'lanıp kapatıldı.", file=sys.stderr, flush=False)


"""Çıktı:
>python p_11801.py
Künyem:
-------------------------
Memet ve Hanım Yavaş oğlu
M.Nihat Yavaş
4/17/1957
Yeşilyurt-Malatya

Veriler 'mny1.txt' dosyasına yazıldı ve dosya da flush'lanıp kapatıldı.
"""