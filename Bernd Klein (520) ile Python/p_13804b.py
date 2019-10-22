# coding:iso-8859-9
# p_13804b.py: @classmethod'la s�n�f metodunun ilk parametresine otomatikmen s�n�f tipini aktarma �rne�i.

class Robot:
    __saya� = 0 # �zel/private tip de�i�keni...
    def __init__ (self): type (self).__saya� += 1

    @classmethod # "Robot.robotTiplemesi()" i�in gerekmez ama "x.robotTiplemesi()" i�in gerekir...
    def robotTiplemesi (s�n�f): return s�n�f, Robot.__saya�


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



"""��kt�:
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