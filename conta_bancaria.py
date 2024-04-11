class ContaBancaria:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor 

    def exibir_detalhes(self):
        print("numero da conta:", self.numero)
        print("titular:", self.titular)
        print("saldo:", self.saldo)

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else: 
            print("vc é pobre")     

numero_conta = input("digite o numero da conta")
titular_conta = input("digite o titular da conta")
saldo_inicial = float(input("digite o saldo inicual da conta").replace(",","."))               
conta_do_raphaelo = ContaBancaria(numero_conta, titular_conta, saldo_inicial)
valor_deposito = float(input("digite o valor a ser depositado").replace(",","."))
valor_saque = float(input("digite o valor a serr sacado").replace(",","."))

conta_do_raphaelo.depositar(valor_deposito)
conta_do_raphaelo.sacar(valor_saque)
conta_do_raphaelo.exibir_detalhes()