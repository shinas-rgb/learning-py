import random

print("1. Create a list")
print("2. exit\n")

li = []
operation = 10
choice = int(input())
if choice == 1:
    print("1. Append an element")
    print("2. Pop an element")
    print("3. remove an element")
    print("4. Insert element at a position")
    print("5. pop element at a position")
    print("6. print list")
    print("7. Choose a random element")
    print("0. exit\n")
    while operation != 0:
        operation = int(input())
        if operation == 1:
            li.append(input("Enter value "))
        elif operation == 2:
            li.pop()
        elif operation == 3:
            del li[-1]
        elif operation == 4:
            li.insert(int(input("Enter position: ")), int(input("Enter value: ")))
        elif operation == 5:
            li.pop(int(input("Position: ")))
        elif operation == 6:
            print(li)
        elif operation == 7:
            print(li[random.randint(0, len(li) - 1)])
    print("Exiting......")
else:
    print("Exiting......")