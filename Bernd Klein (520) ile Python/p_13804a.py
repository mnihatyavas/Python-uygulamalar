# coding:iso-8859-9
# p_13804a.py: @staticmethod'la sınıf nesnesi kopyalarına tip özelliği değerini aktarma örneği.

class Robot:
    __sayaç = 0 # Özel/private tip değişkeni...
    def __init__ (self): type (self).__sayaç += 1

    @staticmethod # "Robot.robotTiplemesi()" için gerekmez ama "x.robotTiplemesi()" için gerekir...
    def robotTiplemesi(): return Robot.__sayaç


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