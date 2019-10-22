# coding:iso-8859-9 Türkçe
# p_20701.py: Bağlantılı ve izole yumruların ilişkilerinin listelenmesi örneği.

ilişkiler = {
        "a" : ["c"],
        "b" : ["c", "e"],
        "c" : ["a", "b", "d", "e"],
        "d" : ["c"],
        "e" : ["c", "b"],
        "f" : [],
        "g" : []
    }

def kenarlarÜret (ilişkiler):
    kenarlar = []
    for yumru in ilişkiler:
        for komşu in ilişkiler [yumru]:
            kenarlar.append ((yumru, komşu))
    return kenarlar

def izoleYumrular (ilişkiler):
    izoleler = []
    for yumru in ilişkiler:
        if not ilişkiler[yumru]: izoleler += yumru
    return izoleler


liste1 = kenarlarÜret (ilişkiler)
print ("Yumru ilişkileri tüple çifti listesi==>\n", liste1)

print ("\nAlt-alta yumru ilişkileri tüple çifti listesi==>")
for i in range (len (liste1)): print ((i+1), ":", liste1 [i])

print ("\nAlt-alta yumru ilişkileri bağlantı çifti listesi==>")
for i in range (len (liste1)): print ((i+1), ":", liste1[i][0], "--->", liste1[i][1])

liste2 = izoleYumrular (ilişkiler)
print ("\nİzole yumru ilişkileri tüple çifti listesi==>", liste2)



"""Çıktı:
>python p_20701.py
Yumru ilişkileri tüple çifti listesi==>
 [('a', 'c'), ('b', 'c'), ('b', 'e'), ('c', 'a'), ('c', 'b'), ('c', 'd'), ('c','e'), ('d', 'c'), ('e', 'c'), ('e', 'b')]

Alt-alta yumru ilişkileri tüple çifti listesi==>
1 : ('a', 'c')
2 : ('b', 'c')
3 : ('b', 'e')
4 : ('c', 'a')
5 : ('c', 'b')
6 : ('c', 'd')
7 : ('c', 'e')
8 : ('d', 'c')
9 : ('e', 'c')
10 : ('e', 'b')

Alt-alta yumru ilişkileri bağlantı çifti listesi==>
1 : a ---> c
2 : b ---> c
3 : b ---> e
4 : c ---> a
5 : c ---> b
6 : c ---> d
7 : c ---> e
8 : d ---> c
9 : e ---> c
10 : e ---> b

İzole yumru ilişkileri tüple çifti listesi==> ['f', 'g']
"""