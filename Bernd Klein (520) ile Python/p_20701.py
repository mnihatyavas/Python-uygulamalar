# coding:iso-8859-9 T�rk�e
# p_20701.py: Ba�lant�l� ve izole yumrular�n ili�kilerinin listelenmesi �rne�i.

ili�kiler = {
        "a" : ["c"],
        "b" : ["c", "e"],
        "c" : ["a", "b", "d", "e"],
        "d" : ["c"],
        "e" : ["c", "b"],
        "f" : [],
        "g" : []
    }

def kenarlar�ret (ili�kiler):
    kenarlar = []
    for yumru in ili�kiler:
        for kom�u in ili�kiler [yumru]:
            kenarlar.append ((yumru, kom�u))
    return kenarlar

def izoleYumrular (ili�kiler):
    izoleler = []
    for yumru in ili�kiler:
        if not ili�kiler[yumru]: izoleler += yumru
    return izoleler


liste1 = kenarlar�ret (ili�kiler)
print ("Yumru ili�kileri t�ple �ifti listesi==>\n", liste1)

print ("\nAlt-alta yumru ili�kileri t�ple �ifti listesi==>")
for i in range (len (liste1)): print ((i+1), ":", liste1 [i])

print ("\nAlt-alta yumru ili�kileri ba�lant� �ifti listesi==>")
for i in range (len (liste1)): print ((i+1), ":", liste1[i][0], "--->", liste1[i][1])

liste2 = izoleYumrular (ili�kiler)
print ("\n�zole yumru ili�kileri t�ple �ifti listesi==>", liste2)



"""��kt�:
>python p_20701.py
Yumru ili�kileri t�ple �ifti listesi==>
 [('a', 'c'), ('b', 'c'), ('b', 'e'), ('c', 'a'), ('c', 'b'), ('c', 'd'), ('c','e'), ('d', 'c'), ('e', 'c'), ('e', 'b')]

Alt-alta yumru ili�kileri t�ple �ifti listesi==>
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

Alt-alta yumru ili�kileri ba�lant� �ifti listesi==>
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

�zole yumru ili�kileri t�ple �ifti listesi==> ['f', 'g']
"""