# coding:iso-8859-9 Türkçe
# p_41501.py: Mastermind usta'kıl çoklu renk dizilimini tahmin oyunu örneği.

from tkinter import *
from p_21601x import tümRenkler
from p_315 import Renk

def tekrarDene():
    global seçiliRenkGrubu
    sonuç = yeniDeğerleme (seçiliRenkGrubu)
    seçiliRenkGrubu = sonuç [0]

def yeniDeğerleme (seçiliRenkGrubu):
    global kere
    kere +=1
    isabet, yakınsı = değerlemeyiAl()
    if isabet == renkSayısı and yakınsı == 0:
        print ("\n=====>", kere,"kerede BİLDİM: Çık")
        etiket.config (text="Aferin sana, [" + str (kere) + "] kerede bildin!..", bg=Renk.renk(), fg=Renk.renk() )
        from tkinter.messagebox import showwarning; showwarning ("BİLDİNİZ", "Çıkmak için tıklayın...")
        import sys; sys.exit (0)
    if not verilerDoğruMu ((isabet, yakınsı)):
        print ("\n==>Veri Giriş Hatası: Girdiğiniz veriler tutarsız, tekrar deneyin!")
        return (seçiliRenkGrubu, (-1, yakınsı) )
    tahminler.append ((seçiliRenkGrubu, (isabet, yakınsı)))
    seçiliRenkGrubu = yeniTahminYap() 
    yeniTahminiGöster (seçiliRenkGrubu)
    tahminleriGöster()
    if not seçiliRenkGrubu: return (seçiliRenkGrubu, (-1, yakınsı))
    return (seçiliRenkGrubu, (isabet, yakınsı))

def değerlemeyiAl():
    isabet = abs (int (isabetGirişi.get() ))
    yakınsı = abs (int (yakınsıGirişi.get() ))
    return (isabet, yakınsı)

def verilerDoğruMu (a):
    (isabet, yakınsı) = a
    if ((isabet + yakınsı) > renkSayısı) or ((isabet + yakınsı) < (len (renklerİNG) - renkSayısı) ): return False
    if isabet == 4 and yakınsı == 1: return False
    return True

def tahminleriGöster():
     satır = 3
     Label (kök, text="Önceki Tahminler").grid (row=satır, column=0, columnspan = renkSayısı)
     Label (kök, text="İsabet").grid (row=satır, padx=5, column=renkSayısı+1)
     Label (kök, text="Yakınsı").grid (row=satır, padx=5, column=renkSayısı+2)
     print ("\nÖnceki tahminler:")
     for tahmin in tahminler:
        tahminiRenkler = tahmin [0]
        kolon = 0
        satır += 1
        print (" ==>", end="")
        for r in tahminiRenkler:
            for i in range (len (renklerİNG)):
                if tahminiRenkler [kolon] == renklerİNG [i]:
                    print (renklerTR [i], end=" ")
                    break
            etiket = Label (kök, text="    ", bg=tahminiRenkler [kolon])
            etiket.grid (row=satır, column=kolon,  sticky=W, padx=2)
            kolon += 1
        for i in (0,1):
            print (tahmin [1] [i], end=" ")
            etiket = Label (kök, text=str (tahmin [1] [i]))
            etiket.grid (row=satır, column=kolon+i+1, padx=2)
        print()

def yeniTahminYap():
    yeniTahmin = next (renkGrupları) 
    while öncekilerleTutarsızMı (yeniTahmin, tahminler):
        try: yeniTahmin = next (renkGrupları)
        except StopIteration:
            print ("Hata: Son (isbt,ykns) verileriniz öncekilerle uyuşmuyor, tekrar deneyin!")
            return ()
    return yeniTahmin

def öncekilerleTutarsızMı (yeni, tahminler):
    for tahmin in tahminler:
        sonuç = kontrol (tahmin [0], yeni)
        (isabet, yakınsı) = tahmin [1]
        if sonuç != [isabet, yakınsı]: return True # öncekilerle tutarsız...
    return False # öncekilerle tutarlı...

def kontrol (t1, t2):
    ykn = 0
    isb = 0
    for i in range (len (t1)):
        if t1 [i] == t2 [i]: ykn += 1
        else:
            if t1 [i] in t2: isb += 1
    return [ykn, isb] 

def yeniTahminiGöster (yeniTahmin):
    satır = 1 
    Label (kök, text="   Yeni Tahmin:   ").grid (row=satır, column=0, columnspan=renkSayısı)
    satır +=1
    kolon = 0
    print ("\nYeni tahmin:", end=" ")
    for r in yeniTahmin:
        for i in range (len (renklerİNG)):
            if r == renklerİNG [i]:
                print (renklerTR [i], end=" ")
                break
        etiket = Label (kök, text="    ", bg=r)
        etiket.grid (row=satır, column=kolon,  sticky=W, padx=2)
        kolon += 1


if __name__ == "__main__":
    renklerİNG = ["red", "green", "blue", "yellow", "orange", "pink", "gray"]
    renklerTR = ["kırmızı", "yeşil", "mavi", "sarı", "turuncu", "pembe", "gri"]
    kere = 0
    tahminler = []				
    renkSayısı = 5
    renkGrupları = tümRenkler (renklerİNG, renkSayısı)
    seçiliRenkGrubu = next (renkGrupları)
    yeniTahmin = (seçiliRenkGrubu, (0,0))

    satırSayacı = 1
    kök = Tk()
    kök.title ("Süperzeka")
    #kök.geometry ("400x200+10+10") # "en x boy + padx + pady"
    #kök.config (bg=Renk.renk())
    kök ["padx"] = 10
    kök ["pady"] = 10   

    verigirişEtiketi = Label (kök)
    verigirişEtiketi ["text"] = "İsabet adedini gir:"
    verigirişEtiketi.grid (row=satırSayacı, sticky=E, padx=5, column=renkSayısı+4)
    isabetGirişi = Entry (kök)
    isabetGirişi ["width"] = 3
    isabetGirişi.grid (row=satırSayacı, column=renkSayısı+5)

    verigirişEtiketi = Label (kök)
    verigirişEtiketi ["text"] = "Yakınsı adedini gir:"
    verigirişEtiketi.grid (row=satırSayacı+1, sticky=E, padx=5, column=renkSayısı+4)
    yakınsıGirişi = Entry (kök)
    yakınsıGirişi ["width"] = 3
    yakınsıGirişi.grid (row=satırSayacı+1, column=renkSayısı+5)

    gönderDüğmesi = Button (kök, text="Gönder", command=tekrarDene)
    gönderDüğmesi.grid (row=0, column=renkSayısı+4)

    çıkDüğmesi = Button (kök, text="ÇIK", command=kök.quit)
    çıkDüğmesi.grid (row=0, column=renkSayısı+5)

    etiket = Label (kök, font=("segoe script", 16, "bold", "italic") )
    etiket.grid (row=satırSayacı+2, column=renkSayısı+4, rowspan=2, columnspan=2)

    yeniTahminiGöster (seçiliRenkGrubu)

    kök.mainloop()