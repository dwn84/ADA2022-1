
def WorstBubbleSort(listData,comparaciones):
    
    for i in range(len(listData)-1):
         for j in range((len(listData)-1)):
            if(listData[j]>listData[j+1]):                
                listData[j],listData[j+1]= listData[j+1],listData[j]
            comparaciones = comparaciones + 1                
    print(comparaciones)
    return listData

def bubbleSort(listData,comparaciones):
    
    for i in range(len(listData)-1):
         for j in range((len(listData)-1)-i):
            if(listData[j]>listData[j+1]):                
                listData[j],listData[j+1]= listData[j+1],listData[j]
            comparaciones = comparaciones + 1                
    print(comparaciones)
    return listData


def bubbleSortCheckOrdered(listData,comparaciones):
    
    for i in range(len(listData)-1):
        sorted = True
        for j in range((len(listData)-1)-i):
           if(listData[j]>listData[j+1]):                
               listData[j],listData[j+1]= listData[j+1],listData[j]
               sorted = False
           comparaciones = comparaciones + 1
        if(sorted):
            break
               
    print(comparaciones)
    
    return listData

def recursiveBubbleSort(listData):
    return recursiveBubbleSortI(listData,len(listData),0)

def recursiveBubbleSortI(listData,n,contador):
    if (n==1):
        return listData

    for j in range(n - 1):
       if(listData[j]>listData[j+1]):                
           listData[j],listData[j+1]= listData[j+1],listData[j]
       contador = contador + 1   
    print(contador)
    return recursiveBubbleSortI(listData,n - 1, contador)

def insertSort(listData):
    comparaciones = 0
    n = len(listData)
    for i in range(1,n):
        aux = listData[i]
        j = i
        while(j>0 and aux<listData[j-1]):
            listData[j]=listData[j-1]
            j = j - 1
            comparaciones = comparaciones + 1
        listData[j] = aux
    print(f"Iteraciones método inserción:{comparaciones}")
    return listData
            
def selectSort(listData):
    comparaciones = 0
    n = len(listData)
    for i in range(0,n):
        min = i
        for j in range(i+1,n):
            if(listData[j]<listData[min]):
                min = j
            comparaciones = comparaciones + 1
        listData[i],listData[min]= listData[min],listData[i]
        
    print(f"Iteraciones método selección:{comparaciones}")
    return listData    

def quick_sort(listData):
    n = len(listData)
    if n<2:
        return listData    
    
    
    frontier = 0
    
    for i in range(frontier+1,n):
        if(listData[1]<listData[0]):
            frontier += 1
            listData[i],listData[frontier] = listData[frontier],listData[i]
    listData[0], listData[frontier]= listData[frontier], listData[0]

    left = quick_sort(listData[0:frontier])
    right= quick_sort(listData[frontier+1:])
    
    listData = left + [listData[frontier]] + right
    return listData

#pendiente por validar
        
        
#miLista = [1,2,3,4,5,6,7,8,9]#el mejor caso posible
miLista = [11,10,9,8,7,6,5,4,3,2,1]#el peor caso posible
miLista1 = miLista.copy()#el peor caso posible
miLista2 = miLista.copy()#el peor caso posible
miLista3 = miLista.copy()#el peor caso posible
miLista4 = miLista.copy()#el peor caso posible
milista5 = miLista.copy()
milista6 = miLista.copy()

print(WorstBubbleSort(miLista,0))
print(bubbleSort(miLista1,0))
print(bubbleSortCheckOrdered(miLista2,0))
print(recursiveBubbleSort(miLista3))
print(insertSort(miLista4))
print(selectSort(milista5))
print("Quick Sort")
print(quick_sort(milista6))
