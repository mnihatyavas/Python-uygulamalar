# coding:iso-8859-9
# p_13801.py: S�n�f �zelli�i ve de�i�tirilmesinin kopyalar�yla ili�kisi �rne�i.

class A: a = "Ben bir s�n�f �zelli�i tip de�i�keniyim!"

x = A()
y = A()

print ("x.a:", x.a)
print ("y.a:", y.a)
print ("A.a:", A.a)
print ("-"*75, "\n", sep="")
#--------------------------------------------------------------------------------------------------

x.a = "x.a i�in yeni bir tip �zelli�i yarat�yorum!"
print ("A.a:", A.a)
print ("y.a:", y.a)

A.a = "�nceki s�n�f �zelli�i 'a'y� de�i�tiriyorum!"
print ("\nA.a:", A.a)
print ("y.a:", y.a)
print ("x.a:", x.a)

# x.__dict__, y.__dict__, A.__dict__ ve x.__class__.__dict__ farkl�d�r...

"""��kt�:
>python p_13801.py
x.a: Ben bir s�n�f �zelli�i tip de�i�keniyim!
y.a: Ben bir s�n�f �zelli�i tip de�i�keniyim!
A.a: Ben bir s�n�f �zelli�i tip de�i�keniyim!
---------------------------------------------------------------------------

A.a: Ben bir s�n�f �zelli�i tip de�i�keniyim!
y.a: Ben bir s�n�f �zelli�i tip de�i�keniyim!

A.a: �nceki s�n�f �zelli�i 'a'y� de�i�tiriyorum!
y.a: �nceki s�n�f �zelli�i 'a'y� de�i�tiriyorum!
x.a: x.a i�in yeni bir tip �zelli�i yarat�yorum!
"""