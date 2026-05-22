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