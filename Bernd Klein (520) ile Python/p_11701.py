#coding:iso-8859-9 Türkçe
# p_11701.py: for-in-taranabilir(liste, tüple ve dizge), next(iter(taranabilir)) ve taranabilirin Tersten dökümü örneği.

print ("Iterable/tekrarlı liste, tüple ve dizge dökümleri:\n", "-"*50, sep="")
for şehir in ["Ankara", "İstanbul", "İzmir", "Adana", "Mersin"]: print (şehir, end=", ")
print()
for dil in ("Basic", "Fortran", "Cobol", "PL/I", "Pascal", "C", "Clipper",
    "Assembler", "Java", "JavaScript", "Python"): print (dil, end=", ")
print()
for krk in "Iteration tekrarlanabilir verilerin işlenme süreçleri çok kolaydır.": print (krk, end=", ")
#---------------------------------------------------------------------------------------------------

şehirler = ["Ankara", "İstanbul", "İzmir", "Adana", "Mersin", "Eskişehir"]
tarayıcı = iter (şehirler) # İterable şehirler listesi, "iter" hazır fonksiyonuyla tarayıcı nesnesi elemanları oldu...

print ("\n\nŞehirler iterator/tarayıcı nesnesi: ", tarayıcı)
print ("Next ile iterator/tarayıcı nesne elemanları dökümü: ", end="")
while True:
    try: print (next (tarayıcı), end=", ")
    except StopIteration: break
#---------------------------------------------------------------------------------------------------

def tekrarlanabilirMi (nesne):
     try:
         iter (nesne)
         return True
     except TypeError: return False 

print("\n")
for eleman in [34, [4, 5], (4, 5), {"a":4}, "dizge", 4.5]: # Sayı, liste, tüple, sözlük, dizge, sayı...
    print (eleman, "==>Iterable/tekrarlanabilir tipli mi? ", tekrarlanabilirMi (eleman) )
#---------------------------------------------------------------------------------------------------

class Tersten: # Verili tekrarlanabiliri tersten taratır...
    def __init__ (self, veri):
        self.veri = veri
        self.endeks = len (veri)

    def __iter__ (self): return self

    def __next__ (self):
        if self.endeks == 0: raise StopIteration
        self.endeks = self.endeks - 1
        return self.veri [self.endeks]

def dök():
    i = 0
    while True:
        try: print (i, ":", next (terstenTarayıcı), sep="", end=", ")
        except StopIteration: break
        i +=1

terstenTarayıcı = Tersten (şehirler)
print ("\nŞehir liste tarayıcısı tersten dökecek: ", end=""); dök()

terstenTarayıcı = Tersten (range (1957, 2019+1) )
print ("\n\nŞimdi de yılları geriye doğru dökecek: ", end=""); dök()


"""Çıktı:
>python p_11701.py
Iterable/tekrarlı liste, tüple ve dizge dökümleri:
--------------------------------------------------
Ankara, İstanbul, İzmir, Adana, Mersin,
Basic, Fortran, Cobol, PL/I, Pascal, C, Clipper, Assembler, Java, JavaScript, Python,
I, t, e, r, a, t, i, o, n,  , t, e, k, r, a, r, l, a, n, a, b, i, l, i, r,  , v, e, r, i, l, e, r, i, n,  , i, ş, l, e, n, m, e,  , s, ü, r, e, ç, l, e, r, i,
, ç, o, k,  , k, o, l, a, y, d, ı, r, .,

Şehirler iterator/tarayıcı nesnesi:  <list_iterator object at 0x00BE9FB0>
Next ile iterator/tarayıcı nesne elemanları dökümü: Ankara, İstanbul, İzmir, Adana, Mersin, Eskişehir,

34 ==>Iterable/tekrarlanabilir tipli mi?  False
[4, 5] ==>Iterable/tekrarlanabilir tipli mi?  True
(4, 5) ==>Iterable/tekrarlanabilir tipli mi?  True
{'a': 4} ==>Iterable/tekrarlanabilir tipli mi?  True
dizge ==>Iterable/tekrarlanabilir tipli mi?  True
4.5 ==>Iterable/tekrarlanabilir tipli mi?  False

Şehir liste tarayıcısı tersten dökecek: 0:Eskişehir, 1:Mersin, 2:Adana, 3:İzmir, 4:İstanbul, 5:Ankara,

Şimdi de yılları geriye doğru dökecek: 0:2019, 1:2018, 2:2017, 3:2016, 4:2015, 5:2014,
6:2013, 7:2012, 8:2011, 9:2010, 10:2009, 11:2008, 12:2007, 13:2006, 14:2005,
15:2004, 16:2003, 17:2002, 18:2001, 19:2000, 20:1999, 21:1998, 22:1997, 23:1996,
24:1995, 25:1994, 26:1993, 27:1992, 28:1991, 29:1990, 30:1989, 31:1988, 32:1987,
33:1986, 34:1985, 35:1984, 36:1983, 37:1982, 38:1981, 39:1980, 40:1979, 41:1978,
42:1977, 43:1976, 44:1975, 45:1974, 46:1973, 47:1972, 48:1971, 49:1970, 50:1969,
51:1968, 52:1967, 53:1966, 54:1965, 55:1964, 56:1963, 57:1962, 58:1961,59:1960,
60:1959, 61:1958, 62:1957,
"""