"""
Emails
Estimated: 45 minutes
Actual:
"""
name_to_email = {}

email = input("Email: ")
while email != '':
    emails = email.split('@')
    name = ' '.join(emails[0].split('.')).title()
    answer = input(f"Is your name {name}? (Y/n) ")
    while answer != '' and answer != 'y':
        if answer == 'n' or answer == 'no':
            name = input("Name: ").title()
            answer = 'y'
        else:
            print("Invalid input")
            answer = input(f"Is your name {name}? (Y/n) ")
    name_to_email[name] = email
    email = input("Email: ")
for name, email in name_to_email.items():
    print(f"{name} ({email})")
