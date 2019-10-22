# coding:iso-8859-9 T�rk�e
# p_10702.py: Dizgelerle �e�itli endeksli i�lemler �rne�i.

dizge = "Python, sen muhte�emsin!"
print ("Tam dizgemiz:", dizge[:])
print ("Dizgenin ilk 6 karakteri:", dizge[0:6] )
print ("Dizgenin 8.den sonras�:", dizge[8:] )
print ("Dizgenin son 12.den �ncesi:", dizge[:-12] )

dizge1 = "Toronto Kanada'n�n Kuzey Amerika'daki en b�y�k �ehri say�l�r"
dizge2 = "Bodenseo taraf�ndan Toronto'da Python kurslar� verilmektedir"
dizge = "".join (["".join (x) for x in zip (dizge1, dizge2)])
print ("\n", dizge1, "\n", dizge2, "\n", dizge, sep="")

print()
# [ilk, son, art��] --> Belirtilmezse ilk 0, son dizge sonu, art�� 1'dir...
print (dizge[::2])
print (dizge[1::2])

print ("\n'P' dizge2'de VAR m�d�r?", "P" in dizge2)
print ("'K' dizge1'de YOK mudur?", "K" not in dizge1)
print ("'P' dizge'de VAR m�d�r?", "P" in dizge)

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


"""��kt�:
>python p_10702.py
Tam dizgemiz: Python, sen muhte�emsin!
Dizgenin ilk 6 karakteri: Python
Dizgenin 8.den sonras�: sen muhte�emsin!
Dizgenin son 12.den �ncesi: Python, sen

Toronto Kanada'n�n Kuzey Amerika'daki en b�y�k �ehri say�l�r
Bodenseo taraf�ndan Toronto'da Python kurslar� verilmektedir
TBoordoenntsoe oK atnaardaaf'�nn�dna nK uTzoeryo nAtmoe'rdiak aP'ydtahkoin  eknu
 rbs�lya�rk�  �veehrriil mseakyt�eld�irr

Toronto Kanada'n�n Kuzey Amerika'daki en b�y�k �ehri say�l�r
Bodenseo taraf�ndan Toronto'da Python kurslar� verilmektedir

'P' dizge2'de VAR m�d�r? True
'K' dizge1'de YOK mudur? False
'P' dizge'de VAR m�d�r? True

d1 = �'ro kdenlrr�Knra�al
d2 = ar�ordtlsrieods�nruk

d1 = aaaaaaaaaaaaaaa
d2 = aaaaaaaaaaaaaaa
"""