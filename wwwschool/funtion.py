

def greet():
    print("hello world")
greet()


#argument
def greet(x):
    print(F"good morning {x}")


greet("yooo")



def area(h,w):
    area=1/2*h*w
    print(area)


area(4,3)




# argument and parameter
print("A parameter is the variable listed inside the parentheses in the function definition.")

print()
print("An argument is the actual value that is sent to the function when it is called.")


#name is parameter
def myfun(name): 
    print(f"my name is {name}")


myfun("jitesh")
# jitesh is argument



#Number of Arguments


#By default, a function must be called with the correct number of arguments.


def myfun(name="Mumbai"):
    print(f"{name} is city of dreams")

myfun()



# Return value s

def rrturn(x,y):
    return x+y

result =rrturn(4,4)
print(result)


def dta():
    return ["a",'c','e','t','u']



x=dta()
print(x[1],end=' ')
print(x[3])


# factorail of number

def fact(y):
    x=1
    for i in range(1,y+1):
        x=x*i
    # print(f"{x}={x*i}")


y=fact(4044)
print(y,end=' ')

print("*"*60)


x=1
for i in range(1,5+1):
    x=x*i

print(x)



#^ By default, a function must be called with the correct number of arguments.

# *args and **kwargs allow functions to accept a unknown number of arguments.

def myfun(*arg):
    print(f"this is the args  {arg[3]} ")


myfun('kara','lora','sora','fora')



def myfun(*args):
    print(f'type of {type(args)}')
    print(f" first argument {args[0]}")
    print(f" second argument {args[2]}")
    print(f"all argument {args}")


myfun('kara','lora','sora','fora')



def sum(*arg):
    Total=0

    for i in arg:
        Total+=i
    print(Total)
    

sum(4,4,7,88,99,88,88)

# f you do not know how many keyword arguments will be passed into your function, add two asterisks ** 

def myfun(**arg):
    print("type ",type(arg))
    print(f"my name ",arg["name"])
    print(f"my age ",arg['age'])

myfun(name='piky',age=78)