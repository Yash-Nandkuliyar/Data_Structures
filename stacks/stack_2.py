class stack(list):
    def isempty(self):
        return len(self)==0
    def push(self,data):
        self.append(data)
    def pop(self):
        if not self.isempty():
            super().pop()
        else:
            raise IndexError("stack is empty")
    def peek(self):
        if not self.isempty():
            return self[-1]
        else:
            raise IndexError("stack is empty")
    def size(self):
        return len(self)
    def insert(self,index,data):
        raise AttributeError("no attribute insert in stack")
    
        
s1=stack()
s1.push(10)
s1.push(20)  
s1.push(30)  
s1.push(40)

print("top value",s1.peek())
print()              

            