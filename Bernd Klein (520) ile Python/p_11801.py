#coding:iso-8859-9 T�rk�e
# p_11801.py: Print ile ekrana, dosyaya ve hataya yazd�rma �rne�i.

import sys

"""print(..) fonksiyonu arg�manlar�:
print (de�er1, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
"""
print ("K�nyem:\n", "-"*25, "\nMemet ve Han�m Yava� o�lu", sep="", end="\n")
print ("M.Nihat Yava�\n", 4, "/", 17, "/", 1957, "\nYe�ilyurt-Malatya", sep="", file=sys.stdout)

#-------------------------------------------------------------------------------------------------------

dosya = open ("mny1.txt", "w")
print ("Cevap tabi ki 42 olacakt�r; fakat affedersiniz unuttum, sorunuz neydi acaba?..", file=dosya, flush=True)
dosya.close()
print ("\nVeriler 'mny1.txt' dosyas�na yaz�ld� ve dosya da flush'lan�p kapat�ld�.", file=sys.stderr, flush=False)


"""��kt�:
>python p_11801.py
K�nyem:
-------------------------
Memet ve Han�m Yava� o�lu
M.Nihat Yava�
4/17/1957
Ye�ilyurt-Malatya

Veriler 'mny1.txt' dosyas�na yaz�ld� ve dosya da flush'lan�p kapat�ld�.
"""