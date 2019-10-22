# coding:iso-8859-9
# p_13704.py: S�n�f arg�manl� fonksiyon, s�n�f�n init tipleri ve fonksiyon metodlar� �rne�i.

def selam (arg�manNesnesi):
    print ("Merhaba, benim ad�m " + arg�manNesnesi.ad + "!")

class Robot: pass

x = Robot()
x.ad = "Robot Ali"

selam (x) # Arg�man� s�n�f olan ve s�n�f �zelli�ini yans�tan fonksiyon...
#-------------------------------------------------------------------------------------------------

class Robot: selamla�ma = selam

x = Robot()
x.ad = "Robot Ali"

Robot.selamla�ma (x) # Fonksiyon i�leten s�n�f metodunun �zellik yans�tmas�...
x.ad = "Robot Muhammed Ali"
x.selamla�ma() # Bir �stekiyle ayn�d�r...
print ("-"*75, "\n", sep="")
#-------------------------------------------------------------------------------------------------

class Robot:
    def __init__ (self, ad� = None):
        self.ad = ad�
        print ("\n==>S�n�f fonksiyonu, metoddur.\nS�n�f nesnesinin her yarat�l�mas�nda otomatik i�letilen metod 'init'dir.\n'init' metodu s�n�f�n tip de�i�kenlerini bar�nd�r�r.")

    def selamla�ma (self):
        if self.ad: print ("Merhaba, benim ad�m " + self.ad + "!")
        else: print ("Merhaba, ben hen�z ad� konulmam�� bir robotum!")

x = Robot()
x.selamla�ma()
y = Robot ("Robot Ali")
y.selamla�ma()
z = Robot ("Robot Muhammed Ali")
z.selamla�ma()

"""��kt�:
>python p_13704.py
Merhaba, benim ad�m Robot Ali!
Merhaba, benim ad�m Robot Ali!
Merhaba, benim ad�m Robot Muhammed Ali!
---------------------------------------------------------------------------

==>S�n�f fonksiyonu, metoddur.
S�n�f nesnesinin her yarat�l�mas�nda otomatik i�letilen metod 'init'dir.
'init' metodu s�n�f�n tip de�i�kenlerini bar�nd�r�r.
Merhaba, ben hen�z ad� konulmam�� bir robotum!

==>S�n�f fonksiyonu, metoddur.
S�n�f nesnesinin her yarat�l�mas�nda otomatik i�letilen metod 'init'dir.
'init' metodu s�n�f�n tip de�i�kenlerini bar�nd�r�r.
Merhaba, benim ad�m Robot Ali!

==>S�n�f fonksiyonu, metoddur.
S�n�f nesnesinin her yarat�l�mas�nda otomatik i�letilen metod 'init'dir.
'init' metodu s�n�f�n tip de�i�kenlerini bar�nd�r�r.
Merhaba, benim ad�m Robot Muhammed Ali!
"""