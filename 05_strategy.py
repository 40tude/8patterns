# Behavioral Patterns
# Strategy

# When to use :
# Use case    :

# If we want to modify or extend the behavior of a class without directly changing it
# then go for the strategy pattern


# Example : filtering an array by removing positive values or by removing odd values

# These are 2 strategies, but may be in the future we want to add more filter
# We want to follow the Open-Closed Principle
# A class is :
#   Open for extension
#   Closed for modifications

from abc import ABC, abstractmethod


# We define a filter strategy with an abstract class
class FilterStrategy(ABC):
    @abstractmethod
    def removeValue(self, val):
        pass


# We create an implementation to remove neg values
class RemoveNegativeStrategy(FilterStrategy):
    def removeValue(self, val):
        return val < 0


# We create an implementation to remove odd values
class RemoveOddStrategy(FilterStrategy):
    def removeValue(self, val):
        return abs(val) % 2


class Values:
    def __init__(self, vals):
        self.vals = vals

    def filter(self, strategy):
        res = []
        for n in self.vals:
            if not strategy.removeValue(n):
                res.append(n)
        return res


values = Values([-7, -4, -1, 0, 2, 6, 9])

# At runtime we can pass these strategies into the values objects as filter method
print(values.filter(RemoveNegativeStrategy()))
print(values.filter(RemoveOddStrategy()))

# So we can add more strategy without modifying the Values class
