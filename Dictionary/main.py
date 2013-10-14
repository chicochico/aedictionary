# -*- encoding: utf-8 -*-

from file import Word
from file import TextPreProcessor
from table import Table
from hash_table import Hash
from avl_tree import AVL



def draw_menu():
    print()
    print("1. Abrir arquivo")
    if file_name != None:
        print("    arquivo aberto: " + file_name)
    print("2. Tabela ordenada")
    print("3. Tabela hash")
    print("4. Arvore AVL")
    print("5. Mostrar dados")
    print("6. Mostrar texto")
    print("0. Sair")
    print()


def take_action(option):
    global file_name
    global file
    global table
    global hash_table
    global avl_tree
    
    old_file = file_name
    
    if option == 1:
        
        try:
            file_name = input("Nome do arquivo:")
            file = TextPreProcessor(file_name)
        except:
            print("arquivo nao encontrado.")
            file_name = old_file
            
    elif option == 2:
        
        try:
            table = Table(file.dictionary_list)
            
            selection = 1
            
            while selection:
                selection = 0
                
                print(table.keys)
                print("1. Remover palavra")
                print("2. Pesquisar ( Pesquisa Binaria )")
                print("0. Voltar")
                
                try:
                    selection = int(input("Selecione: "))
                except:
                    print("insira apenas numero!")
                    
                if selection == 1:
                    word = input("Palavra: ")
                    table.remove(word)
                elif selection == 2:
                    word = input("Palavra: ")
                    position = table.find(word)
                    print(table.keys[position] + " " + str(table.table[table.keys[position]][0]) + "x " + str(table.table[table.keys[position]][1]))
        except:
            pass
        
    elif option == 3:
        
        try:
            hash_table = Hash(file.dictionary_list)
            
            selection = 1
            
            while selection:
                selection = 0
                
                print(hash_table.hash_table)
                print("1. Remover palavra")
                print("2. Pesquisar")
                print("0. Voltar")
                
                try:
                    selection = int(input("Selecione: "))
                except:
                    print("insira apenas numero!")
                    
                if selection == 1:
                    word = input("Palavra: ")
                    hash_table.remove(word)
                elif selection == 2:
                    word = input("Palavra: ")
                    position = hash_table.find(word)
                    print(hash_table.hash_table[position] + " " + str(hash_table.data[hash_table.hash_table[position]][0]) + "x " + str(hash_table.data[hash_table.hash_table[position]][1]))
        except:
            pass

    elif option == 4:
        pass
    elif option == 5:
        
        try:
            for key in file.dictionary_list:
                print(key + " " + str(file.dictionary_list[key][0]) + "x " + str(file.dictionary_list[key][1]))
        except:
            pass
                    
    elif option == 6:
        
        try:
            print(file.text)
        except:
            print("nao ha arquivo aberto")


if __name__ == '__main__':
    
    file_name = None
    word = None
    file = None
    table = None
    hash_table = None
    avl_tree = None

    option = 1
    
    while option:
        option = 0
        
        while True:
            try:
                draw_menu()
                option = int(input("Selecione: "))
                break
            except:
                print("NUMERO! FILHO DA PUTA!")
                print()
        
        if option:
            take_action(option)
            option = 1
    
    
#     print(table.keys)
#     print(table.table)
    

#     print(table.find("aquelas"))
    
#     l = [12,26,29,30,40,31,42,47,85,88,10]
    
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
#     
#     for i in table.table:
#         hash_table.add(i)
#         
#     print(hash_table.hash_table)
#     
#     print(hash_table.find("alimentado"))
#  
#     print(avl_tree.root.word)
#     print(avl_tree.root.rchild.word)