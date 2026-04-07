#reverse each word in string
# str="Hello World"
# print(str[::-1])


# str="Hello World"
# str.reverse()
# print(str.reverse())


#write a word to compress a string by replcing consecutive character with their counts
# abstraction 

# str1="aaabbbcccc"
# str=[]
# for i in str1:
#     if i not in str1:
#         str.append(i)
#         print(str)
#     else:
#         print()


# str="aaabbbcccc"
# str1=[]
# count=3
# n=[]
# for i in str:
#     if i not in str1:
#         str1.append(i)
#     else:
#         pass
# for i in str:
#     if i in n:
#         count+=1
#     else:
#         n.append(i)

# print(str1)
# print(count)


# s = input("Enter string: ")
# result = ""
# count = 1

# for i in range(len(s)):
#     if i < len(s)-1 and s[i] == s[i+1]:
#         count += 1
#     else:
#         result = result + s[i] + str(count)
#         count = 1
# print(result)


# #  Abstarct method 
# from abc import ABC , abstractmethod
# class Help4code(ABC):
#     @abstractmethod 
#     def training(self):
#         pass

#     def placement(self):
#         pass

# class Prashant(Help4code):

#     def training(self):
#         print("c","c++","java")

#     def placement(self):
#         print("java placement")

# class Ashish(Help4code):

#     def training(self):
#         print("python | django")

#     def placement(self):
#         print("python placement student")


# class Ankush(Help4code):

#     def training(self):
#         print("Machine Learning")

#     def placement(self):
#         print("Data science placement")


# obj1=Prashant()
# obj1.training()
# obj1.placement()


# obj2=Ashish()
# obj2.training()
# obj2.placement()


# obj3=Ankush()
# obj3.training()
# obj3.placement()



#IRCTC

# from abc import ABC , abstractmethod

# class irctc(ABC):

#     @abstractmethod
#     def bookTicket(self):
#         pass

# class MakeMyTrip(irctc):

#     def bookTicket(self):
#         print("========================================")
#         print("welcome to makemytrip")
#         source=input("enter a source station name")
#         destination=input("enter a destination station name")
#         date=input("enter date")
#         print("=========================================")



# class Golbibo(irctc):

#     def bookTicket(self):
#         print("welcome to golbibo")
#         source=input("enter a source station name")
#         destination=input("enter a destination station name")
#         date=input("enter date")

# class Yatra(irctc):
#     def bookTicket(self):
#         print("welcome to yatra")
#         source=input("enter a source station name")
#         destination=input("enter a destination station name")
#         date=input("enter date")


# m=MakeMyTrip()
# m.bookTicket()
# g=Golbibo()
# g.bookTicket()
# y=Yatra()
# y.bookTicket()


#Encapsulation is one of the fundamental principles of Object-Oriented Programming (OOP). encapsulation is a way to protect our data member and member function. encapsulation is a way to make your data member and member function Public, Private and Protected.But Python does not have explicit access modifiers like Public, Private and Protected as in languages like Java or C++. Instead, it uses naming conventions:

# class Base: #parent class
#     def __init__(self):
#         print("parent class construtor called")
#         self.a="tanvi" #public data member
#         self.__c="pooja" #private  member

# #creating a derived class /child cxlass
# class Derived(Base): #child class 
#     def __init__(self):
#         #calling constructor of base class
#         Base.__init__(self)
#         # print("calling private member of base class :")
#         # print(self.a)
#         # print(self.__c)


# # obj1=Derived()
# # print(obj1.a)
# # print(obj1.__c)
# obj2=Base()
# print(obj2.a)#accessible
# print(obj2.__c) #not accessible


# class Rbi:
    
#     # declaring public method
#     def publicPolicy(self):
#         print("check the public policy of RBI")

#     # declaring private method
#     def privatePolicy(self):
#         print("there is some private policy which is not accessible for public")

