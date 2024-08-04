class Node:
    def __init__(self,item=None,prev=None,next=None):
        
        self.item=item
        self.next=next
        self.prev=prev

class deque:
    def __init__(self):
        self.front=None
        self.rear=None
        self.itemcount=0

    def isempty(self):
        return self.front==None
    def insertfront(self,data):
        n=Node(data,None,self.front)
        if self.isempty():
            self.front=n
            self.rear=n
        else:
            self.front.prev=n
        self.front=n
        self.itemcount+=1        
    def insertrear(self,data):
        n=Node(data,self.rear)
        if self.isempty():
            self.front=n
        else:
            self.rear.next=n
        self.rear=n
        self.itemcount+=1

    def deletefront(self):
        if self.isempty():
            raise IndexError("is empty")
        if self.front==self.rear:
            self.front=None
            self.rear=None
        else :
            self.front=self.front.next
            self.front.prev=None

    def deleterear(self):
        if self.isempty():
            raise IndexError("is empty")
        if self.front==self.rear:
            self.front=None
            self.rear=None
        else :
            self.rear=self.rear.prev
            self.rear.next=None
        self.itemcount-=1
    def size(self):
        return self.itemcount 
    def getfront(self):
        if self.isempty():
            raise IndexError("fnsefknsdfbndm")
        return self.front.item
    def getrear(self):
        if self.isempty():
            raise IndexError("fnsefknsdfbndm")
        return self.rear.item       
    
d=deque()
d.insertfront(3333)
d.insertfront(4444)
d.insertfront(5555)
d.insertfront(6666)
d.insertrear(343333)
d.insertrear(66676)
print(d.getfront())
print(d.getrear())
print(d.itemcount)
d.deletefront()
d.deleterear()
print(d.getfront())
print(d.getrear())
print(d.itemcount)







 