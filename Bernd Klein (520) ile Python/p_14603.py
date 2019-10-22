# coding:iso-8859-9 Türkçe
# p_14603.py: Harici fonksiyonu sınıfa yönetici fonksiyon vasıtasıyla metod vasfı yapma örneği.

print ("Soru: 2 kere 2 kaç eder?")
cevap = input ("Feylesofların cevaplarını istiyor musun? (e/h): ")
if cevap == "e": cevap = True
else: cevap = False

def cevabım (self, *argümanlar):  return "Şartlara göre değişir!.."

def cevabıEkle (sınıf): # Yönetici fonksiyonu..
    if cevap: sınıf.cevabım = cevabım

class Feylesof1: pass
class Feylesof2: pass
class Feylesof3: pass
class Feylesof4: pass
class Feylesof5: pass

cevabıEkle (Feylesof1)
cevabıEkle (Feylesof2)
cevabıEkle (Feylesof3)
cevabıEkle (Feylesof4)
cevabıEkle (Feylesof5)

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
>python p_14603.py
Soru: 2 kere 2 kaç eder?
Feylesofların cevaplarını istiyor musun? (e/h): e

Sokrat: Şartlara göre değişir!..
Aristo: Şartlara göre değişir!..
Plato: Şartlara göre değişir!..
Kant: Şartlara göre değişir!..
Rasıl: Şartlara göre değişir!..

>python p_14603.py  ** TEKRAR **
Soru: 2 kere 2 kaç eder?
Feylesofların cevaplarını istiyor musun? (e/h): h
Cevabı Filozofların sessizliğinde ara!..
"""