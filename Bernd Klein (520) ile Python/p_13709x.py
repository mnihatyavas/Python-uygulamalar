# coding:iso-8859-9
# p_13709x.py: genel, _korunaklı ve __özel tip değişkenli sınıf nesnesi alt-örneği.

class A():
    def __init__ (self):
        self.__özel = "Ben herkese kapalı sınıfiçi özel bir tip değişkeni özelliğiyim."
        self._korunaklı = "Ben sadece altsıflara açık korunaklı bir tip değişkeni özelliğiyim."
        self.genel = "Ben herkese açık genel bir tip değişkeni özelliğiyim."
