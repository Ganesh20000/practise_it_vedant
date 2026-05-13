num=153
n=num
rem=0
rev=0
d=0
while(num>0):
    rem=num%10
    

    rev=rev*10+rem
    d+=rem**3
    
    num//=10
print()

if d==n:
    print("amstrong no")
else:

    print("not a amstrong no")


print(rev,end=' ')





print()
f=0
nn=5
b=0
a,b=0,1
while(b<=nn):
    print(a,end='')
    a,b=b,a+b
    