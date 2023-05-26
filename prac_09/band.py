class Band:
    def __init__(self, name=""):
        """Initialize a band instance."""
        self.name = name
        self.musicians = []
        self.musicians_dictionary = {}

    def __str__(self):
        """Returns a string representation of the Band."""
        return f"{self.name} ({', '.join(self.musicians)})"

    def add(self, musician):
        """Add a musician and their instruments to the band."""
        self.musicians_dictionary[musician.name] = musician.instruments
        self.musicians.append(f"{musician.name} ({musician.instruments})")

    def play(self):
        """Return a string showing each musician in the band playing their first (or no) instrument."""
        message = []
        for musician in self.musicians_dictionary:
            if not self.musicians_dictionary[musician]:
                message.append(f"{musician} needs an instrument!")
            else:
                message.append(f"{musician} is playing: {self.musicians_dictionary[musician][0]}")
        return '\n'.join(message)
