# coding:iso-8859-9
# p_13709x.py: genel, _korunakl� ve __�zel tip de�i�kenli s�n�f nesnesi alt-�rne�i.

class A():
    def __init__ (self):
        self.__�zel = "Ben herkese kapal� s�n�fi�i �zel bir tip de�i�keni �zelli�iyim."
        self._korunakl� = "Ben sadece alts�flara a��k korunakl� bir tip de�i�keni �zelli�iyim."
        self.genel = "Ben herkese a��k genel bir tip de�i�keni �zelli�iyim."
