class CuentaBancaria:

    def __init__(self, tasa_interes=0.15, balance =1000):
        self.tasa_interes = tasa_interes
        self.balance = balance

    def deposito(self, amount):
        self.balance = self.balance + amount
        print (f' DEPOSITO REALIZADO')
        return self

    def retiro(self, amount):
        self.balance = self.balance - amount
        print (f' RETIRO REALIZADO')
        return self

    def mostrar_info_cuenta(self):
        print(f'BALANCE: {self.balance} \n Interes: {self.tasa_interes}')
        return self

    def generar_interes(self):
        new_interes_amount = self.balance * self.tasa_interes
        print (f' INTERES ADQUIRIDO: {new_interes_amount}')
        self.balance = self.balance + new_interes_amount
        return self

CuentaBancaria1 = CuentaBancaria()

print("Detalles movimientos Cuenta bancaria 1")
CuentaBancaria1.deposito(300).deposito(200).deposito(450).retiro(320).generar_interes().mostrar_info_cuenta()

print("Detalles movimientos Cuenta bancaria 2")
CuentaBancaria2 = CuentaBancaria(tasa_interes=0.22, balance=1500)
CuentaBancaria2.deposito(500).deposito(3000).retiro(1500).retiro(500).retiro(100).retiro(400).generar_interes().mostrar_info_cuenta()