# class Sbi(Rbi):
#     def __init__(self):#1st sbi class const called 
#         Rbi.__init__(self)#2nd parent class constr called


#     def callingPublicMethod(self):#child class public method
#         print("\n inside child class")
#         self.publicPolicy()#calling private class parent method


#     def callingPrivateMethod(self): #child class public method
#         self.privatePolicy() #calling private class parent method

# obj1=Sbi()
# obj1.callingPublicMethod()
# obj1.callingPrivateMethod()
# obj1.publicPolicy()
# obj1.__privatePolicy()
# obj2=Rbi()
# obj2.publicPolicy()
# obj2.__privatePolicy()
# obj2=Rbi()
# obj2.publicPolicy()
# obj2._Rbi__privatePolicy()


# task 1

# n=int(input("enter size of the list :"))
# n1=int(input("enter the values of list :"))
# print(n)
# print(n1,end=" ,")
# for i in n1:
#     if n1 %2 == 0:
#         print("even no")
#     else:
#         print("odd no")



#DATA STRUCTURES AND ALGORITHMS 
#stack implementation without size limit

# import sys 
# class Stack:
#     def __init__(self):
#         self.stackList=[] #stack created

#     def push(self,value):
#         self.stackList.append(value)

#     def displayStack(self):
#         print("-------------------------------")
#         print(self.stackList)
#         print("-------------------------------")

#     def isEmpty(self):
#         if self.stackList==[]:
#             return True
#         else:
#             return False
        
#     def pop(self):
#         if self.isEmpty():
#             return "stack is empty"
#         else:
#             return self.stackList.pop()
        
#     def deleteStack(self):
#         self.stackList=None
#         return "stack is deleted"
    
#     # def exitStack(self):
#     #     self.stackList=[]

#     def peek(self):
#         if self.isEmpty():
#             return "stack is empty"
#         else:
#             return self.stackList[-1]
        
# stackObj = Stack()    # stack object has created 
        
# while True:
#     print("1. push element in stack : ")
#     print("2. Display stack element : ")
#     print("3. check stack is empty")
#     print("4.pop operation")
#     print("5 Delete stack")
#     print("6.peek operetion")
#     print("7 Exit")

#     choice=int(input("enter your choice:"))
#     if choice==1:
#         val=int(input("enter the value for stack : "))
#         stackObj.push(val)

#     elif choice==2:
#         stackObj.displayStack()

#     elif choice==3:
#         print(stackObj.isEmpty())

#     elif choice==4:
#         print(stackObj.pop())

#     elif choice==5:
#         print(stackObj.deleteStack())

#     elif choice==6:
#         print(stackObj.peek())

#     elif choice==7:
#         sys.exit()

        


#stack implementation with size limit
# import sys 
# class Stack:
#     def __init__(self,stackSize):#parameterized construtor
#         self.stackList=[] #stack created
#         self.stackSize=stackSize

#     def isFull(self):
#         if len(self.stackList)==self.stackSize:
#             return True
#         else:
#             return False
        
#     def push(self,value):
#         if self.isFull():
#             print("stack is full")

#         else:
#             self.stackList.append(value)

            
#     def displayStack(self):
#         print("-------------------------------")
#         print(self.stackList)
#         print("-------------------------------")

#     def isEmpty(self):
#         if self.stackList==[]:
#             return True
#         else:
#             return False
        
#     def pop(self):
#         if self.isEmpty():
#             return "stack is empty"
#         else:
#             return self.stackList.pop()
        
#     def deleteStack(self):
#         self.stackList=None
#         return "stack is deleted"
    
#     # def exitStack(self):
#     #     self.stackList=[]

#     def peek(self):
#         if self.isEmpty():
#             return "stack is empty"
#         else:
#             return self.stackList[-1]
        
# size=int(input("enter the size of stack : "))      
# stackObj = Stack(size)    # stack object has created 
        
