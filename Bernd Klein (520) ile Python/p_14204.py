# coding:iso-8859-9 T�rk�e
# p_14204.py: Listeye null, t�ple, aritmetik i�lem, dizge, liste ve k�me ekleme �rne�i.

class ListeyeEkle (list):
    def __init__ (self, lst): self.lst = list #list.__init__ (self, lst)
    def ekle (self, birim): self.append (birim)


if __name__ == "__main__":
    x = ListeyeEkle ("")
    x.ekle ((170, 57))
    x.ekle (2019-1957)
    x.ekle (57+4)
    x.ekle ("M.Nihat Yava�")
    x.ekle ([1957, 4, 17])
    x.ekle ({"Ye�ilyurt", "Malatya"})

    print ("Standart list'e null, t�ple, aritmetik i�lem, dizge, liste, k�me vb ekleme:\n", x)



"""��kt�:
>python p_14204.py
Standart list'e null, t�ple, aritmetik i�lem, dizge, liste, k�me vb ekleme:
 [(170, 57), 62, 61, 'M.Nihat Yava�', [1957, 4, 17], {'Malatya', 'Ye�ilyurt'}]
"""