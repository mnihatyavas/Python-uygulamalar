# coding:iso-8859-9 T�rk�e
# p_10503.py: Tek, �ift ve �� t�rnakl� dizgeler ve endeksli dizge i�lemleri �rne�i.

dizge1 = 'Bu tek t�rnakl� bir dizgedir.'
dizge2 = "Bu ise �ift t�rnakl� bir dizgedir."
dizge3 = """
    Bu dizgenin sat�r say�s� konusunda bir sorun yoktur.
    Zira 3-�ift t�rnakl� dizgelerde, sat�rlar nas�l �ekillendirilmi�se
    ��kt�ya da aynen �yle alt alta olacak �ekilde yans�yacakt�r."""
print ("Tek t�rnakl� dizge: ", dizge1)
print ("�ift t�rnakl� dizge: ", dizge2)
print ("3-�ift t�rnakl� dizge: ", dizge3)

print ('\nTek t�rnakl�da yine tek t�rnakl� \'al�nt�\' esc karakteriyle m�mk�nd�r.')
print ("�ift t�rnakl�da tek t�rnakl� 'al�nt�' aynen m�mk�nd�r.")
print ("�ift t�rnakl�da �ift t�rnakl� \"al�nt�\" yine esc karakteriyle m�mk�nd�r.")
print ("""3-�ift t�rnakl�da 'tek t�rnakl�' veya "�ift t�rnakl�" al�nt� aynen ve hi� sorun de�ildir.""")
print ('''3-tek t�rnakl�da da 'tek t�rnakl�' veya "�ift t�rnakl�" al�nt� aynen ve hi� sorun de�ildir.''')

dizge1 = "M.Nihat Yava�"
print ("\ndizge1 =", dizge1)
for i in range (len (dizge1)): print (i, ":", dizge1[i], sep="", end=" ") # �leri endeks: 0-->12
print()
for i in range (-1, -len (dizge1)-1, -1): print (i, ":", dizge1[i], sep="", end=" ") # Geri endeks: -1-->-13
print()
print ("\nDizgeleri " + "arka arkaya " + "ekleyebilirsiniz.")
print ("Dizgeler * ile tekrarlat�labilir:",  "*_*"*10)
print ("Dizgelerin herhangi tek bir karakterine endeksiyle eri�ilebilir:", dizge1[8])
print ("Dizgelerin herhangi �oklu karakterli bir dilimi al�nabilir:", dizge1[2:7])
print ("Dizgelerin ebat� bellidir:", len (dizge1) )

print()
try:
    print ("Dizgeler de�i�tirilemez, hata verirler:")
    dizge1[2] = "K"
except Exception:
    print ("Dizgeleri de�i�tiremez, ancak yeniden referanslayabilirsiniz.")
    dizge1 = "M.Kemal Atat�rk"
    print (dizge1)

print()
dizge1 = "Merhaba Nihat"
dizge2 = "Merhaba Nihat"
print (dizge1 is dizge2) # "is" operat�r� ayn� bellek adresinin farkl� de�i�kenlerce referanslanmas�d�r: True
print (dizge1 == dizge2) # "==" operat�r� ise 2 ayr� de�er i�eren de�i�kenlerin ayn�l���d�r: True

print ("\nb: Byte dizgesi sadece ascii 0->128 karakterleri i�erebilir.")
x = b"Merhaba M.Nihat" # �mrahim �mer �en�ay�r"
t = str (x)
u = t.encode ("UTF-8")
print (x, t, u)


"""��kt�:
>python p_10503.py
Tek t�rnakl� dizge:  Bu tek t�rnakl� bir dizgedir.
�ift t�rnakl� dizge:  Bu ise �ift t�rnakl� bir dizgedir.
3-�ift t�rnakl� dizge:
    Bu dizgenin sat�r say�s� konusunda bir sorun yoktur.
    Zira 3-�ift t�rnakl� dizgelerde, sat�rlar nas�l �ekillendirilmi�se
    ��kt�ya da aynen �yle alt alta olacak �ekilde yans�yacakt�r.

Tek t�rnakl�da yine tek t�rnakl� 'al�nt�' esc karakteriyle m�mk�nd�r.
�ift t�rnakl�da tek t�rnakl� 'al�nt�' aynen m�mk�nd�r.
�ift t�rnakl�da �ift t�rnakl� "al�nt�" yine esc karakteriyle m�mk�nd�r.
3-�ift t�rnakl�da 'tek t�rnakl�' veya "�ift t�rnakl�" al�nt� aynen ve hi� sorunde�ildir.
3-tek t�rnakl�da da 'tek t�rnakl�' veya "�ift t�rnakl�" al�nt� aynen ve hi� sorun de�ildir.

dizge1 = M.Nihat Yava�
0:M 1:. 2:N 3:i 4:h 5:a 6:t 7:  8:Y 9:a 10:v 11:a 12:�
-1:� -2:a -3:v -4:a -5:Y -6:  -7:t -8:a -9:h -10:i -11:N -12:. -13:M

Dizgeleri arka arkaya ekleyebilirsiniz.
Dizgeler * ile tekrarlat�labilir: *_**_**_**_**_**_**_**_**_**_*
Dizgelerin herhangi tek bir karakterine endeksiyle eri�ilebilir: Y
Dizgelerin herhangi �oklu karakterli bir dilimi al�nabilir: Nihat
Dizgelerin ebat� bellidir: 13

Dizgeler de�i�tirilemez, hata verirler:
Dizgeleri de�i�tiremez, ancak yeniden referanslayabilirsiniz.
M.Kemal Atat�rk

True
True

b: Byte dizgesi sadece ascii 0->128 karakterleri i�erebilir.
b'Merhaba M.Nihat' b'Merhaba M.Nihat' b"b'Merhaba M.Nihat'"

"""