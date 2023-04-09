import random

MIN_RANDOM = 1
MAX_RANDOM = 45
AMOUNT_OF_NUMBERS = 6

line = int(input("How many quick picks do you want? "))
for i in range(line):
    random_numbers = []
    for j in range(AMOUNT_OF_NUMBERS):
        while len(random_numbers) != AMOUNT_OF_NUMBERS:
            k = random.randint(MIN_RANDOM, MAX_RANDOM)
            if k not in random_numbers:
                random_numbers.append(k)
    random_numbers.sort()
    print(' '.join(str(f"{number:>3}") for number in random_numbers))



