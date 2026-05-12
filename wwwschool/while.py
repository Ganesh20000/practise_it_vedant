



print("hello world")


i=0

while (i<=5):
    print(i,end=" ")
    i+=1
print()

print("*"*80)

i=5
while(i>0):
    print(i,end=" ")
    i-=1

# 
num=5









i=1
while (i<=10):
    
    print(f"{num}*{i}={num*i} ")
    i+=1



print("*"*50)


i=5;

# while (i>0):
    # rem=i%10
    # print(rem)
    # i=i//10
    # print(i)
    

#^ reverse a noo

num=45646466



rev=0

while(num>0):
    rem=num%10
    rev=rev*10+rem
    num//=10


print(rev)





#palindrom of a no
no=14141414141
temp=no
rev=0

while(no>0):
    rem=no%10
    rev=rev*10+rem
    no=no//10

print(rev)

if temp==rev:
    print(" palindrom number*")
else:
    print("not a palindrome")






# loop control statement



for i in range(6):
    i+=1
    if(i==4):
        continue
    print(f"i is {i} " )


# break


print("*"*50)
print()
i=0
while(i<=10):
    i+=1
    if i==5:
        break
    print(f"i is {i}")