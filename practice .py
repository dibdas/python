
'''n = int(input())
g=int(n/2)
x=1
for i in range(2,g+1):
    if n%i==0:
        x=0


if x==0:
   print("not prime")
else:
   print("prime")



arr=[]
for i in range(2):
       arr.append(int(input()))

def s(arr1):
    print(sum(arr1))


s(arr)


s=
s= input()

print(s[-1:-len(s)])'''


'''m=input()
for i in range(len(m)-1,-1,-1):
        print(m[i])
        a=m[i]'''

'''m = input()
print(m[::-1])'''


'''m=input()
a=[]
count=0
for i in range(len(m)):
    if m[i]==" ":
        count=count+1

print(count)'''


'''m=input()
a=[]
count=0
for i in range(len(m)):
    if m[i]=="a" or m[i]=="e" or m[i]=="i" or m[i]=="o" or m[i]=="u":
        count=count+1

print(count)'''


'''n = int(input("enter the number more than 3"))
a=[]
for i in range(0,n,3):
    a.append(i)

print(sum(a))'''

'''s=input()
a=[]
count=0
for i in range(len(s)):
    a.append(s[i])
    if s[i]=="m":
        count=count+1

print(count)'''


'''a=[]
ar=[]
for i in range(10):
    a.append(int(input()))
print(a)

for i in range(len(a)):
    if a[i]%5==0:
        ar.append(a[i])
print(ar)
print(sum(ar))
print(sum(ar)/(len(ar)))'''


'''def ranking():
    input("enter the marks of student1")
    physics=int(input())
    chemistry=int(input())
    mathematics=int(input())
    total=physics+mathematics+chemistry

    input("enter the marks student2")
    physics1=int(input())
    chemistry1=int(input())
    mathematics1=int(input())
    total1=physics1+mathematics1+chemistry1

    if  physics>physics1:
        print("student1 better rank 444")

    elif total1==total1 and physics==physics1:
        if mathematics>mathematics1:
            print("student1 better rank 999")
        else:
            print("student2 better rank iii")
    else:
        print("student2 better rank ppp")

ranking()'''
        


for i in range(1,100+1):
    
    if i%5==0 and i%9==0:
        print(i)
        print("Masai School")
    
    elif i%5 ==0 and i%9!=0:
        print(i)
        print('masai')
    elif i%5!=0 and i%9==0:
        print(i)
        print('school')

        




    


