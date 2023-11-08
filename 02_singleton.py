# Creational Pattern
# Singleton

# When to use :
# Use case    : maintain a single copy of the application state
#               multiple components of the app can have a shared source of truth


# A class that can only be instantiated once in the application
# In the app, we want to know whether a user is logged in or not
class ApplicationState:
    instance = None

    def __init__(self):
        self.isLoggedIn = False

    # we don't use the constructor to instantiate the state of the application
    # we use a static method (getAppState) which starts by checking whether there is already an instance (or not) of the application state (ApplicationState)
    # if there isn't, then it creates an instance of ApplicationState and stores it in .instance
    # If an instance already exists (logged in .instance) it returns the existing instance
    # It never creates more than one instance
    @staticmethod  # ! À vérifier
    def getAppState():
        if not ApplicationState.instance:
            ApplicationState.instance = ApplicationState()
        return ApplicationState.instance


appState1 = ApplicationState.getAppState()
print(appState1.isLoggedIn)  # False

appState2 = ApplicationState.getAppState()
appState1.isLoggedIn = True

print(appState1.isLoggedIn)  # True
print(appState2.isLoggedIn)  # True
