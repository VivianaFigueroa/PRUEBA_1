#Básico: imprime todos los números enteros del 0 al 150.
for x in range(0, 151):
    print(x)
print("**"*20)


# Multiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1000
for x in range(5, 1001, 5):
    print(x)
print("**"*20)


# Contar, a la manera del Dojo: imprime números enters del 1 al 100. Si es divisible por 5, imprime "Coding" en su lugar. Si es divisible por 10, imprime "Coding Dojo"
for x in range(1,101):
    if x %10==0:
        print(x)
        print("Coding Dojo")
    elif x %5==0:
        print(x)
        print("Coding")
print("**"*20)


#Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500,000, e imprime la suma final.
ContadorImpares = 0
for x in range(0,500000):
    if x %2==1:
        ContadorImpares = ContadorImpares + x
        print(x)
print(ContadorImpares)
print("**"*20)


#Cuenta regresiva de a 4: imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.
for x in range(2018,0,-4):
        print(x)
print("**"*20)


#Contador flexible: establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, imprime solo los enteros que sean múltiplos de mult.
lowNum = 4
highNum = 20
mult = 2
for x in range(lowNum, highNum):
    if x %mult==0:
        print(x)
print("**"*20)







