# coding:iso-8859-9 Türkçe

for i in range (256): print (i, "=", chr (i), sep="", end=" ")

print("\n")
for i in range (1, 21): print (i, "---", i*i)
print("\n")
for i in range (8, 90, 3): print (i, end=" ")
print("\n")
for i in range (100, 0, -2): print (i, end=" ")

print("\n")
for i in range (10): print ("A", end="")
for i in range (7): print ("B", end="")
for i in range (4): print ("CD", end="")
print ("E", end="")
for i in range (6): print ("F", end="")
print ("G")

isim = input ("\nAd ve soyadınızı girin: ")
kere = eval (input ("Kaç kere yazılsın? "))
for i in range (kere): print (isim)

fib = eval (input ("Kaç adet Fibonacci [enaz:2] yazılsın? "))
a=b=1
print (a,b, end=" ")
for i in range (fib-2):
    print (a+b, end=" ")
    c = a
    a = b
    b = c+b

print("\n")
kere = eval (input ("Azami elmas eni '*' sayısını gir: "))
for i in range (kere):
    print (" " * ((kere-i)//2), end="")
    for j in range (i):
        print ("*", end="")
    print()
for i in range (kere, 0, -1):
    print (" " * ((kere-i)//2), end="")
    for j in range (i):
        print ("*", end="")
    print()

print("\n")
for i in range (1, kere, 2):
    print (" " * ((kere-i)//2), end="")
    for j in range (i):
        print ("*", end="")
    print()
for i in range (kere-1, 0, -2):
    print (" " * ((kere-i)//2), end="")
    for j in range (i):
        print ("*", end="")
    print()

print("\n")
k = kere // 2
for i in range (1, kere, 2):
    print (" " * ((kere-i)//2), end="")
    for j in range (i):
        if j == 0 or j == i-1:
            print ("*", end="")
        elif k == i or k == i+1:
            if k % 2 == 0: print ("*"*(k-2), end="")
            else: print ("*"*(k-1), end="")
            break
        else: print (" ", end="")
    print()
