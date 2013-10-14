class test():
    
    def __init__(self):
        self.foo = None

    def fun(self):
        self.change()
        
    def change(self):
        global foo
        foo = "fuck"
        

if __name__ == '__main__':
    t = test()
    t.fun()
    print(t.foo)