# # num=1537778

# # rem=0
# # rev=0

# # while(num>0):
# #     rem=num%10
# #     rev=rev*10+rem
# #     print(rem,end='')
# #     num//=10

# # print(rev,end=' ')
# data= [101,102,103,101,104,102,105,101]

# c=0
# for i in data:
#     if data.count(i)>1:
#         c+=1
        
# print(c)




# a=data[0]


# for i in data:
#     if i>a:
#          a=i


# print(a)

a=[10,20,30,40,50]

c=0


avg=sum(a)>len(a)
for i in a:
    if i >avg:
        c+=1


print(c)

print(avg)



# three digit moving avg from this
d=0
c=0
for i in a:
    print(i)
    d+=i
    c=d/3

# print(c)

res=[]

for  i in range(len(a)-2):
    avg=(a[i]+a[i+1]+a[i+2])/3

    res.append(avg)

print(res)

data = [('Mon',32),('Tue',35),('Wed',33),('Thu',35),('Fri',30)]

large=data[0][1]
days=[]
for day,values in data:
    if values>large:
        large=values

for day,temp in data:
    if temp==large:
        days.append(day)
        



print(large)
print(days)
        


    

s="Geeks"

d=[]
for i in range(len(s)):
    if i%2==0:
        d.append(s[i])





print(d)