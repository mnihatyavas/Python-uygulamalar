# coding:iso-8859-9 T�rk�e

liste = ["Ankara", "�stanbul", "�zmir", "Konya", "Bursa"]
try: liste += eval (input ("Listeye eklenecek kelimeler (t�rnakl�,virg�lle ayr�k ve enaz 2 adet) girin: "))
except Exception:
    print (end="")
print ("Eklemeli dizge listemiz:", liste)
for i in range (len (liste)): liste[i] = liste[i][1:]
print ("�lk karakterleri k�rp�lm�� listemiz:", liste)
print()
liste2=[]
alfabe = "abc�defg�h�ijklmno�prs�tu�vyz"
print ("Yeni ard���k uzayan alfabe elemanl� listemiz: [", end="")
for i in range (len (alfabe)):
    liste2.append (alfabe[i]*(i+1))
for k in liste2: print (k, "=", len (k), sep="", end= " ")
print ("]")
