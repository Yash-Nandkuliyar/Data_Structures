class deque:
    def __init__(self):
        self.items=[]

    def isempty(self):
        return len(self.items)==0
    def insertfront(self,data):
        self.items.insert(0,data)
    def insertrear(self,data):
        self.items.append(data)
    def deletefront(self):
        if self.isempty():
            raise IndentationError("deque is empty")
        else:
            self.items.pop(0)
    def deleterear(self):
        if self.isempty():
            raise IndentationError("deque is empty")
        else:
            self.items.pop()       
    def getfront(self):

        if self.isempty():
            raise IndexError("deque is empty")
        else:
            return self.items[0]  
    def getrear(self):

        if self.isempty():
            raise IndexError("deque is empty")
        else:
            return self.items[-1]
    def size(self):
        return len(self.items)

q1= deque()
q1.insertfront(10)    
q1.insertfront(20)

q1.insertrear(40) 
q1.insertrear(50)
q1.insertrear(70) 
print(q1.getfront(), q1.getrear())               


