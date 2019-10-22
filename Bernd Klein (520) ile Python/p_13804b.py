# coding:iso-8859-9
# p_13804b.py: @classmethod'la sınıf metodunun ilk parametresine otomatikmen sınıf tipini aktarma örneği.

class Robot:
    __sayaç = 0 # Özel/private tip değişkeni...
    def __init__ (self): type (self).__sayaç += 1

    @classmethod # "Robot.robotTiplemesi()" için gerekmez ama "x.robotTiplemesi()" için gerekir...
    def robotTiplemesi (sınıf): return sınıf, Robot.__sayaç


if __name__ == "__main__":
    print (Robot.robotTiplemesi() )

    print()
    x = Robot()
    print (x.robotTiplemesi() )
    print (Robot.robotTiplemesi() )

    print()
    y = Robot()
    print (x.robotTiplemesi() )
    print (y.robotTiplemesi() )
    print (Robot.robotTiplemesi() )

    print()
    z = Robot()
    print (x.robotTiplemesi() )
    print (y.robotTiplemesi() )
    print (z.robotTiplemesi() )
    print (Robot.robotTiplemesi() )



"""Çıktı:
>python p_13804b.py
(<class '__main__.Robot'>, 0)

(<class '__main__.Robot'>, 1)
(<class '__main__.Robot'>, 1)

(<class '__main__.Robot'>, 2)
(<class '__main__.Robot'>, 2)
(<class '__main__.Robot'>, 2)

(<class '__main__.Robot'>, 3)
(<class '__main__.Robot'>, 3)
(<class '__main__.Robot'>, 3)
(<class '__main__.Robot'>, 3)
"""