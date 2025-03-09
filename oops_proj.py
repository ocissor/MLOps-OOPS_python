class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()
    
    def menu(self):
        user_input = input(""" Welcome! How would you like to proceed? 
                            1. Press 1 to Sign Up
                            2. Press 2 to Log In
                            3. Press 3 to write a post
                            4. press 4 to message a friend
                            5. Press any other key to exit""")

        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            print("Exiting...")
            exit()

    
obj = chatbook() #object of class chatbook