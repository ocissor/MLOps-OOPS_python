#initialize class
class employee:
    #special method/ magic method/ dunder method - __init__ is constructor
    #constructor is called when object is created
    def __init__(self):
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"

    #defining methods
    def report(self,name):
        print(f"Employee {name} is reporting")
    
    def presentation(self):
        print("Employee is presenting")
    
    def travel(self):
        print("Employee is travelling")

#create object/instance of class employee
sam = employee()
sam.report("sam")
print(type(sam))
