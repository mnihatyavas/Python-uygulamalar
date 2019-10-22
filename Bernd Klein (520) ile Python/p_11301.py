# coding:iso-8859-9 Türkçe
# p_11301.py: input ile klavyeden girilen sayısal veya dizgesel verilerin değerlendirilmesi örneği.

ad = input ("Adınızı öğrenebilir miyim?: ")
if ad == "": ad = "Nihat"
print ("Tanıştığımıza memnun oldum, " + ad + "!")

try: yaş = abs (int (eval (input ("\nPeki yaşınız? "))))
except: yaş = 62
print ("O halde, halihazırda siz " + str (yaş) + " yaşındasınız ve " + str (2019-yaş) + " doğumlusunuz, " + ad + "!")
#-----------------------------------------------------------------------------------------------------

şehirler = input ('\nTürkiyenin büyük birkaç şehrini girin: ')
if şehirler == "": şehirler = "Ankara, İstanbul, İzmir"
print ("Girilen şehirler: " + şehirler + "\nVeri tipi: " + str (type (şehirler)) )

try: şehirler = eval (input ('\nTekrar birkaç şehir girin ["..", "..",..]: '))
except: şehirler = ["Ankara", "İstanbul", "İzmir"]
print ("Girilen şehirler:", şehirler, "\nVeri tipi: ", type (şehirler) )

nüfus = input ('\nTürkiyenin yaklaşık nüfusunu girin: ')
if nüfus == "": nüfus = "80,000,000"
print ("Türkiye'nin yaklaşık nüfusu: " + nüfus + "\nVeri tipi: " + str (type (nüfus)) )

try: nüfus = eval (input ('\nSayısal nüfusu tekrar girin: '))
except: nüfus = 80000000
print ("Yaklaşık nüfus:", nüfus, "\nVeri tipi: ", type (nüfus) )

"""Çıktı
>python p_11301.py
Adınızı öğrenebilir miyim?:
Tanıştığımıza memnun oldum, Nihat!

Peki yaşınız?
O halde, halihazırda siz 62 yaşındasınız ve 1957 doğumlusunuz, Nihat!

Türkiyenin büyük birkaç şehrini girin:
Girilen şehirler: Ankara, İstanbul, İzmir
Veri tipi: <class 'str'>

Tekrar birkaç şehir girin ["..", "..",..]:
Girilen şehirler: ['Ankara', 'İstanbul', 'İzmir']
Veri tipi:  <class 'list'>

Türkiyenin yaklaşık nüfusunu girin:
Türkiye'nin yaklaşık nüfusu: 80,000,000
Veri tipi: <class 'str'>

Sayısal nüfusu tekrar girin:
Yaklaşık nüfus: 80000000
Veri tipi:  <class 'int'>
"""