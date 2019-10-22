# coding:iso-8859-9
# p_13802.py: T�pleli s�n�f ip �zelli�i ve init kuruculu tip de�i�ken �zellikleri �rne�i.

class Robot:
    ��l�Kanun = (
        """Bir robot bir insan� yaralayamaz, veya bir insan�n yaralanabilme olay�na duyars�z kalamaz.""",
        """Bir robot bir insan taraf�ndan verilen talimatlara, �lk Kanunu ihlal etmiyorsa uymal�d�r.""",
        """Bir robot kendi varl���n�, �lk ve �kinci Kanunlara ters d��m�yorsa korumal�d�r.""" )
    def __init__ (self, ad�, y�l�):
        self.ad = ad�
        self.y�l = y�l�
    # Gereken di�er metodlar...

x = Robot ("Robot Nihat", "19570417")

for s�ra, metin in enumerate (Robot.��l�Kanun):
    print ("Madde." + str (s�ra+1) + ":\n" + metin + "\n")

print (str ("-"*79) + "\n" + x.��l�Kanun [1] )

print ("\nAd�: " + x.ad + ", �mal tarihi: " + x.y�l)



"""��kt�:
>python p_13802.py
Madde.1:
Bir robot bir insan� yaralayamaz, veya bir insan�n yaralanabilme olay�na duyars�z kalamaz.

Madde.2:
Bir robot bir insan taraf�ndan verilen talimatlara, �lk Kanunu ihlal etmiyorsa uymal�d�r.

Madde.3:
Bir robot kendi varl���n�, �lk ve �kinci Kanunlara ters d��m�yorsa korumal�d�r.

-------------------------------------------------------------------------------
Bir robot bir insan taraf�ndan verilen talimatlara, �lk Kanunu ihlal etmiyorsa uymal�d�r.

Ad�: Robot Nihat, �mal tarihi: 19570417
"""