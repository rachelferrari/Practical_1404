"""
Guitar
Estimated: 60 minutes
Actual: 1 hour 18 minutes
"""


class Guitar:
    def __init__(self, name='', year=0, cost=0):
        """Initialise guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self, current_year):
        return current_year - self.year

    def is_vintage(self, age):
        if age >= 50:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

