# coding:iso-8859-9 Türkçe
# p_11101.py: Set kümelerinin dizge, liste, tüple ve tüpleli tüpleden oluşturulması örneği.

# Set küme elemanlarının hash/kıyma sıralamasına Java'da da Python'daki gibi bir türlü akıl erdiremedim!..
# Saptanabilirliğine dair akıl erdiren varsa söylesin de biz de bilelim!..

print ("Dizgeden dönüşen set tikel karakterler kümesi:",
    set ("Bir set tikel matematiksel nesneler kümesidir.") )

print ("\nListeden dönüşen set tikel elemanlar kümesi:",
    set (["C++", "Python", "Java", "Java", "Java Script"]) )

başkentler = ["Ankara", "Atina", "Londra", "Berlin", "Paris", "Ankara", "Roma"]
küme1 = set ((başkentler))
print ("\nTüpleden dönüşen set tikel elemanlar kümesi:",  küme1)

print ("\nTüpleden dönüşen set tüpleli elemanlar kümesi:",
    set ((("Python", "Perl"), ("Paris", "Berlin", "London", ("Python", "Perl")))) )

# print ("\nDeğişir listeli tüpleden DÖNÜŞEMEYEN set tüpleli elemanlar kümesi:", set((["Python","Perl"], ["Paris", "Berlin", "London"], ["Python","Perl"])) )


"""Çıktı:
>python p_11101.py
Dizgeden dönüşen set tikel karakterler kümesi: {'m', 'l', 'n', '.', 'B', 'ü', 's',
't', 'i', 'k', 'a', 'r', 'e', ' ', 'd'}

Listeden dönüşen set tikel elemanlar kümesi: {'Java Script', 'Python', 'C++', 'Java'}

Tüpleden dönüşen set tikel elemanlar kümesi: {'Berlin', 'Londra', 'Ankara',
'Atina', 'Roma', 'Paris'}

Tüpleden dönüşen set tüpleli elemanlar kümesi: {('Python', 'Perl'), ('Paris',
'Berlin', 'London', ('Python', 'Perl'))}
"""