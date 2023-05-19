from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi simulator program to simulate using taxis and silver service taxis."""
    current_taxi = None
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'c':
            current_taxi = choose_taxi(current_taxi, taxis)
        elif choice == 'd':
            drive_taxi(current_taxi)
        else:
            print("Invalid option")
        try:
            total_bill += current_taxi.get_fare()
        except AttributeError:
            pass
        print(f"Bill to date: ${float(total_bill):.2f}")
        print(MENU)
        choice = input(">>> ").lower()


def drive_taxi(current_taxi):
    """Drive the current taxi."""
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
    else:
        distance = int(input("Drive how far? "))
        current_taxi.drive(distance)
        print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}")


def choose_taxi(current_taxi, taxis):
    """Get user input to choose which taxi to take."""
    print("Taxis available: ")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    is_valid_input = False
    while not is_valid_input:
        try:
            taxi_choice = int(input("Choose taxi: "))
            if taxi_choice < 0:
                print(f"Enter number between 0 - {len(taxis)}")
            elif taxi_choice >= len(taxis):
                print("Invalid taxi choice")
            else:
                is_valid_input = True
                current_taxi = taxis[taxi_choice]
        except ValueError:
            print("Enter an integer")
    return current_taxi


main()
