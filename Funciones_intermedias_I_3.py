estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary2(estudiantes):
    for diccionario in estudiantes: 
        nombre = diccionario["first_name"]
        print(f'{nombre}')

iterateDictionary2(estudiantes)

def iterateDictionary2(estudiantes):
    for diccionario in estudiantes: 
        apellido = diccionario["last_name"]
        print(f'{apellido}')

iterateDictionary2(estudiantes)
