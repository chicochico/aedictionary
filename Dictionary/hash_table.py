# -*- encoding: utf-8 -*-

class Hash():
    
    def __init__(self, data):
        self.hash_table = []
        self.data = data
    
    def hash_function(self, word):
        output = 0
        
        for i, j in enumerate(word):
            output += ord(j) * i

        return output
        
    
    def remove(self):
        pass
    
    def add(self, word):
        pass
    
    def find(self):
        pass
    
    def colision_treatment(self):
        pass
