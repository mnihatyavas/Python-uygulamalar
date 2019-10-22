# coding:iso-8859-9 T�rk�e

# Liste matrissel boyutlu alt listeler [], t�pleler () veya (t�ple de�erli) s�zl�k {anahtar:(de�er1...)} i�erebilir...
L = [{"say�":s, "tak�m":t} for t in ["sinek", "ma�a", "kupa", "karo"] for s in range (1, 14) ]
# Burada L, 2 adet anahtar-de�er �iftli s�zl�k i�eren 52 adet elementten olu�an bir listedir...
from pprint import pprint
print ("52 vanti'lik KARILMAMI� deste listesi:\n", "-"*38, sep="")
pprint (L)

from random import shuffle
shuffle (L)
print ("\n52 vanti'lik KARILMI� deste listesi:\n", "-"*36, sep="")
pprint (L)

while True:
 shuffle (L)
 kazand�L1 = kaybettiL1 = berabereL1 = kazand�L2 = kaybettiL2 = berabereL2 = 0
 for i in range (0, 48, 6):
    L1 = [L[j]["say�"] for j in range (i, i+3)]
    L2 = [L[j]["say�"] for j in range (i+3, i+6)]
    L1.sort(); L1.reverse()
    L2.sort(); L2.reverse()
    if L1[0] > L2[0]: kazand�L1 +=1; kaybettiL2 +=1; continue
    if L1[0] < L2[0]: kaybettiL1 +=1; kazand�L2 +=1; continue
    if L1[1] > L2[1]: kazand�L1 +=1; kaybettiL2 +=1; continue
    if L1[1] < L2[1]: kaybettiL1 +=1; kazand�L2 +=1; continue
    if L1[2] > L2[2]: kazand�L1 +=1; kaybettiL2 +=1; continue
    if L1[2] < L2[2]: kaybettiL1 +=1; kazand�L2 +=1; continue
    berabereL1 +=1; berabereL2 +=1
 if berabereL1 != 0: break # �zellikle enaz 1 beraberlik test edinceye dek oyunu tekrarlatal�m...

print ("\n2 oyuncuya 3'er kart da��t�l�p, toplam 8 oyunun sonucunda:\n", "-"*63, sep="")
print ("Oyuncu-1:", kazand�L1, "kez kazand�", kaybettiL1, "kez kaybetti ve", berabereL1, "kez berabere kald�.")
print ("Oyuncu-2:", kazand�L2, "kez kazand�", kaybettiL2, "kez kaybetti ve", berabereL2, "kez berabere kald�.")

while input ("\nDevam[tu�-Ent], ��k[Ent]"):
    shuffle (L)
    if L[0]["tak�m"] == L[1]["tak�m"] == L[2]["tak�m"]: print ("==>Elinizde FLA�/renk var.")
    if L[0]["say�"] == L[1]["say�"] == L[2]["say�"]: print ("==>Elinizde 3'l� var.")
    elif L[0]["say�"] == L[1]["say�"] or L[0]["say�"] == L[2]["say�"] or L[1]["say�"] == L[2]["say�"]: print ("==>Elinizde D�PER var.")
    L1 = [L[0]["say�"], L[1]["say�"], L[2]["say�"]]; L1.sort()
    if L1[0]+2 == L1[1]+1 == L1[2]: print ("==>Elinizde SIRA var.")

kere = 0
n = 10000
for i in range (n):
    shuffle (L)
    if L[0]["tak�m"] == L[1]["tak�m"] == L[2]["tak�m"] == L[3]["tak�m"] == L[4]["tak�m"]: kere +=1
print ("\n{:,d} oyunda {:,d} kere 5'li FLA�/renk buldunuz, y�zdesi: %{:.2f}" .format (n, kere, kere*100/n) )
