# ---------------------------------------------------------------------------------------------------------------------
# Very Basic Calculator
# ---------------------------------------------------------------------------------------------------------------------
# Addition :
def add(a, b):
    ans = a + b
    print(ans)


# Subtraction
def sub(a, b):
    ans = a - b
    print(ans)


# Multiplication
def mul(a, b):
    ans = a * b
    print(ans)


# Division
def div(a, b):
    ans = a / b
    print(ans)


# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------


# function for main operations.
def calc():
    print("------------------------------------------------------------------")
    print("|                           Calculator                           |")
    print("------------------------------------------------------------------")

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    x = input("Enter your choice: ")
    if x == "1":
        print("Addition: ")
        a = int(input("Enter first no:  "))
        b = int(input("Enter second no:  "))
        add(a, b)
    elif x == "2":
        print("Subtraction: ")
        a = int(input("Enter first no:  "))
        b = int(input("Enter second no:  "))
        sub(a, b)
    elif x == "3":
        print("Multiplication: ")
        a = int(input("Enter first no:  "))
        b = int(input("Enter second no:  "))
        mul(a, b)
    elif x == "4":
        print("Division: ")
        a = int(input("Enter first no:  "))
        b = int(input("Enter second no:  "))
        div(a, b)
    elif x == "5":
        print("Exiting...")
        exit()
    else:
        print("wrong input")
    ch = input("Do you want to continue?(y/n) : ")
    if ch == "y" or ch == "Y":
        calc()
    else:
        print("Exiting...")
        exit()


calc()
