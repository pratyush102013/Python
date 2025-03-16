from traceback import clear_frames
import art


def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    '''Calculates numbers with operations'''
    print(art.logo)
    should_accumulate = True
    while should_accumulate:
        num1 = float(int(input("What is the first number?:\n")))
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: \n")
        num2 = float(input("What is the next number\n"))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} =   {answer}")

        choice = input(f"Type 'y' to continue calculation with {answer} or type 'n' to start a new calculation\n")

        if choice == "y":
            num1 = answer
            for symbol in operations:
                print(symbol)
            operation_symbol = input("Pick an operation: \n")
            num2 = float(input("What is the next number\n"))
            answer = operations[operation_symbol](num1, num2)
            print(f"{num1} {operation_symbol} {num2} =   {answer}")
        else:
            should_accumulate = False
            print(art.logo)
            print("\n" * 1000)
            calculator()

calculator()