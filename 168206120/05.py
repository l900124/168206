def findSmallest(arr):
    smallest = arr[0] 
    smallest_index = 0 

    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr): 
    for i in range(len(arr))
        smallest = findSmallest(arr[0:len(arr)-i])  
        arr.append(arr.pop(smallest))              
    return arr                                      
print (selectionSort([5,3,8,4,10]))
