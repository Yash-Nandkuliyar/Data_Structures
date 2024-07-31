# #l1=[1,2,3]
# #l1.append(12)
# #l1.show()
# class test:
#     x=5
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b 
#     def show(self):
#         print(self.a,self.b)
        
#     @staticmethod
#     def f2():
#         print("hello")
#     @classmethod
#     def f3(cls):
#         print(cls.x)

#     # x=5
#     # def f1():
#     #     print("hello")
# t1=test(3,4)
# t2=test(5,6) 
# t1.show()
# t2.show()
# test.f3()
# test.f2()
# # print(t1.a,t1.b)
# # print(t2.a,t2.b )       
class employee:
    def __init__(self,empid=None,name=None,salary=None):
        self.empid=empid
        self.name=name
        self.salary=salary
    def setempid(self,empid):
        self.empid=empid
    def setname(self,name):
        self.name=name
    def setsalary(self,salary):
        self.salary=salary            
    def getempid(self):
        return self.empid
    def getname(self):
        return self.name
    def getsalary(self):
        return self.salary
e1=employee()
e2=employee(1,"yash",4000)
e1.setempid(2)
e1.setname("nand")
e1.setsalary(100000000)
print(e1.getempid(),e1.getname(),e1.getsalary())
print(e2.getempid(),e2.getname(),e2 .getsalary()) 