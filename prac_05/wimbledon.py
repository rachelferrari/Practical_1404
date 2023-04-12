"""
Game, Set Match
Estimated: 1 hr 15 minutes
Actual:
"""
FILENAME = "../wimbledon.csv"


def main():
    """Shows processed information of the files"""
    data = open_file()
    show_champions_and_wins(data)


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


main()

