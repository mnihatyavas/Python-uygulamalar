# coding:iso-8859-9 Turkish

# M:1,000, D:500, C:100, L:50, X:10, V:5, I:1
# Farzedelim ki; B:5,000, F:10,000, G:50,000, H:100,000, J:500,000, K:1,000,000, N:5,000,000, P:10,000,000

print ("Roma rakamları: birler, onlar, yüzler, binler (ve faraza milyonlar) basamağı:\n", "-"*77, sep="")
L = [ ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
    ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
    ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCC", "CM"],
    ["", "M", "MM", "MMM", "MB", "B", "BM", "BMM", "BMMM", "MF"],
    ["", "F", "FF", "FFF", "FG", "G", "GF", "GFF", "GFFF", "FH"],
    ["", "H", "HH", "HHH", "HJ", "J", "JH", "JHH", "JHHH", "HK"],
    ["", "K", "KK", "KKK", "", "", "", "", "", ""] ]
from pprint import pprint
pprint (L)

from random import randint
sayı = 0
while not (0 < sayı < 4000000):
    try: sayı = abs (int (eval (input ("\n[1->3,999,999] arası bir tamsayı girin: "))))
    except Exception: sayı = randint (1, 3999999)

roma = ""
for i in range (len (str (sayı))):
    for j in range (10):
        if str (sayı)[len(str(sayı))-i-1] == str (j): roma = L[i] [j] + roma
print ("\n{:,d} = Roma rakamı-büyük: {:s}, ve küçük: {:s}" .format (sayı, roma, roma.lower()) )

# 1,073,662 = Roma rakamı-büyük: KGFFMMMDCLXII, ve küçük: kgffmmmdclxii
print()
L = [ {"VIII":8, "VII":7, "III":3, "II":2, "IV":4, "VI":6, "IX":9, "I":1, "V":5},
    {"LXXX":80, "LXX":70, "XXX":30, "XX":20, "XL":40, "LX":60, "XC":90, "X":10, "L":50},
    {"DCCC":800, "DCC":700, "CCC":300, "CC":200, "CD":400, "DC":600, "CM":900, "C":100, "D":500},
    {"BMMM":8000, "BMM":7000, "MMM":3000, "MM":2000, "MB":4000, "BM":6000, "MF":9000, "M":1000, "B":5000},
    {"GFFF":80000, "GFF":70000, "FFF":30000, "FF":20000, "FG":40000, "GF":60000, "FH":90000, "F":10000, "G":50000},
    {"JHHH":800000, "JHH":700000, "HHH":300000, "HH":200000, "HJ":400000, "JH":600000, "HK":900000, "H":100000, "J":500000},
    {"NKKK":8000000, "NKK":7000000, "KKK":3000000, "KK":2000000, "KN":4000000, "NK":6000000, "KP":9000000, "K":1000000, "N":5000000} ]

sayı = 0
roma1 = roma
while len (roma) > 0:
    for i in range (7):
        for j in range (9):
            for k in range (4, -1, -1):
                if roma[-k:] == list (L[i].keys())[j]:
                    sayı += list (L[i].values())[j]
                    roma = roma.replace (list (L[i].keys())[j], "")
                    break
print ("Tersi==> {} veya {} roma rakamı = {:,d}" .format (roma1, roma1.lower(), sayı))
