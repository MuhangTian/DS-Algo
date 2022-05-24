def BinarySearch(array, num):
    array.sort()    # Only works for ordered array
    max_index = len(array) - 1
    min_index = 0
    
    while min_index <= max_index:
        middle = min_index + int((max_index - min_index)/2)
        if num == array[middle]:
            return "Found " + str(array[middle])
        if num < array[middle]:
            max_index = middle - 1
        if num > array[middle]:
            min_index = middle + 1

    return "Not Found"
    
array = [1,5,3,7,13,17,19,11]
num = 11
print(BinarySearch(array, num))