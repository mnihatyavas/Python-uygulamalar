# coding:iso-8859-9
# p_13804a.py: @staticmethod'la s�n�f nesnesi kopyalar�na tip �zelli�i de�erini aktarma �rne�i.

class Robot:
    __saya� = 0 # �zel/private tip de�i�keni...
    def __init__ (self): type (self).__saya� += 1

    @staticmethod # "Robot.robotTiplemesi()" i�in gerekmez ama "x.robotTiplemesi()" i�in gerekir...
    def robotTiplemesi(): return Robot.__saya�


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
>python p_13804a.py
0

1
1

2
2
2

3
3
3
3
"""