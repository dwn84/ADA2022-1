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

def merge_sort(listData):
    
    if(len(listData)>1):
        mid = len(listData)//2
        L=listData[:mid]
        R=listData[mid:]
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0      
        
        
        while(i<len(L) and j<len(R)):
            if(L[i]<R[j]):
                listData[k]=L[i]
                i = i + 1
            else:
                listData[k]=R[j]
                j = j + 1
            k = k + 1
            
        while(i<len(L)) :            
            listData[k]=L[i]
            i = i + 1
            k = k + 1
            
        while(j<len(R)) :            
            listData[k]=R[j]
            j = j + 1
            k = k + 1
            
    return listData

   

def go_Through_Heap(listData, n):
    for i in range(n,-1,-1):
        validate_Max_Heap(listData,i,n)
        
def validate_Max_Heap(listData,k,n):
    leftChild = (2 * k) + 1
    rightChild = (2 * k) + 2
    maximum = k
    
    if(leftChild <= n and listData[leftChild]>listData[maximum]):
        maximum = leftChild
        
    if(rightChild <= n and listData[rightChild]>listData[maximum]):
        maximum = rightChild

    if(maximum != k):
        listData[k],listData[maximum]=listData[maximum],listData[k]
        validate_Max_Heap(listData,maximum,n)
                

def counting_Sort(listData):      
    n = len(listData)
    final = [0] * n
    maxValue = max(listData) + 1
    CountingArray = [0] * maxValue
    for i in range(0,n):        
        print(listData[i])
        CountingArray[listData[i]] += 1    

    for i in range(1,maxValue):
        CountingArray[i] +=CountingArray[i-1]
    print(CountingArray)        

    for i in range(0,n):
        final[CountingArray[listData[i]]-1] = listData[i]
        CountingArray[listData[i]] -= 1  
    print(final)   


def counting_Sort_Radix(listData,group):      
    n = len(listData)
    final = [0] * n    
    CountingArray = [0] * 10
    for i in range(0,n):
        Actual_Group = (listData[i]//group) % 10
        CountingArray[Actual_Group] += 1    

    for i in range(1,10):
        CountingArray[i] +=CountingArray[i-1]
     
    
    i = n - 1
    while i >= 0:
    #for i in range(0,n):
    #WTF!
        Actual_Group = (listData[i]//group) % 10
        CountingArray[Actual_Group] -= 1
        final[CountingArray[Actual_Group]] = listData[i]          
        i -= 1
    
    for i in range(0, n):
        listData[i] = final[i]
    

def radix_Sort(listData):
    maxValue = max(listData)
    group = 1
    while ((maxValue/group) > 1):
        counting_Sort_Radix(listData,group)
        group *= 10
    print(listData)

listaConteo = [218,3333,44,555,219,5,1]
print("Arreglo de conteo")
radix_Sort(listaConteo)

listaMonticulo = [11,99,55,88,33,22]    
go_Through_Heap(listaMonticulo, len(listaMonticulo)-1)
print("validación HEAP")
print(listaMonticulo)

             
#miLista = [1,2,3,4,5,6,7,8,9]#el mejor caso posible
miLista = [11,10,9,8,7,6,5,4,3,2,1]#el peor caso posible
miLista1 = miLista.copy()#el peor caso posible
miLista2 = miLista.copy()#el peor caso posible
miLista3 = miLista.copy()#el peor caso posible
miLista4 = miLista.copy()#el peor caso posible
milista5 = miLista.copy()
milista6 = miLista.copy()
milista7 = [94,	84	,75	,19	,32	,88	,36	,100,22	,67	,3	,30	,54	,25	,55]

print(WorstBubbleSort(miLista,0))
print(bubbleSort(miLista1,0))
print(bubbleSortCheckOrdered(miLista2,0))
print(recursiveBubbleSort(miLista3))
print(insertSort(miLista4))
print(selectSort(milista5))
print("Quick Sort")
print(quick_sort(milista6))
print("Merge Sort")
print(merge_sort(milista7))


