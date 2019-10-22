# coding:iso-8859-9 T�rk�e
# p_14601.py: Arg�mans�z ve arg�man� s�n�f olan s�n�f nesneleri �rne�i.

class Feylesof1:
    def cevap (self, *arg�manlar): return 0
class Feylesof2:
    def cevap (self, *arg�manlar): return 1
class Feylesof3:
    def cevap (self, *arg�manlar): return 4
class Feylesof4:
    def cevap (self, *arg�manlar): return 2
class Feylesof5:
    def cevap (self, *arg�manlar): return "Sonsuz"

sokrat = Feylesof1()
aristo = Feylesof2()
plato = Feylesof3()
kant = Feylesof4()
ras�l = Feylesof5()

print ("Her Feylesof/kafa'dan ayr� ses==>\nSoru: (2 * 2 = ?)\n", "-"*37, sep="")
print ("Sokrat:", sokrat.cevap() )
print ("Aristo:", aristo.cevap() )
print ("Plato:", plato.cevap() )
print ("Kant:", kant.cevap() )
print ("Ras�l:", ras�l.cevap() )
print ("-"*37, "\nOrtak cevap: �artlara g�re de�i�ir!..", sep="")
#------------------------------------------------------------------------------------------------------

class Cevaplar:
    def cevap (self, *arg�manlar):  return "�artlara g�re de�i�ir!.."

class Feylesof1 (Cevaplar): pass
class Feylesof2 (Cevaplar): pass
class Feylesof3 (Cevaplar): pass
class Feylesof4 (Cevaplar): pass
class Feylesof5 (Cevaplar): pass

sokrat = Feylesof1()
aristo = Feylesof2()
plato = Feylesof3()
kant = Feylesof4()
ras�l = Feylesof5()

print ("\n", "="*37, "\nSoru: 2 kere 2 ka� eder?", sep="")
print ("\nSokrat:", sokrat.cevap() )
print ("Aristo:", aristo.cevap() )
print ("Plato:", plato.cevap() )
print ("Kant:", kant.cevap() )
print ("Ras�l:", ras�l.cevap() )



"""��kt�:
>python p_14601.py
Her Feylesof/kafa'dan ayr� ses==>
Soru: (2 * 2 = ?)
-------------------------------------
Sokrat: 0
Aristo: 1
Plato: 4
Kant: 2
Ras�l: Sonsuz
-------------------------------------
Ortak cevap: �artlara g�re de�i�ir!..

=====================================
Soru: 2 kere 2 ka� eder?

Sokrat: �artlara g�re de�i�ir!..
Aristo: �artlara g�re de�i�ir!..
Plato: �artlara g�re de�i�ir!..
Kant: �artlara g�re de�i�ir!..
Ras�l: �artlara g�re de�i�ir!..
"""