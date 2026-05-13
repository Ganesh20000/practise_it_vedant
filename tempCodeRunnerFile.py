num=1537778

rem=0
rev=0

while(num>0):
    rem=num%10
    rev=rev*10+rem
    print(rem,end='')
    num//=10

print(rev,end=' ')