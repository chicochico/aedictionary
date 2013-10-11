# -*- encoding: utf-8 -*-

class Table():
     
    def __init__(self, table):
        self.table = table
        self.keys = sorted(self.table.keys())
        self.keys.sort()
        print(self.keys)
        
    def remove(self, word):
        pass
    
    def find(self, word):
        pass