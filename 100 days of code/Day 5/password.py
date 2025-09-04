import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
           'Z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = [':', ';', '_', '-', '+', '=', '&', '?', '%']

password = ""
length_of_password = int(input("How many elements should your password have: "))
num_of_symbols = int(input("How many symbols should your password have: "))
num_of_numbers = int(input("How many numbers should your password have: "))

for i in range(1, length_of_password + 1):
    list_selector = random.randint(0, 2)
    if list_selector == 1 and num_of_numbers != 0:
        password += str(numbers[random.randint(0, 9)])
        num_of_numbers -= 1
    elif list_selector == 2 and num_of_symbols != 0:
        password += str(symbols[random.randint(0, 8)])
        num_of_symbols -= 1
    else:
        password += str(letters[random.randint(0, 51)])
print(password)