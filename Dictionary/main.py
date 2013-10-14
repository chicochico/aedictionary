# -*- encoding: utf-8 -*-

from file import Word
from file import TextPreProcessor
from table import Table
from hash_table import Hash
from avl_tree import AVL

    
if __name__ == '__main__':
    
    word = Word()
    file = TextPreProcessor("input.txt")
    table = Table(file.dictionary_list)
    hash_table = Hash(file.dictionary_list)
    avl_tree = AVL()

    print(table.keys)
    print(table.table)
    
    l = [12,26,29,30,40,31,42,47,85,88,10]
    
    for i in l:
        avl_tree.add(i)

    print(avl_tree.root.word)
    print(avl_tree.root.rchild.word)