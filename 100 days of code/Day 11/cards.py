import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

start_game = input("Press y to start the game: ")
while 1:
    if start_game != 'y':
        break
    user_total = 0
    ai_total = 0
    user_card = random.choice(cards)
    user_total += user_card
    ai_card = random.choice(cards)
    ai_total += ai_card
    print(f"You got {user_card}")
    print(f"Total: {user_total}")
    print("")
    print(f"Opponent got {ai_card}")
    print(f"Total: {ai_total}")
    while 1:
        draw_card = input("Press y to draw another card or n to end game: ")
        if draw_card == 'y':
            user_card = random.choice(cards)
            if user_card == 11:
                ace_dec = int(input("You got ace. Enter 1 to add 1 or 11 to add 11 to your score: "))
                user_card = ace_dec
            user_total += user_card
            print(f"You got {user_card}")
            print(f"Total: {user_total}")
            print("")
            if ai_total < 17:
                ai_card = random.choice(cards)
                if ai_card == 11:
                    if (ai_total + 11) > 21:
                        ai_card = 1
                    else:
                        ai_card = 11
                ai_total += ai_card
            if user_total > 21:
                print("You lose")
                print(f"User total: {user_total}, Opponent total: {ai_total}")
                break
        elif draw_card == 'n':
            if ai_total > 21:
                print("You win")
                print(f"User total: {user_total}, Opponent total: {ai_total}")
                break
            if user_total == 21 and ai_total == 21:
                print("Draw")
                break
            if user_total < ai_total:
                print("You lose")
                print(f"User total: {user_total}, Opponent total: {ai_total}")
                break
            else:
                print("You win")
                print(f"User total: {user_total}, Opponent total: {ai_total}")
                break
        elif draw_card != 'y' or draw_card != 'n':
            print("You entered a wrong value.")
            draw_card = input("Press y to draw another card or n to end game: ")
    start_game = input("Enter y to play again or any key to end: ")
    if start_game != 'y':
        break


        