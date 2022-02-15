B = [1,2,3,4]

def potencia(c):
    if(len(c)==0):
        return [[]]
    else:
        r = potencia(c[:-1])
        return r + [listaC + [c[-1]]  for listaC in r]    

print(potencia(B))

#Resultado

[[], 
 [1], 
 [2], 
 [1, 2], 
 [3], 
 [1, 3], 
 [2, 3], 
 [1, 2, 3],
 [4], 
 [1, 4],
 [2, 4],
 [1, 2, 4], 
 [3, 4], 
 [1, 3, 4], 
 [2, 3, 4],
 [1, 2, 3, 4]]
        
