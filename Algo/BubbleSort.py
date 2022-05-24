def BubbleSort(array):
    sort = False
    while sort != True:
        sort = True
        for i in range(0, len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                sort = False
    return array

array = [7,6,5,4,3,2,1]
print(BubbleSort(array))
            
    