from prac_06.guitar import Guitar

CURRENT_YEAR = 2022
my_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2013)
print(f"{my_guitar.name} get_age() - Expected {CURRENT_YEAR - my_guitar.year}. Got {my_guitar.get_age(CURRENT_YEAR)}")
print(f"{another_guitar.name} - get_age() - Expected {CURRENT_YEAR - another_guitar.year}. Got {another_guitar.get_age(CURRENT_YEAR)}")
print(f"{my_guitar.name} is_vintage() - Expected True. Got {my_guitar.is_vintage(100)}")
print(f"{another_guitar.name} is_vintage() - Expected False. Got {my_guitar.is_vintage(9)}")
