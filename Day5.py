#Day 5

#Reverse List

#write a function to reverse the order of elements in a list

'''list1=[1,2,3,4,5]
list1.reverse()
print(list1) '''

'''list1=[1,2,3,4,5]
print(list1[::-1])'''

            
#check for palindrome list

'''list1=[1,2,3,2,1]
print(list1)
print(list1[::-1])

if list1==list1[::-1]:
    print("list is palindrome")
else:
    print("list is not palindrome") '''

#common element
'''list1=[1,2,3,4,5,2,3,4,7,8]
list2=[]
list3=[]
for i in list1:
    if i not in list2:
        list2.append(i)
    elif i not in list3:
        list3.append(i)
    else:
        pass
print(list2)
print(list3)
'''

#python object oriented programming

#class and object
# class Student:
#     roll_no = 101
    
#     def studentdata(self):
#         print("Student Information")
        
# obj = Student()
# print(obj.roll_no)
# obj.studentdata()


# class Demo:
#     def __init__(self):
#         print("I am constructor")
#     def msg(self):
#         print("Hello class!")
# obj1 = Demo()#I am constructor

# class Demo:
#     def __init__(self):
#         print("I am constructor")
#     def msg(self):
#         print("Hello class!")
# obj1 = Demo()
# # print(obj1) #<__main__.Demo object at 0x000002666AC88980>
# obj2 = Demo()
# obj1.msg()

# class Hod:
#     def __init__(self):
#         self.name='tanvi dhuri'
#         self.age = 22
#         self.empid = 1001
#     def info(self):
#         print("My name is :",self.name)
#         print("My age is :",self.age)
#         print("My emp id id ",self,self.empid)
# obj = Hod()
# obj.info()
# ---------------------------------------------------------------------
# op
# My name is : Khushi pawar
# My age is : 22
# My emp id id  <__main__.Hod object at 0x000001D6AFA28980> 1001


# class Hod:
#     def __init__(self,name,age,roll_no):
#         self.name = name
#         self.age = age
#         self.roll_no = roll_no
#     def show(self):
#         print("name = ",self.name)
#         print('age = ',self.age)
#         print('roll_no =',self.roll_no)
# obj = Hod('tanvi',43,101)
# obj.show()

# -----------------------------------------------------------------
# 10
# 10
# 10

# 20
# 10
# 10
# ---------------------------------------------------------------

# declaring instance variable outside a class by using object
# class Student:
#     def __init__(self):
#         self.s_name = "tanvi"
#         self.s_rollno = 101#declaring a instance var inside a constructor
#     def getdata(self):
#         self.s_mb = 28282828282#declaring a instance var inside a instance method
# obj = Student()
# obj.getdata()
# del obj.s_mb
# obj.s_branch = 'CS'#delete the instance variable using obj
# print(obj.__dict__)#adding instance variable by using object
# -----------------------------------------------------------
# {'s_name': 'tanvi', 's_rollno': 101, 's_branch': 'CS'}
# --------------------------------------------------------

# class New():
#     a =10
    
#     def __init__(self):
#         self.name = 'tanvi'
# obj1 = New()
# obj2 = New()
# obj3 = New()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)
# New.a = 50
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)


# import sys
# class Student():
#     def __init__(self):
#         print("Student Management System")
#         self.studentID = []
#         self.studentName = []
#         self.studentRollno = []
#         self.studentCity = []
#     def addStudent(self):
#         self.studentID.append(input("Enter the student ID: "))
#         self.studentName.append(input("Enter the student Name: "))
#         self.studentRollno.append(input("Enter the student Roll no: "))
#         self.studentCity.append(input("Enter the student City: "))
    
#     def showStudent(self,studentID,studentName,studentRollno,studentCity):
#         self.studentID = studentID
#         self.studentName = studentName
#         self.studentRollno = studentRollno
#         self.studentCity = studentCity

#     while True:
#         print("1.add student")
#         print("2.show student")
#         print("3.multiplication")
#         print("4.division")
#         print("5.exit")
#         choice=int(input("enter your choice :"))

#     if choice ==1 :
#         ()
#     elif choice ==2:
#         ()
#     elif choice ==3:
#         ()
#     elif choice ==4:
#         ()
#     elif choice ==5:
#          sys.exit()  
               
# obj1 = Student()
# obj1.addStudent()
# obj2 =showStudent()
# obj2.getdata()
        



# class Student:
#     def __init__(self,name,rollno,mob):
#         self.name=name   # instance variable
#         self.rollno=rollno
#         self.mob=mob

#     def display(self): #instance method
#         print(self.name,"",self.rollno,"",self.mob)

