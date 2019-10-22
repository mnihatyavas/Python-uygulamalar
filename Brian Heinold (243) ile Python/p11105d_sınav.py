# coding:iso-8859-9 Türkçe

from random import randint
sayı = 0
while not (10 <= sayı <= 50):
    try: sayı = int (eval (input ("Takım sayısını [10->50] girin: ")))
    except Exception: sayı = randint (10, 50)

S = {}
for i in range (sayı):
    kazandı = randint (0, 10)
    kaybetti = randint (0, (10-kazandı))
    berabere = 10 - (kazandı + kaybetti)
    S["Takım" + str (i+1)] = (kazandı, kaybetti, berabere)

print ("\nTakım adı Kazandı Kaybetti Berabere\n", "-"*35, sep="")
for k in S.items(): print ("{:10s} {}" .format (k[0], k[1]) )

print ("\nTakım adı Kazandı Kaybetti Berabere\n", "-"*35, sep="")
for k in S.items(): print ("{:7s} {:6d} {:8d} {:8d}" .format (k[0], k[1][0], k[1][1], k[1][2]) )

print ("\nTakım adı Başarı %'si\n", "-"*21, sep="")
for k in S.items(): print ("{:12s} {:5.1f}" .format (k[0], k[1][0]*100/10) )

takım = ""
while takım != "q":
    takım = input ("\nSonuçlarını görmek istediğiniz takım adını girin [Çık: q]: ")
    if takım == "q": break
    elif takım not in S: continue
    print ("\nTakım adı Kazandı Kaybetti Berabere Başarı %'si\n", "-"*47, sep="")
    print ("{:7s} {:6d} {:8d} {:8d} {:10.1f}" .format (takım, S[takım][0], S[takım][1], S[takım][2], S[takım][0]*100/10) )
