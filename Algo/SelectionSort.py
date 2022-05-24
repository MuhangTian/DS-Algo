def SelectionSort(array):
    for i in range(0, len(array)):
        lowest_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[lowest_index]:
                lowest_index = j
        array[i], array[lowest_index] = array[lowest_index], array[i]
    return array

array = [7,5,5,4,6,3,1,2]
print(SelectionSort(array))