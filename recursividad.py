import time

#Generar recursivamente la potencia de dos números
#a^b

def potencia(a,b):
    #plantear casos base
    if(b == 0):
        return 1
    elif (a <= 0 and a<=1):
        return a
    elif (b == 1):
        return a
    #llamada recursiva
    else:
        return a * potencia(a , b - 1)
    
print(potencia(0,5))

#ejemplo pictórico de recursividad indirecta
def buscarNodo(a):
    buscarNodoRec(r,a)
    
def buscarNodoRec(raiz,a):
    buscarNodoRec(raiz+siguiente,a):
    
#Análisis fibonacci

#Comportamiento no lineal
def fibo1(n):
    #caso base
    if(n<2):
        return n
    else:
        return fibo1(n-1) + fibo1(n-2)

#Optimización con Memoización
def fibo2(n,datos):
    #caso base
    if(n<2):
        return n
    elif n in datos:
        return datos[n]
    else:
        datos[n] = fibo2(n-1,datos) + fibo2(n-2,datos)
        return datos[n]

#Perspectiva cíclica
def fibo3(n, a, b):
#caso base
    if(n<2):
        return a
    else:
        return fibo3(n-1,b,a+b)

#Medición de tiempo de cada método Fibo

tiempoInicial=time.time()

diccionario = {}

#print(fibo1(40))
#print(fibo2(40,diccionario))
print(fibo3(41,0,1))

tiempoFinal=time.time()

tiempoTotal=tiempoFinal - tiempoInicial

print("Tiempo de ejecución total:{}". format(tiempoTotal))
    
#recursividad mutua...
