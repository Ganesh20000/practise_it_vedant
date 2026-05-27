arr=[1,2,3,3,0,0,0,5,4,7,0,1,4,40,0,0,5,4]

i=0

for  j in range(len(arr)):
    if arr[j]!=0:
        arr[i],arr[j]=arr[j],arr[i]

        # arr[i]=arr[j]
        i+=1
print(arr)


i=0

for  j in range(len(arr)):
    if arr[j] !=arr[i]:
       
        i+=1
        arr[i]=arr[j]

print(i)

print(f"unique ")

uniq=len(set(arr))
print(uniq)


count= list