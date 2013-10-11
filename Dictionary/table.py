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
        pass 