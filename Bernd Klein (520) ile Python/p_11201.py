# coding:iso-8859-9 T�rk�e
# p_11201.py: 11 ayr� Alis kitab�ndaki ortak, farkl�, s�k kullan�lan vb kelimelerin tesbiti �rne�i.

import re

# Toplam 11 kitap kelimeleri (k���k harf) kar��la�t�r�lacak...
kitap11 = open ("metin/Kitap11.html").read().lower()
kelimeler = re.findall (r"\b[\w-]+\b", kitap11)
print ("'Alis Harikalar Diyar�nda' roman serisinin 11.kitab�ndaki kelime toplam�:", len (kelimeler) )

print ("\nKitap11'deki baz� kelimelerin tekrarlanma say�lar�:\n", "-"*50, sep="")
for kelime in ["a", "the", "while", "good", "bad", "nice", "rabbit", "it"]:
    print ("  ==>", kelime, kelimeler.count (kelime), "kez tekrarlanmaktad�r!")
#------------------------------------------------------------------------------------------------------

farkl�Kelimeler = set (kelimeler)
print ("\n'Alis Kitap-11'in i�erdi�i farkl� kelimelerin say�s�: " + str (len (farkl�Kelimeler)) )

print ("\nAlis'in toplam 11 kitab�ndaki farkl� kelimelerin say�s�:\n", "-"*56, sep="")
kitaplar = ['Kitap1.html', 'Kitap2.html', 'Kitap3.html', 'Kitap4.html', 'Kitap5.html',
    'Kitap6.html', 'Kitap7.html', 'Kitap8.html', 'Kitap9.html', 'Kitap10.html', "Kitap11.html"]
for kitap in kitaplar:
    metin = open ("metin/" + kitap).read().lower()
    kelimeler = re.findall (r"\b[\w-]+\b", metin)
    farkl�Kelimeler = set (kelimeler)
    print ("   ==>Alis-{ad:8s}: {uz:4d}" .format (ad=kitap[:-5], uz=len (farkl�Kelimeler)) )
#------------------------------------------------------------------------------------------------------

kitaptakiKelimeler = {}
for kitap in kitaplar:
    metin = open ("metin/" + kitap).read().lower()
    kelimeler = re.findall (r"\b[\w-]+\b", metin)
    kitaptakiKelimeler [kitap] = kelimeler

kitap11Kelimeleri = set (kitaptakiKelimeler ['Kitap11.html'])
kitaplar.remove ('Kitap11.html')
for kitap in kitaplar: kitap11Kelimeleri -= set (kitaptakiKelimeler [kitap] )

with open ("kitap11.txt", "w") as dsy:
    metin = " ".join (kitap11Kelimeleri)
    dsy.write (metin)

print ("\nAlis'in sadece Kitap-11'de bulunan �zel kelimelerin say�s�:", len (kitap11Kelimeleri) )
print (" ->�sterseniz bu kelimelerin listesini 'kitap11.txt' dosyas�nda g�rebilirsiniz.")
#------------------------------------------------------------------------------------------------------

ortakKelimeler = set (kitaptakiKelimeler ['Kitap11.html'])
for kitap in kitaplar: ortakKelimeler &= set (kitaptakiKelimeler [kitap])
with open ("kitap11.txt", "a") as dsy:
    metin = "\n\n" + " ".join (ortakKelimeler)
    dsy.write (metin)
print ("\nT�m kitaplardaki ortak kelimelerin say�s�:", len (ortakKelimeler) )
print (" ->Bu kelimelerin listesi de 'kitap11.txt' dosyas�ndan g�r�lebilir.")
#------------------------------------------------------------------------------------------------------
"""
def kontroll�Oku (ad):
    ba�l�k = re.compile(r" ?<head><title>CHAPTER")
    sonluk = re.compile(r" ?</body></html>")
    dizge = open ("metin/" + ad).read().lower()
    ilk = ba�l�k.search (dizge)
    son = sonluk.search (dizge)
    return dizge [ilk:son]

kitaptakiKelimeler = {}
for kitap in kitaplar + ['Kitap11.html']:
    metin = kontroll�Oku (kitap)
    kelimeler = re.findall (r"\b[\w-]+\b", metin)
    kitaptakiKelimeler [kitap] = kelimeler
kitap11Kelimeleri = set (kitaptakiKelimeler ['Kitap11.html'])
for kitap in kitaplar: kitap11Kelimeleri -= set (kitaptakiKelimeler [kitap] )
with open ("kitap11.txt", "a") as d:
    metin = "\n\n" + " ".join (kitap11Kelimeleri)
    d.write (metin)
print ("\nBa�l�k ve sonluk hari� Alis-Kitap11 �zel kelimeleri:", len (kitap11Kelimeleri) )
"""

print ("\nAlis kitaplar�ndaki ortak kelimelerin ilk 30 adedini inceleyelim:\n", "-"*65, sep="")
saya� = 0
for kelime in ortakKelimeler:
    print (kelime, end=", ")
    saya� += 1
    if saya� == 30: break


"""��kt�:
>python p_11201.py
'Alis Harikalar Diyar�nda' roman serisinin 11.kitab�ndaki kelime toplam�: 4495

Kitap11'deki baz� kelimelerin tekrarlanma say�lar�:
--------------------------------------------------
  ==> a 71 kez tekrarlanmaktad�r!
  ==> the 347 kez tekrarlanmaktad�r!
  ==> while 2 kez tekrarlanmaktad�r!
  ==> good 3 kez tekrarlanmaktad�r!
  ==> bad 0 kez tekrarlanmaktad�r!
  ==> nice 1 kez tekrarlanmaktad�r!
  ==> rabbit 16 kez tekrarlanmaktad�r!
  ==> it 65 kez tekrarlanmaktad�r!

'Alis Kitap-11'in i�erdi�i farkl� kelimelerin say�s�: 906

Alis'in toplam 11 kitab�ndaki farkl� kelimelerin say�s�:
--------------------------------------------------------
   ==>Alis-Kitap1  :  616
   ==>Alis-Kitap2  :  625
   ==>Alis-Kitap3  :  560
   ==>Alis-Kitap4  :  712
   ==>Alis-Kitap5  :  618
   ==>Alis-Kitap6  :  678
   ==>Alis-Kitap7  :  604
   ==>Alis-Kitap8  :  642
   ==>Alis-Kitap9  :  633
   ==>Alis-Kitap10 :  544
   ==>Alis-Kitap11 :  906

Alis'in sadece Kitap-11'de bulunan �zel kelimelerin say�s�: 252
 ->�sterseniz bu kelimelerin listesini 'kitap11.txt' dosyas�nda g�rebilirsiniz.

T�m kitaplardaki ortak kelimelerin say�s�: 118
 ->Bu kelimelerin listesi de 'kitap11.txt' dosyas�ndan g�r�lebilir.

Alis kitaplar�ndaki ortak kelimelerin ilk 30 adedini inceleyelim:
-----------------------------------------------------------------
first, it, its, be, h2, your, h1, all, so, have, go, who, thing, p, been, way, a
re, on, now, did, was, down, only, any, an, herself, looked, say, must, chapter,
"""