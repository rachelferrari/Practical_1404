from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialized version of a Taxi with different fares"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a Silver Service Taxi instance, based on child class Taxi"""
        super().__init__(name, fuel)
        self.current_fare_distance = 0
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string like a Car but with addition of flagfall"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price for the taxi trip."""
        fare = super().get_fare()
        if fare != 0.0:
            fare += self.flagfall
        return fare
