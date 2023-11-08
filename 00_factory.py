# Creational Pattern
# Factory


# A burger is based on a list of ingredients
class Burger:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def print(self):
        print(self.ingredients)


# The factory instanciate the burger and return it to usk
class BurgerFactory:
    def createCheeseBurger(self):
        ingredients = ["bun", "cheese", "beef-patty"]
        return Burger(ingredients)

    def createDeluxeBurger(self):
        ingredients = ["bun", "tomatoe", "lettuce" "cheese", "beef-patty"]
        return Burger(ingredients)

    def createVeganBurger(self):
        ingredients = ["bun", "special-sauce", "veggie-patty"]
        return Burger(ingredients)


# We create a factory
burgerFactory = BurgerFactory()

# We order the burger we want to the factory
# We don't have access to all the detail about the ingredient etc.
# To get more control on the making of => builder pattern
myBurger = burgerFactory.createDeluxeBurger()
myBurger.print()
