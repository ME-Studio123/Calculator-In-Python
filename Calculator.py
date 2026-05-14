import time
import math

def add():
    print("")
    input1 = float(input("Enter first number: "))
    input2 = float(input("Enter second number: "))
    result = input1 + input2
    print("The result is: ", result)
    time.sleep(5)
    calculator()

def subtract():
    print("")
    input1 = float(input("Enter first number: "))
    input2 = float(input("Enter second number: "))
    result = input1 - input2
    print("The result is: ", result)
    time.sleep(5)
    calculator()

def multiply():
    print("")
    input1 = float(input("Enter first number: "))
    input2 = float(input("Enter second number: "))
    result = input1 * input2
    print("The result is: ", result)
    time.sleep(5)
    calculator()

def divide():
    print("")
    input1 = float(input("Enter first number: "))
    input2 = float(input("Enter second number: "))
    result = input1 / input2
    print("The result is: ", result)
    time.sleep(5)
    calculator()

def Exponent():
    print("")
    input1 = float(input("Enter first number: "))
    input2 = float(input("Enter second number: "))
    result = input1 ** input2
    print("The result is: ", result)
    time.sleep(5)
    calculator()

def factorial():
    print("")
    input1 = int(input("Enter a number: "))
    result = math.factorial(input1)
    print("The result is: ", result)
    time.sleep(5)
    calculator()

def SquareRoot():
    print("")
    input1 = float(input("Enter a number: "))
    result = math.sqrt(input1)
    print("The result is: ", result)
    time.sleep(5)
    calculator()

def calculator():
    print("Select operation:")
    print("1. + = Add")
    print("2. - = Subtract")
    print("3. * = Multiply")
    print("4. / = Divide")
    print("5. ** = Exponent")
    print("6. ! = Factorial")
    print("7. sqrt = Square Root")

    choice = input("Enter choice: ")

    if choice == '+':
        add()
    elif choice == '-':
        subtract()
    elif choice == '*':
        multiply()
    elif choice == '/':
        divide()
    elif choice == '**':
        Exponent()
    elif choice == '!':
        factorial()
    elif choice == 'sqrt':
        SquareRoot()
    else:
        print("Invalid input.")
        print("")
        time.sleep(2)
        calculator()

calculator()
