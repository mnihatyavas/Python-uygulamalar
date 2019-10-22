# coding:iso-8859-9 Türkçe

print ("10x10'luk çarpım cetveli:")
for i in range (1,11):
    for j in range (1,11):
        print ('{:4d}'.format (i*j), end='')
    print()

bayrak = True
x = -49
while -50<x<50 and bayrak:
    y = -49
    while -50<y<50 and bayrak:
        if 2 * x + 3 * y ==4 and x - y == 7:
            print ("\n2 * x + 3 * y == 4 ve x - y == 7 ise (x, y) = (", x, ", ", y, ") olur.", sep="")
            bayrak = False
        y +=1
    x +=1

print ("\nPisagor x^2+y^2=z^2 üçlüsüne [1->100] arasında uyan değerler:")
for x in range (1, 100):
    for y in range (x, 100):
        for z in range (y, 100):
            if x**2 + y**2 == z**2:
                for i in range (2,x):
                    if x%i == 0 and y%i == 0 and z%i == 0: break
                else: print ("(x, y, z) = (", x, ", ", y, ", ", z, ")", sep="")

print()
print (''.join ([h * i for h in 'Python' for i in range ("Python".index (h)+1, "Python".index (h)+2)]) )
print (''.join ([h * ("MNihatYavaş".index (h) + 1) for h in "MNihatYavaş"]) )
