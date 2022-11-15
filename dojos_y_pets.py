class mascota:

    def __init__(self, nombre , tipo, trucos, sonido):
        self.nombre = nombre
        self.tipo = tipo
        self.trucos = trucos
        self.salud= 100
        self.energia = 50
        self.sonido = sonido

    def dormir(self):
        self.energia += 25
        return self

    def comer(self):
        self.energia += 5
        self.salud+= 10
        return self

    def jugar(self):
        self.salud+= 5
        self.energia -= 15
        return self

    def sonido(self):
        print(self.sonido)


class Ninja:

    def __init__(self, nombre, apellido , golosinas, mascota_comida, mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.golosinas = golosinas
        self.mascota_comida = mascota_comida
        self.mascota = mascota

    def caminar(self):
        self.mascota.jugar()
        return self

    def alimentar(self):

        if len(self.mascota_comida) > 0:
            comida = self.mascota_comida.pop()
            print(f"Alimentar a  {self.mascota.nombre} con {comida}!")
            self.mascota.comer()
        else:
            print("Sera necesario mas comida para mascotas")
        return self

    def bañar(self):
        self.mascota.sonido()

golosinas = ['Churu','Comida humeda',"Galletas"]
mascota_comida = ['Pellet','Huesitos']

Lulu = mascota("Lulu","Perro",['Lulu baila'],"Ladra")

Viviana  = Ninja("Viviana ","Figueroa", golosinas, mascota_comida, Lulu)

Viviana .alimentar();
Viviana .alimentar();
Viviana .alimentar();

