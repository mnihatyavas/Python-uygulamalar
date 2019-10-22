# coding:iso-8859-9 Türkçe

print ("Tüm sayılar içinde, basamaklarının çarpım ve toplamlarına eşit 9 özel sayı:\n==>", end="")
for i in range (11, 10000):
    d = str (i)
    e = len (d)
    çarp = 1
    topla = sonuç = 0
    for j in range (e):
        çarp *= int (d[j])
        topla += int (d[j])
    sonuç = çarp + topla
    if i == sonuç: print (i, end=" ")

print ("\n\nİlk-son rakamları yerdeğiştirince oranı 3.5 olan ilk sayı:")
for i in range (12, 1000000):
    d = str (i)
    e = len (d)
    d = d[1:] + d[:1]
    if 3.5 < float (d) / i < 3.50009: print (i, d, float (d) / i ); break

çarpım = 1
for i in range (1, 1001):
    çarpım *= i
d = str (çarpım)
e = len (d)
for i in range (0, e):
    if d[e-i-1] != "0": break
print ("\n1000! faktöriyel==>\n", d)
print ("Rakamın uzunluğu:", e)
print ("Sondaki 0-sıfır sayısı:", i)
