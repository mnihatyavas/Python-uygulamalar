# coding:iso-8859-9 T�rk�e
# p_11102.py: De�i�ir ve de�i�mez k�me, silme ve kopyalama �rne�i.

ba�kentler = ["Ankara", "Atina", "Londra", "Berlin", "Paris", "Ankara", "Roma"]
k�me1 = set (ba�kentler)
k�me1.add ("Madrid")
print ("\nYal�n de�i�ir k�meye eleman eklenebilir:", k�me1)

k�me2 = frozenset (ba�kentler)
print ("\nDonuk de�i�mez k�meye eleman eklenemez:", k�me2)
#-----------------------------------------------------------------------------------------------

s�fatlar = {"ucuz", "pahal�", "de�erli", "ekonomik", "g�zel"}
print ("\nSet k�meler s�zl�k gibi ancak anahtars�z tan�mlanabilirler: ", s�fatlar, "\nTip: ", type (s�fatlar), sep="")

s�fatlar.clear()
print ("\n'clear' ile k�me elemanlar� hepten silinir:",  s�fatlar)
#-----------------------------------------------------------------------------------------------

k�me3 = k�me1
k�me4 = k�me1.copy()

k�me1.clear()
print ("\nElemanlar� temizlenen kaynak k�me kopyas�:", k�me1)
print ("Kaynaktan atamal� k�me:", k�me3)
print ("Kaynaktan copy'li k�me:", k�me4)


"""��kt�:
>python p_11102.py

Yal�n de�i�ir k�meye eleman eklenebilir: {'Paris', 'Roma', 'Berlin', 'Londra', 'Atina', 'Madrid', 'Ankara'}

Donuk de�i�mez k�meye eleman eklenemez: frozenset({'Paris', 'Roma', 'Berlin', 'Londra', 'Atina', 'Ankara'})

Set k�meler s�zl�k gibi ancak anahtars�z tan�mlanabilirler: {'g�zel', 'pahal�','ucuz', 'ekonomik', 'de�erli'}
Tip: <class 'set'>

'clear' ile k�me elemanlar� hepten silinir: set()

Elemanlar� temizlenen kaynak k�me kopyas�: set()
Kaynaktan atamal� k�me: set()
Kaynaktan copy'li k�me: {'Ankara', 'Paris', 'Atina', 'Madrid', 'Roma', 'Berlin', 'Londra'}
"""