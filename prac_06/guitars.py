from guitar import Guitar

CURRENT_YEAR = 2022
guitars = []
print("My guitars!")
name = input("Name: ")
while name != '':
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitars.append(Guitar(name, year, cost))
    name = input("Name: ")
print("...snip...")
for i, guitar in enumerate(guitars, 1):
    age = Guitar.get_age(guitar, CURRENT_YEAR)
    vintage_string = " (vintage)" if Guitar.is_vintage(guitar, age) is True else ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")