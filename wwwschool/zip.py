l=[1,5,4]
p=[4,7,8]
u=["OOOO","rtrtrt","rterter"]

f=[4.5,0.8,78.4]



c=list(zip(l,p))
print(c)

d=list(zip(l,p,u,f))
print(d)



# tuple single values is int
x=(1)

print(type(x))


#tuple two values

x=(1,)

print(type(x))


# # print()
# for l,p,f in zip(l,p,f):
#     print(l,p,u)
l = [1,5,4]
u = [4,7,8]
p = ['OOOO', 'rtrtrt', 'rterter']

res = list(zip(l,u,p))

print(res)


res= list(zip(l,u,p))

res = list(zip(l,p,u))
l1,l2,l3=zip(*res)



# filer function is used to get filtered elements


 # filetering function greather than 0
def f(n):
    if n>0:
        return n
    

y=list(filter(f,[1,0,4,5,7,8,9,-4,5,-8,-9]))
print(y)


# none


u= list(filter(None,(1,0,1,2,1,True,False)))

print(u)

l=[1,2,56,8,9,7,4,1,21,0,5,4,-5,7,4,0,]

def checkeven(n):
    if n%2==0:
        return True
    else:
        return False
    



p=list(filter(checkeven,l))
print(p)



# lamda function 
print("*"*50)
d=list(filter(lambda x:x %2==0,l))
print(d)



def even(i):
    vowels=['a','e','i','o','u']
    if i in vowels:
        return True
    else:
        return False
    


    
letter=['a','e','y','p','n']

o=list(filter(even,letter))
print(o)



# reduce

from functools import reduce



nums=[1,2,2,3,4,5,6]


e=reduce(lambda x,y:x+y,nums)
l=reduce(lambda x,y:x*y,nums)

print(e)
print(l)



k=reduce(lambda a,b:a if a>b else b,nums)
print(k)