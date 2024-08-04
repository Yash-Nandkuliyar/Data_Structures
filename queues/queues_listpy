class queue:
    def __init__(self):
        self.items=[]
        #self.front=None
        #self.rear=None
    
    def isempty(self):
        return len(self.items)==0
    
    def enqueue(self,data):
        self.items.append(data)

    def dequeue(self):
        if not self.isempty():
            self.items.pop(0)
        else:
            raise IndexError("underflow")     

    def getfront(self):
        if not self.isempty():
            return self.items[0]
        else:
            raise IndexError("underflow") 
    def getrear(self):
        if not self.isempty():
            return self.items[-1]
        else:
            raise IndexError("underflow")    
    def size(self):
        return len(self.items)
        
q1=queue()
print(q1.getfront())
try:
    print(q1.getfront())
except IndexError as e:
    print(e.args[0])
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
print("front",q1.getfront(),"rear",q1.getrear())

        
