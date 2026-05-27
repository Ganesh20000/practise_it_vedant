class deg:
    # special method or magic method or dunder method
    # called as constructor
    __user_id=1
    def __init__(self):
        print(id(self))
        self.__name="ip"
        self.id=5
        self.age=78
        self.name='alice'

        self.__user_id=deg.__user_id
        deg.__user_id+=1
    #this is called method
    def second(self,score):
        print(f"i am a alice i score {score} ")


    def get_name(self):
        return self.__name
    

    def setter(self,names):
        self.__name=names

    def encap(self):
        self.__name="user not found"
    
    @staticmethod
    def get():
        return deg.__user_id
    

    @staticmethod
    def set(n):
        deg.__user_id= n

d=deg()


d.get()

print(d.get())
d.set(25)

print(d.get())










# inheritance exampe

class parent:
    def __init__(self,name):
        self.name=name
        

    def speak(self):
        print(f"parent name is {self.name}")


# child class

class baby(parent):
    
    def speak(self):
        print(f"child name is {self.name}")

    def speak2(self):
        print(f"second child name is {self.name}")













class animal:
    def __init__(self,name):
        self.name=name

    def method(self):
        print(f"parent name is {self.name}")

class rat(animal):
    
    def method(self):
        print(f"child method {self.name}")



a=animal("amitabh")


a.method()


b=rat("abhishek")

b.method()


# constructor overloading and method overloading


# class animal:
#     def __init__(self,name):
#         self.name=name

#     def speak(self):
#         print(f"parent name is {self.name}")

# class rat(animal):
    
#     def __init__(self):
#         self.method="constructor overloading"
#     def second(self):
#         print(f"child method {self.name} and this called {self.method}")


# # l=animal("PO")

# # l.method()


# k=rat()
# k.method()




# super keyword

class animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        print(f"parent name is {self.name}")

class rat(animal):
    
    def __init__(self,name):
        super().__init__(name)
        self.method="constructor overloading"

    def second(self):
        super().speak()  # call the base class method
        print(f"child method {self.name} and this called {self.method}")


# l=animal("PO")

# l.method()


k=rat("pikachu")
k.speak()










