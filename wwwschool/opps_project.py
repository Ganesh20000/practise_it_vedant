class book:
    def __init__(self):
        self.username=" "
        self.password= " "
        self.menu()


    def menu(self):
        user_input=input(""" welcome to chatbook
1.press 1 to signp
2.press 2  to signin
3. press 3 to login
4.press 4 to message 
5. press 5 to exit
                         """)        
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            pass
        elif user_input=="3":
            pass
        elif user_input=="4":
            pass
        else:
            exit



    def signup(self):
        email=input("enter a email")
        passw=input("enter a pass")

        self.username=email
        self.password=self.password
        print("singup succesfully")
        print("\n")
        self.menu()
        


d=book()


d.signup()

