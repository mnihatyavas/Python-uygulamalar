# coding:iso-8859-9 Türkçe
# p_14601.py: Argümansız ve argümanı sınıf olan sınıf nesneleri örneği.

class Feylesof1:
    def cevap (self, *argümanlar): return 0
class Feylesof2:
    def cevap (self, *argümanlar): return 1
class Feylesof3:
    def cevap (self, *argümanlar): return 4
class Feylesof4:
    def cevap (self, *argümanlar): return 2
class Feylesof5:
    def cevap (self, *argümanlar): return "Sonsuz"

sokrat = Feylesof1()
aristo = Feylesof2()
plato = Feylesof3()
kant = Feylesof4()
rasıl = Feylesof5()

print ("Her Feylesof/kafa'dan ayrı ses==>\nSoru: (2 * 2 = ?)\n", "-"*37, sep="")
print ("Sokrat:", sokrat.cevap() )
print ("Aristo:", aristo.cevap() )
print ("Plato:", plato.cevap() )
print ("Kant:", kant.cevap() )
print ("Rasıl:", rasıl.cevap() )
print ("-"*37, "\nOrtak cevap: Şartlara göre değişir!..", sep="")
#------------------------------------------------------------------------------------------------------

class Cevaplar:
    def cevap (self, *argümanlar):  return "Şartlara göre değişir!.."

class Feylesof1 (Cevaplar): pass
class Feylesof2 (Cevaplar): pass
class Feylesof3 (Cevaplar): pass
class Feylesof4 (Cevaplar): pass
class Feylesof5 (Cevaplar): pass

sokrat = Feylesof1()
aristo = Feylesof2()
plato = Feylesof3()
kant = Feylesof4()
rasıl = Feylesof5()

print ("\n", "="*37, "\nSoru: 2 kere 2 kaç eder?", sep="")
print ("\nSokrat:", sokrat.cevap() )
print ("Aristo:", aristo.cevap() )
print ("Plato:", plato.cevap() )
print ("Kant:", kant.cevap() )
print ("Rasıl:", rasıl.cevap() )



"""Çıktı:
>python p_14601.py
Her Feylesof/kafa'dan ayrı ses==>
Soru: (2 * 2 = ?)
-------------------------------------
Sokrat: 0
Aristo: 1
Plato: 4
Kant: 2
Rasıl: Sonsuz
-------------------------------------
Ortak cevap: Şartlara göre değişir!..

=====================================
Soru: 2 kere 2 kaç eder?

Sokrat: Şartlara göre değişir!..
Aristo: Şartlara göre değişir!..
Plato: Şartlara göre değişir!..
Kant: Şartlara göre değişir!..
Rasıl: Şartlara göre değişir!..
"""