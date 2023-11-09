# Behavioral Patterns
# Observer (publisher, subscriber[s])

# When to use :
# Use case    : YoutubeChannel and notifications to subscribers

# One Subject (Publisher) generating events
# One or more  Observers (Subscribers) notified in realtime when events happens


# Maintain a list of its subscribers
# When a user subcribe it is added to the list of subscribers
# On event, notifications are sent to the members of the list
class YoutubeChannel:
    def __init__(self, name):
        self.name = name
        self.subscribers = []

    def subscribe(self, sub):
        self.subscribers.append(sub)

    def notify(self, event):
        for sub in self.subscribers:
            sub.sendNotification(self.name, event)


# We have to define the subscriber interface
# This can be done with an abstract class (or interface)
from abc import ABC, abstractmethod


class YoutubeSubscriber(ABC):
    @abstractmethod
    def sendNotification(self, event):
        pass


# Different subscribers might define the interface differently
# Here for a YoutubeUser we print the event
class YoutubeUser(YoutubeSubscriber):
    def __init__(self, name):
        self.name = name

    def sendNotification(self, channel, event):
        print(f"User {self.name} received notification from {channel} : {event}")


# Create a Youtube channel
channel = YoutubeChannel("neetcode")

# Add some subcribers
channel.subscribe(YoutubeUser("Name 1"))
channel.subscribe(YoutubeUser("Name 2"))
channel.subscribe(YoutubeUser("Name 3"))

# notify is called once and all the subscribers get notified
channel.notify("A new video released")

# A subscriber can subscribe to multiple channels
