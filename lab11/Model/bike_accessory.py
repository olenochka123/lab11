from accessory import Accessory


class BikeAccessory(Accessory):
    def __init__(self, id, name, price,
                 weight,
                 producer, color, bike_type):
        self.bike_type = bike_type
        super().__init__(id, name, price, weight, producer, color)