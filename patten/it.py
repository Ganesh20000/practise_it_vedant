

row=4


for i in range(1,row-1):
    for j in range(1,i+1):
        print("*",end=' ')
    print()


print("*"*50)


print()
for i in range(row+1):
    # print(i,end=' ')
    for j in range(row,i-1,-1):
        print("*",end=' ')
    print()


