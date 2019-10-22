# coding:iso-8859-9
# p_13711.py: S�n�f nesnesinin init kurucu ve del imhac� haz�r metodlar� �rne�i.

class Robot():
    def __init__ (self, isim):
        self.ad = isim
        print ("Bu kurucu __init__ metodu (" + self.ad + ") adl� robot nesnesini yaratt�!")
    def __del__ (self):
        print ("   Bu imhac� __del__ metodu (" + self.ad + ") adl� robot nesnesini yok etti!")


if __name__ == "__main__":
    x = Robot ("Mahmut Nihat")
    y = Robot ("Muhammed Ali")
    z = x
    q = Robot("")

    print ("\nx robotu siliniyor..."); del x # z, x'i g�rd���nden hen�z silmedi...
    print ("z robotu siliniyor..."); del z # Ba�ka kopyalar kalmay�nca sildi.
    print ("y robotu siliniyor..."); del y
    print ("q robotu siliniyor..."); del q



"""��kt�:
>python p_13711.py
Bu kurucu __init__ metodu (Mahmut Nihat) adl� robot nesnesini yaratt�!
Bu kurucu __init__ metodu (Muhammed Ali) adl� robot nesnesini yaratt�!
Bu kurucu __init__ metodu () adl� robot nesnesini yaratt�!

x robotu siliniyor...
z robotu siliniyor...
   Bu imhac� __del__ metodu (Mahmut Nihat) adl� robot nesnesini yok etti!
y robotu siliniyor...
   Bu imhac� __del__ metodu (Muhammed Ali) adl� robot nesnesini yok etti!
q robotu siliniyor...
   Bu imhac� __del__ metodu () adl� robot nesnesini yok etti!
"""