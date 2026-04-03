'''math=50
name="tanvi"
pi=3.14
result=True
print(type(math))
print(type(name))
print(type(pi))
print(type(result))'''

''' pyhton initerpreter decides runtime environement '''

'''math=50
name="tanvi"
pi=3.14
result=True
print(id(math))
print(id(name))
print(id(pi))
print(id(result))'''


'''math=50
chem = 50
result=True
print(id(math))
print(id(chem))
print(id(result))'''


'''list=[[1,2,3]
      [4,5,6]
      [7,8,9] ]
list[row][col]
list[0][0]=1
list[1][1]=5
list[2][2]=9

if i==j:
    sum +=i '''



'''print(2+2)
print("2"+"2")
val1=input("enter value of val 1:")
val2=input("enter value of val 2:")
print(val1+val2)
'''
''' input funtion by default accept  only string value'''

'''print(2+2)
print("2"+"2")
val1=int(input("enter value of val 1:"))
val2=int(input("enter value of val 2:"))
print(val1+val2)'''


#int() used to covert in integer
#we cant convert complex value to int
#we can not convert flaoting point value string to int

#we cant convert string name int

'''
print(int(3.14))
print(int(10+5j))
print(int(True))
print(int(False))
print(int("4.22"))
print(int("4"))
print(int("tanvi")) 
'''

'''
print(float(3))
print(float(True))
print(float(False))
print(float("4.22"))
print(float("4"))
print(float("tanvi")) '''


'''print(complex(3))
print(complex(12,5))
print(complex(True))
print(complex(False))
print(complex("5"))
print(complex(5.6))
print(complex("name"))
print(complex(5,-3))
print(complex(True,False))'''


'''print(bool(0))
print(bool(14))
print(bool(3.14))
print(bool(0.0))
print(bool(1+2j))
print(bool())
print(bool(-1))
print(bool(False))
print(bool(True))
print(bool("tanvi"))'''


#33 reserve keywords in python , all reserve keywords are inn lower case instead of True False None these three keywords'''



'''val1=input("enter value of val 1:")
val2=input("enter value of val 2:")
print("before swapping val1 =",val1,"val2=",val2)
temp = val1 
val1=val2 
val12=temp
print("after swapping val1 =",val1,"val2=",val2)'''

'''a=100
b=200
print(a)
print(b)
print(a=a+b)
print(b=a-b)
print(a=a-b)
'''
''' (100+200=300)a=300
(300-200=100)b=100
(300-100=200)a=200

'''


'''p1=int(input("enter marks of p1:"))
p2=int(input("enter marks of p2:"))
p3=int(input("enter marks of p3:"))
total=p1+p2+p3
percentage=total/3.0
print("Total =",total )
print("percentage=",percentage)'''


'''p_amount=int(input("enter principle amount :"))
roi=int(input("enter the rate of interest :"))
time=int(input("enter the duration of loan amount :"))

si=p_amount*roi*time/100
print("simple interest =",si)'''


'''h=float(input("enter the height:"))
inch=float(input("enter the inch:"))
cm=float(input("enter the cm:"))
inch=h*12
cm=inch*2.54
print("inch=",inch)
print("cm=",cm)'''


'''num= 123    #num 321
a = num %10
num = num // 10
b=num%10
c=num//10
rev=a*100+b*10+c*1
print(rev)'''


'''123456'''

#when we want to address comparioson then we should go for identity operetor two type of operetor 1.is 1.is not

'''a=10
b=10
print(a is b)#False
print(a is not b)#True
'''



#membership opertaor
#by using membership operetor we check that the object is present or not in collection data struture like list tuple set and dict and string


'''name="help4code"
print("z"in name )
print("p"in name );'''


#wap to accept any one no and  check pos,neg and zero
'''n1 = int(input("enter the any 1st number  :"))
n2= int(input("enter the any 2nd number  :"))
n3 = int(input("enter the any 3rd number  :"))
n4= int(input("enter the any 4th number  :"))
n5= int(input("enter the any 5th number  :"))

if no1<no2:
    print("no2 is maximum")
if no2<no3:
    print("no3 is maximum")
if no3<no4:
    print("no4 is maximum")
if no4<no5:
    print("no5 is maximum")
if no5<no1:
    print("no1 is maximum")

if n1>n2 and n1> n3 and n1>n4 and n1>n5:
    print("n is greater =",n1)
if n2>n1 and n2> n3 and n2>n4 and n2>n5:
    print("n is greater =",n2)
if n3>n1 and n3> n2 and n3>n4 and n3>n5:
     print("n is greater =",n3)
if n4>n1 and n4> n2 and n4>n3 and n4>n5:
    print("n is greater =",n4)
if n5>n1 and n5> n2 and n5>n3 and n5>n4:
    print("n is greater =",n2)
'''



'''username=input("enter username")
password=input("enter password")
if username==password:
    print("login successful")
else:
    print("invalid credential")'''


#wap to accept phy ,chem and maths subjects marks calculate total and percentage and if percetange is greater than equal to 60 and gender is equal to male he is eleigible for placement elese eleigble for data entry job
'''phy = int(input("enter the phy marks:"))
chem= int(input("enter the chem marks :"))
math = int(input("enter the maths marks  :"))
total=phy+chem+math
print("total=",total)
percentage=total/3
print("percentage=",percentage)
gender=input("enter the gender is m/f")
if percentage>60 and gender=="m":
    print("eligeble for placement ")
else:
    print(" not eligeble for placement ")'''



#wap to accept value a,b,c and find max value

'''a= int(input("enter the any 1st number  :"))
b= int(input("enter the any 2nd number  :"))
c = int(input("enter the any 3rd number  :"))
if a>b:
    if a>c:
        print("b is maximum")
    else:
         print("c is maximum")

else:
    if b>a:
        print("c is maximum")
    else :
        print("a is maximum")
'''

#weekdays
'''day=input("enter the day :")
if day=="saturday" or day=="sunday" or day=="SATURDAY" or day=="SUNDAY":
    print("its holiday today")
else:
   print ("its working day ")'''



#wap to accept any one char from keyboard and check it is in upper case ,lower case,digit and special symbol so print message with respect to enetred value :

''' ch=ord(input( "enter any word ,digit ,or symbol : "))

if ch>=65 and ch<=91:#A=65
    print("your entered charcater is in uppper case")
elif ch>=97 and ch<=122:#a=97
    print("your entered charcater is in lowerr case")
elif ch>=48 and ch<=57:#0=48
    print("your entered charcahter is digit")
else:
     print("your entered charcater is special symbols")

'''

'''#wap for change calculation with respect to total amount
amount=int(input("please enter amount for withdraw:"))#785
print("100 notes =",amount//100)
print("50 notes =",(amount %100)//50)
print("20 notes =",((amount %100)%50)//20)
print("10 notes =",(((amount %100)%50)%20)//10)
print("5 notes =",((((amount %100)%50)%20)%10)//5)

'''      




