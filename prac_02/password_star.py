# password = input("Password: ")
# length_of_password = len(password)
# while password != '':
#     if length_of_password > 6:
#         for i in range(length_of_password):
#             print('*', end='')
#         break
#     else:
#         print("Try again")
#         password = input("Password: ")
#         length_of_password = len(password)


def main():
    length_of_password = get_valid_password()
    print_asterisk(length_of_password)


def print_asterisk(length_of_password):
    """Print asterisks to length of password"""
    for i in range(length_of_password):
        print('*', end='')


def get_valid_password():
    """Get valid password"""
    password = input("Password: ")
    length_of_password = len(password)
    while password != '':
        if length_of_password >= 6:
            return length_of_password
        else:
            print("Try again")
            password = input("Password: ")
            length_of_password = len(password)


main()
