def search(array):
    # Create a dummy array at size of the max value, to hold whether things are present
    dummy = [0 for i in range(0, max(array)+1)]
    for i in range(0, len(array)):
        if dummy[array[i]] == 1:
            return True
        else:
            dummy[array[i]] = 1
    
    return False

array = [1,2,2,3,4,5]
print(search(array))