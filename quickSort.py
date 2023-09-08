import math

def quicksort(array):
    if len(array) < 2:
        # If array is smaller that 2 this means 0 and 1 return the array as it is. Sorting it won't change anything.
        return array
    else:
        # Pivot is our check number, we take it from the middle of the array
        pivot = array[math.floor(len(array) / 2)]

        # Put every smaller number than pivot into less array
        less = [i for i in array[1:] if i <= pivot]

        # Put every bigger number than pivot into greater array
        greater = [i for i in array[1:] if i > pivot]

        # Merge the arrays into one, on the left put the  smaller numbers, on the right the bigger numbers
        # and in the middle put your check number this means variable witch pivot in this example
        return quicksort(less) + [pivot] + quicksort(greater)

# Your array can have duplicates of numbers
print(quicksort([10, 2, 5, 77, 32, 1, 8 ,5, 5, 4, 3, 1, 89, 54, 32, 13]))