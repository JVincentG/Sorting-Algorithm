
from math import floor

print("Algorithm Sorter")
numbers = []
while True:
    while True:

        choice = ''

        while True:

            print(numbers)
            print("add number: ")
            add = int(input())
            numbers.append(add)
            print(numbers)

            if input('Do you wish to add more numbers? \nPress any key for yes \nPress n for no \n') == 'n':
                break
      

        print(numbers)
        if input('Confirm numbers? (y or n) ') == 'y':
            break


    print('Select sorting algorithm:\n[1] bubble sort\n[2] insertion sort\n[3] shell sort\n[4] merge sort\n[5] bucket sort\n[6] radix sort\n[7] selection sort\n[8] quick sort')
    algo = int(input())

    if algo == 1:
        # bubble_sort

        def bubble_sort(numbers):
            
            for i in range(len(numbers) - 1, 0, -1):

                for j in range(i):

                    if numbers[j] > numbers[j + 1]:
                        temporary = numbers[j]

                        numbers[j] = numbers[j + 1]

                        numbers[j + 1] = temporary

        
        bubble_sort(numbers)
        
        print("bubble sort: ")

        print(numbers)

    elif algo == 2:
        # insertion_sort

        def insertion_sort(numbers):

            indexing_length = range(1, len(numbers))

            for i in indexing_length:

                value_to_sort = numbers[i]

                while numbers[i - 1] > value_to_sort and i > 0:
                    numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]

                    i = i - 1

            return numbers


        print("insertion sort: ")

        print(insertion_sort(numbers))
    elif algo == 3:
        # shell_sort

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

        print("shell sort: ")

        print(numbers)

    elif algo == 4:
        # merge_sort

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
                    numbers[k] = right[j]

                    j += 1

                    k += 1

        mergeSort(numbers)

        print("merge sort: ")

        print(numbers)
    elif algo == 5:
        # bucket_sort

        def insertion(inpvalue):
            for i in range(1, len(inpvalue)):
                temp = inpvalue[i]
                j = i - 1
                while (j >= 0 and temp < inpvalue[j]):
                    inpvalue[j + 1] = inpvalue[j]
                    j = j - 1
                inpvalue[j + 1] = temp

        def bucket_sort(inpvalue):
            largest = max(inpvalue)
            length = len(inpvalue)
            size = largest/length
 
            buckets = [[] for _ in range(length)]
            for i in range(length):
                j = int(inpvalue[i]/size)
        
                if j != length:
                    buckets[j].append(inpvalue[i])
                else:
                    buckets[length - 1].append(inpvalue[i])
 
            for i in range(length):
                insertion(buckets[i])
 
            res = []
    
            for i in range(length):
                res = res + buckets[i]
 
            return res
 
 

        inpvalue = numbers

        sorted_list = bucket_sort(inpvalue)
        print("bucket sort: ", end='')
        print(sorted_list)



        

       

       
    elif algo == 6:
        # radix_sort

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
    elif algo == 7:
        # selection_sort

        def selection_sort(numbers):

            indexing_length = range(0, len(numbers) - 1)

            for i in indexing_length:

                min_value = i

                for j in range(i + 1, len(numbers)):

                    if numbers[j] < numbers[min_value]:
                        min_value = j

                if min_value != i:
                    numbers[min_value], numbers[i] = numbers[i], numbers[min_value]

            return numbers


        print("selection sort: ")

        print(selection_sort(numbers))
    elif algo == 8:
        # quick_sort

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


        print("quick sort: ")

        print(quick_sort(numbers))

    if input('Continue? (y or n)') != 'y':
        break

