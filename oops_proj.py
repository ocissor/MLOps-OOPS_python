class chatbook:
    #this is a class variable shared across all instances of this class
    user_id = 0

    def __init__(self):
        self.id = chatbook.user_id
        #chatbook.user_id += 1
        chatbook.update_user_id()
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.username_list = ["rahul", "rohan", "ram"]
        self.__name = "Default User" #private variable
        self._var = "random" #protected variable
#        self.menu()
    

    def __temp(self):
        print("This is a private method")
    
    def _temp(self):
        print("This is a protected method")

    @classmethod
    def update_user_id(cls):
        cls.user_id += 1

    @staticmethod
    def get_user_id():
        return chatbook.user_id
    
    @staticmethod
    def set_user_id(user_id):
        chatbook.user_id = user_id
        return
    
    #getter
    def get_name(self):
        return self.__name
    
    #setter
    def set_name(self,name):
        self.__name = name
        return


    def menu(self):
        user_input = input(""" Welcome! How would you like to proceed? 
                            1. Press 1 to Sign Up
                            2. Press 2 to Log In
                            3. Press 3 to write a post
                            4. press 4 to message a friend
                            5. Press any other key to exit
                           
                           -> """)

        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.login()
        elif user_input == "3":
            self.write_post()
        elif user_input == "4":
            self.message_friend()
        else:
            print("Exiting...")
            exit()
    
    def signup(self):
        self.username = input("Enter username: ")
        self.password = input("Enter password: ")
        print("Signed up successfully!")
        self.menu()
    
    def login(self): 
        if self.username=="" and self.password=="":
            print("No user found. Please sign up!")
            return
        username = input("Enter username: ")
        password = input("Enter password: ")
        if self.username==username and self.password==password:
            self.loggedin = True
            print("Logged in successfully!")
        else:
            print("Invalid credentials!")
        
        self.menu()

    def write_post(self):
        if self.loggedin:
            post = input("Enter your post: ")
            print("peview of your post: ", post)
        else:
            print("Please login to write a post!")
        
        self.menu()
    
    def message_friend(self):
        if self.loggedin:
            friend = input("Enter friend's name: ")
            if friend in self.username_list:
                message = input("Enter your message: ")
                print(f"Message sent to {friend} successfully!")
            else:
                print("Friend not found!")
        else:
            print("Please login to message a friend!")

        self.menu()

print(chatbook.user_id)
chatbook.update_user_id()
obj1 = chatbook() #object of class chatbook
print(obj1._temp())
print(obj1.id)
obj2 = chatbook() #object of class chatbook
print(obj2.id)

class Employee:
    raise_percentage = 1.05  # Class variable

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary  # Instance variable

    @classmethod
    def set_raise_percentage(cls, new_percentage):
        cls.raise_percentage = new_percentage

# Before updating class variable
print(Employee.raise_percentage)  # Output: 1.05

# Updating using class method
Employee.set_raise_percentage(1.10)

# After updating class variable
print(Employee.raise_percentage)  # Output: 1.10
