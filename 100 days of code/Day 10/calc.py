import os
num1 = int(input("Enter the first number: "))
operation = input("Enter the operation(+, -, *, /): ")
num2 = int(input("Enter the second number: "))

def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiple(num1, num2):
    return num1 * num2
def devide(num1, num2):
    return num1 / num2

operations = {
    '+': add,
    '-': subtract,
    '*': multiple,
    '/': devide,
}

function_operation = operations[operation]
result = function_operation(num1, num2)
print(result)

while 1:
    ans = input("Do you want to continue with the result(y / n): ")
    if ans == 'y':
        os.system('cls' if os.name=='nt' else 'clear')
        print(f"number 1: {result}")
        num1 = result
        operation = input("Enter the operation(+, -, *, /): ")
        num2 = int(input("Enter the second number: "))
        function_operation = operations[operation]
        result = function_operation(num1, num2)
        print(result)
    elif ans == 'n':
        break
