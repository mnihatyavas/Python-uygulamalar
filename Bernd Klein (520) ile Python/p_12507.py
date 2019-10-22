# coding:iso-8859-9 T�rk�e
# p_12507.py: ��i�e dekorat�rl� ambalaja 3.d�� selamlama fonksiyonu sarmalama �rne�i.

def ikindiSelam� (fonk):
    def ambalaj (x):
        print ("\nT�nayd�n, " + fonk.__name__ + " mesaj�n�z: ")
        fonk (x)
    return ambalaj

def sabahSelam� (fonk):
    def ambalaj (x):
        print ("G�nayd�n, " + fonk.__name__ + " mesaj�n�z: ")
        fonk (x)
    return ambalaj

@sabahSelam�
def do�um_g�n� (x): print (str (x) + " do�um g�n�n�z kutlu olsun!..")

do�um_g�n� (7.8)

@ikindiSelam�
def do�um_g�n� (x): print (str (x) + " do�um g�n�n�z kutlu olsun!..")

do�um_g�n� ("7 A�ustos")
print ("-"*75, "\n")
#--------------------------------------------------------------------------------------------------------

def selam (ibare):
    def dekorat�r (fonk):
        def ambalaj (x):
            print ("\n" + ibare + ", " + fonk.__name__ + " mesaj�n�z:")
            fonk (x)
        return ambalaj
    return dekorat�r

def do�um_g�n� (x): print (str (x) + " do�um g�n�n�z kutlu olsun!..")

# En anla��l�r ve @'siz kullan�m...
selam ("G�nayd�n") (do�um_g�n�) (7.8)
selam ("T�nayd�n") (do�um_g�n�) ("7 A�ustos")
selam ("Merhaba") (do�um_g�n�) ("14 Nisan")

# Veya pratik @'li kullan�m...
@selam ("�yi ak�amlar")
def do�um_g�n�2 (x): print (str (x) + " do�um g�n�n�z kutlu olsun!..")

do�um_g�n�2 ("17 Nisan")

# Veya dolaylamal� @'siz kullan�m...
kutlama = selam ("Selam") (do�um_g�n�)
kutlama ("4 May�s")


"""��kt�:
>python p_12507.py
G�nayd�n, do�um_g�n� mesaj�n�z:
7.8 do�um g�n�n�z kutlu olsun!..

T�nayd�n, do�um_g�n� mesaj�n�z:
7 A�ustos do�um g�n�n�z kutlu olsun!..
---------------------------------------------------------------------------


G�nayd�n, do�um_g�n� mesaj�n�z:
7.8 do�um g�n�n�z kutlu olsun!..

T�nayd�n, do�um_g�n� mesaj�n�z:
7 A�ustos do�um g�n�n�z kutlu olsun!..

Merhaba, do�um_g�n� mesaj�n�z:
14 Nisan do�um g�n�n�z kutlu olsun!..

�yi ak�amlar, do�um_g�n�2 mesaj�n�z:
17 Nisan do�um g�n�n�z kutlu olsun!..

Selam, do�um_g�n� mesaj�n�z:
4 May�s do�um g�n�n�z kutlu olsun!..
"""