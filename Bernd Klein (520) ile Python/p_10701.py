# coding:iso-8859-9 T�rk�e
# p_10701.py: Dizge, liste, t�ple ve byte dizilerle endeksli i�lemler �rne�i.

# Dizge, byte, byte dizi, liste, t�ple, range/erim s�ral� veri tipini kullan�r...

dizge = "Dizgenin herbir s�ral� endeks karakterine ula��labilir!"
print (dizge, "\n==>", dizge[0], dizge[len (dizge) // 2], dizge[len (dizge)-1], dizge[-1], dizge[-len (dizge)])

print()
liste = ["Tokyo", "Astana", "Bankok", "Singapur", "Moskova", "Kiev",
    "Tahran", "Tiflis", "Na�civan", "Halep", "Dubai", "Kahire", "�artum",
    "Lefko�e", "Atina", "Sofya", "Saraybosna", "Rabat", "Sao Paola", "Buenos Aires"]
print (liste, "\n==>", liste[0], liste[len (liste) // 2], liste[len (liste)-1], liste[-1], liste[-len (liste)])

print ("\nBo� liste:", [])
print ("Tamsay�lar listesi:", [1,1,2,3,5,8])
print ("Kar���k veri tipli liste:", [42, "Ne sormu�tunuz?", 3.1415])
print ("\nDizgeler listesi:", ["Ankara", "�stanbul", "�zmir", "Adana",
    "Konya", "Mersin","Bursa", "Samsun", "Antalya"])
print ("\n��-i�e listelerli liste:", [["Londra","�ngiltere", 7556900],
     ["Paris","Fransa",2193031], ["Bern", "�svi�re", 123466]]	)
print ("\nDerin i�-i�e liste:", ["�st seviye", ["2.alt seviye", ["ve 3.a�a��s�",
    ["4.derin alt seviye", "cevap", 42]]]])

�ah�s = [ ["Yava�", "M.Nihat"], ["217, An�tlar Cd", "No: 9","Toroslar-Mersin"],
     ["090.555.551.94.64", "mnyavas@hotmail.com"] ]
print ("\n�ahs�n ad� ve soyad�:", �ah�s[0][1], �ah�s[0][0])
print ("�ahs�n adresi:", �ah�s[1])
print ("�ahs�n epostas�:", �ah�s[2][1])

kompleksListe = [ ["a", ["b", ["c", "x"]]] , 42]
print ("\nKompleks liste eleman say�s�:", len (kompleksListe))
print ("En derin ilk eleman:", kompleksListe[0][1][1][0])


L = ["a", "b", "c"]
print ("\nL :", L)
L *=3
print ("L *=3:", L)
L[1] = "P"
print ("L[1] = 'P':", L)
L = ["a", "b", "c"]
L = [L]*3
print ("L=[L]*3:", L)
L[1][0] = "P"
print ("HATA: L[1][0] = 'P':", L)

t�ple = ("T�ple", "eleman", "say�s�n� ve de�erlerini", "listeler gibi", "de�i�tiremezsiniz.")
print ("\nT�ple sembol� parantezdir:", t�ple)
print ("Endekslenmesi listelerle ayn�d�r:", t�ple[0], t�ple[len (t�ple)//2], t�ple[-1])
# t�ple[0] = "T�pleler" ==>Derleme hatas�...

print()
byteNesnesi = b"M.Nihat Yavas, 1957"
print ("Byte nesnesi 0->127 ASCII karakterlidir:", byteNesnesi,
    byteNesnesi[0], chr (byteNesnesi[8]), ord (chr (byteNesnesi[16])) )


"""��kt�:
>python p_10601.py
Toplama ve ��karma (10+/-3): 13 7
�arpma, b�lme ve kalan (27*/+7): 189 3.857142857142857 6
K�s�rats�z (-+//) zemin b�lme ve -+int(10/3) kesik b�lmesi: 3 3 -4.0 -3
�ebirsel -+ i�areti: -3 3
Bitvari negatifleme: -8 6
-+�s (**): -199.5690776400273 0.00501079632087968
Boolean or/veya, and/ve ve not/de�il: False
Eleman� m� (True/False)? True
Kar��la�t�rma (2 ila 5) operat�rleri (<, <=, >, >=, ==, !=): True True False False False True
Bitvari |/veya, &/ve, ^/farkl�ysa (6=110 ila 3=011): 7 2 5
Kayd�rma << ve >> operat�rleri (6=110'y� 2 kez kayd�r): 24 1

C:\Users\pc\Desktop\MyFiles\4. Dersler\python>python p_10701.py
Dizgenin herbir s�ral� endeks karakterine ula��labilir!
==> D k ! ! D

['Tokyo', 'Astana', 'Bankok', 'Singapur', 'Moskova', 'Kiev', 'Tahran', 'Tiflis',
 'Na�civan', 'Halep', 'Dubai', 'Kahire', '�artum', 'Lefko�e', 'Atina', 'Sofya',
'Saraybosna', 'Rabat', 'Sao Paola', 'Buenos Aires']
==> Tokyo Dubai Buenos Aires Buenos Aires Tokyo

Bo� liste: []
Tamsay�lar listesi: [1, 1, 2, 3, 5, 8]
Kar���k veri tipli liste: [42, 'Ne sormu�tunuz?', 3.1415]

Dizgeler listesi: ['Ankara', '�stanbul', '�zmir', 'Adana', 'Konya', 'Mersin', 'Bursa', 'Samsun', 'Antalya']

��-i�e listelerli liste: [['Londra', '�ngiltere', 7556900], ['Paris', 'Fransa',2193031], ['Bern', '�svi�re', 123466]]

Derin i�-i�e liste: ['�st seviye', ['2.alt seviye', ['ve 3.a�a��s�', ['4.derin alt seviye', 'cevap', 42]]]]

�ahs�n ad� ve soyad�: M.Nihat Yava�
�ahs�n adresi: ['217, An�tlar Cd', 'No: 9', 'Toroslar-Mersin']
�ahs�n epostas�: mnyavas@hotmail.com

Kompleks liste eleman say�s�: 2
En derin ilk eleman: c

L : ['a', 'b', 'c']
L *=3: ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']
L[1] = 'P': ['a', 'P', 'c', 'a', 'b', 'c', 'a', 'b', 'c']
L=[L]*3: [['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c']]
HATA: L[1][0] = 'P': [['P', 'b', 'c'], ['P', 'b', 'c'], ['P', 'b', 'c']]

T�ple sembol� parantezdir: ('T�ple', 'eleman', 'say�s�n� ve de�erlerini', 'listeler gibi', 'de�i�tiremezsiniz.')
Endekslenmesi listelerle ayn�d�r: T�ple say�s�n� ve de�erlerini de�i�tiremezsiniz.

Byte nesnesi 0->127 ASCII karakterlidir: b'M.Nihat Yavas, 1957' 77 Y 57
"""