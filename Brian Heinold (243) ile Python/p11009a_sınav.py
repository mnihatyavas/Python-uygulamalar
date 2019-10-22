# coding:iso-8859-9 Türkçe

L = [i for i in range (3, 100, 3)]
print (L)

kelime = input ("\nKelime girin: ")
K = list (kelime)
for h in K:
    if h == " ": K.remove (h)
K.sort()
print ("Kelimenin [a->z] sıralısı:", "".join (K) )

L = [["Elma", 3.75], ["Armut", 4.35], ["Havuç", 2.45], ["Nar", 3.67], ["Domates", 1.67],
    ["Hurma", 5.78], ["Mandalina", 2.87], ["Portakal", 2.78], ["Kivi", 5.50], ["Hıyar", 1.85]]
from pprint import pprint
toplam = 0
print ("\nAlışveriş Faturanız:\n{:s}" .format ("="*26) )
for i in range (len (L)):
    print ("{:9s}:{:5.2f} TL" .format (L[i][0], L[i][1]) )
    toplam += L[i][1]
print ("{:s}\nToplam   : {:5.2f} TL" .format ("-"*26, toplam) )
print ("İskonto  : {:5.2f} TL (-%11)" .format (toplam*.11) )
print ("Fatura   : {:5.2f} TL" .format (toplam - toplam*.11) )