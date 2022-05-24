# NOTE: use Prefix Tree to implement autocomplete feature for an input word 
# when given a dictionary of words, then output the autocomplete words in order of frequency
# 1. Store array of words paired with their frequency in a hashmap
# 2. Insert those words into prefix tree, with frequency at the last node for each word
# 3. Get input, collect all autocomplete words with key as word and value as freq into hashmap
# 4. Sort hashmap according to value(freq), return the words as an array with most popular word first
def StoreWord(arr, map):
    for word in arr:
        if map.get(word) != None:
            map[word] += 1
        else:
            map[word] = 1

def sort_freq(map, arr=[]):
    while len(map) != 0:
        a = list(map.keys())
        b = list(map.values())
        max_word = a[b.index(max(b))]
        arr.append(max_word)
        map.pop(max_word)
    return arr
            
class PrefixTree:
    
    def __init__(self) -> None:
        self.children = {}
    
    def insert(self, word, freq):
        if len(word) == 0:
            self.children['*'] = freq
            return
        if self.children.get(word[0]) == None:
            self.children[word[0]] = PrefixTree()
            return self.children.get(word[0]).insert(word[1:], freq)
        else:
            return self.children.get(word[0]).insert(word[1:], freq)
    
    def collect_all(self, map, str=''):
        first = 0
        
        if len(self.children) == 1 and self.children.get('*') != None:
            map[str] = self.children.get('*')
            return
        
        for val in self.children.keys():
            if val == '*':
                map[str] = self.children.get('*')
            else:
                if first == 0:
                    str = str + val
                    first = 1
                    self.children.get(val).collect_all(map, str)
                else:
                    tmp = list(str)
                    tmp[-1] = val
                    str = ''.join(tmp)
                    self.children.get(val).collect_all(map, str)
    
    # NOTE: search for prefix of a word, and then return the prefix if exist
    def search_prefix(self, word):
        if len(word) == 0:
            return self
        if self.children.get(word[0]) != None:
            return self.children.get(word[0]).search_prefix(word[1:])
        else:
            return False
    
    # NOTE: autocomplete is search to end node of prefix + collect_all
    def auto_complete(self, prefix):
        map = {}
        node = self.search_prefix(prefix)
        node.collect_all(map, prefix)
        return sort_freq(map)


# Test
arr = ['cat', 'catch', 'catch', 'cartilage', 'boy', 'bobby', 'at', 'at', 'all', 'alter',
       'cat', 'cat', 'boy', 'boss', 'boss', 'boat', 'below', 'belly', 'belly', 'at', 
       'all', 'best', 'best', 'best', 'best']
map = {}
StoreWord(arr, map)
tree = PrefixTree()
for word, freq in map.items():
    tree.insert(word, freq)
# tree.collect_all(map2)
# print(map2)
# print(map)
print(tree.auto_complete('bo'))

