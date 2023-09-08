def recursive_sum(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        # Sum the first element with the sum of the rest of the elements in the array.
        return arr[0] + recursive_sum(arr[1:])

array = [2, 4, 6, 10, 1, 6, 8]
array2 = []

result1 = recursive_sum(array2)
result2 = recursive_sum(array)

print("Sum of array2:", result1)  # This will print "Sum of array2: 0"
print("Sum of array:", result2)    # This will print "Sum of array: 37"
