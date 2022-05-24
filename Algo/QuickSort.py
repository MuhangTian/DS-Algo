# NOTE this nested loop is not quadratic, since we approximately vist all entries from left
# to right, so O(N)
# NOTE: why left < right is not ok for while loop:
# Mainly due to missing line 19, which is NOT trivial
# This line takes care of value=pivot scenario by increment left pointer by 1
# Without it, left pointer would not be able to continue, since we only check arr[piv] > arr[left]
# which gives us false since we get equal, meaning the pointers are ended before it should be
    
def partition(arr, start, end):
    left = start
    right = end-1
    piv = end
    
    while True:     # NOTE: Got this wrong, used left < right as condition
        while arr[piv] > arr[left]:
            left += 1
        while arr[piv] < arr[right]:
            right -= 1
        if left >= right:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1   # NOTE: Missed this part
    
    arr[left], arr[piv] = arr[piv], arr[left]
    return left

def QuickSort(arr, start, end):
    if start-end >= 0:
        return
    
    piv = partition(arr, start, end)
    QuickSort(arr, start, piv-1)
    QuickSort(arr, piv+1, end)
    
    return arr

arr = [2,7,3,6,4,1,8,6,5,19,18,20,14]
print(QuickSort(arr,0,len(arr)-1))
arr.sort()
print(arr) 