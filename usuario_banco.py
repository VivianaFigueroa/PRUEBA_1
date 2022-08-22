from cuenta_bancaria import CuentaBancaria

class usuario:
    def __init__(self, balance = 200):
        self.account = CuentaBancaria(balance=900)

    def deposito(self, amount):
        self.account.deposito(amount)

    def retiro(self, amount):
        self.account.retiro(amount)
    
    def mostrar_info_cuenta(self):
        self.account.mostrar_info_cuenta()


usuario1 = usuario()
usuario2 = usuario()

usuario1.deposito(300)
usuario2.deposito(500)


usuario1.mostrar_info_cuenta()
usuario2.mostrar_info_cuenta()
