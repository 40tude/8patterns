# Behavioral Patterns
# Iterator

# When to use :
# Use case    :

# Define how the values in an object can be iterated trough
# think about a list, a for loop and the in keyword
# use the built-in list iterator
# no need to index the array

mylist = [1, 2, 3]
for n in mylist:
    print(n)

# we can define our own iterator for more complex object
# linked lists, binary trees


# A list node concist of a value and a next pointer
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# A linked list has a head pointer and a current pointer
class LinkedList:
    def __init(self, head):
        self.head = head
        self.current = None

    # we define the iterator with the __iter__ inner function
    # set the current pointer to head and return a reference to the linked list
    def __iter__(self):
        self.current = self.head
        return self

    # To get the next value in the list, we define the __next__ inner function
    # If the current point is not null, update the current point to point the next and return the current val
    # Otherwise, send the signal that we are going to stop iterating
    def __next__(self):
        if self.current:
            val = self.current.val
            self.current = self.current.next
            return val
        else:
            raise StopIteration


# Initialize
# ! I don't like that but it is simple
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

myList = LinkedList(head)

# Iterate
for n in mylist:
    print(n)
