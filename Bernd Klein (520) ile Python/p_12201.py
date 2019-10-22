# coding:iso-8859-9 Türkçe
# p_12201.py: Fonksiyon içi lokal ve genel değişkenlerin eklenmesinin yan etkilerini giderme örneği.

def örnek (x):
    print ("\nFonksiyon içi:\nx=", x, "id=", id (x) )
    x = 1957
    print ("x=", x, "id=", id (x) )

x = 2019
print ("Ana program:\nx=", x, "id(x)=", id (x) )

örnek (x)

print ("\nTekrar ana program:\nx=", x, "id(x)=", id (x) )
#---------------------------------------------------------------------------------------------------------

def yanEtkisiz (x):
    print ("\nFonksiyon içinde, önce:", x)
    x = x + ["Malatya", "Bursa"] # Ekleme ve atama işlemi...
    print ("Fonksiyon içinde, sonra:", x)

şehirler = ["Ankara", "İstanbul", "İzmir", "Mersin"]
print ("-"*70, "\nAna programda, önce:", şehirler)

yanEtkisiz (şehirler)

print ("\nAna programda, sonra:", şehirler)
#---------------------------------------------------------------------------------------------------------

def yanEtkili (x):
    print ("\nFonksiyon içinde, önce:", x)
    x += ["Malatya", "Bursa"] # Artış operatörlü işlem...
    print ("Fonksiyon içinde, sonra:", x)

şehirler = ["Ankara", "İstanbul", "İzmir", "Mersin"]
print ("-"*70, "\nAna programda, önce:", şehirler)

yanEtkili (şehirler[:]) # Tek boyutlu listenin sığ kopyası gönderilir...

print ("\nAna programda, sonra:", şehirler)


"""Çıktı:
>python p_12201.py
Ana program:
x= 2019 id(x)= 27812848

Fonksiyon içi:
x= 2019 id= 27812848
x= 1957 id= 6541872

Tekrar ana program:
x= 2019 id(x)= 27812848
----------------------------------------------------------------------
Ana programda, önce: ['Ankara', 'İstanbul', 'İzmir', 'Mersin']

Fonksiyon içinde, önce: ['Ankara', 'İstanbul', 'İzmir', 'Mersin']
Fonksiyon içinde, sonra: ['Ankara', 'İstanbul', 'İzmir', 'Mersin', 'Malatya', 'Bursa']

Ana programda, sonra: ['Ankara', 'İstanbul', 'İzmir', 'Mersin']
----------------------------------------------------------------------
Ana programda, önce: ['Ankara', 'İstanbul', 'İzmir', 'Mersin']

Fonksiyon içinde, önce: ['Ankara', 'İstanbul', 'İzmir', 'Mersin']
Fonksiyon içinde, sonra: ['Ankara', 'İstanbul', 'İzmir', 'Mersin', 'Malatya', 'Bursa']

Ana programda, sonra: ['Ankara', 'İstanbul', 'İzmir', 'Mersin']
"""