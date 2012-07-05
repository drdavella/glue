from glue.core.message import DataMessage, SubsetMessage
from glue.core.hub import Hub, HubListener
from glue.core.data import Data
from glue.core.data_collection import DataCollection

class MyClient(HubListener):
    def register_to_hub(self, hub):
        """ Sign up to receive DataMessages from the hub """
        hub.subscribe(self,                     # subscribing object
                      DataMessage, # message type to subscribe to
                      handler = self.receive_message) # method to call


    def receive_message(self, message):
        """ Receives each DataMessage relay """
        print "    MyClient received a message \n"


# create objects
hub = Hub()
client = MyClient()
data = Data()
subset = data.new_subset()
data_collection = DataCollection()

# connect them to each other
data_collection.append(data)
data_collection.register_to_hub(hub)
client.register_to_hub(hub)

# manually send a DataMessage. Relayed to MyClient
print 'Manually sending DataMessage'
message = DataMessage(data)
hub.broadcast(message)

#modify the data object. Automatically generates a DataMessage
print 'Automatically triggering DataMessage'
data.label = "New label"

#send a SubsetMessage to the Hub.
print 'Manually sending SubsetMessage'
message = SubsetMessage(subset)
hub.broadcast(message) # nothing is printed