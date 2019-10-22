# coding:iso-8859-9 T�rk�e
# p_11101.py: Set k�melerinin dizge, liste, t�ple ve t�pleli t�pleden olu�turulmas� �rne�i.

# Set k�me elemanlar�n�n hash/k�yma s�ralamas�na Java'da da Python'daki gibi bir t�rl� ak�l erdiremedim!..
# Saptanabilirli�ine dair ak�l erdiren varsa s�ylesin de biz de bilelim!..

print ("Dizgeden d�n��en set tikel karakterler k�mesi:",
    set ("Bir set tikel matematiksel nesneler k�mesidir.") )

print ("\nListeden d�n��en set tikel elemanlar k�mesi:",
    set (["C++", "Python", "Java", "Java", "Java Script"]) )

ba�kentler = ["Ankara", "Atina", "Londra", "Berlin", "Paris", "Ankara", "Roma"]
k�me1 = set ((ba�kentler))
print ("\nT�pleden d�n��en set tikel elemanlar k�mesi:",  k�me1)

print ("\nT�pleden d�n��en set t�pleli elemanlar k�mesi:",
    set ((("Python", "Perl"), ("Paris", "Berlin", "London", ("Python", "Perl")))) )

# print ("\nDe�i�ir listeli t�pleden D�N��EMEYEN set t�pleli elemanlar k�mesi:", set((["Python","Perl"], ["Paris", "Berlin", "London"], ["Python","Perl"])) )


"""��kt�:
>python p_11101.py
Dizgeden d�n��en set tikel karakterler k�mesi: {'m', 'l', 'n', '.', 'B', '�', 's',
't', 'i', 'k', 'a', 'r', 'e', ' ', 'd'}

Listeden d�n��en set tikel elemanlar k�mesi: {'Java Script', 'Python', 'C++', 'Java'}

T�pleden d�n��en set tikel elemanlar k�mesi: {'Berlin', 'Londra', 'Ankara',
'Atina', 'Roma', 'Paris'}

T�pleden d�n��en set t�pleli elemanlar k�mesi: {('Python', 'Perl'), ('Paris',
'Berlin', 'London', ('Python', 'Perl'))}
"""