# stud=Student("tanvi",1013,8989898989)
# stud.display()



##static method
# we can use static method when the code that belongs to class it do not use the object


# class Student:
#     #by using class name we can access static method 
#     @staticmethod #decorator

#     def get_personal_detail(firstname,lastname):
#         print("your personal detail =",firstname,lastname)

#     @staticmethod 
#     def contact_detail(mobil_no,roll_no):
#         print("your contact detail=",mobil_no,roll_no)

# Student.get_personal_detail("tanvi","dhuri")
# Student.contact_detail(9898989898,1013)



#inheritance in python
#extending property from one to another class is called inheritance

# directly we are getting here reusability concept
#base class: a class which inherits its property to another is called base class or parent class
#derived class: a class in which properties are inherited called derived class or child class

#1:single level inheritance

# class collage:
#     def collage_name(self):
#         print("modern collage")

# class Student(collage):
#     def student_info(self):
#         print("name : tanvi dhuri")
#         print("branch : cs")

# obj=Student()
# obj.collage_name()
# obj.student_info()/

#multilevel inheritance


# class collage:
#     def collage_name(self):
#         print("modern collage")

# class Student(collage):
#     def student_info(self):
#         print("name : tanvi dhuri")
#         print("branch : cs")

# class Exam(Student):
#     def subject(self):
#         print("subject1 :python")
#         print("subject 2 : math")
#         print("subject3 : c ")

# obj=Exam()
# obj.collage_name()
# obj.student_info()
# obj.subject()

# class SubjMarks:
#     math=int(input("enter marks of math :"))
#     de=int(input("enter marks of DE :"))
#     c=int(input("enter marks of c"))
#     english=int(input("enter marks of english"))

# class PracMarks:
#     cpract= int(input("enter practicals marks of c langauge :"))

# class Result(SubjMarks,PracMarks):
#     def total(self):
#         if self.math>=40 and self.de>=40 and self.c>=40 and self.english>=40 and self.cpract>=20:
#             print("pass")
#         else:
#             print("fail")
# obj=Result()
# obj.total()


#polymorphism means having many forms 

#we can define polymorphism as the ability of message to be displayed in more than one form 

#poly example

# class principle:
#     def role(self):
#         print("i am managing all activity of collage")

# class Dean:
#     def role(self):
#         print("Dean = i am decision taking person ")

# class Hod:
#     def role(self):
#         print("Hod = i have responsibibilty of teachers and students ")

# class Faculty:
#     def role(self):
#         print("faculty = i have to complete syllabus successfully ")

# #class declaration complteted

# def func(obj):
#     obj.role() #calling fun
# campus=[principle(),Dean(),Hod(),Faculty()]

# for obj in campus:
#     func(obj) # calling function


#function overloading/Method overloading

# funtion overloading: a function having 

# class Arithmetic:
#     def add(self,a):
#         print(a)

#     def add(self,a,b):
#         print(a+b)

#     def add(self,a,b,c):
#         print(a+b+c)

# obj=Arithmetic()
# obj.add(10)
# obj.add(10,20)
# obj.add(1,2,3)

# to handle overloded method in python
# if mthod with variable number of argurments required then we can 
# handle ith default argument x 

# class Arithmetic:
#     def add(self,a=None,b=None,c=None):
#         if a!= None and b!= None:
#             print(a+b)
#         elif a!=None and b!=None and c!= None:
#             print(a+b+c)
#         else:
#             print("enter atleast 2 arguments")
# obj=Arithmetic()
# obj.add(10)
# obj.add(10,20)
# obj.add(1,2,3)            

   

#constuctor overloading
#consturtor overloading is not posssible in python
# if we ddefine multiple

#python support method overriding
#and constructor overriding 
#there is need to be parents and child reltion otherwise u cannot do verriding in python 
# #parents and child reltionship must be there 

# class Rbi:
#     def home_loan(self):
#         print("Home Loan =7.5")

#     def car_loan(self):
#         print("car loan 8 %")

# class Sbi(Rbi):
#     def home_loan(self):
#         print("Sbi provide home loan =6.5")
#         super().home_loan() # using super method we can access the parents class method in the child class

# obj=Sbi()
# obj.home_loan() #child class method overdide the parrent class method
# obj.car_loan()



#consturtor overriding
#child class consturor override the parents class 
# #parents and child reltionship must be there 
class Father:
    def __init__(self):
        print("father = i am already at the breakfasst ")

   
class Child(Father):
    def __init__(Father):

        print("child= i will be late for breakfast")
        super().__init__()

obj=Child()