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


Daniela = Usuario()
Isabel = Usuario()
Viviana = Usuario()

print("Detalles movimientos Daniela")
Daniela.deposito(300).deposito(200).deposito(450).retiro(320).mostrar_info_cuenta()

print("Detalles movimientos Isabel")
Isabel.deposito(100).deposito(250).retiro(160).retiro(220).mostrar_info_cuenta()

print("Detalles movimientos Viviana")
Viviana.deposito(250).retiro(160).retiro(220).retiro(70).mostrar_info_cuenta()