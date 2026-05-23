l=[]

for i in range(0,50):
    if i%2==0:
        l.append(i)

print(l)


l=[i for i in range(0,50) if i%2==0]
print(l)



grammer=['ja','o','i0,','n','no','nahi']


l=[i for i in grammer if i.startswith("n") ]
print(l)

print("*"*50)


b=[i**2 for i in range(44) ]
print(b);


lib=[('book1',2004),('book2',2008),('book5',2015),('book6',2018),('book7',2019)]


l=lib[0][1]

print(l)

for i,j in lib:
    if j>2014:
        
        print(i,j)


print("*"*50)

l=[(i ,j) for i,j  in lib if j>2014]
print(l)