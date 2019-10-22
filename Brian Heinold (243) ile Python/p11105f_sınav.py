# coding:iso-8859-9 Türkçe

# Liste matrissel boyutlu alt listeler [], tüpleler () veya (tüple değerli) sözlük {anahtar:(değer1...)} içerebilir...
L = [{"sayı":s, "takım":t} for t in ["sinek", "maça", "kupa", "karo"] for s in range (1, 14) ]
# Burada L, 2 adet anahtar-değer çiftli sözlük içeren 52 adet elementten oluşan bir listedir...
from pprint import pprint
print ("52 vanti'lik KARILMAMIŞ deste listesi:\n", "-"*38, sep="")
pprint (L)

from random import shuffle
shuffle (L)
print ("\n52 vanti'lik KARILMIŞ deste listesi:\n", "-"*36, sep="")
pprint (L)

while True:
 shuffle (L)
 kazandıL1 = kaybettiL1 = berabereL1 = kazandıL2 = kaybettiL2 = berabereL2 = 0
 for i in range (0, 48, 6):
    L1 = [L[j]["sayı"] for j in range (i, i+3)]
    L2 = [L[j]["sayı"] for j in range (i+3, i+6)]
    L1.sort(); L1.reverse()
    L2.sort(); L2.reverse()
    if L1[0] > L2[0]: kazandıL1 +=1; kaybettiL2 +=1; continue
    if L1[0] < L2[0]: kaybettiL1 +=1; kazandıL2 +=1; continue
    if L1[1] > L2[1]: kazandıL1 +=1; kaybettiL2 +=1; continue
    if L1[1] < L2[1]: kaybettiL1 +=1; kazandıL2 +=1; continue
    if L1[2] > L2[2]: kazandıL1 +=1; kaybettiL2 +=1; continue
    if L1[2] < L2[2]: kaybettiL1 +=1; kazandıL2 +=1; continue
    berabereL1 +=1; berabereL2 +=1
 if berabereL1 != 0: break # Özellikle enaz 1 beraberlik test edinceye dek oyunu tekrarlatalım...

print ("\n2 oyuncuya 3'er kart dağıtılıp, toplam 8 oyunun sonucunda:\n", "-"*63, sep="")
print ("Oyuncu-1:", kazandıL1, "kez kazandı", kaybettiL1, "kez kaybetti ve", berabereL1, "kez berabere kaldı.")
print ("Oyuncu-2:", kazandıL2, "kez kazandı", kaybettiL2, "kez kaybetti ve", berabereL2, "kez berabere kaldı.")

while input ("\nDevam[tuş-Ent], Çık[Ent]"):
    shuffle (L)
    if L[0]["takım"] == L[1]["takım"] == L[2]["takım"]: print ("==>Elinizde FLAŞ/renk var.")
    if L[0]["sayı"] == L[1]["sayı"] == L[2]["sayı"]: print ("==>Elinizde 3'lü var.")
    elif L[0]["sayı"] == L[1]["sayı"] or L[0]["sayı"] == L[2]["sayı"] or L[1]["sayı"] == L[2]["sayı"]: print ("==>Elinizde DÖPER var.")
    L1 = [L[0]["sayı"], L[1]["sayı"], L[2]["sayı"]]; L1.sort()
    if L1[0]+2 == L1[1]+1 == L1[2]: print ("==>Elinizde SIRA var.")

kere = 0
n = 10000
for i in range (n):
    shuffle (L)
    if L[0]["takım"] == L[1]["takım"] == L[2]["takım"] == L[3]["takım"] == L[4]["takım"]: kere +=1
print ("\n{:,d} oyunda {:,d} kere 5'li FLAŞ/renk buldunuz, yüzdesi: %{:.2f}" .format (n, kere, kere*100/n) )
