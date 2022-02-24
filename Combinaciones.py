class Persona:
    
    def __init__(self,nombre,sexo):
        self.nombre = nombre
        self.sexo = sexo
        
        
a = Persona('Diego','M')
b = Persona('Daniel','M')
c = Persona('Michell','F')
d = Persona('Jorge','M')
e = Persona('Luissa','F')
f = Persona('Edwin','M')
g = Persona('Melquiadez','M')
h = Persona('Esperanza','F')

personitas = [a,b,c,d,e,f,g,h]
def soloHombres(listaP):    
    if (listaP.sexo == "M"):
        return True
    else:
        return False
  
#Lista sin mujeres
filtered = filter(soloHombres, personitas)


def mostrarNombrepersona(listapersonas):
    listaNombres =[]
    for p in listapersonas:
        listaNombres.append(p.nombre)
    return listaNombres

print(mostrarNombrepersona(personitas))

print(mostrarNombrepersona(filtered))
#Calcular la cantidad total de combinaciones de tamaño específico
def potencia(c):
    if(len(c)==0):
        return [[]]
    else:
        r = potencia(c[:-1])
        return r + [listaC + [c[-1]]  for listaC in r]    



def factorial(n):
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

B = ["Diego", "Daniel", "Cristian", "Michell", "Jorge", "Maria Camila", "Luissa", "Edwin"]

def combinaciones(n,r):
    return [datos for datos in potencia(n) if len(datos)== r]

print(combinaciones(B, 3))

#Experimento combinaciones: pareja, mínimo una mujer
parejasMin1Muj = [['Diego', ' '], 
 ['Daniel', 'Michell'],
 ['Cristian', 'Michell'], 
 ['Michell', 'Jorge'],
 ['Diego', 'Maria Camila'],
 ['Daniel', 'Maria Camila'],
 ['Cristian', 'Maria Camila'], 
 ['Michell', 'Maria Camila'],
 ['Jorge', 'Maria Camila'], 
 ['Diego', 'Luissa'],
 ['Daniel', 'Luissa'], 
 ['Cristian', 'Luissa'],
 ['Michell', 'Luissa'], 
 ['Jorge', 'Luissa'], 
 ['Maria Camila', 'Luissa'],  
 ['Michell', 'Edwin'],
  ['Maria Camila', 'Edwin'],
 ['Luissa', 'Edwin']]
print(f" total de parejas : {len(parejasMin1Muj)}")

def totalCombinaciones(n,r):
    return (factorial(n))/(factorial(r)*factorial(n-r))

#ingredientes para el sanduche:tomate, lechuga, cebolla, pepino
#Solo puede seleccionar dos vegetales
#¿Cuántas posibilidades tenemos?
print(f"Total de posibilidades del sanduche: {totalCombinaciones(3,2)}" )
#Total de posibilidades del sanduche: 6.0

#¿Cuáles posibilidades existen para el sanduche?
print(combinaciones(B, 3))


parejas = combinaciones(personitas, 2)
parejasValidas = []
#Validación de parejas
for posiblePareja in parejas:
    contadorMujeres = 0
    for personaPareja in posiblePareja:
        if(personaPareja.sexo=='F'):
            contadorMujeres = contadorMujeres + 1
        
    if(contadorMujeres>0):
        parejasValidas.append(posiblePareja)
        
print("Posibles parejas:")        
for p in parejas:
    print(mostrarNombrepersona(p))
print("Parejas que cumplen la condición:")
print(len(parejasValidas))        
for p in parejasValidas:
    print(mostrarNombrepersona(p))

