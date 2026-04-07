#program1
'''name="tanvidhuri"
#indexing=0123456789
print(name[0])
print(name[1])
print(name[-1])
#print(name[15]) string range out of range
print(name[0:5])#end -1 5-1=4 tanv
print(name[1:])#anvidhuri 
print(name[:5])#5-1=4 tanv
print(name[:])#tanvidhuri
print(name[1:6:2])#6-1=5=
print(name[::-1])'''

#program2
'''s="Python is a High level programming Language"
print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.title())
print(s.capitalize())'''

#program3
'''print("subjects marks:")
phy=50
chem=60
math=70
print("physics={} chemistry={} Math={}".format(phy,chem,math))
print("physics={0} chemistry={1} Math={2}".format(phy,chem,math))
print("physics={x} chemistry={y} Math={z}".format(x=phy,y=chem,z=math))
total=phy+chem+math
print("Total marks ",f"{total}")
print("Roll no=","7".zfill(4)) '''


#for loop
#program4
#looping (for(inti,con,inc/dec))
'''for i in range(1,11,2):#i=0
    print(i)'''


'''for i in range(1,11):
    print(i*2)'''

#program 5
''''for i in range(1,11):
     print(i*2," ", i*3," ",i*4," ",i*5)

print()

for i in range(1,11):
     print(i*11," ", i*12," ",i*13," ",i*14)'''

#program 6
'''name="racear"
            #012345
for i in name:
    print(i)'''

#program 7
#WAP to remove duplicates
'''uname=" tanvviii"
tname=" "
for i in uname:
    if i not in tname:
        tname+= i
print(uname)
print(tname)'''

'''for i in range(5,0,-1):
    print(i)'''

'''for i in range(10,0,-1):
    print(i)'''

'''name="tanvii"
nname=""
n=len(name)
for i in range(n-1,-1,-1):
    nname+=name[i]
print(nname)'''

#program 8
#wap to check for palindrome

'''str="racecar"
nname=""
n=len(str)
for i in range(n-1,-1,-1):
    nname+=str[i]
print(nname)'''

'''str="tanvi"
print(str)#left to right
print(str[::-1])#right to left

if str ==str[::-1]:
    print("str is palindrome")
else:
    print("str is not palindrome")'''



#list
##program 8 list program 
'''mylist=["tanvi","dipak",16,"darshana","dasharath","anu","shubhra",2,]
sprint(mylist)
print(type(mylist))
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[-1])
print(mylist[2:5])
print(mylist[:5])
print(mylist[1:])
print(mylist[1:8:2])
print(mylist[:])
print(mylist[::-1])

mylist[2]="pooja" '''

'''if "tanvi" in mylist:
    print("yes tanvi is there")
else:
    print("no tanvi is not")'''


'''mylist.append("khushi")
mylist.append("disha")
print(mylist)'''


'''mylist.insert(1,"ankita")
mylist.insert(2,"dipali")
print(mylist)'''

'''mylist.remove(2)
print(mylist)'''


'''newlist=mylist.copy()#cloning
print(newlist)'''

''''mylist=[["tanvi","dhuri"],["86.90"],[410022,"yyy"]]
print("eg of multidimentional list:")
print(mylist)
#print(mylist[row][col])
print(mylist[0][0])#tanvi
print(mylist[0][1])#dhuri
print(mylist[1][0])#86.90
print(mylist[2][0])#410022
print(mylist[2][1])#yyy'''

'''list1=["tanvi","dhuri"]
#print(list1*2) #it will print 2 lines

list2=[58,78,90]
#print(list1+list2)'''

'''list2=[58,78,90,"tanvi"]
del list2[2]
list2.clear()
print(list2)'''



'''name="tanvi" #str
print(name)
myname=list(name)
print(myname)'''


'''list2=[58,78,90]
list2.reverse()
print(list2)'''


'''list2=[58,78,90,99,45]
list2.sort(reverse=True) #reverse=True
print(list2)'''

'''list2=[58,78,90,99,45]
newlist=list2
print(id(list2))
print(id(newlist))
list2[0]="tanvi"
print(list2)
print(newlist)'''



#mcq1
'''arr=[[1,2,3,4],
         [4,5,6,7],
         [8,9,10,11],
         [12,13,14,15]]
for i in range(0,4):
    print(arr[i].pop())'''

#mcq2
'''arr=[1,2,3,4,5,6]
for i in range(1,6):
    arr[i-1]=arr[i]
for i in range(0,6):
    print(arr[i],end="")'''

