# coding:iso-8859-9 T�rk�e
# p_30805.py: �oklu �lkelerden depremzedelere a��rl�kl�, yegane ve bi�imli yard�m listesi �rne�i.

import p_30801 as p381

�lkeliAdlar = {
    "Fransa" : [
        ("Marie", 10), ("Thomas", 10), ("Camille", 10), ("Nicolas", 9),
        ("L�a", 10), ("Julien", 9), ("Manon", 9), ("Quentin", 9),
        ("Chlo�", 8), ("Maxime", 9), ("Laura", 7), ("Alexandre", 6),
        ("Clementine", 2), ("Gr�gory", 2), ("Sandra", 1), ("Philippe", 1) ],
    "�svi�re": [
        ("Sarah", 10), ("Hans", 10), ("Laura", 9), ("Peter", 8),
        ("M�lissa", 9), ("Walter", 7), ("Oc�ane", 7), ("Daniel", 7),
        ("No�mie", 6), ("Reto", 7), ("Laura", 7), ("Bruno", 6),
        ("Eva", 2), ("Urli", 4), ("Sandra", 1), ("Marcel", 1) ],
    "Almanya": [
        ("Ursula", 10), ("Peter", 10), ("Monika", 9), ("Michael", 8),
        ("Brigitte", 9), ("Thomas", 7), ("Stefanie", 7), ("Andreas", 7),
        ("Maria", 6), ("Wolfgang", 7), ("Gabriele", 7), ("Manfred", 6),
        ("Nicole", 2), ("Matthias", 4), ("Christine", 1), ("Dirk", 1) ],
    "�talya" : [
        ("Francesco", 20), ("Alessandro", 19), ("Mattia", 19), ("Lorenzo", 18),
        ("Leonardo", 16), ("Andrea", 15), ("Gabriele", 14), ("Matteo", 14),
        ("Tommaso", 12), ("Riccardo", 11), ("Sofia", 20), ("Aurora", 18),
        ("Giulia", 16), ("Giorgia", 15), ("Alice", 14), ("Martina", 13) ],
    "T�rkiye":[
        ("Mehmet", 35), ("Nihat", 3), ("Hatice", 32), ("Ali", 19),
        ("Hasan", 25), ("Ay�e", 27), ("Kezban", 9), ("Yavuz", 3),
        ("�zcan", 8), ("Mahmut", 22), ("Belk�s", 1) ] }

�lkeliSoyadlar = {
    "Fransa" : [
        ("Matin", 10), ("Bernard", 10), ("Camille", 10), ("Nicolas", 9),
        ("Dubois", 10), ("Petit", 9), ("Durand", 8), ("Leroy", 8),
        ("Fournier", 7), ("Lambert", 6), ("Mercier", 5), ("Rousseau", 4),
        ("Mathieu", 2), ("Fontaine", 2), ("Muller", 1), ("Robin", 1) ],
    "�svi�re": [
        ("M�ller", 10), ("Meier", 10), ("Schmid", 9), ("Keller", 8),
        ("Weber", 9), ("Huber", 7), ("Schneider", 7), ("Meyer", 7),
        ("Steiner", 6), ("Fischer", 7), ("Gerber", 7), ("Brunner", 6),
        ("Baumann", 2), ("Frei", 4), ("Zimmermann", 1), ("Moser", 1) ],
    "Almanya": [
        ("M�ller", 10), ("Schmidt", 10), ("Schneider", 9), ("Fischer", 8),
        ("Weber", 9), ("Meyer", 7), ("Wagner", 7), ("Becker", 7),
        ("Schulz", 6), ("Hoffmann", 7), ("Sch�fer", 7), ("Koch", 6),
        ("Bauer", 2), ("Richter", 4), ("Klein", 2), ("Schr�der", 1) ],
    "�talya" : [
        ("Rossi", 20), ("Russo", 19), ("Ferrari", 19), ("Esposito", 18),
        ("Bianchi", 16), ("Romano", 15), ("Colombo", 14), ("Ricci", 14),
        ("Marino", 12), ("Grecco", 11), ("Bruno", 10), ("Gallo", 12),
        ("Conti", 16), ("De Luca", 15), ("Costa", 14), ("Giordano", 13),
        ("Mancini", 14), ("Rizzo", 13), ("Lombardi", 11), ("Moretto", 9) ],
    "T�rkiye" : [
        ("�zt�rk", 25), ("Hast�rk", 19), ("G�kt�rk", 19), ("Yava�", 3),
        ("�zen", 14), ("F�rat", 13), ("K�l�k", 1), ("Eskici", 1) ] }

�lkelerinA��rl��� = [
    ("Almanya", 0.3),
    ("Fransa", 0.4),
    ("�svi�re", 0.1),
    ("�talya", 0.1),
    ("T�rkiye", 0.1)]

yard�mc�lar�nA��rl��� = [
    ("T�bbi Yard�m", 0.3),
    ("Bar�nma Yard�m�", 0.1),
    ("Beslenme Yard�m�", 0.2),
    ("Sosyal Yard�m", 0.1),
    ("Enkaz Kaz�c�", 0.3)]

