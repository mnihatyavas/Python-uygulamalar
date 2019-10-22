# coding:iso-8859-9
# p_13702.py: Sınıf nesnesi, değişkene atama, özellik kazandırma, dict vasıfları örneği.

class Robot: pass

if __name__ == "__main__":
    x1 = Robot()
    y1 = Robot()

    x2 = x1
    y2 = y1

    print (type (Robot) )
    print (type (x1) )

    print ("\nx1 == x2:", x1 == x2)
    print ("y1 == y2:", y1 == y2)
    print ("x2 == y2:", x2 == y2)

    print ("-"*75, "\n", sep="")
    #--------------------------------------------------------------------------------------------------

    x1.ad = "1.Robot"
    y1.ad = "2.Robot"

    x1.imalatTarihi = 20181231
    y1.imalatTarihi = 20190423

    print ("\nx1 robotun adı:", x1.ad)
    print ("x2 robotun imalat tarihi:", x2.imalatTarihi)
    print ("\ny2 robotun adı:", y2.ad)
    print ("y1 robotun imalat tarihi:", y1.imalatTarihi)
    print ("-"*75, "\n", sep="")
    #--------------------------------------------------------------------------------------------------

    print ("\nx1 sınıfının özellikleri:", x1.__dict__)
    print ("y2 sınıfının özellikleri:", y2.__dict__)
    print ("-"*75, "\n", sep="")
    #--------------------------------------------------------------------------------------------------

    Robot.marka = "Şahin"
    print ("\nx1 markası:", x1.marka)
    print ("y1 markası:", y1.marka)

    x1.marka = "Kartal"
    print ("\nx1 markası:", x1.marka)
    print ("y1 markası:", y1.marka)

    print ("\nx1.__dict__:", x1.__dict__)
    print ("y1.__dict__:", y1.__dict__)
    print ("Robot.__dict__:", Robot.__dict__)
    print ("-"*75, "\n", sep="")
    #--------------------------------------------------------------------------------------------------

    try: print ("\nx1 robotun enerji seviyesi:", x1.şarj)
    except AttributeError: print ("\nx1 robotun enerji seviyesi:", getattr (x1, "şarj", "boş") )

    y1.şarj = 90
    try: print ("y1 robotun enerji seviyesi:", y1.şarj)
    except AttributeError: print ("y1 robotun enerji seviyesi:", getattr (y1, "şarj", "boş") )

"""Çıktı:
>python p_13702.py
<class 'type'>
<class '__main__.Robot'>

x1 == x2: True
y1 == y2: True
x2 == y2: False
---------------------------------------------------------------------------

x1 robotun adı: 1.Robot
x2 robotun imalat tarihi: 20181231

y2 robotun adı: 2.Robot
y1 robotun imalat tarihi: 20190423
---------------------------------------------------------------------------

x1 sınıfının özellikleri: {'ad': '1.Robot', 'imalatTarihi': 20181231}
y2 sınıfının özellikleri: {'ad': '2.Robot', 'imalatTarihi': 20190423}
---------------------------------------------------------------------------

x1 markası: Şahin
y1 markası: Şahin

x1 markası: Kartal
y1 markası: Şahin

x1.__dict__: {'ad': '1.Robot', 'imalatTarihi': 20181231, 'marka': 'Kartal'}
y1.__dict__: {'ad': '2.Robot', 'imalatTarihi': 20190423}
Robot.__dict__: {'__module__': '__main__', '__dict__': <attribute '__dict__' of 'Robot' objects>,
'__weakref__': <attribute '__weakref__' of 'Robot' objects>, '__doc__': None, 'marka': 'Şahin'}
---------------------------------------------------------------------------

x1 robotun enerji seviyesi: boş
y1 robotun enerji seviyesi: 90
"""