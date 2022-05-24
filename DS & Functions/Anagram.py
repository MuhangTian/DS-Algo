from math import factorial

# NOTE: return array of anagrams in each call, then concatenate the words in the array
# with a specific letter to get all possible combinations. Although there are three nested
# for loops, runtime is actually O(N!)

# NOTE: alternative version simply writes less code using insert(), runtime and idea is exactly same
# NOTE: the first approach returns in specific order whereas the alternative approach doesn't
def Anagram(str):
    arr = []
    if len(str) == 1:
        return str[0]
    for i in range(0, len(str)):
        if i == 0:
            for word in Anagram(str[1:len(str)]):
                arr.append(str[i] + word)
        elif i == len(str)-1:
            for word in Anagram(str[0:len(str)-1]):
                arr.append(str[i] + word)
        else:
            for word in Anagram(str[0:i] + str[i+1:len(str)]):
                arr.append(str[i] + word)
    return arr

def AnagramAlt(str):
    arr = []
    if len(str) == 1:
        return str[0]
    ana = AnagramAlt(str[1:len(str)])
    
    for word in ana:
        # Concatenation of the first letter to different indices of anagram words
        for i in range(0, len(word)+1):
            new = word[:i] + str[0] + word[i:]
            arr.append(new)
    return arr

str = 'abc'
print(Anagram(str))
print(AnagramAlt(str))
