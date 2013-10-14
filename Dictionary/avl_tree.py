# -*- encoding: utf-8 -*-

class Node():
    
    def __init__(self):
        self.word = None
        self.bfactor = 0
        self.lchild = None
        self.rchild = None


class AVL():
    
    def __init__(self):
        self.root = None
    
    def is_leaf(self, node):
        if node.lchild == None and node.rchild == None:
            return True
        else:
            return False
    
    
    def is_emtpy(self, node):
        if node == None:
            return True
        else:
            return False
    
    def add(self, word):
        self.root = self.find_add(self.root, False, word)
#         new_node = self.find(self.root, word)
#          
#         if new_node.word > word:
#             new_node.lchild = Node()
#             new_node.lchild.word = word
#         else:
#             new_node.rchild = Node()
#             new_node.rchild.word = word
#              
#         self.rebalance()


    def delete(self):
        pass
                          
    
    def find(self, node, word):
        if self.is_leaf(node):
            return node
        
        if node.word == word:
            return node
        elif node.word > word:
            if node.lchild != None:
                return self.find(node.lchild, word)
            else:
                return node
        else:
            if node.rchild != None:
                return self.find(node.rchild, word)
            else:
                return node
    
    
    def find_add(self, node, hchanged, word):
        if node == None:
            node = Node()
            hchanged = True
            node.word = word
            return node
        elif node.word > word:
            node = self.find_add(node.lchild, hchanged, word)
           
            if hchanged:
                if node.bfactor == -1:
                    node.bfactor = 0
                    hchanged = False
                    return node
                elif node.bfactor == 0:
                    node.bfactor = 1
                    return node
                elif node.bfactor == 1:
                    bnode = node.lchild
                    
                    if bnode.bfactor == 1:
                        node = self.ll(node, bnode)
                    else:
                        node = self.lr(node, bnode)
                            
                    node.bfactor = 0
                    hchanged = False
                    return node
                    
        elif node.word < word:
            node = self.find_add(node.rchild, hchanged, word)
            
            if hchanged:
                if node.bfactor == 1:
                    node.bfactor = 0
                    hchanged = False
                    return node
                elif node.bfactor == 0:
                    node.bfactor = 1
                    return node
                elif node.bfactor == -1:
                    bnode = node.rchild
                    
                    if bnode.bfactor == -1:
                        node = self.rr(node, bnode)
                    else:
                        node = self.rl(node, bnode)
                            
                    node.bfactor = 0
                    hchanged = False
                    return node
        else:
            return node
        
        
    def rebalance(self):
        pass
    
    
    def ll(self, anode, bnode):
        anode.lchild = bnode.rchild
        bnode.rchild = anode
        anode.bfactor = 0
        anode = bnode
        return anode
    
    
    def rr(self, anode, bnode):
        anode.rchild = bnode.lchild
        bnode.lchild = anode
        anode.bfactor = 0
        anode = bnode
        return anode
    
    
    def lr(self, anode, bnode):
        cnode = bnode.rchild
        bnode.rchild = cnode.lchild
        cnode.lchild = bnode
        anode.lchild = cnode.rchild
        cnode.rchild = anode
        
        if cnode.bfactor == 1:
            anode.bfactor = -1
        else:
            anode.bfactor = 0
            
        if cnode.bfactor == -1:
            bnode.bfactor = 1
        else:
            bnode.bfactor = 0
            
        return anode
    
    
    def rl(self, anode, bnode):
        cnode = bnode.lchild
        bnode.lchild = cnode.rchild
        cnode.rchild = bnode
        anode.rchild = cnode.lchild
        cnode.lchild = anode
        
        if cnode.bfactor == -1:
            anode.bfactor = 1
        else:
            anode.bfactor = 0
            
        if cnode.bfactor == 1:
            bnode.bfactor = -1
        else:
            bnode.bfactor = 0
            
        return anode
    
    
    def in_order(self, node):
        if node != None:
            self.in_order(node.lchild)
            print(node.word)
            self.in_order(node.parent)
            self.in_order(node.rchild)
    
    
    def pre_order(self, node):
        if node != None:
            print(node.word)
            self.in_order(node.parent)
            self.in_order(node.lchild)
            self.in_order(node.rchild)


    def post_order(self, node):
        if node != None:
            self.in_order(node.lchild)
            self.in_order(node.rchild)
            self.in_order(node.parent)
            print(node.word)
