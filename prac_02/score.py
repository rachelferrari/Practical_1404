"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!


"""score = int(input("Enter score: "))
# if score < 0:
#     print("Invalid score")
# else:
#     if score > 100:
#         print("Invalid score")
#     if score > 50:
#         print("Passable")
#     if score > 90:
#     print("Excellent")
# if score < 50:
#     print("Bad")
if score > 100 or score < 0:
    # print("Invalid input")
    message = "Invalid input"
elif score >= 90:
    # print("Excellent")
    message = "Excellent"
elif score >= 50:
    # print("Passable")
    message = "Passable"
else:
    # print("Bad")
    message = "Bad"
print(message)"""
import random


def main():
    score = int(input("Enter score: "))
    message = determine_message(score)
    print(message)
    score = random.randint(0, 100)
    print(f"Random score: {score}")
    message = determine_message(score)
    print(message)


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


main()
