# coding:iso-8859-9 Türkçe
# p_11201.py: 11 ayrı Alis kitabındaki ortak, farklı, sık kullanılan vb kelimelerin tesbiti örneği.

import re

# Toplam 11 kitap kelimeleri (küçük harf) karşılaştırılacak...
kitap11 = open ("metin/Kitap11.html").read().lower()
kelimeler = re.findall (r"\b[\w-]+\b", kitap11)
print ("'Alis Harikalar Diyarında' roman serisinin 11.kitabındaki kelime toplamı:", len (kelimeler) )

print ("\nKitap11'deki bazı kelimelerin tekrarlanma sayıları:\n", "-"*50, sep="")
for kelime in ["a", "the", "while", "good", "bad", "nice", "rabbit", "it"]:
    print ("  ==>", kelime, kelimeler.count (kelime), "kez tekrarlanmaktadır!")
#------------------------------------------------------------------------------------------------------

farklıKelimeler = set (kelimeler)
print ("\n'Alis Kitap-11'in içerdiği farklı kelimelerin sayısı: " + str (len (farklıKelimeler)) )

print ("\nAlis'in toplam 11 kitabındaki farklı kelimelerin sayısı:\n", "-"*56, sep="")
kitaplar = ['Kitap1.html', 'Kitap2.html', 'Kitap3.html', 'Kitap4.html', 'Kitap5.html',
    'Kitap6.html', 'Kitap7.html', 'Kitap8.html', 'Kitap9.html', 'Kitap10.html', "Kitap11.html"]
for kitap in kitaplar:
    metin = open ("metin/" + kitap).read().lower()
    kelimeler = re.findall (r"\b[\w-]+\b", metin)
    farklıKelimeler = set (kelimeler)
    print ("   ==>Alis-{ad:8s}: {uz:4d}" .format (ad=kitap[:-5], uz=len (farklıKelimeler)) )
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

print ("\nAlis'in sadece Kitap-11'de bulunan özel kelimelerin sayısı:", len (kitap11Kelimeleri) )
print (" ->İsterseniz bu kelimelerin listesini 'kitap11.txt' dosyasında görebilirsiniz.")
#------------------------------------------------------------------------------------------------------

ortakKelimeler = set (kitaptakiKelimeler ['Kitap11.html'])
for kitap in kitaplar: ortakKelimeler &= set (kitaptakiKelimeler [kitap])
with open ("kitap11.txt", "a") as dsy:
    metin = "\n\n" + " ".join (ortakKelimeler)
    dsy.write (metin)
print ("\nTüm kitaplardaki ortak kelimelerin sayısı:", len (ortakKelimeler) )
print (" ->Bu kelimelerin listesi de 'kitap11.txt' dosyasından görülebilir.")
#------------------------------------------------------------------------------------------------------
"""
def kontrollüOku (ad):
    başlık = re.compile(r" ?<head><title>CHAPTER")
    sonluk = re.compile(r" ?</body></html>")
    dizge = open ("metin/" + ad).read().lower()
    ilk = başlık.search (dizge)
    son = sonluk.search (dizge)
    return dizge [ilk:son]

kitaptakiKelimeler = {}
for kitap in kitaplar + ['Kitap11.html']:
    metin = kontrollüOku (kitap)
    kelimeler = re.findall (r"\b[\w-]+\b", metin)
    kitaptakiKelimeler [kitap] = kelimeler
kitap11Kelimeleri = set (kitaptakiKelimeler ['Kitap11.html'])
for kitap in kitaplar: kitap11Kelimeleri -= set (kitaptakiKelimeler [kitap] )
with open ("kitap11.txt", "a") as d:
    metin = "\n\n" + " ".join (kitap11Kelimeleri)
    d.write (metin)
print ("\nBaşlık ve sonluk hariç Alis-Kitap11 özel kelimeleri:", len (kitap11Kelimeleri) )
"""

print ("\nAlis kitaplarındaki ortak kelimelerin ilk 30 adedini inceleyelim:\n", "-"*65, sep="")
sayaç = 0
for kelime in ortakKelimeler:
    print (kelime, end=", ")
    sayaç += 1
    if sayaç == 30: break


"""Çıktı:
>python p_11201.py
'Alis Harikalar Diyarında' roman serisinin 11.kitabındaki kelime toplamı: 4495

Kitap11'deki bazı kelimelerin tekrarlanma sayıları:
--------------------------------------------------
  ==> a 71 kez tekrarlanmaktadır!
  ==> the 347 kez tekrarlanmaktadır!
  ==> while 2 kez tekrarlanmaktadır!
  ==> good 3 kez tekrarlanmaktadır!
  ==> bad 0 kez tekrarlanmaktadır!
  ==> nice 1 kez tekrarlanmaktadır!
  ==> rabbit 16 kez tekrarlanmaktadır!
  ==> it 65 kez tekrarlanmaktadır!

'Alis Kitap-11'in içerdiği farklı kelimelerin sayısı: 906

Alis'in toplam 11 kitabındaki farklı kelimelerin sayısı:
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

Alis'in sadece Kitap-11'de bulunan özel kelimelerin sayısı: 252
 ->İsterseniz bu kelimelerin listesini 'kitap11.txt' dosyasında görebilirsiniz.

Tüm kitaplardaki ortak kelimelerin sayısı: 118
 ->Bu kelimelerin listesi de 'kitap11.txt' dosyasından görülebilir.

Alis kitaplarındaki ortak kelimelerin ilk 30 adedini inceleyelim:
-----------------------------------------------------------------
first, it, its, be, h2, your, h1, all, so, have, go, who, thing, p, been, way, a
re, on, now, did, was, down, only, any, an, herself, looked, say, must, chapter,
"""