# #Python collection data type(There are 4 types of collection data type in python)-> list[],tuple(),set{},dictionary{key: value}
#1)list
#mylist = ["prashant","Ashish","komal","Ashish",77,"sandip",60.52,"prashant"]

# print(mylist)
# print(type(mylist))#<List>
# print(mylist[0]) #prashant
# print(mylist[1]) #Ashish
# print(mylist[2]) #komal
# print(mylist[-1]) #prashant last one
# print(mylist[2:5]) #n=5,n-1=4
# print(mylist[:5]) #n=5, n-1=4
# print(mylist[1:]) #n=8,n-1=8-1=7
# print(mylist[1:8:2])#1,3,5,7...

# mylist[2]="Akshay" #list is mutable(changable)
# print(mylist)

# if "ankush" in mylist:
#     print("yes ankush is avilable")
# else:
#     print("not avilable")

# mylist.append("harsh") #append function is used in list and it added in right side
# mylist.append("laxman")
# print(mylist)
# #apppend() and extend() btoh work like same

# mylist.insert(3,"sanket")
# print(mylist)

# mylist.remove("sandip")
# print(mylist)

# newlist = mylist.copy() #cloning
# print(newlist)

# mylist = [["prashant","jha"],[85.56],[440022,"yyy"]]
# print("example of multidimensional list: ")
# print(mylist)
# #print(mylist[row][column])
# print(mylist[0][0])#prashant
# print(mylist[0][1])#jha
# print(mylist[1][0])#85.56
# print(mylist[2][0])#440022
# print(mylist[2][1])#yyy
# #     0          1
# #0= [["prashant","jha"],
# #1= [85.56],
# #2= [440022,"yyy"]]


# list2 =[50,25.50,'prashant']
# del list2[2] #for delete particular element 
# #del list2 #for deleting entire list
# print(list2)

# list2 =[50,25.50,'prashant']
# list2.clear()
# print(list2)


# #converting string to list
# name="prashant" #['p','r','a']
# print(name)
# myname=list(name) #typecasting
# print(myname)
# # we have used list constructor


# #sorting example
# mylist=[44,22,77,0,9,88] #0,9,22,44,77,88
# mylist.sort() #by default it is sorted in ascending order
# #mylist.sort(reserve=True) #for decending order
# print(mylist)
'''default sorting order for number is ascending order default
sorting order for string is alphabetical order we show know that list should 
contain homogenious data type python2 first short number then string follow'''

# #Alising concep-> means assigining one variblen reference to another
# mylist=[44,22,77,0,9,88]
# newlist = mylist
# print(id(mylist))
# print(id(newlist))

# mylist=[44,22,77,0,9,88]
# for i in mylist: #i=6
#     print(i)

'''Que- i/p =[0,1,4,0,2,5]
     o/p =[1,4,2,5,0,0]'''
# # Move the zero in last
# list1=[0,1,4,0,2,5]
# for i in list1:#i=0:0
#     if i == 0:
#         list1.remove(i)
#         list1.append(i)
# print(list1)

'''Que- find the second largest element in an array    
    i/p = [7,3,9,2,8]
    o/p = 8 second largest element '''
# list1=[7,3,9,2,8]
# list1.sort()
# print(list1[-2]) #second largest element

##MCQ
#Que-
# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60 #value error 
# print(a)

#Que-
# a=[1,2,3,4,5]
# print(a[3:0:-1]) 

#Que-
# arr = [[1,2,3,4],
#        [4,5,6,7],
#        [8,9,10,11],
#        [12,13,14,15]]
# for i in range(0,4): #i=0,1,2,3 only focused on your row's
#     print(arr[i].pop())

#Que-
# arr = [1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i-1]=arr[i]
        
# for i in range(0,6):
#     print(arr[i], end = " ")

#Que-
# fruit_list1=['Apple','Berry','Cherry','Papaya']
# fruit_list2=fruit_list1
# fruit_list3=fruit_list1[:]
# fruit_list2[0]='Guava'
# fruit_list3[1]='Kiwi'

# sum = 0
# for ls in (fruit_list1,fruit_list2,fruit_list3):
#     if ls[0] == 'Guava':
#         sum += 1
#     if ls[1] == 'Kiwi':
#         sum += 20
# print(sum)

#Que-
#Find the common elements in three arrays
#i/p- [1,2,3],[2,3,4],[3,4,5]
#o/p- 3
# A=[1,2,3]
# B=[2,3,4]
# C=[3,4,5]
# for i in A:#i=0,1,2  and for each list common is 3
#     if i in B and i in C:
#         print(i)

#Que-
mylist=[]
N = int(input("Enter the value of N :")) #5
for i in range(N):
    val = int(input("Enter the value: "))
    mylist.append(val)
#print(mylist) #[10, 11, 7, 12, 14]
#print(len(mylist)) #5
sum =0
for i in range(len(mylist)-1):
    if i+1 in range(len(mylist)):
        sum += abs(mylist[i]-mylist[i+1])
print(sum)
