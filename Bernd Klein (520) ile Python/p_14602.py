# coding:iso-8859-9 Türkçe
# p_14602.py: Harici fonksiyonu sınıf özelliği metodu yapma örneği.

print ("Soru: 2 kere 2 kaç eder?")
cevap = input ("Feylesofların cevaplarını istiyor musun? (e/h): ")
if cevap == "e": cevap = True
else: cevap = False

def cevabım (self, *argümanlar):  return "Şartlara göre değişir!.."

class Feylesof1: pass
class Feylesof2: pass
class Feylesof3: pass
class Feylesof4: pass
class Feylesof5: pass

if cevap:
    Feylesof1.cevabım = cevabım
    Feylesof2.cevabım = cevabım
    Feylesof3.cevabım = cevabım
    Feylesof4.cevabım = cevabım
    Feylesof5.cevabım = cevabım

sokrat = Feylesof1()
aristo = Feylesof2()
plato = Feylesof3()
kant = Feylesof4()
rasıl = Feylesof5()

if cevap:
    print ("\nSokrat:", sokrat.cevabım() )
    print ("Aristo:", aristo.cevabım() )
    print ("Plato:", plato.cevabım() )
    print ("Kant:", kant.cevabım() )
    print ("Rasıl:", rasıl.cevabım() )
else: print ("Cevabı Filozofların sessizliğinde ara!..")



"""Çıktı:
>python p_14602.py
Soru: 2 kere 2 kaç eder?
Feylesofların cevaplarını istiyor musun? (e/h): e

Sokrat: Şartlara göre değişir!..
Aristo: Şartlara göre değişir!..
Plato: Şartlara göre değişir!..
Kant: Şartlara göre değişir!..
Rasıl: Şartlara göre değişir!..

>python p_14602.py  ** TEKRAR **
Soru: 2 kere 2 kaç eder?
Feylesofların cevaplarını istiyor musun? (e/h): h
Cevabı Filozofların sessizliğinde ara!..
"""