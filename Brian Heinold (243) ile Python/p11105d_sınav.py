# coding:iso-8859-9 T�rk�e

from random import randint
say� = 0
while not (10 <= say� <= 50):
    try: say� = int (eval (input ("Tak�m say�s�n� [10->50] girin: ")))
    except Exception: say� = randint (10, 50)

S = {}
for i in range (say�):
    kazand� = randint (0, 10)
    kaybetti = randint (0, (10-kazand�))
    berabere = 10 - (kazand� + kaybetti)
    S["Tak�m" + str (i+1)] = (kazand�, kaybetti, berabere)

print ("\nTak�m ad� Kazand� Kaybetti Berabere\n", "-"*35, sep="")
for k in S.items(): print ("{:10s} {}" .format (k[0], k[1]) )

print ("\nTak�m ad� Kazand� Kaybetti Berabere\n", "-"*35, sep="")
for k in S.items(): print ("{:7s} {:6d} {:8d} {:8d}" .format (k[0], k[1][0], k[1][1], k[1][2]) )

print ("\nTak�m ad� Ba�ar� %'si\n", "-"*21, sep="")
for k in S.items(): print ("{:12s} {:5.1f}" .format (k[0], k[1][0]*100/10) )

tak�m = ""
while tak�m != "q":
    tak�m = input ("\nSonu�lar�n� g�rmek istedi�iniz tak�m ad�n� girin [��k: q]: ")
    if tak�m == "q": break
    elif tak�m not in S: continue
    print ("\nTak�m ad� Kazand� Kaybetti Berabere Ba�ar� %'si\n", "-"*47, sep="")
    print ("{:7s} {:6d} {:8d} {:8d} {:10.1f}" .format (tak�m, S[tak�m][0], S[tak�m][1], S[tak�m][2], S[tak�m][0]*100/10) )
