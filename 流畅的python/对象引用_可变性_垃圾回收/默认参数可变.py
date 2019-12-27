class Bus:
    def __init__(self, passenger = []):
        self.passenger = passenger
    
    def pick(self, name):
        self.passenger.append(name)

    def drop(self, name):
        self.passenger.pop(name)


bus = Bus(["ajin", "xialin"])
print(bus.passenger)

bus.pick("xx")
print(bus.passenger)
bus2 = Bus()
print(bus2.passenger)
bus2.pick("yy")
print(bus2.passenger)
bus3 = Bus()
print(bus3.passenger)

# ['ajin', 'xialin']
# ['ajin', 'xialin', 'xx']
# []
# ['yy']
# ['yy']