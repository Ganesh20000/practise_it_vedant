f=open("file_handling/one.txt",'r')
read=f.read()

print(read)
f.close()

f2=open("file_handling/one.txt",'w')
write=f2.write('i love pythoon')
print(write)
f2.close()

f3=open("file_handling/one.txt",'a')
aa=f3.write("file is appending the txt")
print(aa)
f3.close()

f6=open("file_handling/one.txt","a")
jj=f6.write("\n the book \n the noodle \n mark ")

print(jj)

f6.close()



def op(path,message):
    file=open(f"{path}","a")
    bok=file.write(f"{message}")
    print(bok)
    file.close()

op("file_handling/two.txt","Thala for reason \n and the srh is the ")





# def withop(path,encoding='utf-8'):
#     with open(f"{path}",'r') as file:
#         print(file.read())
#         file.close()

# withop("C:\Users\karli\OneDrive\Desktop\all\Powerbi\p.txt")





def withop(path):
    with open(f"{path}",'r') as file:
        print(file.read())
        file.close()

withop("C:\\Users\\karli\\OneDrive\\Desktop\\all\\Powerbi\\p.txt")


#print the file2

with open("C:\\Users\\karli\\OneDrive\\Desktop\\all\\Powerbi\\p.txt",'a') as file2:
    c=file2.write("\n group the data based on mark")

print(c)
file2.close()




f1=open("C:\\Users\\karli\\OneDrive\\Desktop\\all\\Powerbi\\p.txt") 
f2=open("copytext.txt",'a') 

for i in f1:
    f2.write(i)
    print(i)












