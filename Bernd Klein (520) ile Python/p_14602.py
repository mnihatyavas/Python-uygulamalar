# coding:iso-8859-9 T�rk�e
# p_14602.py: Harici fonksiyonu s�n�f �zelli�i metodu yapma �rne�i.

print ("Soru: 2 kere 2 ka� eder?")
cevap = input ("Feylesoflar�n cevaplar�n� istiyor musun? (e/h): ")
if cevap == "e": cevap = True
else: cevap = False

def cevab�m (self, *arg�manlar):  return "�artlara g�re de�i�ir!.."

class Feylesof1: pass
class Feylesof2: pass
class Feylesof3: pass
class Feylesof4: pass
class Feylesof5: pass

if cevap:
    Feylesof1.cevab�m = cevab�m
    Feylesof2.cevab�m = cevab�m
    Feylesof3.cevab�m = cevab�m
    Feylesof4.cevab�m = cevab�m
    Feylesof5.cevab�m = cevab�m

sokrat = Feylesof1()
aristo = Feylesof2()
plato = Feylesof3()
kant = Feylesof4()
ras�l = Feylesof5()

if cevap:
    print ("\nSokrat:", sokrat.cevab�m() )
    print ("Aristo:", aristo.cevab�m() )
    print ("Plato:", plato.cevab�m() )
    print ("Kant:", kant.cevab�m() )
    print ("Ras�l:", ras�l.cevab�m() )
else: print ("Cevab� Filozoflar�n sessizli�inde ara!..")



"""��kt�:
>python p_14602.py
Soru: 2 kere 2 ka� eder?
Feylesoflar�n cevaplar�n� istiyor musun? (e/h): e

Sokrat: �artlara g�re de�i�ir!..
Aristo: �artlara g�re de�i�ir!..
Plato: �artlara g�re de�i�ir!..
Kant: �artlara g�re de�i�ir!..
Ras�l: �artlara g�re de�i�ir!..

>python p_14602.py  ** TEKRAR **
Soru: 2 kere 2 ka� eder?
Feylesoflar�n cevaplar�n� istiyor musun? (e/h): h
Cevab� Filozoflar�n sessizli�inde ara!..
"""