class CuentaBancaria:
    # ¡No olvides agregar algunos valores predeterminados para estos parámetros!
    def __init__(self, tasa_interes=0.15, balance =1000):
        self.tasa_interes = tasa_interes
        self.balance = balance
        # tu código aquí (recuerda, los atributos de instancia van aquí)
        # no te preocupes por la información del usuario aquí; pronto involucraremos la clase de usuario
    def deposito(self, amount):
        print ('DEPOSITO')
        self.balance = self.balance + amount
        # tu código aquí
    def retiro(self, amount):
        print('RETIRO')
        self.balance = self.balance - amount
        # tu código aquí
    def mostrar_info_cuenta(self):
        print(f'BALANCE: {self.balance} \n Interes: {self.tasa_interes}')
        # tu código aquí
    def generar_interes(self):
        print('GENERAR INTERES')
        new_interes_amount = self.balance * self.tasa_interes
        print (f' INTERES ADQUIRIDO: {new_interes_amount}')
        self.balance = self.balance + new_interes_amount
        # tu código aquí

CuentaBancaria1 = CuentaBancaria()
CuentaBancaria1.deposito(200)
CuentaBancaria1.deposito(400)
CuentaBancaria1.deposito(800)
CuentaBancaria1.retiro(1200)
CuentaBancaria1.generar_interes()
CuentaBancaria1.mostrar_info_cuenta()

CuentaBancaria2 = CuentaBancaria(tasa_interes=0.22, balance=1500)
CuentaBancaria2.deposito(500)
CuentaBancaria2.deposito(3000)
CuentaBancaria2.retiro(1500)
CuentaBancaria2.retiro(200)
CuentaBancaria2.retiro(600)
CuentaBancaria2.retiro(700)
CuentaBancaria2.generar_interes()
CuentaBancaria2.mostrar_info_cuenta()