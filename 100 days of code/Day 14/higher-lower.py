import random
import sys

def higher_lower():
    global winner

    print(f"A: {person_1['name']} from {person_1['nation']}")
    print("OR")
    print(f"B: {person_2['name']} from {person_2['nation']}")

    choice = input("Put your answer: ")

    if choice == 'a':
        if person_1['followers'] > person_2['followers']:
            print("You're right!!")
            winner = person_1
            win()
        else:
            print("You failed!!")
            retry()
    elif choice == 'b':
        if person_1['followers'] < person_2['followers']:
            print("You're right!!")
            winner = person_2
            win()
        else:
            print("You failed!!")
            retry()
    else:
        print("Wrong Choice")


def retry():
    retry_choice = input("Do you want to retry? Y/N: ")
    if retry_choice == 'y':
        data = dup_data.copy()
        higher_lower()
    else:
        sys.exit(0)

def win():
    global person_1, person_2, data, winner
    if not data:
        print("You win.")
        sys.exit(0)
    person_1 = winner
    person_2 = random.choice(data)
    data.remove(person_2)
    higher_lower()


print("Welcome to the Higher Lower game\nGuess which person has more followers in instagram")

data = [
    {
        'name': 'Cristiano Ronaldo',
        'nation': 'Portugal',
        'followers': 664000000
    },
    {
        'name': 'Lionel Messi',
        'nation': 'Argentina',
        'followers': 506000000
    },
    {
        'name': 'Neymar',
        'nation': 'Brazil',
        'followers': 231500000
    },
    {
        'name': 'Paulo Dybala',
        'nation': 'Argentina',
        'followers': 57000000
    },
    {
        'name': 'Luiz Suarez',
        'nation': 'Argentina',
        'followers': 48700000
    },
    {
        'name': 'David Beckham',
        'nation': 'England',
        'followers': 88400000
    },
    {
        'name': 'Harry Kane',
        'nation': 'England',
        'followers': 17700000
    },
]

dup_data = data.copy()
person_1 = random.choice(data)
data.remove(person_1)
person_2 = random.choice(data)
data.remove(person_2)
winner = {}

higher_lower()





