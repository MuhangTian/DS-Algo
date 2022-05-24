# Takes two sorted arrays and return a merged sorted array
# NOTE: key is Merge(), where the main idea is to compare min values of array
# We compare min since we only check first value in a sorted ascending array
# NOTE: different from QuickSort in that we never get left > right due to different calculation (halfing
# rather than incrementing)

def Merge(arr1, arr2):
    arr = []
    i = 0
    j = 0
    while i <= len(arr1)-1 and j <= len(arr2)-1:
        if arr1[i] <= arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1
    if i > j:
        arr = arr + [arr2[k] for k in range(j, len(arr2))]
    else:
        arr = arr + [arr1[k] for k in range(i, len(arr1))]
    return arr

def MergeSort(arr, left, right):
    if left == right:
        return [arr[right]]
    mid = int((right+left)/2)   # right-left/2 + left = right+left/2
    arr1 = MergeSort(arr, left, mid)
    arr2 = MergeSort(arr, mid+1, right)
    
    return Merge(arr1, arr2)

arr = [1,7,6,2,3,9,10,14,17,20,14,4,7,8,2]
print(MergeSort(arr, 0, len(arr)-1))
arr.sort()
print(arr) 