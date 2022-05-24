def InsertionSort(array):
    for i in range(1, len(array)):
        temp = array[i]
        index = i-1
        while index >= 0:
            if temp < array[index]:
                array[index+1] = array[index]
            else:
                break
            index -= 1
        array[index+1] = temp
    return array