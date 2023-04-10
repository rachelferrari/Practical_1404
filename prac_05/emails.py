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
        name = input("Name: ")
        answer = 'y'
    email = input("Email: ")
