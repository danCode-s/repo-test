print("Hello, World!")

def enterName():
    checker = 0
    while (checker == 0):
        name = input("What is your name: ")
        if(type(name) != str):
            checker = 0
            return "Please Enter a String\n"
        else:
            checker = 1
            return f"Welcome, {name}"
        
   
print(enterName())
    