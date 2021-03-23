class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True # we don't need parameter for this

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})" # !r - close the repr method of self.name - shows up
        # as having the quotes already

    def disconnect(self):
        self.connected = False
        print("Disconnected.")

printer = Device("Printer", "USB")
print(printer)
printer.disconnect()


# printer = Device("Printer", "USB")
# print(printer)

# We don't want to add printer-specific stuff to Device, so...


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        # self.name = name                      this changed to the super super().__init__(name, connected_by)
        # self.connected_by = connected_by
        # self.connected = True 

        # super(Printer, self).__init__(name, connected_by)  - Python2.7
        super().__init__(name, connected_by)  # Python3+
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected!")
            return
            #raise TypeError("Device is disconnected at this time, cannot print.")
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages




printer = Printer("Printer", "USB", 500)
printer.print(20)
print(printer)
printer.print(50)
print(printer)
printer.disconnect()
printer.print(30)  # Error TypeError: Device is disconnected at this time, cannot print.
