# -*- encoding: utf-8 -*-

'''
Created on Oct 2, 2013

@author: Chico
'''

class TextFileInput(object):
    
    file_name = None
    file = None

    
    def __init__(self):
        pass    
#         self.file = self.get_text_data(file_name)
        
    def get_text_data(self, file_name):
        
        file = open(file_name, 'r', encoding="utf-8")
        data = file.read()
        file.close()
        print(data)
        return data