# while True:
#     print("1. push element in stack : ")
#     print("2. Display stack element : ")
#     print("3. check stack is empty")
#     print("4.pop operation")
#     print("5 Delete stack")
#     print("6.peek operetion")
#     print("7 Exit")

#     choice=int(input("enter your choice:"))
#     if choice==1:
#         val=int(input("enter the value for stack : "))
#         stackObj.push(val)

#     elif choice==2:
#         stackObj.displayStack()

#     elif choice==3:
#         print(stackObj.isEmpty())

#     elif choice==4:
#         print(stackObj.pop())

#     elif choice==5:
#         print(stackObj.deleteStack())

#     elif choice==6:
#         print(stackObj.peek())

#     elif choice==7:
#         sys.exit()

        


#TOWER OF HANNOI

import sys
a=[1,2,3]
b=[]
c=[]
i=0
class TowerOfHannoi:
    pass

    def  A(self):
        if i in a:
            a.pop(i)
            c.append(i)
            print(c)
        else:
            pass

    def B(self):

        if i in b:
            a.pop(i)
            b.append(i)
            print(b)

    def C(self):

        if i in c:
            a.pop(i)
            b.append(i)
            print(b)
        else: 
            pass

obj1=TowerOfHannoi()
obj1.A()
obj1.B()
obj1.C()





import time
class Tower:
    def __init__(self):
        print("WELCOME TO TOWER OF HANNOI GAME")
        print()
        print("given problem A=[3,2,1] , B=[],C=[]")
        print()
        print("expected output A=[] ,b=[],c[3,2,1]")
        self.A=[]
        self.B=[]
        self.C=[]

def Tower(self,item):
    self.A.append(item)
    time.sleep(3)
    print("A=",self.A)
    print("items in tower A\n")


def pass1(self):
    self.temp=self.A.pop(2)#a=[3,2]
    self.C.append(self.temp) #c=[1] => temp1
    time.sleep(3)
    print("A =",self.A,"  ","B =",self.B,"    ","C=",self.c)
    print("pass one completed =============================")


def pass2(self):
    self.temp=self.A.pop(2)#a=[3,2]
    self.C.append(self.temp) #b=[2] => temp2
    time.sleep(3)
    print("A =",self.A,"  ","B =",self.B,"    ","C=",self.c)
    print("pass one completed =============================")


def pass3(self):
    self.temp=self.A.pop(0)#c=[]
    self.C.append(self.temp) #c=[2,1] => temp1
    time.sleep(3)
    print("A =",self.A,"  ","B =",self.B,"    ","C=",self.c)
    print("pass one completed =============================")

def pass4(self):
    self.temp=self.A.pop(0)#a=[3,2]
    self.C.append(self.temp) #c=[1] => temp1
    time.sleep(3)
    print("A =",self.A,"  ","B =",self.B,"    ","C=",self.c)
    print("pass one completed =============================")

def pass5(self):
    self.temp=self.A.pop(1)#a=[3,2]
    self.C.append(self.temp) #c=[1] => temp1
    time.sleep(3)
    print("A =",self.A,"  ","B =",self.B,"    ","C=",self.c)
    print("pass one completed =============================")

def pass6(self):
    self.temp=self.A.pop(2)#a=[3,2]
    self.C.append(self.temp) #c=[1] => temp1
    time.sleep(3)
    print("A =",self.A,"  ","B =",self.B,"    ","C=",self.c)
    print("pass one completed =============================")



def pass7(self):
    self.temp=self.A.pop(3)#a=[3,2]
    self.C.append(self.temp) #c=[1] => temp1
    time.sleep(3)
    print("A =",self.A,"  ","B =",self.B,"    ","C=",self.c)
    print("pass one completed =============================")


obj=Tower()
obj.Tower(3)
obj.Tower(2)
obj.Tower(1)
obj.pass1()
obj.pass2()
obj.pass3()
obj.pass4()
obj.pass5()
obj.pass6()
obj.pass7()