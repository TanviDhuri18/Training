
#Day 4
 #program 1
'''print('tanvidhuri222'.isalnum())
print('tanvidhuriS'.isalpha())
print('222f'.isdigit())
print('sdsdsdsdssd'.islower())
print(''.islower())
print('TANVId'.isupper())
print('My Name Is Tanvi'.istitle())
print(''.istitle())
print(''.isspace())
print('hello'.startswith('He'))
print('hello'.endswith('lo'))
'''

#jaffrie inetern
#amriecan genius



'''print("tanvi".find("z"))
print("tanvi".index("t"))
print("tanvi dhuri".count("i"))'''


#Q 4 check if key exists in  a dictionary
'''dict1={"tanvi":2,"darshana":5,"dipak":16}
rec=input("enter the name :")
rec1=(dict1,key=dict1.get)

if  dict1==rec1:
    print("key exists ")
else:
    print("no ")'''


#count frequecy of elements in a list using a dictionary
'''count1={"tanvi":2,"darshana":5,"dipak":16}
print("tanvi,darshana,dipak".count(""))
'''



#Exception Handling
#runtime error callled exception

'''n1=int(input("enter 1st the value :"))
n2=int(input("enter 2nd the value :"))
try:
    print(n1/n2)
except:
    print("cant divide by zero")

print("to be continnue")'''



'''try:
    n1=int(input("enter 1st the value :"))
    n2=int(input("enter 2nd the value :"))
    print(n1/n2)
except ValueError:
    print("enter only integer")
    
except ZeroDivisionError:
    print("cant divide by zero")

print("to be continnue")'''


#handling multiple exception with single except block
'''try:
    n1=int(input("enter 1st the value :"))
    n2=int(input("enter 2nd the value :"))
    print(n1/n2)
except (ValueError,ZeroDivisionError) as message:
    print(message)'''


#the concept of default except block ,generly we uesd 

'''try:
    n1=int(input("enter 1st the value :"))
    n2=int(input("enter 2nd the value :"))
    print(n1/n2)
except (ValueError,ZeroDivisionError) as message:
    print("enter the correct no ",message)
except:
    print("this is default part of except block ")'''

#we can use else block if no error will generte it is
'''try:
    n1=int(input("enter 1st the value :"))
    n2=int(input("enter 2nd the value :"))
    print(n1/n2)
except (ValueError,ZeroDivisionError) as message:
    print("enter the correct no ",message)
else:
    print("everything is okay")
    '''

#finally block will always exceuted whether try block
#generate error or not

'''try:
    n1=int(input("enter 1st the value :"))
    n2=int(input("enter 2nd the value :"))
    print(n1/n2)
except (ValueError,ZeroDivisionError) as message:
    print("enter the correct no ",message)
finally:
    print("i will always executed")'''



#nested try except block
#try

'''try:
    n1=int(input("enter 1st the value :"))
    n2=int(input("enter 2nd the value :"))

    try:
         print(n1/n2)

    except ZeroDivisionError as msg:
        print(msg)
        
except ValueError as msg:
       print(msg)'''


'''try:
    n1=int(input("enter 1st the value :"))
    n2=int(input("enter 2nd the value :"))
    print(n1/n2)
    
except (ValueError,ZeroDivisionError) as message:
    print("enter the correct no ",message)
    
else:
    print("everything is okay")
    
finally:
    print("i will always executed")
'''

#user defined  exception by raise keyword 


'''l1=[1,2,3,4,5,6,6,9,6,7,8,9]
l2=[]
l2=l1.copy()
l2.count()
print("this are the data which is reciving from the another server",l2)
print("this is the count: ",l2)
try:
    print(" server ")
finally:
    print("data transmitted succesfully") '''


'''l1=[5,7,8,3,7,8,9,2,3]
l2=[]

for i in range(len(l1)):
    count=0
    key=l1[i]

    j=i+1
    while j<len(l1):
        if key == l1[j]:
            l2.append(key)
        j=j+1
print(len(l2))
'''

#find the 2nd largest element

'''list=[7,3,9,2,8]
list.sort()
print(list)
print(list[-3])'''

#while loop

'''i=1
while i<=5:
    print(i)
    i=i+2
    
'''

'''username=""
password=""
while username!="admin" or  password!="admin":
    username=input("enter username :")
    password=input("enter password : ")'''


'''
name="programming"
vowels=['a','e','i','o','u']
cons=0
vowel=0
for i in name:
    if i in vowels:
        vowel+=1
    else:
        cons+=1
print("consonent in str is:",cons)
print("vowels in str is :" ,vowel)'''
    

  
#remove all occurence of an element in a list
'''list1=[1,2,2,3,4,2]
list2=[]
for i in list1:
    if i ==list2:
        print(list2)
    else:
        list2.append(list1)
        print("")'''

#write function to calculate the product of all elements 

'''list1=[1,2,2,3,4,2]
list2=[]
for i in list1:
    if i!=2:
        list2.append(i)
        print(list2)'''

'''list1=[1,2,2,3,4,2]
while 2 in list1:
    list1.remove(2)
print(list1)'''


#calculate the product of list

'''list1=[1,2,2,3,4,2]
list2=[]
list2=list1*list1
print(list2)'''




#file Handling
#program1
'''f=open("myfile.txt","w")
print("my name of file :",f.name)
print("file mode :",f.mode)
print("readable :",f.readable())
print("writable :",f.writable())
print("file closed :",f.closed)
f.close()
print("file closed: ",f.closed)'''


#program2
'''f=open("myfile.txt","w")
f.write("\n pune is smart city")
f.close()
print("file operation is done")'''


#insert list
'''f=open("myfile.txt","w")
mylist=["tanvi","pooja","khushi","disha"]
f.writelines(mylist)
f.close()
print("written work is done successfully ")'''


#reading data from a file
'''f=open("myfile.txt","r")
print(f.read())
f.close()'''

#with statement
'''with open("myfile.txt","w") as f:
    f.write("tanvi\n")
    f.write("pooja\n")
    f.write("disha\n")
    f.write("khushi\n")
    print("file closed :",f.closed)
print("file closed :",f.closed)'''


'''with open("myfile.txt","r") as f:
    content=f.read()
    print(content)'''


'''f1=open("con.png","rb")
f2=open("conn.png","wb")
data=f1.read() #it will read entire binary information of png
f2.write(data)
print("new image is available with the name")'''



#operation with csv file
'''import csv
f = open("student.csv", "a", newline="")
a = csv.writer(f)
a.writerow(["studentID", "rollno", "name", "mobileno"])

studentid=int(input("enter student id :"))
rollno=int(input("enter your roll no: "))
name=input("enter your name :")
mobileno=int(input("enter your mobile no:"))
a.writerow([studentid, rollno, name, mobileno])
print("student record has save")
f.close() '''


import csv
f = open("student1.csv", "a", newline="")
a = csv.writer(f)
'''a.writerow([ "rollno", "name", "mobileno","p1","p2","p3","total","percentage"])'''

rollno=int(input("enter your roll no: "))
name=input("enter your name :")
mobileno=int(input("enter your mobile no:"))
email=int(input("enter your email:"))
p1=int(input("enter p1"))
p2=int(input("enter p2"))
p3=int(input("enter p3"))

if p1>=40 and p2>40 and p3>40:
    result="pass"
else:
    result=" fail"
    
total=p1+p2+p3
percentage=total/3

a.writerow([rollno, name, mobileno,p1,p2,p3,total,percentage,result])
print("student record has save")
f.close()


