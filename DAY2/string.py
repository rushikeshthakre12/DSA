# name= "prashantjha"  # this is our string
# print(name[0])
# print(name[1])
# print(name[-1])
# #print(name[15]) #string index out of range
# print(name[0:5]) # end-1, 5-1=4 prash
# print(name[1:])#rashantjha
# print(name[:5])#prash  5-1=4
# print(name[:])#prashantjha
# print(name[1:8:2])#rsat 8-1=7
# print(name[::-1])#reverse of string


# s = "Python are High level programming Language"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())


# #Format functions
# name = "prashant" 
# sal=5000
# age = 28
# print("{} sal is {} age is {}".format(name,sal,age)) #There are 3 ways to print 
# print("{0} sal is {1} age is {2}".format(name,sal,age))
# print("{x} sal is {y} age is {z}".format(x=name,y=sal,z=age))
# A=1
# print(f"{A} is a good boy")


# name = "prashant"
# for i in name:#i=4:p
#     print(i)


#Que- i/p =prashant
#     o/p =prashnt
#WAP to remove duplicate chr
# name = "prashant"
# newname ="" #prashnt
# for i in name: 
#         if i not in newname:
#             newname += i
# print(newname)


#Que- i/p =prashant
#     o/p =tnahsarp
#WAP to reverse a string
# name = "prashant"
# newname="" #tnah
# N = len(name) #8-1=7
# for i in range(N-1,-1,-1): #i=7 7>-1 -1 for reverse indexing
#     newname += name[i] 
# print(newname)


#Que- i/p = racecar
#     o/p = racecar 
#WAP palindrome
# name = "racecar" #example1
# #name = "help4code" #example2
# print(name) #left to right
# print(name[::-1]) # right to left
# if name == name[::-1]:
#     print("Palindrome String")
# else:
#     print("Not a Palindrome String")


#Que- i/p = hello
#     o/p = vowels: 2, consonants: 3
#WAP count vowels and consonants
# vowels =['a','e','i','o','u']
# name="hello"
# con=0
# vow=0
# for i in name:
#     if i in vowels:
#         vow +=1
#     else:
#         con +=1
# print("vow",vow,"con",con)
    

#Que- i/p = "listen"and"silent"
#     o/p = Anagrams
#WAP to check for Anagrams
# name="listen"
# N = print(len(name))


#Que- i/p = "This is a sentence"
#     o/p = 4
# name="This is a sentence"
# space=""
# count=0
# for i in name:
#     if name==space:
#         space += space
# print(space) 

# #BODMAS
# a=50
# b=30
# c=20
# d=10
# print((a+b)*c/d)
# print((a-b)*(c/d))
# print(a+(b*c)/d)


#Que- i/p = gasgg54@#vscsd!s*
#     o/p = 4
# var ='gasgg54@#vscsd!s*'
# count=0
# z=ord(i)
# print(z)
# if z>=97 and z <=122:
#     continue
# elif z >=48 and z<=57:



#Que- i/p = "this is a test"
#     o/p = "This Is A Test"
# name="this is a test"
# print(name.title())


#String Concept-
# print('prashantjha777'.isalnum())
# print('prashantjha'.isalpha())
# print('777f'.isdigit())
# print(''.islower())
# print('PRASHANTj'.isupper())
# print('My Name Is Rushikesh'.istitle())
# print(''.istitle())
# print(''.isspace())
# print("Hello".startswith("He"))
# print("Hello".endswith("lo"))

#----------------------------------------------------

# print("Prashant".find("r"))
# print("Prashant".index("r"))
# print("Prashant jha".count("a"))

#----------------------------------------------------
#Pattern Coding
#1
# for i in range(1,4):
#     for j in range(1,4):
#         print(i,end=" ")
#     print()

#2
# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i),end=" ")
#     print()

#3
# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,1+i):
#         print("*",end=" ")
#     print()

#4
# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(chr(64+j),end=" ")
#     print()

#5
# import time

# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     for j in range(1,1+i):
#         time.sleep(3)
#         print("*",end=" ")
#     print()

#i/p-1,2,3,4
#o/p-24,12,8,6

    

# i/p- "Hello world"
#o/p- "olleH dlrow"
# s = "Hello world"
# words = s.split()
# print(words)
# for i in words:
#     print(i[::-1], end=" ")


#i/p- ({[()]})
#o/p- Valid