bire�im = {}
for �lke in �lkeliAdlar:
    adlar, a��rl�klar� = zip (*�lkeliAdlar[�lke])
    a��rl�klarToplam� = sum (a��rl�klar�)
    adlar�nA��rl�klar� = [x / a��rl�klarToplam� for x in a��rl�klar�]
    �lkeliAdlar[�lke] = [adlar, adlar�nA��rl�klar�]
    soyadlar, a��rl�klar� = zip (*�lkeliSoyadlar[�lke])
    a��rl�klarToplam� = sum (a��rl�klar�)
    soyadlar�nA��rl�klar� = [x / a��rl�klarToplam� for x in a��rl�klar�]
    �lkeliSoyadlar[�lke] = [soyadlar, adlar�nA��rl�klar�]
    bire�im[�lke] = p381.bire�imci (
        (adlar, soyadlar),
        (adlar�nA��rl�klar�, soyadlar�nA��rl�klar�),
        bi�imlemeFonksiyonu=lambda x: " ".join (x),
        tekrarlanabilirSe�imMi=False)

try: say� = abs (int (input ("Ka� afetzade yard�mc�s� se�ilecek [10]? "))); print()
except: say� = 10

yard�mc�lar = []
kimlikNo = 1
for _ in range (say�):
    �lke = p381.a��rl�kl�Kar��l�kl�Se�im (zip (*�lkelerinA��rl���))
    yard�mKonusu = p381.a��rl�kl�Kar��l�kl�Se�im (zip (*yard�mc�lar�nA��rl���))
    �lke, yard�mKonusu = �lke[0], yard�mKonusu[0]
    yard�mc� = bire�im[�lke]()
    kn = "{kn:05d}".format (kn=kimlikNo)
    yard�mc�lar.append ( (kn, �lke, next (yard�mc�), yard�mKonusu) )
    kimlikNo += 1

print (yard�mc�lar); print()
for i in range (say�):
    for j in range (4): print (yard�mc�lar[i][j], end=", ")
    print()

if input ("\nG�n�ll�ler listesi disk dosyas�na yaz�ls�n m�? [e/h] ") == "e":
    with open ("p_30805x.txt", "w") as dosya:
        dosya.write ("Referans No, �lkesi, Ad ve Soyad�, G�revi\n")
        for g�n�ll� in yard�mc�lar: dosya.write (", ".join (g�n�ll�) + "\n")



"""��kt�:
>python p_30805.py
Ka� afetzade yard�mc�s� se�ilecek [10]? 2

[('00001', 'Almanya', 'Brigitte Richter', 'Enkaz Kaz�c�'), ('00002', 'Almanya', 'Ursula Wagner', 'Enkaz Kaz�c�')]

00001, Almanya, Brigitte Richter, Enkaz Kaz�c�,
00002, Almanya, Ursula Wagner, Enkaz Kaz�c�,

G�n�ll�ler listesi disk dosyas�na yaz�ls�n m�? [e/h]

>python p_30805.py  ** TEKRAR **
Ka� afetzade yard�mc�s� se�ilecek [10]?
[('00001', 'Fransa', 'Marie Petit', 'Bar�nma Yard�m�'), ('00002', 'T�rkiye', 'Hatice �zt�rk', 'Enkaz Kaz�c�'),
('00003', 'T�rkiye', 'Kezban �zen', 'T�bbi Yard�m'), ('00004', 'Almanya', 'Manfred Bauer', 'T�bbi Yard�m'),
('00005', '�svi�re', 'Daniel Meyer', 'T�bbi Yard�m'), ('00006', 'Fransa', 'Thomas Mercier', 'Beslenme Yard�m�'),
('00007', 'Almanya', 'Manfred Becker', 'Beslenme Yard�m�'), ('00008', 'T�rkiye', '�zcan F�rat', 'T�bbi Yard�m'),
('00009', 'T�rkiye', 'Mahmut G�kt�rk', 'T�bbi Yard�m'), ('00010', 'Fransa', 'Nicolas Nicolas', 'Enkaz Kaz�c�')]

00001, Fransa, Marie Petit, Bar�nma Yard�m�,
00002, T�rkiye, Hatice �zt�rk, Enkaz Kaz�c�,
00003, T�rkiye, Kezban �zen, T�bbi Yard�m,
00004, Almanya, Manfred Bauer, T�bbi Yard�m,
00005, �svi�re, Daniel Meyer, T�bbi Yard�m,
00006, Fransa, Thomas Mercier, Beslenme Yard�m�,
00007, Almanya, Manfred Becker, Beslenme Yard�m�,
00008, T�rkiye, �zcan F�rat, T�bbi Yard�m,
00009, T�rkiye, Mahmut G�kt�rk, T�bbi Yard�m,
00010, Fransa, Nicolas Nicolas, Enkaz Kaz�c�,
"""