
#file read
f=open("t.txt",'r')
u=f.read()
print(u)
f.close()


# file write

f=open("t.txt",'w')
u=f.write("python is the rision ")
print(u)
f.close()

#append the file

f2=open("t.txt",'a')
o=f2.write("python is language \n and i love jave \n i like dax\n ")
print(o)
f2.close()



# using the function i am writing the thing


def  o(path,mess):
    with open(f"{path}",'a') as fo:
        fo.write(f"{mess}")

        print(fo)
        fo.close()

o("t.txt","okkkk")


# file read 

def o(path):
    file=open(f"{path}",'r')
    u=file.read()
    print(u)
    file.close()


o("t.txt")



def uuu(path,mess):
    with open(f"{path}",'a')as file:
        h=file.write(f"{mess}")
        print(h)
        file.close()

uuu("C:\\Users\\karli\\OneDrive\\Desktop\\all\\it_python\\tt.txt","\n python is the programming languege")


def iii(path,path2):
    with open(f'{path}') as f1:
        with open(f"{path2}",'a') as f2:
            for i in f1:
                f2.write(i)

            print(f2)
                
        




iii("C:\\Users\\karli\\OneDrive\\Desktop\\all\\it_python\\tt.txt","C:\\Users\\karli\\OneDrive\\Desktop\\all\\it_python\\t.txt")


