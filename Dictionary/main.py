# -*- encoding: utf-8 -*-

from file import Word
from file import TextPreProcessor
from table import Table
from hash_table import Hash
from avl_tree import AVL, Node

    
if __name__ == '__main__':
    
    word = Word()
    file = TextPreProcessor("input.txt")
    table = Table(file.dictionary_list)
    hash_table = Hash(file.dictionary_list)
    avl_tree = AVL()

    print(table.keys)
    print(table.table)
    
    l = [12,26,29,30,40,31,42,47,85,88,10]
    
#     avl_tree.root = Node()
#     avl_tree.root.word = 4
#     avl_tree.root.rchild = Node()
#     avl_tree.root.rchild.word = 5
#     avl_tree.root.rchild.rchild = Node()
#     avl_tree.root.rchild.rchild.word = 7
#     
#     print(avl_tree.root.word)
#     print(avl_tree.root.rchild.word)
#     print(avl_tree.root.rchild.rchild.word)
#     
#     bnode = avl_tree.root.rchild
#     
#     avl_tree.root = avl_tree.rr(avl_tree.root, bnode)
#     print("fuck")
#     
#     print(avl_tree.root.word)
#     print(avl_tree.root.lchild.word)
#     print(avl_tree.root.rchild.word)
    
    for i in l:
        avl_tree.add(i)
 
    print(avl_tree.root.word)
    print(avl_tree.root.rchild.word)