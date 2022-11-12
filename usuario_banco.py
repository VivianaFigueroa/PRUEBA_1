class CuentaBancaria:

    def __init__(self, tasa_interes=0.15, balance =1000):
        self.tasa_interes = tasa_interes
        self.balance = balance

    def deposito(self, amount):
        print ('DEPOSITO')
        self.balance = self.balance + amount

    def retiro(self, amount):
        print('RETIRO')
        self.balance = self.balance - amount

    def mostrar_info_cuenta(self):
        print(f'BALANCE: {self.balance} \n Interes: {self.tasa_interes}')

    def generar_interes(self):
        print('GENERAR INTERES')
        new_interes_amount = self.balance * self.tasa_interes
        print (f' INTERES ADQUIRIDO: {new_interes_amount}')
        self.balance = self.balance + new_interes_amount

class Usuario:
    def __init__(self, balance = 100):
        self.account = CuentaBancaria(balance=1200)

    def deposito(self, amount):
        self.account.deposito(amount)
        return self

    def retiro(self, amount):
        self.account.retiro(amount)
        return self
    
    def mostrar_info_cuenta(self):
        self.account.mostrar_info_cuenta()
        return self


usuario1 = Usuario()
usuario2 = Usuario()
usuario3 = Usuario()

print("Detalles movimientos usuario1")
usuario1.deposito(300)
usuario1.deposito(200)
usuario1.deposito(450)
usuario1.retiro(320)
usuario1.mostrar_info_cuenta()

print("Detalles movimientos usuario2")
usuario2.deposito(100)
usuario2.deposito(250)
usuario2.retiro(160)
usuario2.retiro(220)
usuario2.mostrar_info_cuenta()

print("Detalles movimientos usuario3")
usuario3.deposito(250)
usuario3.retiro(160)
usuario3.retiro(220)
usuario3.retiro(70)
usuario3.mostrar_info_cuenta()