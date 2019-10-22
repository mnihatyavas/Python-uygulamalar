# coding:iso-8859-9
# p_13711.py: Sınıf nesnesinin init kurucu ve del imhacı hazır metodları örneği.

class Robot():
    def __init__ (self, isim):
        self.ad = isim
        print ("Bu kurucu __init__ metodu (" + self.ad + ") adlı robot nesnesini yarattı!")
    def __del__ (self):
        print ("   Bu imhacı __del__ metodu (" + self.ad + ") adlı robot nesnesini yok etti!")


if __name__ == "__main__":
    x = Robot ("Mahmut Nihat")
    y = Robot ("Muhammed Ali")
    z = x
    q = Robot("")

    print ("\nx robotu siliniyor..."); del x # z, x'i gördüğünden henüz silmedi...
    print ("z robotu siliniyor..."); del z # Başka kopyalar kalmayınca sildi.
    print ("y robotu siliniyor..."); del y
    print ("q robotu siliniyor..."); del q



"""Çıktı:
>python p_13711.py
Bu kurucu __init__ metodu (Mahmut Nihat) adlı robot nesnesini yarattı!
Bu kurucu __init__ metodu (Muhammed Ali) adlı robot nesnesini yarattı!
Bu kurucu __init__ metodu () adlı robot nesnesini yarattı!

x robotu siliniyor...
z robotu siliniyor...
   Bu imhacı __del__ metodu (Mahmut Nihat) adlı robot nesnesini yok etti!
y robotu siliniyor...
   Bu imhacı __del__ metodu (Muhammed Ali) adlı robot nesnesini yok etti!
q robotu siliniyor...
   Bu imhacı __del__ metodu () adlı robot nesnesini yok etti!
"""