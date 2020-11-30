from math import floor


numbers = [8,5,60,25,45,35,12,1]


#selection_sort
def selection_sort(numbers):
    indexing_length = range(0, len(numbers)-1)

    for i in indexing_length:
        min_value = i

        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[min_value]: 
                min_value = j


        if min_value != i:
            numbers[min_value], numbers[i] = numbers[i], numbers[min_value]

    return numbers
print("selection sort: " )
print(selection_sort(numbers))

#bubble_sort
def bubble_sort(numbers):
    for i in range(len(numbers)-1,0,-1):
        for j in range(i):
            if numbers[j]>numbers[j+1]:
                temporary = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1]=temporary



bubble_sort(numbers)
print("bubble sort: " )
print ( numbers)

#insertion_sort
def insertion_sort(numbers):
    indexing_length = range(1, len(numbers))
    for i in indexing_length:
        value_to_sort = numbers[i]

        while numbers[i-1] > value_to_sort and i > 0:
            numbers[i], numbers[i-1] = numbers[i-1], numbers[i]
            i = i -1

    return numbers

print("insertion sort: " )
print(insertion_sort(numbers))

#quick_sort
def quick_sort(numbers):
    length = len(numbers)
    if length <= 1:
        return numbers
    else:
        pivot = numbers.pop()

    items_greater = []
    items_lower = []

    for item in numbers:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)
print("quick sort: " )
print(quick_sort(numbers))



#shell_sort
def shellSort(numbers):
    n = len(numbers)
    # Gap sequence
    gap = floor(n / 2)
    while gap > 0:
        for i in range(gap, n):
            temp = numbers[i]
            j = i
            # Compare elements at equal gap.
            while j >= gap and temp < numbers[j - gap]:
                numbers[j] = numbers[j - gap]
                j -= gap
        numbers[j] = temp
        gap = floor(gap / 2)



shellSort(numbers)
print("shell sort: " )
print(numbers)




#merge_sort
def mergeSort(numbers):
    if len(numbers) > 1:
        mid = len(numbers) // 2
        left = numbers[:mid]
        right = numbers[mid:]

  
        mergeSort(left)
        mergeSort(right)

        
        i = 0
        j = 0
        
      
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
             
              numbers[k] = left[i]
              
              i += 1
            else:
                numbers[k] = right[j]
                j += 1
            
            k += 1

        
        while i < len(left):
            numbers[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            numbers[k]=right[j]
            j += 1
            k += 1


mergeSort(numbers)
print("merge sort: " )
print(numbers)

#bucket_sort
def insertionSort(b): 
    for i in range(1, len(b)): 
        up = b[i] 
        j = i - 1
        while j >= 0 and b[j] > up:  
            b[j + 1] = b[j] 
            j -= 1
        b[j + 1] = up      
    return b      
              
def bucketSort(x): 
    arr = [] 
    slot_num = 10 # 10 means 10 slots, each 
                  # slot's size is 0.1 
    for i in range(slot_num): 
        arr.append([]) 
          
    
    for j in x: 
        index_b = int(slot_num * j)  
        arr[index_b].append(j) 
      
    # Sort individual buckets  
    for i in range(slot_num): 
        arr[i] = insertionSort(arr[i]) 
          
    # concatenate the result 
    k = 0
    for i in range(slot_num): 
        for j in range(len(arr[i])): 
            x[k] = arr[i][j] 
            k += 1
    return x 

x = [0.897, 0.565, 0.656, 
     0.1234, 0.665, 0.3434]  
print("bucket sort: " )
print(bucketSort( x)) 

#radix_sort
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

   
    for i in range(1, 10):
        count[i] += count[i - 1]

    
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]



def radixSort(array):
   
    max_element = max(array)

    
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10


data = numbers
radixSort(data)
print("radix sort: ")
print(data)