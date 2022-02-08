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
    
#recursividad mutua...
