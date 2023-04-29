class Guitar:
    def __init__(self, name='', year=0, cost=0.0):
        """Initialise guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self, current_year):
        """Get guitar age"""
        return current_year - self.year

    def is_vintage(self, age):
        """Determine if guitar is more than 50 years old or not"""
        if age >= 50:
            return True
        else:
            return False

    # def __str__(self):
    #     return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __repr__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        """Determine which guitar is older based on another guitar's age"""
        return self.year < other.year
