"""
loop:

Homework 1:

n=input("請輸入階梯層數:")
n=int(n)
if 10>n>=1:
    sum=0
    for n in range(n):
        sum=sum+(10**(n))   
        n+=1  
        print(sum*n)  
else:
    print("不支援")
"""


n=input("請輸入階梯層數:")
n=int(n)
if 10>n>=1:
    sum=0
    for n in range(n):
        sum=sum+(10**(n)*10**(n)) 
        n+=1    
        print(sum*n)
else:
    print("不支援")
