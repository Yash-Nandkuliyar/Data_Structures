class node:
    def __init__(self, item=None,next=None):
        self.item=item
        self.next=next

class queue:
    def __init__(self):
        self.item_count=0
        self.front=None
        self.rear=None

    def isempty(self):
        return self.front==None
    def enqueue(self,data):
        n=node(data)
        if self.isempty():
            self.front=n
        else:
            self.rear.next=n
        self.rear=n
        self.item_count+=1
    def dequeue(self):
        if self.isempty():
            raise IndexError("empty queue")
        elif self.front==self.rear:
            self.front==None
            self.rear==None
        else:
            self.front=self.front.next

        self.item_count-=1

    def getfront(self):
        if self.isempty():
            raise IndexError("empty queue") 
        else:
            return self.front.item

    def getrear(self):
        if self.isempty():
            raise IndexError("empty queue") 
        else:
            return self.rear.item
    def size(self):
        return self.item_count
    
q1=queue()
q1.enqueue(19)
q1.enqueue(13)
q1.enqueue(15)
q1.enqueue(10)
print(q1.getfront(),q1.getrear())
q1.dequeue()
print(q1.getfront(),q1.getrear())


    
             