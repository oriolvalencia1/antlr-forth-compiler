class Stack:
    def __init__(self):
        self.items = []
        
    def clear(self):
        self.items.clear()
    ###################
    #operacions sobre l'stack
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if(self.empty()):
            raise Exception(f"Error:pila buida")
        return self.items.pop()
    
    def swap(self):
        self.items[-2],self.items[-1] = self.items[-1],self.items[-2]
    
    def swap2(self):
        self.items[-3],self.items[-1] = self.items[-1],self.items[-3]
        self.items[-4],self.items[-2] = self.items[-2],self.items[-4]

    def dup(self):
        self.push(self.items[-1])
        
    def dup2(self):
        self.push(self.items[-2])
        self.push(self.items[-2])
    
    def over(self):
        self.push(self.items[-2])
    
    def over2(self):
        self.push(self.items[-4])
        self.push(self.items[-4])
        
    def rot(self):
        self.push(self.items.pop(-3))
        
    def drop(self):
        self.pop()
        
    def drop2(self):
        self.pop()
        self.pop()
    
    def empty(self):
        return len(self.items) == 0
    
    def popBoolean(self):
        v = self.items.pop()
        if v != 0 and v != -1:
            raise Exception("Error: operand no booleà (-1 o 0)")
        return v
    
    def size(self):
        return len(self.items)
    
    def printAll(self):
        print ("[" + (", ".join(str(e) for e in self.items) + "]"))
        
    def printOne(self):
        if(len(self.items) > 0): 
            print (self.pop())
        else :raise Exception(f"Error:pila buida")
    
    