#mcq 3
'''a=[1,2,3,4,5,6,7,8,9]
a[::2]=10,20,30,40,50,60
print(a)'''

#mcq 4
'''a=[1,2,3,4,5]
print(a[3:0:-1])'''



#Tuple

#program 9
'''mytuple=("tanvi","dipak",16,"darshana","dasharath","anu","shubhra",2)
print(mytuple)
print(type(mytuple))

mytuple[3]="pooja"
print(mytuple)'''

#mcq1

'''init_tuple=()#o/p=0
print(type(init_tuple))
print(init_tuple.__len__())'''

#mcq2
'''init_tuple_a='a','b'
init_tuple_b=('a','b')
print(init_tuple_a==init_tuple_b)'''


#mcq3
'''init_tuple_a='1','2'
init_tuple_b=('3','4')
print(init_tuple_a+init_tuple_b)'''

#mcq4
'''init_tuple=('python',)
print(type(init_tuple))'''

#mcq5
'''init_tuple=(1,)*3
init_tuple[0]=2
print(init_tuple)'''


#mcq6

'''init_tuple=((1,2),)*7
print(len(init_tuple[3:8]))'''



'''names=[4,2,5,6,8,2]
for i in names:
    print(i)'''


#program 10
'''a=[4,0,2,5,0,1]#moves zero in the last
for i in a:

    if i==0:
        a.remove(i)
        a.append(i)
print(a)'''


#program 11
'''a=[1,2,2,3,4,4,5]
newlist=[]
for i in a:
    if i not in newlist:
        newlist.append(i)
print(newlist)
'''

#program 12

'''a=[1,2,3]
b=[2,3,4]
c=[3,4,5]
for i in a:
    if i in b and i in c :
        print(i)
    '''
#WAP a program to calculate and return the sum of distances between the adjacent numbers in an array of positive integers
'''n=int(input("enter the size of array"))
arr=[]
for i in range (n):
    val=int(input("enter the value of array"))
    arr.append(val)
    sum=0#12
print(arr) #[10,11,7,12,14]
for i in range(n):
    if i+1 in range(n):
        sum+=abs(arr[i]-arr[i+1])
print(sum)
    '''

'''for i in range (1,5):
    if i==3:
        continue
    print(i)'''




'''for i in range(1):
     print(1,5)
     print(2,4)
     print(4,2)
     print(5,1)
     continue
print()'''

#zip () inside we can take multiple range function
'''for i,j in zip(range(1,6),range(5,0,-1)):
    if i ==3 and j==3:
        continue
    print(i," ",j)'''


#WAP to move *
'''p=prashant*is*a*good*programmer
if i==*:''
    
a=("prashant" ,"*","a","*","good","*","programmer ")
for i in a:
    if i==:
        a.remove(i)
        a.append(i)
print(a)


val=int(input("enter the string "))'''

'''name="prashant *iis* a* good * programmer"
newname=' '
val=''# ****
for i in name:
    if i !='*'
        newname += i
    else:
          val+=i
print(newname)
print(str(val+newname))'''

#BODMAS
'''a=50
b=30
c=20
d=10
print((a+b)*c/d)
print((a-b)*(c/d))
print(a+(b*c)/d)'''

'''x=['A','B','C']
y=['A','B','C']
z=[1,2,3,4]
print(x==y)
print(x==z)
print(x!=z)'''


#check for anagram
#WAP to check if two strings are anagram of each other
#op: anagram
'''a="listen"
b="silent"

if  sorted(a)==sorted(b):
    print("is a anagram")
else:
    print("is not anagram")

    '''


#count words in a string
#wap count words in string 
#ip:"this is a sentence"

'''str="This is a sentence"
count=1
for i in str:
    if i ==' ':
        count+=1
print(str)
print(count)'''


#product of array except self
#given an array where each element is the product of all the elements in the array except itself
#sample input[1,2,3,4]
#op:[24,12,8,6]

'''ip=[1,2,3,4]
value=[]
for i in ip :'''


#rearrange positive and negative numbers :
#given an array containing both positive and negative numbers ,rearranging them in alternative fashion
#logic : seprate psoitive and negative numbers and merge them alertantively

'''
a=[-1,2,-3,4,5,-6]
pos=[]
neg=[]
for i in a:
    if i<0:
        neg.append(i)
    else:
        pos.append(i)
print(pos)
print(neg)
print(neg+pos)

'''

#find the majority element
#find the majority element which appears more than n\2 times in array
arr=[2,3,4,5,5,5,5,6,]
count=1
n=[]
for i in arr:
    if i in n:
        count+=1
    else:
        n.append(i)
print(count)
      
