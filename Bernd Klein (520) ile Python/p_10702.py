# coding:iso-8859-9 Türkçe
# p_10702.py: Dizgelerle çeşitli endeksli işlemler örneği.

dizge = "Python, sen muhteşemsin!"
print ("Tam dizgemiz:", dizge[:])
print ("Dizgenin ilk 6 karakteri:", dizge[0:6] )
print ("Dizgenin 8.den sonrası:", dizge[8:] )
print ("Dizgenin son 12.den öncesi:", dizge[:-12] )

dizge1 = "Toronto Kanada'nın Kuzey Amerika'daki en büyük şehri sayılır"
dizge2 = "Bodenseo tarafından Toronto'da Python kursları verilmektedir"
dizge = "".join (["".join (x) for x in zip (dizge1, dizge2)])
print ("\n", dizge1, "\n", dizge2, "\n", dizge, sep="")

print()
# [ilk, son, artış] --> Belirtilmezse ilk 0, son dizge sonu, artış 1'dir...
print (dizge[::2])
print (dizge[1::2])

print ("\n'P' dizge2'de VAR mıdır?", "P" in dizge2)
print ("'K' dizge1'de YOK mudur?", "K" not in dizge1)
print ("'P' dizge'de VAR mıdır?", "P" in dizge)

from random import randint
d1 = d2 = ""
for i in range (20):
    d1 = d1 + dizge[randint (0, len(dizge)-1)]
    d2 +=dizge[randint (0, len(dizge)-1)]
print ("\nd1 =", d1, "\nd2 =", d2)

d1 = d2 = "a"
d1 = d1*15
d2 *=15
print ("\nd1 =", d1, "\nd2 =", d2)


"""Çıktı:
>python p_10702.py
Tam dizgemiz: Python, sen muhteşemsin!
Dizgenin ilk 6 karakteri: Python
Dizgenin 8.den sonrası: sen muhteşemsin!
Dizgenin son 12.den öncesi: Python, sen

Toronto Kanada'nın Kuzey Amerika'daki en büyük şehri sayılır
Bodenseo tarafından Toronto'da Python kursları verilmektedir
TBoordoenntsoe oK atnaardaaf'ınnıdna nK uTzoeryo nAtmoe'rdiak aP'ydtahkoin  eknu
 rbsülyaürkı  şveehrriil mseakytıeldıirr

Toronto Kanada'nın Kuzey Amerika'daki en büyük şehri sayılır
Bodenseo tarafından Toronto'da Python kursları verilmektedir

'P' dizge2'de VAR mıdır? True
'K' dizge1'de YOK mudur? False
'P' dizge'de VAR mıdır? True

d1 = ı'ro kdenlrrıKnraıal
d2 = arıordtlsrieodsınruk

d1 = aaaaaaaaaaaaaaa
d2 = aaaaaaaaaaaaaaa
"""