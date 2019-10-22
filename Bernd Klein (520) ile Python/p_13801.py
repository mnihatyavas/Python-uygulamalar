# coding:iso-8859-9
# p_13801.py: Sınıf özelliği ve değiştirilmesinin kopyalarıyla ilişkisi örneği.

class A: a = "Ben bir sınıf özelliği tip değişkeniyim!"

x = A()
y = A()

print ("x.a:", x.a)
print ("y.a:", y.a)
print ("A.a:", A.a)
print ("-"*75, "\n", sep="")
#--------------------------------------------------------------------------------------------------

x.a = "x.a için yeni bir tip özelliği yaratıyorum!"
print ("A.a:", A.a)
print ("y.a:", y.a)

A.a = "Önceki sınıf özelliği 'a'yı değiştiriyorum!"
print ("\nA.a:", A.a)
print ("y.a:", y.a)
print ("x.a:", x.a)

# x.__dict__, y.__dict__, A.__dict__ ve x.__class__.__dict__ farklıdır...

"""Çıktı:
>python p_13801.py
x.a: Ben bir sınıf özelliği tip değişkeniyim!
y.a: Ben bir sınıf özelliği tip değişkeniyim!
A.a: Ben bir sınıf özelliği tip değişkeniyim!
---------------------------------------------------------------------------

A.a: Ben bir sınıf özelliği tip değişkeniyim!
y.a: Ben bir sınıf özelliği tip değişkeniyim!

A.a: Önceki sınıf özelliği 'a'yı değiştiriyorum!
y.a: Önceki sınıf özelliği 'a'yı değiştiriyorum!
x.a: x.a için yeni bir tip özelliği yaratıyorum!
"""