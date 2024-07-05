def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    num1 = int(input("Enter The First Number: "))
    for operation in operations:
        print(operation)
    
    is_continue = True

    while is_continue:
        operation = input("Pick an operation: ")
        num2 = int(input("Enter the second number: "))
        calc_func = operations[operation]
        output = calc_func(num1, num2)
        print(f'{num1} {operation} {num2} = {output}')

        if input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ") == 'y':
            num1 = output
        else:
            is_continue = False
            calculator()

calculator()