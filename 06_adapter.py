# Structural Patterns
# Adapter

# When to use :
# Use case    :

# Screw too small
# Adapter to make the screw compatible with the hole
# Here USB and micro USB adapter


# We have a USB cable
class USBCable:
    def __init__(self):
        self.isPlugged = False

    def plugUsb(self):
        self.isPlugged = True


# And a USB Port
class USBPort:
    def __init__(self):
        self.portAvailable = True

    def plug(self, usb):
        if self.portAvailable:
            # We can plug ONLY USB cable
            usb.plugUsb()
            self.portAvailable = False


# USBCable can plug directly into USB ports
myUSBCable = USBCable()
USBPort1 = USBPort()
USBPort1.plug(myUSBCable)


# But if we have a micro USB cable it is not compatible
class MicroUSBCable:
    def __init__(self):
        self.isPlugged = False

    def plugMicroUsb(self):
        self.isPlugged = True


# This does NOT work
# myMicroUSBCable = MicroUSBCable()
# USBPort3 = USBPort()
# USBPort3.plug(myMicroUSBCable)


# So we need a micro USB to USB adapter
# It extends from the USB class but is composed of a micro USB cable
# wich will be plugged into the adpater
class MicroToUSBAdapter(USBCable):
    def __init__(self, microUsbCable):
        self.microUsbCable = microUsbCable
        self.microUsbCable.plugMicroUsb()

    # can override UsBCable.plugUsb() from the parent class if needed
    # This is not the case here


# We can plug the micro USB cable into the adapter
myMicroToUSBAdapter = MicroToUSBAdapter(MicroUSBCable())
USBPort2 = USBPort()
# and then plug the adapter into the USB port
USBPort2.plug(myMicroToUSBAdapter)
