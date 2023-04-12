"""
Game, Set, Match
Estimated: 1 hr 15 minutes
Actual: 57 minutes
"""
FILENAME = "../wimbledon.csv"


def main():
    """Shows processed information of the file"""
    data = open_file()
    show_champions_and_wins(data)
    print()
    show_countries(data)


def open_file():
    """Opens and reads the file"""
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        rows = [row.strip().split(',') for row in in_file.readlines()]
        return rows


def show_champions_and_wins(data):
    """Show champions and the amount of wins"""
    winner_to_win = {}
    winners = []
    print("Wimbledon Champions:")
    for i in range(1, len(data)):
        winners.append(data[i][2])
    for i in range(len(winners)):
        winner_to_win[winners[i]] = winners.count(winners[i])
    for winner, win in winner_to_win.items():
        print(f"{winner} {win}")


def show_countries(data):
    """Show countries that have won"""
    countries = set()
    for i in range(1, len(data)):
        countries.add(data[i][1])
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(', '.join(sorted(countries)))


main()
