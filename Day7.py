#1. sort Dictionary by key value pair
 #  write a function to sort dictionary by keys or values in ascending or descending order 
#program1

#sample output : {"C":3,"b":2,"A":1}
# my_dict = {'b': 2, 'a': 1, 'c': 3}
# sorted_dict = dict(sorted(my_dict.items()))
# print(sorted_dict)
# sorted_dict = dict(sorted(my_dict.items(), reverse=True))
# print(sorted_dict)

# program2
#remove all elements from dictionary 
# dict1={'c':3,'b':2,'a':1}
# dict1.clear()
# print(dict1)

# COMPLEXITY
# TIME/SPACE COMPLEXITY
# constant time o(1)

# def findbiggestNumber(array):#[2,4,5,6,7,1,9,3,4,5,6]
#     firstValue=array[0] #firstValue=2
#     for i in range(1,len(array)):#i=2 ======> O(N)
#         if array[i]>firstValue:#4>2 =======> O(1)
#             firstValue=array[i]#i=4 =======> O(1)
#     return firstValue  #=======> O(1)

# array=[2,4,5,6,7,1,9,3,4,5,6]
# print(findbiggestNumber(array))#=======> O(1)

#final time complexity : O(1)+O(n)+O(1)=O(N)



# msg=input(" Enter the string : ")
# if msg>=65 and msg<=91:#A=65
#     print("your entered charcater is in uppper case")
# elif msg>=97 and msg<=122:#a=97
#     print("your entered charcater is in lowerr case")
# elif msg>=48 and msg<=57:#0=48
#     print("your entered charcahter is digit")
# else:
#      print("your entered charcater is special symbols")


# msg=input(" Enter the string : ")
# a=ascii(msg)
# for i in msg:


#write a  code to help agency to count the number of white spaces and special symbols in string
#sol1:

# msg=input(" Enter the string : ")

# special_count=0
# space_count=0

# for ch in msg:
#     if ch == "":
#         space_count+=1
#     elif not ch.isalnum():
#         special_count+=1

# print("Number of whitespace :",space_count)
# print("number of special characters :",special_count)

# sol2:
# var="gasgg54@#vscd!s"
# count=0
# for i in var:
#     z=ord(i) #typecast in ascii
#     #print(z)

#     if z>=97 and z<=122:
#         continue
#     elif z>=48 and z<=57:
#         continue
#     else:
#         count+=1

# print(count)   

#write a program to help apparel find the number of plotss that it canselect for its outlets


#linear search
# def linearSearch(array,target): #[1,2,3,4,5,6,7,8,9] =====>o(n)
#     for i in range(len(array)):#i=3 =====> o(n)
#         if array[i] == target: #=====> o(1)
#             return i #=====> o(1)
#     return -1 #=====> o(1)
# array=[1,2,3,4,5,6,7,8,9]
# target=55 # 4 we have to search
# result=linearSearch(array,target)
# if result == -1:
#     print("no found")
# else: 
#     print("element found at index no =",result)
        
#binary seacrh  
#binary search is faster than linear serach
# binary search only works on sorted list

# def binarySearch(array,target):#[1,2,3,4,5,6,7,8,9]
#     start=0
#     end=len(array)-1 #calculating mid value
#     while start<=end:
#         mid =(start+end)//2
#         if array[mid]==target:
#             return mid
#         elif array[mid]<target:
#             start=mid+1
#         else: 
#             end=mid-1
#     return -1
# sorteArray=[1,2,3,4,5,6,7,8,9]
# target=55
# result=binarySearch(sorteArray,target)
# print(result)
# if result == -1:
#     print("no found")
# else: 
#     print("element found at index no =",result)    




#link data structure
#1.add node in begnning 2. add node in between 3.add node in the end 4.
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None

linkedlist=LinkedList()


linkedlist.head=Node(5) #first Node
second         =Node(10)
third          =Node(15)
fourth          =Node(20)

#linking part

linkedlist.head.next=second
second.next=third
third.next=fourth

print(linkedlist.head.data)
print(second.next)
print(third.next)
print(fourth.next)

#display linked list
while linkedlist.head!=None:
    print("|",linkedlist.head.data,"|",linkedlist.head.next,"====>",end="")
    linkedlist.head=linkedlist.head.next

    


        