#coding:iso-8859-9 T�rk�e
# p_11701.py: for-in-taranabilir(liste, t�ple ve dizge), next(iter(taranabilir)) ve taranabilirin Tersten d�k�m� �rne�i.

print ("Iterable/tekrarl� liste, t�ple ve dizge d�k�mleri:\n", "-"*50, sep="")
for �ehir in ["Ankara", "�stanbul", "�zmir", "Adana", "Mersin"]: print (�ehir, end=", ")
print()
for dil in ("Basic", "Fortran", "Cobol", "PL/I", "Pascal", "C", "Clipper",
    "Assembler", "Java", "JavaScript", "Python"): print (dil, end=", ")
print()
for krk in "Iteration tekrarlanabilir verilerin i�lenme s�re�leri �ok kolayd�r.": print (krk, end=", ")
#---------------------------------------------------------------------------------------------------

�ehirler = ["Ankara", "�stanbul", "�zmir", "Adana", "Mersin", "Eski�ehir"]
taray�c� = iter (�ehirler) # �terable �ehirler listesi, "iter" haz�r fonksiyonuyla taray�c� nesnesi elemanlar� oldu...

print ("\n\n�ehirler iterator/taray�c� nesnesi: ", taray�c�)
print ("Next ile iterator/taray�c� nesne elemanlar� d�k�m�: ", end="")
while True:
    try: print (next (taray�c�), end=", ")
    except StopIteration: break
#---------------------------------------------------------------------------------------------------

def tekrarlanabilirMi (nesne):
     try:
         iter (nesne)
         return True
     except TypeError: return False 

print("\n")
for eleman in [34, [4, 5], (4, 5), {"a":4}, "dizge", 4.5]: # Say�, liste, t�ple, s�zl�k, dizge, say�...
    print (eleman, "==>Iterable/tekrarlanabilir tipli mi? ", tekrarlanabilirMi (eleman) )
#---------------------------------------------------------------------------------------------------

class Tersten: # Verili tekrarlanabiliri tersten tarat�r...
    def __init__ (self, veri):
        self.veri = veri
        self.endeks = len (veri)

    def __iter__ (self): return self

    def __next__ (self):
        if self.endeks == 0: raise StopIteration
        self.endeks = self.endeks - 1
        return self.veri [self.endeks]

def d�k():
    i = 0
    while True:
        try: print (i, ":", next (terstenTaray�c�), sep="", end=", ")
        except StopIteration: break
        i +=1

terstenTaray�c� = Tersten (�ehirler)
print ("\n�ehir liste taray�c�s� tersten d�kecek: ", end=""); d�k()

terstenTaray�c� = Tersten (range (1957, 2019+1) )
print ("\n\n�imdi de y�llar� geriye do�ru d�kecek: ", end=""); d�k()


"""��kt�:
>python p_11701.py
Iterable/tekrarl� liste, t�ple ve dizge d�k�mleri:
--------------------------------------------------
Ankara, �stanbul, �zmir, Adana, Mersin,
Basic, Fortran, Cobol, PL/I, Pascal, C, Clipper, Assembler, Java, JavaScript, Python,
I, t, e, r, a, t, i, o, n,  , t, e, k, r, a, r, l, a, n, a, b, i, l, i, r,  , v, e, r, i, l, e, r, i, n,  , i, �, l, e, n, m, e,  , s, �, r, e, �, l, e, r, i,
, �, o, k,  , k, o, l, a, y, d, �, r, .,

�ehirler iterator/taray�c� nesnesi:  <list_iterator object at 0x00BE9FB0>
Next ile iterator/taray�c� nesne elemanlar� d�k�m�: Ankara, �stanbul, �zmir, Adana, Mersin, Eski�ehir,

34 ==>Iterable/tekrarlanabilir tipli mi?  False
[4, 5] ==>Iterable/tekrarlanabilir tipli mi?  True
(4, 5) ==>Iterable/tekrarlanabilir tipli mi?  True
{'a': 4} ==>Iterable/tekrarlanabilir tipli mi?  True
dizge ==>Iterable/tekrarlanabilir tipli mi?  True
4.5 ==>Iterable/tekrarlanabilir tipli mi?  False

�ehir liste taray�c�s� tersten d�kecek: 0:Eski�ehir, 1:Mersin, 2:Adana, 3:�zmir, 4:�stanbul, 5:Ankara,

�imdi de y�llar� geriye do�ru d�kecek: 0:2019, 1:2018, 2:2017, 3:2016, 4:2015, 5:2014,
6:2013, 7:2012, 8:2011, 9:2010, 10:2009, 11:2008, 12:2007, 13:2006, 14:2005,
15:2004, 16:2003, 17:2002, 18:2001, 19:2000, 20:1999, 21:1998, 22:1997, 23:1996,
24:1995, 25:1994, 26:1993, 27:1992, 28:1991, 29:1990, 30:1989, 31:1988, 32:1987,
33:1986, 34:1985, 35:1984, 36:1983, 37:1982, 38:1981, 39:1980, 40:1979, 41:1978,
42:1977, 43:1976, 44:1975, 45:1974, 46:1973, 47:1972, 48:1971, 49:1970, 50:1969,
51:1968, 52:1967, 53:1966, 54:1965, 55:1964, 56:1963, 57:1962, 58:1961,59:1960,
60:1959, 61:1958, 62:1957,
"""