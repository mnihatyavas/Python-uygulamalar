# coding:iso-8859-9 T�rk�e
# p_41501.py: Mastermind usta'k�l �oklu renk dizilimini tahmin oyunu �rne�i.

from tkinter import *
from p_21601x import t�mRenkler
from p_315 import Renk

def tekrarDene():
    global se�iliRenkGrubu
    sonu� = yeniDe�erleme (se�iliRenkGrubu)
    se�iliRenkGrubu = sonu� [0]

def yeniDe�erleme (se�iliRenkGrubu):
    global kere
    kere +=1
    isabet, yak�ns� = de�erlemeyiAl()
    if isabet == renkSay�s� and yak�ns� == 0:
        print ("\n=====>", kere,"kerede B�LD�M: ��k")
        etiket.config (text="Aferin sana, [" + str (kere) + "] kerede bildin!..", bg=Renk.renk(), fg=Renk.renk() )
        from tkinter.messagebox import showwarning; showwarning ("B�LD�N�Z", "��kmak i�in t�klay�n...")
        import sys; sys.exit (0)
    if not verilerDo�ruMu ((isabet, yak�ns�)):
        print ("\n==>Veri Giri� Hatas�: Girdi�iniz veriler tutars�z, tekrar deneyin!")
        return (se�iliRenkGrubu, (-1, yak�ns�) )
    tahminler.append ((se�iliRenkGrubu, (isabet, yak�ns�)))
    se�iliRenkGrubu = yeniTahminYap() 
    yeniTahminiG�ster (se�iliRenkGrubu)
    tahminleriG�ster()
    if not se�iliRenkGrubu: return (se�iliRenkGrubu, (-1, yak�ns�))
    return (se�iliRenkGrubu, (isabet, yak�ns�))

def de�erlemeyiAl():
    isabet = abs (int (isabetGiri�i.get() ))
    yak�ns� = abs (int (yak�ns�Giri�i.get() ))
    return (isabet, yak�ns�)

def verilerDo�ruMu (a):
    (isabet, yak�ns�) = a
    if ((isabet + yak�ns�) > renkSay�s�) or ((isabet + yak�ns�) < (len (renkler�NG) - renkSay�s�) ): return False
    if isabet == 4 and yak�ns� == 1: return False
    return True

def tahminleriG�ster():
     sat�r = 3
     Label (k�k, text="�nceki Tahminler").grid (row=sat�r, column=0, columnspan = renkSay�s�)
     Label (k�k, text="�sabet").grid (row=sat�r, padx=5, column=renkSay�s�+1)
     Label (k�k, text="Yak�ns�").grid (row=sat�r, padx=5, column=renkSay�s�+2)
     print ("\n�nceki tahminler:")
     for tahmin in tahminler:
        tahminiRenkler = tahmin [0]
        kolon = 0
        sat�r += 1
        print (" ==>", end="")
        for r in tahminiRenkler:
            for i in range (len (renkler�NG)):
                if tahminiRenkler [kolon] == renkler�NG [i]:
                    print (renklerTR [i], end=" ")
                    break
            etiket = Label (k�k, text="    ", bg=tahminiRenkler [kolon])
            etiket.grid (row=sat�r, column=kolon,  sticky=W, padx=2)
            kolon += 1
        for i in (0,1):
            print (tahmin [1] [i], end=" ")
            etiket = Label (k�k, text=str (tahmin [1] [i]))
            etiket.grid (row=sat�r, column=kolon+i+1, padx=2)
        print()

def yeniTahminYap():
    yeniTahmin = next (renkGruplar�) 
    while �ncekilerleTutars�zM� (yeniTahmin, tahminler):
        try: yeniTahmin = next (renkGruplar�)
        except StopIteration:
            print ("Hata: Son (isbt,ykns) verileriniz �ncekilerle uyu�muyor, tekrar deneyin!")
            return ()
    return yeniTahmin

def �ncekilerleTutars�zM� (yeni, tahminler):
    for tahmin in tahminler:
        sonu� = kontrol (tahmin [0], yeni)
        (isabet, yak�ns�) = tahmin [1]
        if sonu� != [isabet, yak�ns�]: return True # �ncekilerle tutars�z...
    return False # �ncekilerle tutarl�...

def kontrol (t1, t2):
    ykn = 0
    isb = 0
    for i in range (len (t1)):
        if t1 [i] == t2 [i]: ykn += 1
        else:
            if t1 [i] in t2: isb += 1
    return [ykn, isb] 

def yeniTahminiG�ster (yeniTahmin):
    sat�r = 1 
    Label (k�k, text="   Yeni Tahmin:   ").grid (row=sat�r, column=0, columnspan=renkSay�s�)
    sat�r +=1
    kolon = 0
    print ("\nYeni tahmin:", end=" ")
    for r in yeniTahmin:
        for i in range (len (renkler�NG)):
            if r == renkler�NG [i]:
                print (renklerTR [i], end=" ")
                break
        etiket = Label (k�k, text="    ", bg=r)
        etiket.grid (row=sat�r, column=kolon,  sticky=W, padx=2)
        kolon += 1


if __name__ == "__main__":
    renkler�NG = ["red", "green", "blue", "yellow", "orange", "pink", "gray"]
    renklerTR = ["k�rm�z�", "ye�il", "mavi", "sar�", "turuncu", "pembe", "gri"]
    kere = 0
    tahminler = []				
    renkSay�s� = 5
    renkGruplar� = t�mRenkler (renkler�NG, renkSay�s�)
    se�iliRenkGrubu = next (renkGruplar�)
    yeniTahmin = (se�iliRenkGrubu, (0,0))

    sat�rSayac� = 1
    k�k = Tk()
    k�k.title ("S�perzeka")
    #k�k.geometry ("400x200+10+10") # "en x boy + padx + pady"
    #k�k.config (bg=Renk.renk())
    k�k ["padx"] = 10
    k�k ["pady"] = 10   

    verigiri�Etiketi = Label (k�k)
    verigiri�Etiketi ["text"] = "�sabet adedini gir:"
    verigiri�Etiketi.grid (row=sat�rSayac�, sticky=E, padx=5, column=renkSay�s�+4)
    isabetGiri�i = Entry (k�k)
    isabetGiri�i ["width"] = 3
    isabetGiri�i.grid (row=sat�rSayac�, column=renkSay�s�+5)

    verigiri�Etiketi = Label (k�k)
    verigiri�Etiketi ["text"] = "Yak�ns� adedini gir:"
    verigiri�Etiketi.grid (row=sat�rSayac�+1, sticky=E, padx=5, column=renkSay�s�+4)
    yak�ns�Giri�i = Entry (k�k)
    yak�ns�Giri�i ["width"] = 3
    yak�ns�Giri�i.grid (row=sat�rSayac�+1, column=renkSay�s�+5)

    g�nderD��mesi = Button (k�k, text="G�nder", command=tekrarDene)
    g�nderD��mesi.grid (row=0, column=renkSay�s�+4)

    ��kD��mesi = Button (k�k, text="�IK", command=k�k.quit)
    ��kD��mesi.grid (row=0, column=renkSay�s�+5)

    etiket = Label (k�k, font=("segoe script", 16, "bold", "italic") )
    etiket.grid (row=sat�rSayac�+2, column=renkSay�s�+4, rowspan=2, columnspan=2)

    yeniTahminiG�ster (se�iliRenkGrubu)

    k�k.mainloop()