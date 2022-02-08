#Análisis a posteriori
import time
import matplotlib.pyplot as g

def comportamientoAlgoritmo(n):
    x = 0
    j = 1
    while(j<n):
    #for j in range(1,n):     
        #for m in range(0,n):
        #print(j)
        j*=2    
        x+=1
    
tiempo = []

for i in range(1,100000000,100):
    tiempoInicial=time.time()
    
    comportamientoAlgoritmo(i)
    
    tiempoFinal=time.time()
    
    tiempoTotal=tiempoFinal - tiempoInicial
    
    tiempo.append(tiempoTotal)
    
g.plot(tiempo)
g.ylabel("Tiempo")
g.xlabel("datos")
g.show()
