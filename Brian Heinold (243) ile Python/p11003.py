# coding:iso-8859-9 Türkçe

a = 5
print (a, "+=2: ", end="")
a +=2; print (a)

print (a, "-=3: ", end="")
a -=3; print (a)

print (a, "*=4: ", end="")
a *=4; print (a)

a=b=c=0
print ("a=b=c=0:", a, b, c)

L = [i for i in range (3)]
x,y,z=L
print ("L:", L, " ve x,y,z=L:", x,y,z)

x,y,z = y,z,x
print ("x,y,z=y,z,x:", x, y, z)

print ("x==y==z", x==y==z)
print ("0<=z<x<y<3", 0<=z<x<y<3)

kelime = "Nihat"
if len (kelime) > 4 and kelime[4] == "t": print (len (kelime), kelime[4])
if kelime[4] == "t" or len (kelime) > 10: print (len (kelime), kelime[4])

if kelime[0] == "N" and kelime[1] == "i" and \
kelime[2] == "h" and kelime[3] == "a" and \
    kelime[4] == "t": print (kelime)

if "N" in kelime and "i" in kelime and \
    "h" in kelime and "a" in kelime and \
"t" in kelime: print (kelime)
