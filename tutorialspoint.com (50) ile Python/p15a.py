# coding:iso-8859-9 Türkçe
# Python 3 - Exceptions Handling

def Kelvin_Fahrenheit (k):
    assert (k >= 0), "Mutlak sıfırdan daha soğuk!"
    return ((k-273)*1.8)+32

def Fahrenheit_Celcius (f):
    assert (f >= -459.5), "Mutlak sıfırdan daha soğuk!"
    return ((5 / 9) * (f - 32));

d = Kelvin_Fahrenheit (273)
print ("Kelvin-->Fahrenheit(273):", d)
print ("Fahrenheit-->Celcius(", d, "): ", Fahrenheit_Celcius (d))
d = int (Kelvin_Fahrenheit (505.708))
print ("\nint(Kelvin-->Fahrenheit(505.78)):", d)
print ("Fahrenheit-->Celcius(", d, "):", Fahrenheit_Celcius (d))
d=Kelvin_Fahrenheit (0)
print ("\nKelvin-->Fahrenheit(0):", Kelvin_Fahrenheit (0))
print ("Fahrenheit-->Celcius(", d, "):", Fahrenheit_Celcius (d))
print ("\nKelvin-->Fahrenheit(-5):", Kelvin_Fahrenheit (-5))
