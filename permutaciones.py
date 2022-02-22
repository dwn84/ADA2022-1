#agregar en todos las posibles posiciones de una lista un nueva dato

def agregarDato(n, lista, i):
    return lista[:i]+[n]+lista[i:]

listaPruebaDatos = [1,2,3]
#listaPruebaDatos = agregarDato(55,listaPruebaDatos,2)
#print(listaPruebaDatos)

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

    
listaPruebaDatos = permutacion(listaPruebaDatos)
print(listaPruebaDatos)
