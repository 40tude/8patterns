# Creational Pattern
# Builder

# When to use :
# Use case    :

# No need to select all the ingredients when the burger is created
# We have more control on what is in the burger


# The burger is empty by default
class Burger:
    def __init__(self):
        self.buns = None
        self.patty = None
        self.cheese = None

    def setBuns(self, bunStyle):
        self.buns = bunStyle

    def setPatty(self, pattyStyle):
        self.patty = pattyStyle

    def setCheese(self, cheeseStyle):
        self.cheese = cheeseStyle

    def print(self):
        print(self.buns, self.patty, self.cheese)


# The burger builder exposes methods to add individual ingredients
class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()

    def addBuns(self, bunStyle):
        self.burger.setBuns(bunStyle)
        return self

    def addPatty(self, pattyStyle):
        self.burger.setPatty(pattyStyle)
        return self

    def addCheese(self, cheeseStyle):
        self.burger.setCheese(cheeseStyle)
        return self

    def build(self):
        return self.burger


# Watch out the syntax
# We have more control when the burger is instanciated
myBurger = (
    BurgerBuilder()
    .addBuns("sesame")
    .addPatty("fish-patty")
    .addCheese("swiss cheese")
    .build()
)

myBurger.print()

# this may not be a good idea but this is legal
myBurger.setCheese("Zoubida")
myBurger.print()
