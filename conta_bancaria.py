class ContaBancaria:
    def __init__(self,numero,titular,saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
    def deposita(self,valor):
        self.saldo += valor     