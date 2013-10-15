# -*- encoding: utf-8 -*-

class Table():
     
    def __init__(self, table):
        self.table = table
        self.keys = sorted(self.table.keys())
        self.keys.sort()
        self.comps = 0
        
    def remove(self, word):
        self.keys.remove(word)
        del self.table[word]
    
    def find(self, word):
        return self.binary_search(0, len(self.keys)-1, word)
        
        
    def binary_search(self, lo, hi, word):
        if (lo == hi and self.keys[lo] != word):
            self.comps += 2
            return False
        else:
            mid =  (lo + hi)//2
            
            if (self.keys[mid] == word):
                self.comps += 1
                return mid
            elif (self.keys[mid] < word):
                self.comps += 1
                return self.binary_search(mid+1, hi, word)
            else:
                return self.binary_search(lo, mid-1, word)