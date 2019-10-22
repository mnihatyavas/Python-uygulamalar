# coding:iso-8859-9 T�rk�e
# p_12201.py: Fonksiyon i�i lokal ve genel de�i�kenlerin eklenmesinin yan etkilerini giderme �rne�i.

def �rnek (x):
    print ("\nFonksiyon i�i:\nx=", x, "id=", id (x) )
    x = 1957
    print ("x=", x, "id=", id (x) )

x = 2019
print ("Ana program:\nx=", x, "id(x)=", id (x) )

�rnek (x)

print ("\nTekrar ana program:\nx=", x, "id(x)=", id (x) )
#---------------------------------------------------------------------------------------------------------

def yanEtkisiz (x):
    print ("\nFonksiyon i�inde, �nce:", x)
    x = x + ["Malatya", "Bursa"] # Ekleme ve atama i�lemi...
    print ("Fonksiyon i�inde, sonra:", x)

�ehirler = ["Ankara", "�stanbul", "�zmir", "Mersin"]
print ("-"*70, "\nAna programda, �nce:", �ehirler)

yanEtkisiz (�ehirler)

print ("\nAna programda, sonra:", �ehirler)
#---------------------------------------------------------------------------------------------------------

def yanEtkili (x):
    print ("\nFonksiyon i�inde, �nce:", x)
    x += ["Malatya", "Bursa"] # Art�� operat�rl� i�lem...
    print ("Fonksiyon i�inde, sonra:", x)

�ehirler = ["Ankara", "�stanbul", "�zmir", "Mersin"]
print ("-"*70, "\nAna programda, �nce:", �ehirler)

yanEtkili (�ehirler[:]) # Tek boyutlu listenin s�� kopyas� g�nderilir...

print ("\nAna programda, sonra:", �ehirler)


"""��kt�:
>python p_12201.py
Ana program:
x= 2019 id(x)= 27812848

Fonksiyon i�i:
x= 2019 id= 27812848
x= 1957 id= 6541872

Tekrar ana program:
x= 2019 id(x)= 27812848
----------------------------------------------------------------------
Ana programda, �nce: ['Ankara', '�stanbul', '�zmir', 'Mersin']

Fonksiyon i�inde, �nce: ['Ankara', '�stanbul', '�zmir', 'Mersin']
Fonksiyon i�inde, sonra: ['Ankara', '�stanbul', '�zmir', 'Mersin', 'Malatya', 'Bursa']

Ana programda, sonra: ['Ankara', '�stanbul', '�zmir', 'Mersin']
----------------------------------------------------------------------
Ana programda, �nce: ['Ankara', '�stanbul', '�zmir', 'Mersin']

Fonksiyon i�inde, �nce: ['Ankara', '�stanbul', '�zmir', 'Mersin']
Fonksiyon i�inde, sonra: ['Ankara', '�stanbul', '�zmir', 'Mersin', 'Malatya', 'Bursa']

Ana programda, sonra: ['Ankara', '�stanbul', '�zmir', 'Mersin']
"""