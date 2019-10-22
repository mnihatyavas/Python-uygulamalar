# coding:iso-8859-9 Türkçe

liste = ["Ankara", "İstanbul", "İzmir", "Konya", "Bursa"]
try: liste += eval (input ("Listeye eklenecek kelimeler (tırnaklı,virgülle ayrık ve enaz 2 adet) girin: "))
except Exception:
    print (end="")
print ("Eklemeli dizge listemiz:", liste)
for i in range (len (liste)): liste[i] = liste[i][1:]
print ("İlk karakterleri kırpılmış listemiz:", liste)
print()
liste2=[]
alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
print ("Yeni ardışık uzayan alfabe elemanlı listemiz: [", end="")
for i in range (len (alfabe)):
    liste2.append (alfabe[i]*(i+1))
for k in liste2: print (k, "=", len (k), sep="", end= " ")
print ("]")
