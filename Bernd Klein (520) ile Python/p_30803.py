# coding:iso-8859-9 T�rk�e
# p_30803.py: A��rl�kl� kar��l�kl� se�ilen yegane elemanlar�n bi�imli d�k�m� �rne�i.

from p_30801 import kar��l�kl�Se�im as ks, a��rl�kl�Kar��l�kl�Se�im as aks

def bire�imci (veriler, a��rl�klar�=None, bi�imlemeFonksiyonu=None, tekrarlanabilirSe�imMi=True):
    def tercih (veriler, a��rl�klar�):
        if a��rl�klar�: return aks (*zip (veriler, a��rl�klar�))
        else: return ks (*veriler)

    def bire�imle():
        if not tekrarlanabilirSe�imMi: belle = set()
        while True:
            yeniSe�ilen = tercih (veriler, a��rl�klar�)
            if not tekrarlanabilirSe�imMi:
                se�ilen = str (yeniSe�ilen)
                while se�ilen in belle:
                    yeniSe�ilen = tercih (veriler, a��rl�klar�)
                    se�ilen = str (yeniSe�ilen)
                belle.add (se�ilen)
            if bi�imlemeFonksiyonu: yield bi�imlemeFonksiyonu (yeniSe�ilen)
            else: yield yeniSe�ilen
    return bire�imle


a��rl�kl�Adlar = [("Hatice", 60), ("S�heyla", 12) , ("Zeliha", 8), ("Nihat", 35), ("Song�l", 37), ("Nedim", 29), ("Sevim", 45),
    ("Nur", 7), ("Y�cel", 19), ("Serap", 52), ("Sema", 45), ("Fatih", 48), ("Selda", 37), ("Canan", 17), ("Zafer", 25), ("Belk�s", 8),
    ("Hilal", 33), ("Atilla", 42)]

a��rl�kl�Soyadlar = [("Yava�", 15), ("K���kbay", 7), ("Ka�ar", 4), ("Candan", 37), ("�zbay", 43), ("G�kt�rk", 49),
    ("Eskici", 3), ("Aydan", 19), ("�iller", 23), ("Ak�ener", 17), ("�i�ek", 72), ("�zt�rk", 95), ("Amanat", 3), ("Hast�rk", 71),
    ("K�l�k", 12), ("F�rat", 47), ("Havlucu", 34), ("�zen", 51)] # Liste uzunluklar� ayn� olmak zorunda de�il...

adlar, a��rl�klar� = zip (*a��rl�kl�Adlar)
a��rl�kToplam� = sum (a��rl�klar�)
adlar�nA��rl�klar� = [x / a��rl�kToplam� for x in a��rl�klar�]
soyadlar, a��rl�klar� = zip (*a��rl�kl�Soyadlar)
a��rl�kToplam� = sum (a��rl�klar�)
soyadlar�nA��rl�klar� = [x / a��rl�kToplam� for x in a��rl�klar�]
a��rl�klar� = (adlar�nA��rl�klar�, soyadlar�nA��rl�klar�)

eleman = bire�imci (
    (adlar, soyadlar),
    a��rl�klar� = a��rl�klar�,
    bi�imlemeFonksiyonu=lambda x: " ".join (x),
    tekrarlanabilirSe�imMi=False)
eleman = eleman()

try: say� = abs (int (input ("Ka� eleman se�ilecek [15]? ")))
except: say� = 15

print ("\nA��rl�kl� kar��l�kl� se�ilen yegane ", say�, " eleman listesi:", "\n", "-"*54, sep="")
for _ in range (say�): print ((_+1), ": ", next (eleman), sep="")



"""��kt�:
>python p_30803.py
Ka� eleman se�ilecek [15]?

A��rl�kl� kar��l�kl� se�ilen yegane 15 eleman listesi:
------------------------------------------------------
1: Canan Candan
2: Hatice �iller
3: Hatice �zt�rk
4: Hatice Candan
5: Sevim Hast�rk
6: Selda �i�ek
7: Nihat �i�ek
8: S�heyla Yava�
9: Song�l �zt�rk
10: Hilal �zt�rk
11: Zeliha Hast�rk
12: Serap �zt�rk
13: Hatice �zbay
14: Serap �i�ek
15: Atilla Havlucu

>python p_30803.py  ** TEKRAR **
Ka� eleman se�ilecek [15]? 2

A��rl�kl� kar��l�kl� se�ilen yegane 2 eleman listesi:
------------------------------------------------------
1: Hilal �zen
2: Atilla Hast�rk
"""