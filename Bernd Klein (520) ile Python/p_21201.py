# coding:iso-8859-9 Türkçe
# p_21201.py: Girilen (İng.) cümlenin olumlu, olumsuz ve hatalı anlam içerdiğinin tespiti örneği.

from p_21201x import StateMachine

positive_adjectives = ["great","super", "fun", "entertaining", "easy"]
negative_adjectives = ["boring", "difficult", "ugly", "bad"]

def start_transitions (txt):
    splitted_txt = txt.split (None,1)
    word, txt = splitted_txt if len (splitted_txt) > 1 else (txt,"")
    if word == "Python": newState = "Python_state"
    else: newState = "error_state"
    return (newState, txt)

def python_state_transitions (txt):
    splitted_txt = txt.split (None,1)
    word, txt = splitted_txt if len (splitted_txt) > 1 else (txt,"")
    if word == "is": newState = "is_state"
    else: newState = "error_state"
    return (newState, txt)

def is_state_transitions (txt):
    splitted_txt = txt.split (None,1)
    word, txt = splitted_txt if len (splitted_txt) > 1 else (txt,"")
    if word == "not": newState = "not_state"
    elif word in positive_adjectives: newState = "pos_state"
    elif word in negative_adjectives: newState = "neg_state"
    else: newState = "error_state"
    return (newState, txt)

def not_state_transitions (txt):
    splitted_txt = txt.split (None,1)
    word, txt = splitted_txt if len (splitted_txt) > 1 else (txt,"")
    if word in positive_adjectives: newState = "neg_state"
    elif word in negative_adjectives: newState = "pos_state"
    else: newState = "error_state"
    return (newState, txt)

def neg_state (txt):
    print ("Hallo")
    return ("neg_state", "")


if __name__== "__main__":
    m = StateMachine()

    m.add_state ("Start", start_transitions)
    m.add_state ("Python_state", python_state_transitions)

    m.add_state ("is_state", is_state_transitions)
    m.add_state ("not_state", not_state_transitions)

    m.add_state ("pos_state", None, end_state=1)
    m.add_state ("neg_state", None, end_state=1)
    m.add_state ("error_state", None, end_state=1)

    m.set_start ("Start")

    m.run ("Python great")
    m.run ("Python great is")
    m.run ("Python is great")
    m.run ("Python is difficult")
    m.run ("Python is not bad")
    m.run ("Python is not super")
    m.run ("Perl is ugly")



"""Çıktı:
>python p_21201.py
Cümle tahlil sonucu [Python great]: ERROR_STATE
Cümle tahlil sonucu [Python great is]: ERROR_STATE
Cümle tahlil sonucu [Python is great]: POS_STATE
Cümle tahlil sonucu [Python is difficult]: NEG_STATE
Cümle tahlil sonucu [Python is not bad]: POS_STATE
Cümle tahlil sonucu [Python is not super]: NEG_STATE
Cümle tahlil sonucu [Perl is ugly]: ERROR_STATE
"""