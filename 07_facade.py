# Structural Patterns
# Facade

# When to use :
# Use case    :

# Facade : an outward appearance that is used to conceal a less pleasant of credible reality
# A wrapper class that hide the complexity behind (abstract)
# Example : HTTP clients or dynamics arrays (vectors in C++)

# Not sure this example is so great
# Indeed, by definition, a class is supposed to hide the detail of the implemenation


class Array:
    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.arr = [0] * self.capacity  # ! I don't know if this is licit

    # insert n in last position
    def pushback(self, n):
        if self.length == self.capacity:
            self.resize()

        # insert
        self.arr[self.length] = n
        self.length += 1

    def resize(self):
        # create an array of double capacity
        self.capacity = 2 * self.capacity
        newArr = [0] * self.capacity

        # copy
        for i in range(self.length):
            newArr[i] = self.arr[i]

        self.arr = newArr


bob = Array()
bob.pushback(1)
bob.pushback(11)
bob.pushback(111)
bob.pushback(2)
bob.pushback(22)
bob.pushback(222)

for n in bob.arr:
    print(n)
