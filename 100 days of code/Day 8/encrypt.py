def letter_enc(index_letter, result, letters):
    i = 0
    while index_letter != letters[i]:
        i += 1
    if (i + shift_code) > (len(letters) - 1):
        result += letters[((i + shift_code) - (len(letters) - 1)) - 1]
    else:
        result += letters[i + shift_code]
    return result

def letter_dec(index_letter, result, letters):
    i = 0
    while index_letter != letters[i]:
        i += 1
    if(i - shift_code) < 0:
        result += letters[((len(letters)) + (i - shift_code))]
    else:
        result += letters[i - shift_code]
    return result
        
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



while 1:
    result = ""
    usr_choice = input("Type \"encode\" or \"decode\"\n").lower()
    if usr_choice == "encode":
        message = input("Enter the message: ")
        shift_code = int(input("Enter the shift code: "))
        for index_lettr in message:
            result = letter_enc(index_lettr, result, letters)
    elif usr_choice == "decode":
        message = input("Enter the message: ")
        shift_code = int(input("Enter the shift code: "))
        for index_lettr in message:
            result = letter_dec(index_lettr, result, letters)
    print(result)
    if not (input("Do you want to try again ?(\"y\" or \"n\"): ") != "n"):
        break