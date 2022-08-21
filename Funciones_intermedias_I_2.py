estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary(estudiantes):
    for diccionario in estudiantes: #esto es para establecer que recorra la lista estudiantes
        nombre = diccionario["first_name"] #definimos nombre como variable, para que diccionario guarde "first name" de la lista se repite abajo
        apellido = diccionario["last_name"]
        print(f'first_name - {nombre}, last_name - {apellido}')#se imprime first name y las name. F es para añadir un formato de impresión.

iterateDictionary(estudiantes)#acá no estoy definiendo, sino que estoy usándola.



# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
# un bonus para que aparezcan exactamente como se muestra a continuación)
#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel
