# -*- encoding: utf-8 -*-

class Hash():
    
    def __init__(self, data):
        self.hash_table = [None]*5000
        self.data = data
        
        for key in data:
            self.add(key)
    
    def hash_function(self, word):
        output = 0
        
        for i, j in enumerate(word):
            output += ord(j) * i

        return output % 5000
    
          
    def remove(self, word):
        position = self.hash_function(word)
        
        if self.hash_table[position] == word:
            self.hash_table[position] = None
        else:
            position = self.colision_treatment(position+1, word)
            if position != None:
                self.hash_table[position] = word
    
    
    def add(self, word):
        position = self.hash_function(word)
        if self.hash_table[position] == None:
            self.hash_table[position] = word
        else:
            position = self.colision_treatment(position+1, None)
            if (position != None):
                self.hash_table[position] = word
    
    
    def find(self, word):
        position = self.hash_function(word)
        
        if self.hash_table[position] == word:
            return position
        else:
            return self.colision_treatment(position, word)
    
            
    def colision_treatment(self, start, word):
        for i in range(start, 5000):
            if i == word:
                return i
        else:
            return None