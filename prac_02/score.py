"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!


# score = int(input("Enter score: "))
# # if score < 0:
# #     print("Invalid score")
# # else:
# #     if score > 100:
# #         print("Invalid score")
# #     if score > 50:
# #         print("Passable")
# #     if score > 90:
# #     print("Excellent")
# # if score < 50:
# #     print("Bad")
# if score > 100 or score < 0:
#     # print("Invalid input")
#     message = "Invalid input"
# elif score >= 90:
#     # print("Excellent")
#     message = "Excellent"
# elif score >= 50:
#     # print("Passable")
#     message = "Passable"
# else:
#     # print("Bad")
#     message = "Bad"
# print(message)

import random


def main():
    score = int(input("Enter score: "))
    determine_message(score)
    score = randomize_score()
    print(f"Random score: {score}")
    determine_message(score)


def determine_message(score):
    """Determine message according to score inputted"""
    if score > 100 or score < 0:
        message = "Invalid input"
    elif score >= 90:
        message = "Excellent"
    elif score >= 50:
        message = "Passable"
    else:
        message = "Bad"
    print(message)


def randomize_score():
    """Get random score"""
    score = random.randint(0, 100)
    return score


main()

