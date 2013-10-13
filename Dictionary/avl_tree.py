# -*- encoding: utf-8 -*-

class Node():
    
    def __init__(self):
        self.word = None
        self.bfactor = 0
        self.lchild = None
        self.rchild = None


class AVL():
    
    def __init__(self):
        self.root = Node()
    
    def add(self, word):
        new_node = self.find(self.root, None)
        new_node.word = word
        self.rebalance()

    def delete(self):
        pass
    
    def find(self, node, word):
        if node.word == word:
            return node
        elif node.word > word:
            return self.find(node.lchild, word)
        else:
            return self.find(node.rchild, word)
        
    
    def rebalance(self):
        pass
    
    def ll(self):
        pass
    
    def rr(self):
        pass
    
    def lr(self):
        pass
    
    def rl(self):
        pass