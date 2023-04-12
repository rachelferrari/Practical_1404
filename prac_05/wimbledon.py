"""
Game, Set Match
Estimated: 1 hr 15 minutes
Actual:
"""
FILENAME = "../wimbledon.csv"


def main():
    """Shows processed information of the files"""
    data = open_file()
    print(data)


def open_file():
    """Opens and reads the file"""
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        rows = [row.strip().split(',') for row in in_file.readlines()]
        return rows


main()

