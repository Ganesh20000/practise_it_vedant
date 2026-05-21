# class book:
#     def __init__(self):
#         self.username=" "
#         self.password= " "
#         self.menu()


#     def menu(self):
#         user_input=input(""" welcome to chatbook
# 1.press 1 to signp
# 2.press 2  to signin
# 3. press 3 to login
# 4.press 4 to message 
# 5. press 5 to exit""")        
#         if user_input=="1":
#             self.signup()
#         elif user_input=="2":
#             self.signin()
#         elif user_input=="3":
#             pass
#         elif user_input=="4":
#             pass    
#         else:
#             exit



#     def signup(self):
#         email=input("enter a email")
#         passw=input("enter a pass")

#         self.username=email
#         self.password=passw
#         print("singup succesfully")
#         print("\n")
#         self.menu()




#     def signin(self):
#         if self.username==" " and self.password==" ":
#             print("singup first")
#         else:
#             email=input("enter a user name")
#             passw=input("enter a password")
#         if self.username==email and self.password==passw:
#             print("login is succesfull")
#         else:
#             print("invalid credential")
#         self.menu()
        


# d=book()


# d.signup()

# d.signin()
class Book:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.menu()

    def menu(self):
        while True:   # loop until user exits
            user_input = input("""\nWelcome to ChatBook
1. Signup
2. Signin
3. Login
4. Message
5. Exit
Choose an option: """)

            if user_input == "1":
                self.signup()
            elif user_input == "2":
                self.signin()
            elif user_input == "3":
                self.post()
            elif user_input == "4":
                self.message()
            elif user_input == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice, try again.")

    def signup(self):
        email = input("Enter email: ")
        passw = input("Enter password: ")
        self.username = email
        self.password = passw
        print("Signup successful!\n")

    def signin(self):
        if not self.username or not self.password:
            print("No account found. Please signup first.\n")
            return

        email = input("Enter username: ")
        passw = input("Enter password: ")

        if self.username == email and self.password == passw:
            print("Signin successful!\n")
        else:
            print("Invalid credentials.\n")

    # def login(self):
    #     print("Login feature not implemented yet.\n")

    # def message(self):
    #     print("Messaging feature not implemented yet.\n")

    def post(self):
        if self.signin==True:
            txt=input("enter a post")
            print(f"the followig  txt is posted {txt}")
        else:
            print("login first"
                  )
            self.menu()
# Run program
d = Book()
