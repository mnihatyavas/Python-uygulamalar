# coding:iso-8859-9 Türkçe
# p_10503.py: Tek, çift ve üç tırnaklı dizgeler ve endeksli dizge işlemleri örneği.

dizge1 = 'Bu tek tırnaklı bir dizgedir.'
dizge2 = "Bu ise çift tırnaklı bir dizgedir."
dizge3 = """
    Bu dizgenin satır sayısı konusunda bir sorun yoktur.
    Zira 3-çift tırnaklı dizgelerde, satırlar nasıl şekillendirilmişse
    çıktıya da aynen öyle alt alta olacak şekilde yansıyacaktır."""
print ("Tek tırnaklı dizge: ", dizge1)
print ("Çift tırnaklı dizge: ", dizge2)
print ("3-çift tırnaklı dizge: ", dizge3)

print ('\nTek tırnaklıda yine tek tırnaklı \'alıntı\' esc karakteriyle mümkündür.')
print ("Çift tırnaklıda tek tırnaklı 'alıntı' aynen mümkündür.")
print ("Çift tırnaklıda çift tırnaklı \"alıntı\" yine esc karakteriyle mümkündür.")
print ("""3-çift tırnaklıda 'tek tırnaklı' veya "çift tırnaklı" alıntı aynen ve hiç sorun değildir.""")
print ('''3-tek tırnaklıda da 'tek tırnaklı' veya "çift tırnaklı" alıntı aynen ve hiç sorun değildir.''')

dizge1 = "M.Nihat Yavaş"
print ("\ndizge1 =", dizge1)
for i in range (len (dizge1)): print (i, ":", dizge1[i], sep="", end=" ") # İleri endeks: 0-->12
print()
for i in range (-1, -len (dizge1)-1, -1): print (i, ":", dizge1[i], sep="", end=" ") # Geri endeks: -1-->-13
print()
print ("\nDizgeleri " + "arka arkaya " + "ekleyebilirsiniz.")
print ("Dizgeler * ile tekrarlatılabilir:",  "*_*"*10)
print ("Dizgelerin herhangi tek bir karakterine endeksiyle erişilebilir:", dizge1[8])
print ("Dizgelerin herhangi çoklu karakterli bir dilimi alınabilir:", dizge1[2:7])
print ("Dizgelerin ebatı bellidir:", len (dizge1) )

print()
try:
    print ("Dizgeler değiştirilemez, hata verirler:")
    dizge1[2] = "K"
except Exception:
    print ("Dizgeleri değiştiremez, ancak yeniden referanslayabilirsiniz.")
    dizge1 = "M.Kemal Atatürk"
    print (dizge1)

print()
dizge1 = "Merhaba Nihat"
dizge2 = "Merhaba Nihat"
print (dizge1 is dizge2) # "is" operatörü aynı bellek adresinin farklı değişkenlerce referanslanmasıdır: True
print (dizge1 == dizge2) # "==" operatörü ise 2 ayrı değer içeren değişkenlerin aynılığıdır: True

print ("\nb: Byte dizgesi sadece ascii 0->128 karakterleri içerebilir.")
x = b"Merhaba M.Nihat" # İmrahim Ömer Şençayır"
t = str (x)
u = t.encode ("UTF-8")
print (x, t, u)


"""Çıktı:
>python p_10503.py
Tek tırnaklı dizge:  Bu tek tırnaklı bir dizgedir.
Çift tırnaklı dizge:  Bu ise çift tırnaklı bir dizgedir.
3-çift tırnaklı dizge:
    Bu dizgenin satır sayısı konusunda bir sorun yoktur.
    Zira 3-çift tırnaklı dizgelerde, satırlar nasıl şekillendirilmişse
    çıktıya da aynen öyle alt alta olacak şekilde yansıyacaktır.

Tek tırnaklıda yine tek tırnaklı 'alıntı' esc karakteriyle mümkündür.
Çift tırnaklıda tek tırnaklı 'alıntı' aynen mümkündür.
Çift tırnaklıda çift tırnaklı "alıntı" yine esc karakteriyle mümkündür.
3-çift tırnaklıda 'tek tırnaklı' veya "çift tırnaklı" alıntı aynen ve hiç sorundeğildir.
3-tek tırnaklıda da 'tek tırnaklı' veya "çift tırnaklı" alıntı aynen ve hiç sorun değildir.

dizge1 = M.Nihat Yavaş
0:M 1:. 2:N 3:i 4:h 5:a 6:t 7:  8:Y 9:a 10:v 11:a 12:ş
-1:ş -2:a -3:v -4:a -5:Y -6:  -7:t -8:a -9:h -10:i -11:N -12:. -13:M

Dizgeleri arka arkaya ekleyebilirsiniz.
Dizgeler * ile tekrarlatılabilir: *_**_**_**_**_**_**_**_**_**_*
Dizgelerin herhangi tek bir karakterine endeksiyle erişilebilir: Y
Dizgelerin herhangi çoklu karakterli bir dilimi alınabilir: Nihat
Dizgelerin ebatı bellidir: 13

Dizgeler değiştirilemez, hata verirler:
Dizgeleri değiştiremez, ancak yeniden referanslayabilirsiniz.
M.Kemal Atatürk

True
True

b: Byte dizgesi sadece ascii 0->128 karakterleri içerebilir.
b'Merhaba M.Nihat' b'Merhaba M.Nihat' b"b'Merhaba M.Nihat'"

"""