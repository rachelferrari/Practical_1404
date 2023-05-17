class Band:
    def __init__(self, name=""):
        self.name = name
        self.musicians = []
        self.musicians_dictionary = {}

    def __str__(self):
        return f"{self.name} ({', '.join(self.musicians)})"

    def add(self, musician):
        self.musicians_dictionary[musician.name] = musician.instruments
        self.musicians.append(f"{musician.name} ({musician.instruments})")

    def play(self):
        message = []
        for musician in self.musicians_dictionary:
            if not self.musicians_dictionary[musician]:
                message.append(f"{musician} needs an instrument!")
            else:
                message.append(f"{musician} is playing: {self.musicians_dictionary[musician][0]}")
        return '\n'.join(message)
