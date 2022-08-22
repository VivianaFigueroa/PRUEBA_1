dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(a):
    print(len(dojo["ubicaciones"]), "ubicaciones") 
    for a in dojo["ubicaciones"]: 
        print(a)
    print("-----------------------------------")
    print(len(dojo["instructores"]),"instructores")
    for a in dojo["instructores"]: 
        print(a)

printInfo(dojo)