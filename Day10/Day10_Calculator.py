from Day10_art import logo


def add(n1, n2):
   return n1 + n2


def subtract(n1, n2):
    return n1-n2


def multiply(n1, n2):
    return n1*n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add
    , "-": subtract
    , "*": multiply
    , "/": divide
}


def calculator():
    """Returns the result of an equation of two numbers provided from inputs and a chosen operation"""
    print(logo)
    num1 = float(input("What is the first number? "))
    for symbol in operations:
        print(symbol)
    keep_calc = True
    while keep_calc:
        operation = input("Pick an operation: ")
        num2 = float(input("What is the next number? "))
        calculation_function = operations[operation]
        answer = calculation_function(num1,num2)
        print(f"{num1} {operation} {num2} = {answer}")
        cont = input(f"Type y for additional calculations with {answer}, type r to start with a new number, or type 'n' to exit\n")
        num1 = answer
        if cont == "n":
            keep_calc = False
        elif cont == "r":
            keep_calc = False
            calculator()


calculator()




