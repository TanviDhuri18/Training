#Dictionary


#program1
'''mydict={
    101:"pooja",
    102:"tanvi",
    "103":"ankita",
    "104":"dipali",
    101:"tanvi",
    104:"tanvi"

}
print(mydict)'''


#with the help of key we have to print values

'''a=mydict[102]
print(a)'''


#we will replace old value with new value
'''mydict[102]="dipak"
print(mydict)'''


#only print key x=0,1
'''for x in mydict:
    print(x)'''

'''for x in mydict.values():
    print(x)'''

'''for x,y in mydict.items():
    print(x,y)'''


#if i have to add new key and value pair in my dictionary
'''mydict["mobile_no"]=8468945854
print(mydict)'''


#mcq1
'''a={(1,2):1,(2,3):2,(4,5):3}
print(a[4,5])'''


#mcq2
'''a={'a':1,'b':2,'c':3}
print(a['a','b'])'''

#mcq3
'''arr={}
arr[1]=1
arr['1']=2
arr[1]+=1

sum=0
for k in arr:
    sum+=arr[k]
print(sum) '''

#mcq4
'''my_dict={}
my_dict[1]=1
my_dict['1']=2
my_dict[1.0]=4

sum=0
for k in my_dict:
    sum+=my_dict[k]
print(my_dict)
print(sum) 
'''

#mcq5

'''my_dict={}
my_dict[(1,2,4)]=8
my_dict[(4,2,1)]=10
my_dict[(1,2)]=12

sum=0
for k in my_dict:
    sum+=my_dict[k]
print(my_dict)
print(sum) '''


#mcq6
'''box={}
jars={}
crates={}
box['biscuit']=1
box['cake']=3
jars['jam']=4
crates['box']=box
crates['jars']=jars
print(len(crates[box]))'''

#mcq7
'''dict={'c':97,'a':96,'b':98}
for _ in sorted(dict):
    print(dict[ _ ])'''

#mcq8
'''rec={"name":"python","age":"20"}
r=rec.copy()
print(id(r))
print(id(rec))

print(id(r)==id(rec))'''

#mcq9
'''rec={"name":"python","age":"20"}
id1=id(rec)
print(id(id1))
del rec
rec={"name":"python","age":"20"}
id2=id(rec)
print(id(id2))
print(id1==id2)'''

#program 2
#find the key with the minimum value in dictionary
'''rec={"a":67,"b":89,"d":20}
for i in rec:
    if i>rec:
        min.rec(item)
        print(rec)'''
     
'''rec={"a":67,"b":89,"d":20}
rec1=min(rec,key=rec.get)
print("print minimum value form key value pairs:",rec1)'''



#pop item 
'''mydict={
    101:"pooja",
    102:"tanvi",
    "103":"ankita",
    "104":"dipali",
    104:"tanvi"

}
mydict.pop(101)
print(mydict)'''


#nested for loop

#(i,j)=(2,3)

'''for i in range(1,4):
    for j in range(1,4):
        print(i,end="  ")
    print()'''

'''n=int(input("enter no of rows :"))
for i in range(1,n+1):
    for j in range(1,1+i):
        print(j,end="  ")
    print()'''

'''n=int(input("enter no of rows :"))
for i in range(1,n+1):
    for j in range(1,1+i):
        print(chr(64+i),end="  ")
    print()'''

'''import time
n=int(input("enter no of rows :"))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        time.sleep(2)
        print("*",end=" ")
    print()


n=int(input("enter no of rows :"))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(chr(64+j),end="  ")
    print()'''

#program 8

'''import time
n=int(input("enter no of rows :"))
for i in range(1,n+1): #i=1
    print(""*(n-i),end="")
    for j in range(1,i+1):#3
        time.sleep(2)
        print(chr(64+i),end=" ")
    print()
'''




#function in python
'''def msg():#called function
    print("hello world")


msg()#calling function
msg()'''


'''def arithmetic():
    a=int(input("enter the value of A: "))
    b=int(input("enter the value of B: "))
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return add,sub,mul,div

#print(arithmetic())#calling function

result=arithmetic()
print('arithmetic=',result)'''



#how many types of argumets we can pass in function : ans= 1) positional arg 2)keyword arg 3) default arg 4)variable no of arg / variable length arg


#positional arg
'''def login(username,password):
    if username== password:
        print("login successful")
    else:
        print("invalid credintial")


username=input("eneter username :")
password=input("enter password : ")
login(username,password) #calling function'''



#keyword arg
'''def login(username,password):
    if username== password:
        print("login successful")
    else:
        print("invalid credintial")

login(username="tanvi",password="tanvi")'''


#default arg
'''def cityName(city="goa"):
    print(city)

cityName("delhi")
cityName("nagpur")
cityName()'''


#variable length arg / variable no of arg

'''def nameOfCity(*city):
    print("city name's=",city)
nameOfCity("goa","sawantwadi","vengurla","kudal")

'''


#wap for menu driven code
'''import sys
def add():
    val1=int(input("enter the value of val1 :"))
    val2=int(input("enter the value of val2 :"))
    print("add=",val1+val2)

def sub():
    val1=int(input("enter the value of val1 :"))
    val2=int(input("enter the value of val2 :"))
    print("sub=",val1-val2)
    
def mul():
    val1=int(input("enter the value of val1 :"))
    val2=int(input("enter the value of val2 :"))
    print("mul=",val1*val2)

def div():
    val1=int(input("enter the value of val1 :"))
    val2=int(input("enter the value of val2 :"))
    print("div=",val1/val2)
    
while True:
    print("1.addition")
    print("2.substraction")
    print("3.multiplication")
    print("4.division")
    print("5.exit")
    choice=int(input("enter your choice :"))

    if choice ==1 :
        add()
    elif choice ==2:
        sub()
    elif choice ==3:
        mul()
    elif choice ==4:
        div()
    elif choice ==5:
         sys.exit()'''

#codility         
    


#1.rstrip() ==> to remove spaces at a right hand side
#2.lstrip() ==> to remove spaces at a left hand side 
#3.strip() ==> to remove spaces at a both side 

'''programming =input("enter your programming name:")
p_name=programming.rstrip()
if p_name=='python':
     print(p_name)
elif p_name=='java':
     print(p_name)
elif p_name=='cpp':
     print(p_name)
else:
    print("wrong programming name ")'''

def timeConversion(s):
    # Write your code here
    hour_str=s[:2]
    minutes_seconds=s[2:8]
    am_pm=s[8:]
    
    
    hour_int=int(hour_str)
    
    
    if am_pm=="pm":
        if hour_int!=12:
            hour_int+=12
    else: 
        if hour_int==12:
            hour_int=0
            
            
    hour_str_24=str(hour_int).zfill(2)
    
    return hour_str_24 + minutes_seconds
        
    

