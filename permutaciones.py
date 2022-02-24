#agregar en todos las posibles posiciones de una lista un nueva dato
def potencia(c):
    if(len(c)==0):
        return [[]]
    else:
        r = potencia(c[:-1])
        return r + [listaC + [c[-1]]  for listaC in r]    


def agregarDato(n, lista, i):
    return lista[:i]+[n]+lista[i:]

listaPruebaDatos = [1,2,3]

print(potencia(listaPruebaDatos))
#listaPruebaDatos = agregarDato(55,listaPruebaDatos,2)
#print(listaPruebaDatos)

[[1, 2],  [1, 3], [2, 3]]
[[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]

def agregarDatoPosicionesPosibles(n, lista):
    return [agregarDato(n,lista,i) for i in range(len(lista)+1)]

#listaPruebaDatos = agregarDatoPosicionesPosibles(55,listaPruebaDatos)
#print(listaPruebaDatos)

#Método recursivo para generar todas las permutaciones

def permutacion(lista):
    if(len(lista)==0):
        return [[]]
    else:        
        return sum([agregarDatoPosicionesPosibles(lista[0],i) for i in permutacion(lista[1:])],[])

def permutacionR(lista,r):
    return sum([permutacion(datos) for datos in potencia(lista) if len(datos)== r],[])


    
listaPermutacion = permutacion(listaPruebaDatos)
print(listaPermutacion)
listaPruebaDatos2 = permutacionR(listaPruebaDatos,2)
print(listaPruebaDatos2)
[[1, 2], [2, 1], [1, 3], [3, 1], [2, 3], [3, 2]]
