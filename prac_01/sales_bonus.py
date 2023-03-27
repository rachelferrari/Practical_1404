"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
VALIDITY_THRESHOLD = 0
HIGH_BONUS_THRESHOLD = 1000
HIGH_PERCENTAGE = 0.15
LOW_PERCENTAGE = 0.10

sales = float(input("Enter sales: $"))
while sales >= VALIDITY_THRESHOLD:
    if sales >= HIGH_BONUS_THRESHOLD:
        user_bonus = sales * HIGH_PERCENTAGE
    else:
        user_bonus = sales * LOW_PERCENTAGE
    print(user_bonus)
    sales = float(input("Enter sales: $"))