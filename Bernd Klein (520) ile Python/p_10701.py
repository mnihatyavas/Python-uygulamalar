# coding:iso-8859-9 Türkçe
# p_10701.py: Dizge, liste, tüple ve byte dizilerle endeksli işlemler örneği.

# Dizge, byte, byte dizi, liste, tüple, range/erim sıralı veri tipini kullanır...

dizge = "Dizgenin herbir sıralı endeks karakterine ulaşılabilir!"
print (dizge, "\n==>", dizge[0], dizge[len (dizge) // 2], dizge[len (dizge)-1], dizge[-1], dizge[-len (dizge)])

print()
liste = ["Tokyo", "Astana", "Bankok", "Singapur", "Moskova", "Kiev",
    "Tahran", "Tiflis", "Nağcivan", "Halep", "Dubai", "Kahire", "Ğartum",
    "Lefkoşe", "Atina", "Sofya", "Saraybosna", "Rabat", "Sao Paola", "Buenos Aires"]
print (liste, "\n==>", liste[0], liste[len (liste) // 2], liste[len (liste)-1], liste[-1], liste[-len (liste)])

print ("\nBoş liste:", [])
print ("Tamsayılar listesi:", [1,1,2,3,5,8])
print ("Karışık veri tipli liste:", [42, "Ne sormuştunuz?", 3.1415])
print ("\nDizgeler listesi:", ["Ankara", "İstanbul", "İzmir", "Adana",
    "Konya", "Mersin","Bursa", "Samsun", "Antalya"])
print ("\nİç-içe listelerli liste:", [["Londra","İngiltere", 7556900],
     ["Paris","Fransa",2193031], ["Bern", "İsviçre", 123466]]	)
print ("\nDerin iç-içe liste:", ["Üst seviye", ["2.alt seviye", ["ve 3.aşağısı",
    ["4.derin alt seviye", "cevap", 42]]]])

şahıs = [ ["Yavaş", "M.Nihat"], ["217, Anıtlar Cd", "No: 9","Toroslar-Mersin"],
     ["090.555.551.94.64", "mnyavas@hotmail.com"] ]
print ("\nŞahsın adı ve soyadı:", şahıs[0][1], şahıs[0][0])
print ("Şahsın adresi:", şahıs[1])
print ("Şahsın epostası:", şahıs[2][1])

kompleksListe = [ ["a", ["b", ["c", "x"]]] , 42]
print ("\nKompleks liste eleman sayısı:", len (kompleksListe))
print ("En derin ilk eleman:", kompleksListe[0][1][1][0])


L = ["a", "b", "c"]
print ("\nL :", L)
L *=3
print ("L *=3:", L)
L[1] = "P"
print ("L[1] = 'P':", L)
L = ["a", "b", "c"]
L = [L]*3
print ("L=[L]*3:", L)
L[1][0] = "P"
print ("HATA: L[1][0] = 'P':", L)

tüple = ("Tüple", "eleman", "sayısını ve değerlerini", "listeler gibi", "değiştiremezsiniz.")
print ("\nTüple sembolü parantezdir:", tüple)
print ("Endekslenmesi listelerle aynıdır:", tüple[0], tüple[len (tüple)//2], tüple[-1])
# tüple[0] = "Tüpleler" ==>Derleme hatası...

print()
byteNesnesi = b"M.Nihat Yavas, 1957"
print ("Byte nesnesi 0->127 ASCII karakterlidir:", byteNesnesi,
    byteNesnesi[0], chr (byteNesnesi[8]), ord (chr (byteNesnesi[16])) )


"""Çıktı:
>python p_10601.py
Toplama ve çıkarma (10+/-3): 13 7
Çarpma, bölme ve kalan (27*/+7): 189 3.857142857142857 6
Küsüratsız (-+//) zemin bölme ve -+int(10/3) kesik bölmesi: 3 3 -4.0 -3
Çebirsel -+ işareti: -3 3
Bitvari negatifleme: -8 6
-+Üs (**): -199.5690776400273 0.00501079632087968
Boolean or/veya, and/ve ve not/değil: False
Elemanı mı (True/False)? True
Karşılaştırma (2 ila 5) operatörleri (<, <=, >, >=, ==, !=): True True False False False True
Bitvari |/veya, &/ve, ^/farklıysa (6=110 ila 3=011): 7 2 5
Kaydırma << ve >> operatörleri (6=110'yı 2 kez kaydır): 24 1

C:\Users\pc\Desktop\MyFiles\4. Dersler\python>python p_10701.py
Dizgenin herbir sıralı endeks karakterine ulaşılabilir!
==> D k ! ! D

['Tokyo', 'Astana', 'Bankok', 'Singapur', 'Moskova', 'Kiev', 'Tahran', 'Tiflis',
 'Nağcivan', 'Halep', 'Dubai', 'Kahire', 'Ğartum', 'Lefkoşe', 'Atina', 'Sofya',
'Saraybosna', 'Rabat', 'Sao Paola', 'Buenos Aires']
==> Tokyo Dubai Buenos Aires Buenos Aires Tokyo

Boş liste: []
Tamsayılar listesi: [1, 1, 2, 3, 5, 8]
Karışık veri tipli liste: [42, 'Ne sormuştunuz?', 3.1415]

Dizgeler listesi: ['Ankara', 'İstanbul', 'İzmir', 'Adana', 'Konya', 'Mersin', 'Bursa', 'Samsun', 'Antalya']

İç-içe listelerli liste: [['Londra', 'İngiltere', 7556900], ['Paris', 'Fransa',2193031], ['Bern', 'İsviçre', 123466]]

Derin iç-içe liste: ['Üst seviye', ['2.alt seviye', ['ve 3.aşağısı', ['4.derin alt seviye', 'cevap', 42]]]]

Şahsın adı ve soyadı: M.Nihat Yavaş
Şahsın adresi: ['217, Anıtlar Cd', 'No: 9', 'Toroslar-Mersin']
Şahsın epostası: mnyavas@hotmail.com

Kompleks liste eleman sayısı: 2
En derin ilk eleman: c

L : ['a', 'b', 'c']
L *=3: ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']
L[1] = 'P': ['a', 'P', 'c', 'a', 'b', 'c', 'a', 'b', 'c']
L=[L]*3: [['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c']]
HATA: L[1][0] = 'P': [['P', 'b', 'c'], ['P', 'b', 'c'], ['P', 'b', 'c']]

Tüple sembolü parantezdir: ('Tüple', 'eleman', 'sayısını ve değerlerini', 'listeler gibi', 'değiştiremezsiniz.')
Endekslenmesi listelerle aynıdır: Tüple sayısını ve değerlerini değiştiremezsiniz.

Byte nesnesi 0->127 ASCII karakterlidir: b'M.Nihat Yavas, 1957' 77 Y 57
"""