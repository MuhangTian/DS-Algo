# NOTE
# While this method seems dumb when only search for 1 element
# (Same as linear search and compare each element in array, both O(n))
# Sometimes might even be worse than linear search since it always has n loops
# Whereas linear search may break once an element is found, thus not always has n loops
# HOWEVER, once this is complete, we can always search for elements with O(1)
# This will become extremeply versatile if we are searching for multiple elements
# Since in linear search, we must go through array in each search
# But with hashmap, we can get constant time since hashmap has constant lookup time
# CONCLUSION: the setting up hashmap part is the step that takes most runtime, once it's done, it's constant

# NOTE
# to get constant time, we need to use:
# if dict.get(key) != None, which checks that PARTICULAR key and return value if present
# rather than: if key in dict, the latter one is actually linear search in list of keys, so still O(n)
def HashSearch(array, num):
    dummy = {}
    for val in array:
        dummy[val] = 1
    if dummy.get(num) != None:
        return True
    else:
        return False

array = [1,2,2,2,2,3,4,5]
num = 5
print(HashSearch(array, num))