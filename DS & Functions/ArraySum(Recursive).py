def Sum(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] + Sum(arr[1:len(arr)])

arr = [1,2,3,4,5,6]
print(Sum(arr))
print(sum(arr))