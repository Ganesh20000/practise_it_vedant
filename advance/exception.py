# try catch block

try:
    with open("advance/tt.txt",'r') as file:
        print(file.read())
except:
    print("file not found")




# handling specific type of error   
try:
    m=0
    f=open("advance/practise.txt",'r')
    p=f.read()
    print(m)
    print(5/5)
    print(p)
    

except FileNotFoundError:
    print("file not found")
except NameError:
    print("variable not define")
except ZeroDivisionError:
    print("zero division error")
except Exception as e:
    print(e)















class bank:

    def __init__(self,balance):
        self.balance=balance


    def withdraw(self,amount):
        if amount <0:
            raise Exception("amount cant be -ve")
        elif self.balance<amount:
            raise Exception("amount cant be greater than balance")
        self.balance=self.balance-amount


new=bank(10000)
try:
    new.withdraw(5000)
except Exception as e:
    print(e)
else:
    print("everything is ok")



# except and else 


try:
    f=open("advance/t.txt",'r')
except FileNotFoundError:
    print("file not found")
except NameError:
    print("namer error")
else:
    print(f.read())
finally:
    print("ye to print hi hoga")








#it vedant expection handling 

d=8
c=0

try:
    print(c)
except NameError as e:
    print(f" error arrived {e}")
else:
    print("there is no erro")
finally:
    print("done succesfully")



try:
    print(c/d)
except ZeroDivisionError as z:
    print(f" error {z}")
except Exception as e:
    print(f"error {e}")
else:
    print("there is no error")
finally:
    print("thank you")











x=5
y=0

try:
    a=x+y
    b=x-y
    c=x*y
    d=x/y

except Exception as e:
    print(e)

    y=5
    c=x*y
    d=x/y
    p=x**y


finally:
    print(a)
    print(b)
    print(c)
    print(d)






class human():
    eye="wavy"
    hair="black"
    gender='female'

    def talking(self):
        return ' i am talking'

    def walking(self):
        return ' i am walking'
    


b=human()

print(b.talking())
print(b.walking())






class myclass:

    def one(self,name):
        self.name=name
        
    def two(self):
        return self.name
    
    def sayhello(self): 
        return f"hello {self.name} {id(self)}"
    



k=myclass()


print(k.one("divya"))


print(k.two())



# it vedant class
class parent:
    def __init__(self,name):
        self.name=name
    

    def method(self):
        print(f"the inital {self.name}")

class child(parent):
    def method(self):
        print(f"child method {self.name}")

k=parent("kiyo")

h=child("kiyo")

h.method()



# deault paramter


class parent:
    def __init__(self):
        self.name="user"

    
class tow(parent):
    def method(self):
        print(f" child method {self.name}")

l=parent()

u=tow()
u.method()



class Product:

    def __init__(self,id,name,price,qty):
        self.id=id
        self.name=name
        self.price=price
        self.qty=qty


    def retur(self):
        return f"{self.id},{self.name},{self.price},{self.qty}"

    def method(self):
        print(f" product name is {self.name}")
        print(f"product id is {self.id}")
        print(f" product qty is {self.qty}")

    



k=Product(1,"jeans",500,3)
k.retur()
k.method()
