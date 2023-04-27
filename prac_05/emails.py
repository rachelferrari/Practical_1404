"""
Emails
Estimated: 45 minutes
Actual: 28 minutes
"""
name_to_email = {}

email = input("Email: ")
while email != '':
    emails = email.split('@')
    name = ' '.join(emails[0].split('.')).title()
    answer = input(f"Is your name {name}? (Y/n) ")
    while answer != '' and answer != 'y':
        name = input("Name: ").title()
        answer = 'y'
    name_to_email[name] = email
    email = input("Email: ")
for name, email in name_to_email.items():
    print(f"{name} ({email})")
