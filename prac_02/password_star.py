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
    password = get_valid_password()
    length_of_password = len(password)
    while password != '':
        if length_of_password > 6:
            return print_asterisk(length_of_password)
        else:
            print("Try again")
            password = get_valid_password()
            length_of_password = len(password)


def print_asterisk(length_of_password):
    for i in range(length_of_password):
        print('*', end='')
    return


def get_valid_password():
    password = input("Password: ")
    while password == '':
        print("Invalid input")
        password = input("Password: ")
    return password




main()
