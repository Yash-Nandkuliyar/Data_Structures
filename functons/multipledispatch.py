from multipledispatch import dispatch

@dispatch(int,int)
def mult(a, b):
    print(a * b)
    
@dispatch(int,int,int)    
def mult(a, b, c):
    print(a * b * c)
    
    
mult(2, 3, 5)
mult(2, 3)