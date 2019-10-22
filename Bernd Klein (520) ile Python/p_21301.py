# coding:iso-8859-9 T�rk�e
# p_21301.py: Teypten okunan bit verilerini t�mleyen Tape ve TuringMachine �rne�i.

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

print ("\nTM t�mleme sonucu:")    
print (t.get_tape())



"""��kt�:
>python p_21301.py
Teypten okunan veriler:
0100111000111101100111000101000111101010101

TM t�mleme sonucu:
1011000111000010011000111010111000010101010
"""