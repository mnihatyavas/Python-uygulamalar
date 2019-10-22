# coding:iso-8859-9 Türkçe
# p_21301.py: Teypten okunan bit verilerini tümleyen Tape ve TuringMachine örneği.

from p_21301x import TuringMachine as TM

initial_state = "init"
transition_function = {
    ("init","0"):("init", "1", "R"),
    ("init","1"):("init", "0", "R"),
    ("init"," "):("final"," ", "N") }
final_states = {"final"}

t = TM (
    "0100111000111101100111000101000111101010101 ",
    initial_state = initial_state,
    final_states = final_states,
    transition_function = transition_function )

print ("Teypten okunan veriler:\n" + t.get_tape())

while not t.final(): t.step()

print ("\nTM tümleme sonucu:")    
print (t.get_tape())



"""Çıktı:
>python p_21301.py
Teypten okunan veriler:
0100111000111101100111000101000111101010101

TM tümleme sonucu:
1011000111000010011000111010111000010101010
"""