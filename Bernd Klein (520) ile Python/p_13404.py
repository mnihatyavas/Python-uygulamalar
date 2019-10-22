# coding:iso-8859-9 Türkçe
# p_13404.py: Argümansız send-yield değer geçirme, print üreteç ve istisnası örneği.

def argümansız_iletişim():
    print ("Argümansız iletişim fonksiyonu başlatıldı!")
    x = yield # send(..) ile yield'e argüman aktarılabilir...
    print ("send->yield ile alınan değer:", x)

fonk1 = argümansız_iletişim()

try:
    next (fonk1) # İlk next ile ilk print çalıştırılır...
    next (fonk1) # İkinci next ile yield-x'li ikinci print çalıştırılır...
    next (fonk1) # except işletilir...
except StopIteration: print ("HATA1")
#--------------------------------------------------------------------------------------------------

fonk2 = argümansız_iletişim()

print()
try:
    next (fonk2) # ilk print...
    print (fonk2.send ("Merhaba!") ) # yield'e gönderilen mesajlı x print'i...
    next (fonk2) # except...
except StopIteration: print ("HATA2")

"""Çıktı:
>python p_13404.py
Argümansız iletişim fonksiyonu başlatıldı!
send->yield ile alınan değer: None
HATA1

Argümansız iletişim fonksiyonu başlatıldı!
send->yield ile alınan değer: Merhaba!
HATA2
"""