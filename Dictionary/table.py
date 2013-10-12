# -*- encoding: utf-8 -*-

class Table():
     
    def __init__(self, table):
        self.table = table
        self.keys = sorted(self.table.keys())
        self.keys.sort()
        
    def remove(self, word):
        self.keys.remove(word)
        del self.table[word]
    
    def find(self, word):
        return self.binary_search(0, len(self.keys), word)
        
        
    def binary_search(self, leftIndex, rightIndex, word):
        if (leftIndex == rightIndex and self.keys[leftIndex] != word):
            return -1
        
        middleIndex = int((leftIndex + rightIndex) / 2)
        
        if (self.keys[middleIndex] == word):
            return middleIndex
        elif (self.keys[middleIndex] > word):
            self.binary_search(middleIndex+1, rightIndex, word)
        else:
            self.binary_search(leftIndex, middleIndex-1, word)
        