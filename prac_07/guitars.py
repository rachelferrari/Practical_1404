from guitar import Guitar


def main():
    """Read file, save file contents as objects to Guitar class, and display contents"""
    guitars = []

    with open("guitars.csv", 'r') as in_file:
        for line in in_file.readlines():
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)

    for guitar in guitars:
        print(guitar)


main()
