import random

from car import Car


class UnreliableCar(Car):
    """Derived class of a Car that computes the chances of actually driving the car"""

    def __init__(self, name, fuel, reliability):
        """Initialize an Unreliable Car instance, based on Car class"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return string with car reliability to drive"""
        return f"{super().__str__()}, Reliability level={self.reliability}"

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        chance = random.randint(0, 100)
        if self.reliability > chance:
            distance_driven = super().drive(distance)
        else:
            distance_driven = super().drive(0)
        return distance_driven


