# coding:iso-8859-9 Türkçe
# p_12504.py: Parametrik içiçe fonksiyonlarda @ direktifi örneği.

def dekoratörüm (fonksiyon):
    def sarmalayıcım (x):
        print (fonksiyon.__name__ + " adlı fonksiyon çağrılmadan önce")
        fonksiyon (x)
        print (fonksiyon.__name__ + " adlı fonksiyon çağrıldıktan sonra")
    return sarmalayıcım

def fonk (x): print ("Merhaba, fonk('" + str (x) + "') çağrıldı!")

print ("fonk('Selam') dekoratörsüz çağrılıyor:")
fonk ("Selam")

print ("\nŞimdi fonk(x) dekorlanıyor...")
f = dekoratörüm (fonk)
print ("Ve dekorlu fonk(1957) çağrılıyor:")
f (1957)
print ("-"*75, "\n")
#------------------------------------------------------------------------------------------------------

# f, son dekarötörlü isim için, argüman olan fonk fonksiyon adı kullanılabilir...
fonk = dekoratörüm (fonk)
print ("Dekorlu fonk('17/04/1957') yeniden çağrılıyor:")
fonk ("17/04/1957")
print ("-"*75, "\n")
#------------------------------------------------------------------------------------------------------

# Hatta def fonk önüne @dekoratörüm tanıtımıyla fonk=dekoratörüm(fonk) gereksizleşir...
@dekoratörüm
def fonk (x): print ("Merhaba, fonk('" + str (x) + "') çağrıldı!")
print ("@ dekorlu fonk('17 Nisan 1957') yeniden çağrılıyor:")
fonk ("17 Nisan 1957")



"""Çıktı:
>python p_12504.py
fonk('Selam') dekoratörsüz çağrılıyor:
Merhaba, fonk('Selam') çağrıldı!

Şimdi fonk(x) dekorlanıyor...
Ve dekorlu fonk(1957) çağrılıyor:
fonk adlı fonksiyon çağrılmadan önce
Merhaba, fonk('1957') çağrıldı!
fonk adlı fonksiyon çağrıldıktan sonra
---------------------------------------------------------------------------

Dekorlu fonk('17/04/1957') yeniden çağrılıyor:
fonk adlı fonksiyon çağrılmadan önce
Merhaba, fonk('17/04/1957') çağrıldı!
fonk adlı fonksiyon çağrıldıktan sonra
---------------------------------------------------------------------------

@ dekorlu fonk('17 Nisan 1957') yeniden çağrılıyor:
fonk adlı fonksiyon çağrılmadan önce
Merhaba, fonk('17 Nisan 1957') çağrıldı!
fonk adlı fonksiyon çağrıldıktan sonra
"""