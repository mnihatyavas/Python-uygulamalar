# coding:iso-8859-9 Türkçe
# p_13202.py: C, F, ve K dereceleri normal def ve anonim lambda ile map haritalamayala çevirme örneği.

def fahrenhayt (D): return ((float (9) / 5) * D + 32)
def kelvin (D): return ((D + 459.4) * float (5) / 9)
def selsiyüs (D): return (D - 273)

dereceler = (-273, 0, 32, 100, 500)
F = list (map (fahrenhayt, dereceler) ) # dereceler listesini tek tek fahrenhayt'a çevirir ve listeler...
K = list (map (kelvin, F) )
S = list (map (selsiyüs, K) )

print ("(-273, 0, 32, 100, 500) derecelerin normal fonksiyonla harita'lanması:", "\n", "-"*70, sep="")
print ("S'ler fahrenhayt F'ye:", F )
print ("F'ler kelvin K'ye:", K )
print ("K'ler tekrar selsiyüs S'ye:", S )
#--------------------------------------------------------------------------------------------------------

F = list (map (lambda x: (float (9) / 5) * x + 32, dereceler)) # Doğrudan lambdalı map listesi elde edilmesi...
K = list (map (lambda x: (x + 459.4) * float (5) / 9, F))
S = list (map (lambda x: x - 273, K))

print ("\n(-273, 0, 32, 100, 500) derecelerin lambda anonim fonksiyonla harita'lanması:", "\n", "-"*77, sep="")
print ("S'ler fahrenhayt F'ye:", F )
print ("F'ler kelvin K'ye:", K )
print ("K'ler tekrar selsiyüs S'ye:", S )


"""Çıktı:
>python p_13202.py
(-273, 0, 32, 100, 500) derecelerin normal fonksiyonla harita'lanması:
----------------------------------------------------------------------
S'ler fahrenhayt F'ye: [-459.40000000000003, 32.0, 89.6, 212.0, 932.0]
F'ler kelvin K'ye: [-3.157967714489334e-14, 273.0, 305.0, 373.0, 773.0]
K'ler tekrar selsiyüs S'ye: [-273.00000000000006, 0.0, 32.0, 100.0, 500.0]

(-273, 0, 32, 100, 500) derecelerin lambda anonim fonksiyonla harita'lanması:
-----------------------------------------------------------------------------
S'ler fahrenhayt F'ye: [-459.40000000000003, 32.0, 89.6, 212.0, 932.0]
F'ler kelvin K'ye: [-3.157967714489334e-14, 273.0, 305.0, 373.0, 773.0]
K'ler tekrar selsiyüs S'ye: [-273.00000000000006, 0.0, 32.0, 100.0, 500.0]
"""