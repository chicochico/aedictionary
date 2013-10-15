# -*- encoding: utf-8 -*-

import re

class TextPreProcessor():
       
    def __init__(self, file_name):
        self.file_name = file_name
        self.text = self.get_file_input(file_name)
        self.word_list = self.process()
        self.dictionary_list = self.create_data_strcture()
    
    def get_file_input(self, file_name):
        file = open(file_name, 'r', encoding="utf-8")
        data = file.read()
        file.close()
        return data
    
    def process(self):
        self.text = self.text.lower()
        
        characters_replacements = {'[àáâã]':'a',
                                     '[éê]':'e',
                                        'í':'i',
                                    '[óôõ]':'o',
                                     '[úü]':'u',
                                        'ç':'c',
        }

              
        for exp, rep in characters_replacements.items():
            self.text = re.sub(exp, rep, self.text)

        self.text = re.sub('[ \t\n\r\f\v]|[^a-z_]', ' ', self.text)
        
        return re.split(' +', self.text)
    
    def create_data_strcture(self):
        word_set = set(self.word_list)
        output = {}
        
        for word in word_set:
            if word != '':
                output[word] = [self.word_list.count(word),[]]
        
        for key in output:
            for i, word in enumerate(self.word_list):
                if key == word:
                    output[key][1].append(i)
        
        return output