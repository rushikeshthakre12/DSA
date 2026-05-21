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

    
