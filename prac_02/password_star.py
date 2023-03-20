password = input("Password: ")
length_of_password = len(password)
while length_of_password > 0:
    if length_of_password > 6:
        for i in range(length_of_password):
            print('*', end='')
        break
    else:
        print("Invalid input ")
        password = input("Password: ")
        length_of_password = len(password)


