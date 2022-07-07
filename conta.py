
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo do {} é: {}".format(self.__titular, self.__saldo))

    def saca(self, valor):
        self.__saldo -= valor
        print("Saldo após o saque do {} é: {}".format(self.__titular, self.__saldo))

    def depoista(self, valor):
        self.__saldo += valor
        print("Saldo após o depósito do {} é: {}".format(self.__titular, self.__saldo))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite

    def set_limite(self, valor):
        self.__limite = valor

