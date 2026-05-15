#^ Write a program to calculate the sum of all numbers from 1 to N. Example: If N = 100, output → 5050

t=0
N=100
for i in  range(N+1):
    t+=i

print(t)


# write a program to count the number of digits in a given number. Example: If input is 4567, output → 4

N=47844778
count=0
while(N>0):
    rem=N%10
    N//=10
    count+=1

print(count)




# amstrong or not

Num=370
count=0
N=Num

while(N>0):
    rem=N%10
    # rev=rem*10+rem
    count+=rem**3
    N//=10
    
    

print(count)

print(N)
if count==Num:
    print("amstrong no")
else:
    print("not amstrong no")


print(count)




# prime no

N=10

# count=0
# if N>1:
#     print("prime ")
# else:
#     for i in range(N):
#         if (N%i==0):
#             print("prime")
#             count+=1
        
#             if(N==2):
#                 print("prime")
#             else:
#                 print("odd")

num=10

if num<=1:
    print(f'{num} is not prime')
elif num>1:
    for i in range(2,num):
        if num%i==0:
            print("Not prime")
            break

    else:
        print(f"{num}");



# Program to print all prime numbers between 1 and N

# N = int(input())   # take input from user
N=7
for num in range(2, N+1):   # start from 2 up to N
    for i in range(2, num):
        if num % i == 0:    # if divisible, not prime
            break
    else:
        print(num)



ls=[10,20,30,40,50,60]
a=len(ls)
print(a)


print(sum(ls)/len(ls))


c=0
for i in ls:
    if i>sum(ls)/len(ls):
        c+=1;


print(c)



l=['na','i','e','n','p','nn',47,78,4]





for i in l:
    if i not in ('NA',None):
        l.append(i)

print(l)

