import math

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[math.floor(len(array) / 2)]

        less = [i for i in array[1:] if i <= pivot]

        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)
    
print(quicksort([10, 2, 5, 77, 32, 1, 8 ,5, 5, 4, 3, 1, 89, 54, 32, 13]))