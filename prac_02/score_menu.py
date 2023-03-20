MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit
"""


def main():
    print(MENU)
    choice = get_valid_choice()
    while choice != 'Q':
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            message = determine_message(score)
            print(message)
        elif choice == 'S':
            print_asterisk(score)
            print()
        else:
            print("Invalid input")
        print(MENU)
        choice = get_valid_choice()
    print("Farewell")


def get_valid_choice():
    return input(">>> ").upper()


def get_valid_score():
    score = int(input('Enter score: '))
    while score > 100 or score < 0:
        print("Invalid input")
        score = int(input('Enter score: '))
    return score


def determine_message(score):
    if score > 100 or score < 0:
        message = "Invalid input"
    elif score >= 90:
        message = "Excellent"
    elif score >= 50:
        message = "Passable"
    else:
        message = "Bad"
    return message


def print_asterisk(score):
    for i in range(score):
        print('*', end='')


main()