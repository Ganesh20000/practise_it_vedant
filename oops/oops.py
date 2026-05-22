#^ Initialize the class 
class deg:
    # special method or magic method or dunder method
    # called as constructor
    def __init__(self):
        self.id=5
        self.age=78
        self.name='alice'
    #this is called method
    def second(self,score):
        print(f"i am a alice i score {score} ")


# creating a obj or insteance of classs
op=deg()

op.second(7)
# calling method in this class


print(op.name)


