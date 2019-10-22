# coding:iso-8859-9 T�rk�e
# p_12006.py: Fonksiyon �oklu parametre ve arg�manlar�nda *liste kullan�lmas� �rne�i.

from random import randint, random

def aritmetikOrtalama1 (ilk, *di�erleri): return (ilk + sum (di�erleri)) / (1 + len (di�erleri))
def aritmetikOrtalama2 (liste): return sum (liste) / len (liste)

print ("4 say�n�n ortalamas�:", aritmetikOrtalama1 (45, 32, 89, 78) )
print ("7 say�n�n ortalamas�:", aritmetikOrtalama1 (0, 0, 8989.8, 78787.78, 3453, 78778.73, 0) )
print ("2 say�n�n ortalamas�:", aritmetikOrtalama1 (45, 32) )
print ("Tek bir say�n�n ortalamas�:", aritmetikOrtalama1 (45) )

a = randint (1,100)
print ("\nGeli�ig�zel", a, "elemanl� say�sal bir listenin ortalamas�:", aritmetikOrtalama2 ([randint(0,100)+random() for i in range (a)]) )

b = randint (1,100)
liste = [randint (0, 100) + random() for i in range (b)]
print ("Geli�ig�zel", b, "elemanl� say�sal arg�manlar�n ortalamas�:", aritmetikOrtalama1 (*liste) )
#----------------------------------------------------------------------------------------------------------

listem = [('Nihat', 1047, 79.5), ('Sami', 1044, 35), ('�hsan', 1042, 67.5), ('Necati', 1048, 56), ("Hamit", 1057, 91.5), ("Zeki", 1039, 75.5)]
print ("\nOrijinal listem:", listem)

yeniListem = list (zip (*listem))
print ("\nZip'lenen listem:", yeniListem)
print ("\nS�n�ftaki toplam", len (listem), "��rencinin not ortalamas�:", aritmetikOrtalama1 (*yeniListem[2]) )


"""��kt�:
>python p_12006.py
4 say�n�n ortalamas�: 61.0
7 say�n�n ortalamas�: 24287.044285714284
2 say�n�n ortalamas�: 38.5
Tek bir say�n�n ortalamas�: 45.0

Geli�ig�zel 49 elemanl� say�sal bir listenin ortalamas�: 52.51783109803962
Geli�ig�zel 61 elemanl� say�sal arg�manlar�n ortalamas�: 55.712565881134395

Orijinal listem: [('Nihat', 1047, 79.5), ('Sami', 1044, 35), ('�hsan', 1042, 67.5),
('Necati', 1048, 56), ('Hamit', 1057, 91.5), ('Zeki', 1039, 75.5)]

Zip'lenen listem: [('Nihat', 'Sami', '�hsan', 'Necati', 'Hamit', 'Zeki'),
(1047, 1044, 1042, 1048, 1057, 1039), (79.5, 35, 67.5, 56, 91.5, 75.5)]

S�n�ftaki toplam 6 ��rencinin not ortalamas�: 67.5
"""